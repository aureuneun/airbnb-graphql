import graphene
from .models import Room
from .types import RoomList, RoomType


class Query(object):

    rooms = graphene.Field(RoomList, page=graphene.Int())
    room = graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        page_size = 5
        skip = page_size * (page - 1)
        take = page_size * page
        rooms = Room.objects.all()[skip:take]
        total = Room.objects.count()
        return RoomList(rooms=rooms, total=total)

    def resolve_room(self, info, id):
        return Room.objects.get(id=id)
