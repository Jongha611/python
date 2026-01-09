class Car:

    def __init__(self, body_type):
        self.bodytype = body_type
        
    def __repr__(self):
        return f'Car({self.body_type} body type)'

    def set_body_type(self, body_type):
        self.body_type = body_type