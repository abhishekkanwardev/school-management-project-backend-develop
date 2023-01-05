
from rest_framework.response import Response as DefaultResponse

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

    return DefaultResponse(response)



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