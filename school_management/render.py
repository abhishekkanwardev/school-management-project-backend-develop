from rest_framework.renderers import JSONRenderer
from rest_framework import status



SUCCESS = "success"
ERROR = "error"
         
         
def api_response(status_value=SUCCESS, data=list(), message=str(), error=None, **kwargs):
    response = {'status': status_value}
    if kwargs:
        response.update(**kwargs)
    if error:
        response = {'status': ERROR}
        response['error'] = error
    response['data'] = data
    response['message'] = message
    return response


class CustomJsonRender(JSONRenderer):
    """
        Custom Render class to standardize the API response.
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
            [1] success single
                {
                "status": success,
                "message": "The success message",
                "data": {}
                }
            [2] success list
                {
                "status": success,
                "message": null,
                "data": [], # list of objects
                }
            [3] failed
                {
                "status": "error",
                "error":"error_message"
                "message": "The failed message",
                "data": []
                }
        """
        if not renderer_context:
            return super().render(data, accepted_media_type, renderer_context)

        response = renderer_context['response']
        
        print(response.data,'==================')
        
        if response.status_code == status.HTTP_204_NO_CONTENT:
            updated_response = api_response(
                message = "Deleted successfully."
            )
            return super().render(updated_response, accepted_media_type, renderer_context)
        if response.data and 'data' not in response.data:
            if response.status_code in [status.HTTP_400_BAD_REQUEST, status.HTTP_404_NOT_FOUND]:
                updated_response = api_response(
                    error = response.data,
                    message = "Something went wrong."
                )
            else:
                updated_response = api_response(
                    data = response.data
                )
            return super().render(updated_response, accepted_media_type, renderer_context)
        return super().render(data, accepted_media_type, renderer_context)
        
        
        
def custom_response(data, code, status, message):
    if isinstance(data, list):
        ready_data = []
        for d in data:
            ready_data.append(d)

    else:
        ready_data = data

    response = {
        "status": status,
        "message": message,
        "code": code,
        "data": {
            "response": ready_data
        }
    }

    return response