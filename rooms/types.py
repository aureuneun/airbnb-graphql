import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class RoomList(graphene.ObjectType):

    rooms = graphene.List(RoomType)
    total = graphene.Int()
