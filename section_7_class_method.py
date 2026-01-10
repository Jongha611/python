class Car:
    
     # init은 초기설정 어트리뷰트를 만드는데, init에 self 외의 파라미터를 넣어놓았다는 것은...
     # ...c = Car() 초기 인스턴스 생성 할당시 인자로 해당 파라미터의 인자 값을...
     # ...넣는다는것을 의미한다.
    def __init__(self, body_type):
        self.body_type = body_type

    def __repr__(self):
        return f'Car({self.body_type} body type)'

    def set_body_type(self, body_type):
        self.body_type = body_type
        
    
    # 클래스메소드(팩토리 메소드)는 만약 self.(= 인스턴스.) 를 사용했다면 직접 인스턴스를 생성할 때 입력해야 했던 옵션값들을...
    # ... 클래스 자체에서 특정 조합으로 미리 넣어두고 사용할 수 있게 해주는 장점이 있다.
    # 이 때, self(= 인스턴스.) 대신 cls(= 클래스.) 를 사용한다.
    @classmethod
    def hyundai(cls):
        return cls("sedan")

    @classmethod
    def ferrari(cls):
        return cls("convertible")
    

# c = Car(body_type="sport")
# c.set_body_type("sedan")
# print(c.body_type)
# print(Car.hyundai())
print(Car.ferrari())


# class methods take a cls parameter that points to the class—and not the object...
# ...instance—when the method is called

# Because the class method only has access to this cls argument, it...
# ...can’t modify object instance state. That would require...
# ...access to self. However, class methods can still modify...
# class state that applies across all instances of the class.