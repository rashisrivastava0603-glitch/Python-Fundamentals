order_size=input("Enter order_size:")
extra_shot=True
if(order_size  ==  " small "):
    coffee = order_size  +  "with an extra shot"
    print(coffee)
elif(order_size == "medium"):
    coffee = order_size + " coffee "
    print(coffee)
else:
    coffee = order_size  +  " coffee "
    print("order:",coffee)