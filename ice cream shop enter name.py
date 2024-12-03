''''''

from breezypythongui import EasyFrame

class IceCreamShopNameEntry(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title=" Ice Cream Shop Name Entry")

        #Promps the user to add a nmae to their order.

        self.messageLabel = self.addLabel(text= "Please enter your name for your order.", row=0, column=0, columnspan= 2, sticky= "NWES")

        self.namelabel = self.addLabel(text="Name:", row=1, column=0, sticky= "NSEW")
        self.nameInput = self.addTextField(text="", row=1, column=1, sticky="NSEW")

        #Adds back and Next buttons

        self.backbtn = self.addButton(text= "BACK", row=2, column=0)

        self.nextbtn = self.addButton(text="NEXT", row=2, column=1)





def main():

    IceCreamShopNameEntry().mainloop()

if __name__ == "__main__":
    main()
                           
                        
                           