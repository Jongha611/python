class Car():
    def __init__(self, body_type):
        self.body_type = body_type
        
    def __repr__(self):
        return f"Car({self.body_type} body type)"
    
    def set_body_type(self, body_type):
        self.body_type = body_type

    @classmethod
    def hyundai(cls):
        return cls("sedan")
    @classmethod
    def ferrari(cls):
        return cls("convertible")
    

c = Car(body_type="sport")
c.set_body_type("sedan")

print(c.body_type)