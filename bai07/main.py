from car import Car
from electrical_car import ElectricalCar
from gasoline_car import GasolineCar
from hybrid_car import HybridCar

car1 = Car("Toyoto", "yellow", 2017)
electrical_car1 = ElectricalCar("Toyoto2", "red", 2018, 220)
print(str(car1))
print(str(electrical_car1))

hybrid_car1 = HybridCar("Toyoto3", "green", 2019, 230, 1000)
print(str(hybrid_car1))