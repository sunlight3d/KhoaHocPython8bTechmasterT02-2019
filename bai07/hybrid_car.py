from gasoline_car import GasolineCar
from electrical_car import ElectricalCar
from car import Car

class HybridCar(GasolineCar,ElectricalCar):
    def __init__(self, name,color, year,charging_voltage, volume):
        GasolineCar.__init__(self,name, color, year, volume)
        ElectricalCar.__init__(self,name, color, year, charging_voltage)
    def __repr__(self):
        return Car.__repr__(self)+"Charging voltage: "\
            +str(self.charging_voltage)\
            +"volume = " + str(self.volume)
