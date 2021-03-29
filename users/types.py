import graphene
from graphene_django import DjangoObjectType
from users.models import User


class UserType(DjangoObjectType):

    rooms = graphene.List("rooms.types.RoomType")

    class Meta:
        model = User
        exclude = ["password", "is_superuser", "last_login"]
