def checkPrice(pizza):
    size = pizza[0]
    if pizza[1] is None or len(pizza[1]) < 4:
        toppingNumbers = 3
    else:
        toppingNumbers = len(pizza[1])
    if size == 'S':
        baseCost = 7.99
        extraCost = (toppingNumbers - 3) * 0.5
    elif size == 'M':
        baseCost = 9.99
        extraCost = (toppingNumbers - 3) * 0.75
    elif size == 'L':
        baseCost = 11.99
        extraCost = (toppingNumbers - 3)
    elif size == 'XL':
        baseCost = 13.99
        extraCost = (toppingNumbers - 3) * 1.25
    if extraCost < 0:
        extraCost = 0
    totalPrice = baseCost + extraCost
    return baseCost, extraCost, totalPrice


def generateReceipt(pizzaOrder):
    if len(pizzaOrder) == 0:  # how to check "", test 1 always fail
        print("You did not order anything")
    else:
        print("Your order: ")
        count = 0
        price = 0
        for pizza in pizzaOrder:
            count = count + 1
            costBase, costExtra, wholePrice = checkPrice(pizza)
            print(
                "Pizza %d:  %s " % (count, pizza[0]) + str(costBase))  # how to align the prices on the rightest column?
            price = price + wholePrice
            if pizza[1] is None:
                print("No toppings")
            else:
                # print(pizza[1])
                for toppings in pizza[1]:
                    print("-%s" % toppings)
                if costExtra != 0:
                    print("Extra Topping " + "(" + (pizza[0]) + ")\t" + (str(costExtra)))
            tax = price * 0.13
            price = price + tax
            print("Tax: %.2f\nTotal: %.2f\n" % (tax, price))

# generateReceipt([('L',['HAM', 'BACON', 'ONION', 'TOMATO']),
# ('S', ['PEPPERONI', 'SAUSAGE', 'CHICKEN', 'HAM']), ('L', ['BROCCOLI', 'CHICKEN', 'ONION'])])
# generateReceipt([""])
