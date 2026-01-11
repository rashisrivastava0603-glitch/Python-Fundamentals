
Distance = int(input("Enter a Distance:"))
if(Distance<3):
    mode="walk"
    print(mode)
elif(3<Distance<15):
    mode="Bike"
    print(mode)
else:
    mode="Car"
    print(mode)