from crop_class import *

class Potato(Crop):
    """A potato crop"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for potatoe
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self.type = "Potato"
    #override grow method for subclass
    def grow(self,light,water):
        if light >= self.light_need and water >= self.water_need:
            if self.status == "Seedling" and water > self.water_need:
                self.growth += self.growth_rate * 1.5
            elif self.status == "Young" and water > self.water_need:
                self.growth += self.growth_rate * 1.25
            else:
                self.growth += self.growth_rate
        #increament day growing
        self.days_growing += 1
        #update the status
        self.update_status()

def main():
    #create a new potato crop
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())

if __name__ == "__main__":
    main()