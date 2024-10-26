#!/usr/bin/python3
"""
Module base.

This module defines the class Base.

The Base class will be the parent class for subsequent child classes
in this project.
"""
json = __import__("json")
csv = __import__("csv")
os = __import__("os")


class Base:
    """Manages id attributes in classes derived from Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes already set from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file containing JSON string."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r', encoding="utf-8") as f:
                json_string = f.read()
        except FileNotFoundError:
            return ([])

        list_dictionaries = cls.from_json_string(json_string)
        return ([cls.create(**dictionary) for dictionary in list_dictionaries])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves a list of objects to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            wrt = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    wrt.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    wrt.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and loads a list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return ([])

        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            instances = []
            if cls.__name__ == "Rectangle":
                for row in reader:
                    id_value = int(row[0])
                    width = int(row[1])
                    height = int(row[2])
                    x = int(row[3])
                    y = int(row[4])
                    instance = cls(width, height, x, y, id_value)
                    instances.append(instance)
            elif cls.__name__ == "Square":
                for row in reader:
                    id_value = int(row[0])
                    size = int(row[1])
                    x = int(row[2])
                    y = int(row[3])
                    instance = cls(size, x, y)
                    instances.append(instance)
        return (instances)
