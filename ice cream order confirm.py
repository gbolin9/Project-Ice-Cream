''''''

from breezypythongui import EasyFrame

class IceCreamShopOrderConfirm(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title=" Ice Cream Shop Name Entry")


        self.orderconfirm = self.addLabel(text= "Would you like to confirm this order?", row=0, column=0, columnspan=2)

        self.orderName = self.addLabel(text= "Name", row=1, column=0, sticky="NWSE")

        self.nameOutput = self.addLabel(text= "", row=1, column=1, sticky= "NSEW")

        self.containerLabel = self.addLabel(text= "Container", row=2, column=0, sticky= "NSEW")

        self.containerOutput = self.addLabel(text="", row=2, column=1, sticky= "NSEW")

        self.flavorLable = self.addLabel(text= "Flavor", row=3, column=0, sticky= "NSEW")

        self.flavorOut = self.addLabel(text="", row=3, column=2, sticky= "NSEW")

        self.toppingsLable = self.addLabel(text= "Toppings", row=4, column=0, sticky= "NSEW")
        
        self.toppingsOutput = self.addLabel(text= "", row=4, column=1, sticky="NSEW")

        self.priceLabel = self.addLabel(text= "Price", row= 5, column= 0, sticky= "NSEW")

        self.priceOutput = self.addLabel (text= "", row=5, column= 1, sticky= "NSEW" )


        #Add confirm and back buttons

        self.backbtn = self.addButton(text= "BACK", row=6, column= 0)

        self.confirmbtn = self.addButton(text="CONFIRM", row= 6, column= 1)


                                       





def main():

    IceCreamShopOrderConfirm().mainloop()

if __name__ == "__main__":
    main()