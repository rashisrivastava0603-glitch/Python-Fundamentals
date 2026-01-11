age=int(input("Enter age:"))
day = input(("Enter day:"))
if(age>=18):
    Ticket_price= 12
    print(Ticket_price)
else:
    Ticket_price=8
    print(Ticket_price)
if day == "Wednesday":
    Ticket_price = Ticket_price-2
    print(Ticket_price)

