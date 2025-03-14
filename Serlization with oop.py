
import pickle

class PickleSerializer:
    def __init__(self):
        pass

    def serialize(self, obj, file_name):
        """Serializes an object and saves it to a file."""
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(obj, file)
            print(f"Object serialized and saved to {file_name}")
        except Exception as e:
            print(f"Error serializing object: {e}")

    def deserialize(self, file_name):
        """Deserializes an object from a file."""
        try:
            with open(file_name, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from {file_name}")
            return obj
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
if __name__ == "__main__":
    serializer = PickleSerializer()
    data = {'name': 'bob', 'age': 30, 'city': 'New York'}
    serializer.serialize(data, 'data.pkl')
    deserialized_data = serializer.deserialize('data.pkl')
    print(deserialized_data)
