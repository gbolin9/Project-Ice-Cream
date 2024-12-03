''''''

from breezypythongui import EasyFrame

class IceCreamShopOrder(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title= "Ice Cream Shop")

        self.welcomeLabel = self.addLabel(text= "Welcome. Press start order to begin.", row=0, column=0, sticky= "NSEW")

        self.picturePlaceHolderLabel = self.addLabel(text= "This is where a picture will go.", row=1, column=0, columnspan=4,sticky="NSEW")

        self.startOrderbtn = self.addButton(text= "START ORDER", row=2, column=0, columnspan= 2)









def main():

    IceCreamShopOrder().mainloop()

if __name__ == "__main__":
    main()
        