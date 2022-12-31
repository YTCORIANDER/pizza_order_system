from Assign2 import pizzaReceipt

flavour = ["ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER",
           "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE"]
pizzaList = []


def orderOnePizza():
    pizza = ["0", "0"]
    sizes = ["S", "M", "L", "XL"]
    newOrder = ""
    toppings = []
    chooseSize = input("Choose a size: S, M, L or XL:  ")
    chooseSize = chooseSize.upper()
    if chooseSize in sizes:
        pizza[0] = chooseSize
        request = input("Type in one of our toppings to add it to your pizza."
                        "To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X'")
        newTopping = requestChecking(request, toppings)

        pizza[1] = newTopping
    else:
        orderOnePizza()
    return pizza


def requestChecking(checkRequest, toppings):
    checkRequest = checkRequest.upper()
    if checkRequest == "LIST":
        print(flavour)
        newRequest = input(
            "Type in one of our toppings to add it to your pizza."
            "To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X")
        requestChecking(newRequest, toppings)

    if checkRequest in flavour:
        print("Added " + checkRequest + " to your pizza")
        toppings.append(checkRequest)
        print(toppings)
        newTopping = input(
            "Type in one of our toppings to add it to your pizza."
            "To see the list of toppings, enter 'LIST'. When you are done adding toppings, enter 'X'")
        requestChecking(newTopping, toppings)
        return toppings


def main():
    q = input("Do you want to order a pizza?")
    q = q.upper()
    if q == "YES":
        newPizza = tuple(orderOnePizza())
        pizzaList.append(newPizza)
        isNewPizza = input("Do you want to continue ordering?")
        if isNewPizza.upper() == "YES":
            pizzaTwo = tuple(orderOnePizza())
            pizzaList.append(pizzaTwo)
            isNewPizza = input("Do you want to continue ordering?")
            if isNewPizza.upper() == "YES":
                pizzaThree = tuple(orderOnePizza())
                pizzaList.append(pizzaThree)
                isNewPizza = input("Do you want to continue ordering?")
                if isNewPizza.upper() == "YES":
                    pizzaFour = tuple(orderOnePizza())
                    pizzaList.append(pizzaFour)
                    isNewPizza = input("Do you want to continue ordering?")
                    if isNewPizza.upper() == "YES":
                        pizzaFour = tuple(orderOnePizza())
                        pizzaList.append(pizzaFour)
                        isNewPizza = input("Do you want to continue ordering?")
                        if isNewPizza.upper() == "YES":
                            pizzaFour = tuple(orderOnePizza())
                            pizzaList.append(pizzaFour)
                        else:
                            pizzaReceipt.generateReceipt(pizzaList)
                    else:
                        pizzaReceipt.generateReceipt(pizzaList)
                else:
                    pizzaReceipt.generateReceipt(pizzaList)
            else:
                pizzaReceipt.generateReceipt(pizzaList)
        else:
            pizzaReceipt.generateReceipt(pizzaList)
    else:
        pizzaReceipt.generateReceipt(pizzaList)


main()
