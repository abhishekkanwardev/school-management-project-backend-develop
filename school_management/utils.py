from rest_framework.response import Response as DefaultResponse
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination



def Response(data, code, status, message):
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
        "data": ready_data
    }
    return DefaultResponse(response, status=code)

def mail_send(subject, message, email_from, recipient_list):
    try:
        send_mail(subject, message, email_from, recipient_list )
        return True
    except Exception as e:
        return False


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return DefaultResponse({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })


class ResponseMessage(object):
    SUCCESS = "Success"
    LOGOUT = "Succesfully logout"
    FORGET_PASSWORD_SUBJECT = "Forgot Password Code"
    RESET_PASSWORD_SUBJECT = "Reset Password Code"
    FORGOT_PASSWORD_MAIL_SEND_SUCCESS = "Forgot password verification code sent to your email"
    RESET_PASSWORD_MAIL_SEND_SUCCESS = "Reset password verification code sent to your email"
    USER_NOT_FOUND_BY_EMAIL = "User Not found with this email"
    SOMETHING_WENT_WRONG = "Something went wrong. Please try again"
    Invalid_OTP = "Invalid OTP"
    PASSWORD_CHANGED = "Password Succesfylly Chnaged"