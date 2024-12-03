''''''

from breezypythongui import EasyFrame

class IceCreamShopOrderEndMessage(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title=" Ice Cream Shop End Message")

        estimatedDeliveryTime = 15

        self.thankYouMessage = self.addLabel(text="Thank you for ordering.", row=0, column=0, columnspan=2, sticky="NSEW")

        self.placeHolder = self.addLabel(text= "This is where a picture will go", row=1, column= 0, columnspan= 2, sticky= "NSEW")

        self.estimatedtime = self.addLabel(text="Your estimated wait time will be " + str(estimatedDeliveryTime) + " minutes", row=2, column= 0, columnspan= 2, sticky= "NSEW")


        #Add an exit button

        self.exitbun = self.addButton(text= "EXIT", row= 3, column= 0)






def main():

    IceCreamShopOrderEndMessage().mainloop()

if __name__ == "__main__":
    main()
