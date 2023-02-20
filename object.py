import json
from .constants import *
import logging

class ItemData:
    """
    An ItemData object
    """
    def __init__(self, item, display=None, count=1, df_nbt=None):
        """
        Create a new ItemData object for Item class

        Parameters:
            item - The item to create
            display - The display name for the item. Supports § codes and & codes = None
            count - The number of items in the item stack = 1
            df_nbt - A number of the DF_NBT in the Item object = None

        Examples:
            ```py
            checkpoint_item = ItemData(ItemEnum.EMERALD, "&cReturn to Checkpoint")
            ```
        """
        self.item = item
        self.display = display
        self.count = count
        self.df_nbt = df_nbt
        print(f"Initiated Item {self.item} display {self.display} count {self.count}{f' and df_nbt {self.df_nbt}' if df_nbt else ''}")

    def to_dict(self):
        """
        Returns the dictionary object for the data
        """
        dictionary = {
            "item": "{Count:" + str(self.count) + "b," + (("DF_NBT:" + str(self.df_nbt) + ",") if self.df_nbt else '') + \
                    'id:"minecraft:' + self.item + '"' + (',tag:{display:{' + self.display + '}}' if self.display else '') + \
                    '}'
        }
        return dictionary

class VarData:
    """
    Variable Data
    """
    def __init__(self, name, scope=Code.VAR_GLOBAL):
        """
        Initiates a new VarData

        Parameters:
            name - The name of the variable
            scope - The scope of the variable = Code.VAR_GLOBAL

        No Examples
        """
        self.name = name
        self.scope = scope

    def to_dict(self):
        """
        Pack data into dictionary
        """
        dictionary = {
            "name": self.name,
            "scope": self.scope
        }
        return dictionary

class SoundData:
    """
    A Sound Data for Sounds
    """
    def __init__(self, sound, pitch=1, volume=1):
        """
        Initiates a SoundData

        Parameters:
            sound - The sound name of the sound
            pitch - The pitch of the sound = 1
            volume - The volume of the sound = 2

        No Examples
        """
        self.sound = sound
        self.pitch = pitch
        self.volume = volume

    def to_dict(self):
        """
        Generates dictionary of SoundData
        """
        dictionary = {
            "sound": self.sound,
            "pitch": self.pitch,
            "vol": self.volume
        }
        return dictionary

class NumberData:
    """
    Creates a NumberData
    """
    def __init__(self, num):
        """
        Initiate a NumberData

        Parameters:
            num - The number of the NumberData, could include text codes

        No Examples
        """
        self.num = num

    def to_dict(self):
        """
        Pack NumberData into a dictionary
        """
        dictionary = {
            "name": str(self.num)
        }
        return dictionary

class LocData:
    """
    A location data
    """
    def __init__(self, x, y, z, pitch = 0, yaw = 0):
        """
        Initialize a new LocData object

        Parameters:
            x - The x coordinate of the location
            y - The y coordinate of the location
            z - The z coordinate of the location
            pitch - The pitch of the location
            yaw - The yaw of the location

        No Examples
        """
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw

    def to_dict(self):
        """
        Converts the location to a dictionary
        """
        return {
            "loc": {
                "x": self.x,
                "y": self.y,
                "z": self.z,
                "pitch": self.pitch,
                "yaw": self.yaw
            }
        }

class VecData:
    """
    A new VecData
    """
    def __init__(self, x, y, z):
        """
        Initialize a new VecData

        Parameters:
            x - The x offset for the vector
            y - The y offset for the vector
            z - The z offset for the

        No Examples
        """
        self.x = x
        self.y = y
        self.z = z

    def to_dict(self):
        """
        Pack data into a dictionary
        """
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z
        }

class Item:
    """
    An Item object for chest items
    """
    def __init__(self, id, data):
        """
        Initiate a new Item

        Parameters:
            id - The id of the item
            data - The data of the item

        Examples:
            ```py
            Item(Code.ITEM, ItemData(ItemEnum.STONE))
            ```
        """
        if id == Code.ITEM:
            if not isinstance(data, ItemData):
                raise ValueError(
                    "Expected ItemData in parameter data for id of Code.ITEM"
                )
        if id == Code.VAR:
            if not isinstance(data, VarData):
                raise ValueError(
                    "Expected VarData in parameter data for id of Code.VAR"
                )
        if id == Code.SOUND:
            if not isinstance(data, SoundData):
                raise ValueError(
                    "Expected SoundData in parameter data for id of Code.SOUND"
                )
        if id == Code.NUM:
            if not isinstance(data, NumberData):
                raise ValueError(
                    "Expected NumberData in parameter data for id of Code.NUM"
                )

        self.id = id
        self.data = data

    def to_dict(self):
        """
        Converts Item object to dictionary
        """
        dictionary = {"item": {
            "id": self.id,
            "data": self.data.to_dict() if not isinstance(self.data, dict) else self.data
        }}
        return dictionary

class Tag(Item):
    """
    A Tag object that is responsible for a tag
    """
    def __init__(self, option, tag, action, block):
        """
        Initiates a new Tag object

        Parameters:
            option - Current chosen string
            tag - Tag name
            action - Action / function parent block performs
            block - Category block of parent block

        Examples:
            ```py
            WaitTicks = Tag("Ticks", "Time Unit", "Wait", "control)
            ```
        """
        super().__init__(Code.TAG, {
            "option": option,
            "tag": tag,
            "action": action,
            "block": block
        })
        self.action = action
        self.tag = tag
        self.action = action
        self.block = block

class Object:
    """
    You shouldn't initialize this on your won **UNLESS YOU KNOW WHAT YOU ARE DOING**
    Anyway this is an Object class for objects in templates
    """
    def __init__(self, id=Code.B_BLOCK, items=None, tags=None, **kwargs):
        """
        Initiate a new Object

        Parameters:
            id - The id of the object, either Code.B_BLOCK or Code.B_BRACKET
            items - A list of items in arguments = []
            tags - A list of tags for the object = []
            **kwargs - Additional data

        No examples
        """
        if items is None:
            items = []
        if tags is None:
            tags = []
        self.id = id
        self.data = kwargs
        new_items = []
        for slot, item in enumerate(items):
            a = item
            a["slot"] = slot
            new_items.append(a)
        for slot, tag in enumerate(tags):
            a = tag
            a["slot"] = 26 - slot
            new_items.append(a)
        self.data = self.data | {"args": {"items": new_items}}
        self.items = items
        keys = kwargs.keys()
        if id == Code.B_BLOCK:
            if not "block" in keys:
                raise ValueError(
                    "No \"block\" key found in Object data for id of Code.B_BLOCK"
                )
        if id == Code.B_BRACKET:
            if not "direct" in keys:
                raise ValueError(
                    "No direction found in Object data for id of Code.B_BRACKET"
                )
            elif not "type" in keys:
                raise ValueError(
                    "No type found in Object data for id of Code.B_BRACKET"
                )

        logging.info(f"Initialized an Object {id}, {kwargs}")

    def to_dict(self):
        """
        Converts Object attributes to a dictionary (python's json)
        """
        dictionary = {"id": self.id}
        dictionary = dictionary | self.data
        return dictionary

if __name__ == "__main__":
    obj = Object(block=Code.B_CONTROL, items=[
        Item(Code.NUM, NumberData(5)).to_dict()
    ], tags=[
        Tag("Seconds", "Unit", Actions.Control.WAIT, Code.B_CONTROL).to_dict()
    ], action=Actions.Control.WAIT)
    print(json.dumps(obj.to_dict(), indent=2))
