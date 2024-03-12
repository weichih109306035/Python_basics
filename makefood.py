def make_icecream(*toppings):
    print("冰淇淋配料如下")
    for topping in toppings:
        print("---",topping)
def make_drink(size,kind):
    print("所點飲料如下")
    print("---",size.title())
    print("---",kind.title())
