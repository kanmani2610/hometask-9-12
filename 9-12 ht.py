class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
    
    def take_photo(self):
        print(f"Taking a photo with resolution: {self.resolution} MP")
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    
    def make_call(self, number):
        print(f"Calling {number} from {self.phone_number}")
    
    def send_message(self, number, message):
        print(f"Sending message to {number} from {self.phone_number}: {message}")
class Smartphone(Camera, Phone):
    def __init__(self, resolution, phone_number, brand, model):
        Camera.__init__(self, resolution)
        Phone.__init__(self, phone_number)
        self.brand = brand
        self.model = model
    
    def display_device_information(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
        print(f"Camera Resolution: {self.resolution} MP")
        print(f"Phone Number: {self.phone_number}")
smartphone = Smartphone(resolution=108, phone_number="123-456-7890", brand="XYZ", model="Galaxy Pro")
smartphone.display_device_information()
smartphone.take_photo()
smartphone.make_call("987-654-3210")
smartphone.send_message("987-654-3210", "Hello! How are you?")
