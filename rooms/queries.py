from .models import Room
from .types import RoomList


def resolve_rooms(root, info, page=1):
    if page < 1:
        page = 1
    page_size = 5
    skip = page_size * (page - 1)
    take = page_size * page
    rooms = Room.objects.all()[skip:take]
    total = Room.objects.count()
    return RoomList(rooms=rooms, total=total)


def resolve_room(root, info, id):
    return Room.objects.get(id=id)
