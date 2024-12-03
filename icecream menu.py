''''''

from breezypythongui import EasyFrame

class IceCreamShopMenu(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title= "Ice Cream Shop Menu")

        #Sets up the container options.

        self.containterlabel = self.addLabel(text= "Containter", row=0, column= 0, sticky="NSEW")

        self.containergroup = self.addRadiobuttonGroup(row= 1, column= 0, rowspan= 3)

        defaultRB = self.containergroup.addRadiobutton(text="Regular Cone: $0.99")
        self.containergroup.setSelectedButton(defaultRB)

        self.containergroup.addRadiobutton(text="Waffle Cone: $2.99")

        self.containergroup.addRadiobutton(text= "Bowl: $1.50")

        #Sets up the flavor options

        self.flavorlable = self.addLabel(text= "Flavor", row=0, column=1, sticky= "NSEW")

        self.flavorGroup = self.addRadiobuttonGroup(row=1, column=1, rowspan=3)

        defaultRB = self.flavorGroup.addRadiobutton(text= "Vanilla: $1.00")
        self.flavorGroup.setSelectedButton(defaultRB)  

        self.flavorGroup.addRadiobutton(text= "Chocolate: $1.00")

        self.flavorGroup.addRadiobutton(text= "Swirl: $1.00")

        #sets up the toppings options

        self.toppingslabel = self.addLabel(text= "Topping", row=0, column=2, sticky="NSEW")

        self.toppingsGroup = self.addRadiobuttonGroup(row=1,column=2, rowspan=4)

        defaultRB = self.toppingsGroup.addRadiobutton(text= "none: $0.00")

        self.toppingsGroup.setSelectedButton(defaultRB)

        self.toppingsGroup.addRadiobutton(text= "Chocloage Syrup: $0.99")

        self.toppingsGroup.addRadiobutton(text= "Sprinkles: $.50")\
        
        self.toppingsGroup.addRadiobutton(text= "Cookie Crumble: $2.00")

        #Adds Buttons

        self.backbtn = self.addButton(text="BACK", row= 5, column= 0)

        self.nextbtn = self.addButton(text="NEXT", row=5, column=2)




def main():

    IceCreamShopMenu().mainloop()

if __name__ == "__main__":
    main()