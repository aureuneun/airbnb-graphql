import graphene
from .types import RoomList, RoomType
from .queries import resolve_rooms, resolve_room


class Query(object):

    rooms = graphene.Field(RoomList, page=graphene.Int(), resolver=resolve_rooms)
    room = graphene.Field(
        RoomType, id=graphene.Int(required=True), resolver=resolve_room
    )
