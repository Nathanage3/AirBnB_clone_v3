#!/usr/bin/python3
""" Test .get() and .count() methods
"""
'''from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
'''
#!/usr/bin/python3
"""Doc
"""
from models.engine.db_storage import DBStorage


class DBStorage(DBStorage):
    """Doc
    """

    def get(self, cls, id):
        """
        returns the object by class and ID
        """
        return None