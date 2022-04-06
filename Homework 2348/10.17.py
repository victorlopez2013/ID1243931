#Victor Lopez
#PSID: 1243931

class Item_Purchase:
    def __init__(self):
        self.i_n = 'none'
        self.i_p = 0
        self.i_q = 0

    def p_i_c(self):
        print(self.i_n + " " + str(self.i_q) + " @ $" + str(self.i_p) + " = $" + str(self.i_p * self.i_q))


if __name__ == "__main__":
    print("Item 1")
    i1 = Item_Purchase()
    i2 = Item_Purchase()

    i1.i_n = input("Enter the item name:\n")
    i1.i_p = int(input("Enter the item price:\n"))
    i1.i_q = int(input("Enter the item quantity:\n"))
    print()

    print("Item 2")
    i2.i_n = input("Enter the item name:\n")
    i2.i_p = int(input("Enter the item price:\n"))
    i2.i_q = int(input("Enter the item quantity:\n"))
    print()

    print("TOTAL COST")
    i1.p_i_c()
    i2.p_i_c()
    print()
    total = (i1.i_q * i1.i_p + i2.i_q * i2.i_p)
    print("Total: $" + str(total))