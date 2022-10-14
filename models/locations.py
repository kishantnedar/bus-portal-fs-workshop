import uuid


class Locations():
    def __init__(self, location_name, _id=None):
        self._id = _id if _id else uuid.uuid4().hex
        self.location = location_name
