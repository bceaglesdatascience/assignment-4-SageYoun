numPurchases = int(input("Number of purchases: "))
salesTax = float(input("Sales tax: "))

customerNames = []
itemCosts = []
i = 1

while i <= numPurchases:
    customer = str(input("Customer: "))
    cost = float(input("Cost: "))
    customerNames.append(customer)
    itemCosts.append(cost)
    i += 1   

def add_tax(itemCosts_list, salesTax_value):
    List = []
    for cost in itemCosts:
        finalCost = cost * (1 + salesTax_value)
        List.append(finalCost)
    return List
newList = add_tax(itemCosts, salesTax)

dictionary = {}
for j in range(numPurchases):
    if customer in dictionary:
        dictionary[customer] += newList[j]
    else:
        dictionary[customerNames[j]] = newList[j]
print(dictionary)
