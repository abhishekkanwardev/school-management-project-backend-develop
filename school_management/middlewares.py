# from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken
from accounts.models import User

 
@database_sync_to_async
def get_user(id):
    try:
        user = User.objects.get(id=id)
    except:
        user = AnonymousUser()
    return user


class TokenAuthMiddleWare:
    def __init__(self, app):
        self.app = app
 
    async def __call__(self, scope, receive, send):
        query_string = scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        token = query_dict["token"][0]
        try:
            access_token = AccessToken(token)
            user = await get_user(access_token['user_id'])
            scope["user"] = user
        except Exception as e:
            scope["user"] =  None
        return await self.app(scope, receive, send)
    
    
    