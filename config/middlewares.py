import jwt
from django.conf import settings
from users.models import User


class JWTMiddleware(object):
    def resolve(self, next, root, info, **kwargs):
        try:
            token = info.context.META.get("HTTP_AUTHORIZATION")
            if token:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)
                info.context.user = user
        except Exception:
            pass
        return next(root, info, **kwargs)
