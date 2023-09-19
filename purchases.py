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
    finalCosts = []
    for cost in itemCosts:
        finalCost = cost * (1 + salesTax_value)
        finalCosts.append(finalCost)
    return finalCosts
newList = add_tax(itemCosts, salesTax)

dictionary = {}
for j in range(numPurchases):
    if customer[j] in dictionary:
        dictionary[customerNames[j]] += newList[j]
    else:
        dictionary[customerNames[j]] = newList[j]
print(dictionary)
