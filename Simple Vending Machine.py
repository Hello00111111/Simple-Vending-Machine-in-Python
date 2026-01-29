print(f" {'Product Name':14}{'Price':7}")
print(f" {'Coca Cola':14}{'$1.5':7}")
print(f" {'Sprite':14}{'$2.0':7}")
print(f" {'Ginger Ale':14}{'$2.0':7}")
print(f" {'Hot Chocolate':14}{'$3.5':7}")
product_list= {"Coca Cola $1.5" : 1,"Sprite $2.0" : 2, "Ginger Ale $2.0" : 3, 
                "Hot Chocolate $3.5" : 4}
print(product_list)
total_price = []
car = []

while True:
 desired_product = int(input("Input the code of the product. Press 0 to pay."))
 if desired_product == 1:
    total_price.append(1.5)
    car.append("Coca Cola")
 elif desired_product == 2:
    total_price.append(2)
    car.append("Sprite")
 elif desired_product == 3:
    total_price.append(2)
    car.append("Ginger Ale")
 elif desired_product == 4:
    total_price.append(3.5)
    car.append("Hot Chocolate")
 elif desired_product == 0:
    break
 else:
    print("Invalid Code")

print("You have selected", car, ". Here is the total cost: $", sum(total_price))
money = float(input("How much money do you have?"))
if money < sum(total_price):
   print("You don't have enough money.")
elif money > sum(total_price):
   change = money - sum(total_price)
   print("Thanks for purchashing. Your change is $", change)
else:
   print("You have selected", car, ". Thanks for purchasing!")




