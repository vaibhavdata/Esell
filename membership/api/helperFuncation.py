from rest_framework_simplejwt.tokens import RefreshToken
class MainService:
    @staticmethod
    def getJwtToken(typeName, user):
        refresh = RefreshToken.for_user(user)
        data = {}
        if typeName == 'ACCESS_TOKEN':
            data['access_token'] = str(refresh.access_token)
        else:
            data['refresh_token'] = str(refresh)
        return data
    
