import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room


class RoomType(DjangoObjectType):

    is_fav = graphene.Boolean()

    class Meta:
        model = Room

    def resolve_is_fav(parent, info):
        user = info.context.user
        if user.is_authenticated:
            return parent in user.favs.all()
        return False


class RoomList(graphene.ObjectType):

    rooms = graphene.List(RoomType)
    total = graphene.Int()
