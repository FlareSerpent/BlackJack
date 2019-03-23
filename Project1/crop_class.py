import random

class Crop:
    """ A Generic Food Crop"""

    #constructor
    def __init__(self,growth_rate,light_need,water_need):
        #set attributes with initial value

        self.growth = 0
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.light_need = light_need
        self.water_need = water_need
        self.status = "Seed"
        self.type = "Generic"

    def needs(self):
        #return a dictionary containing the light and water needs
        return{'light need': self.light_need,'water need':self.water_need}

    def report(self):
        return{'type':self.type,'status':self.status,'growth':self.growth,'days growing':self.days_growing}

    def update_status(self):
        if self.growth > 15:
            self.status = "Old"
        elif self.growth > 10:
            self.status = "Mature"
        elif self.growth > 5:
            self.status = "Young"
        elif self.growth > 0:
            self.status = "Seedling"
        elif self.growth == 0:
            self.status = "Seed"


    def grow(self,light,water):
        if light >= self.light_need and water >= self.water_need:
            self.growth += self.growth_rate
        self.days_growing += 1
        self.update_status()

def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)
def manual_grow(crop):
    #get the light and water values from the user
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered is not valid - please enter a valid between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered is not valid - please enter a valid between 1 and 10")
    #grow the crop
    crop.grow(light,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu. ")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return (choice)

def manage_crop(crop):
    print("This is the crop management program")
    print()
    exit = False
    while not exit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop,30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            exit = True
            print()
    print("Thank you for using our the crop management program")
def main():
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)


if __name__ == "__main__":
    main()