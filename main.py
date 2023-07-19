from abc import ABC, abstractmethod

class Vehicle (ABC):


    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass


class Car (Vehicle):
    def __init__(self,max_speed,current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        print ("car started")

    def stop_engine(self):
        print ("car stopped")

class Sports_car(Car):

    def __init__(self,max_speed,current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed


    def start_engine(self,max_speed):
        return ("car started and max speed = ",max_speed)


    def stop_engine(self,current_speed):
        return ("car stopped and current speed =",current_speed)



#vehicle = Vehicle()
sport_car = Sports_car(max_speed=500,current_speed=0)
car = Car("290","90")
car.stop_engine()

print(sport_car.start_engine(500))
print(sport_car.stop_engine(0))
