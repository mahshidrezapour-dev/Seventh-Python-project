# پروژه هفتم
# سیستم مدیریت هزینه ها
from decimal import Decimal , InvalidOperation
def costs(title=None):
    if title is None:

        title = input("title>>")
    title=title.strip().casefold()
    while not title:
        print("title cannot be empty")
        title=input("title>>").strip().casefold()
    while True:
        try:
            amount = Decimal(input("amount>>"))
#amount.is_finite() رو هم بررسی کنی تا مقادیری مثل NaN و Infinity پذیرفته نشن.
            if not amount.is_finite():
                print("please enter a finite number")
                continue
            if amount <0:
                print("amount cannot be negative")
                continue
            break
        except InvalidOperation:
            print("please enter a valid Decimal number")
    category = input("category>>>").strip().casefold()
    money = {
        "title": title,
        "amount": amount,
        "category": category
    }
    return money


all_costs = {}
while True:
    try:
        i = int(input("how many expenses do you have : "))
        if i <0:
            print("number of expenses cannot be negative")
        else:
            break
    except ValueError:
        print("please enter a valid integer")
total = Decimal("0")
for number in range(i):
    outgo = costs()
    while outgo["title"] in all_costs:
        print("this title already exists")
        outgo=costs()
    all_costs[outgo["title"]] = outgo
    total += outgo["amount"]
print("menue=, add, show all, search, total , category total , delete, exit")
while True:
    search = input("what you looking for? >>>").strip().casefold()
    if search == "add":
        name = input("what do you want to add? >>>").strip().casefold()
        if name in all_costs:
            print("already exists")
        else:
            outgo = costs(name)
            all_costs[outgo["title"]] = outgo
            total += outgo["amount"]
    elif search == "show all":
        if not all_costs:
            print("no expenses recorded")
        else:
            for title , cost in all_costs.items():
                print("-"*30)
                print(f"title : {title}")
                print(f"amount : {cost['amount']}")
                print(f"category:{cost['category']}")
            print("-"*30)
    elif search== "search":
        answer = input("what >>>").strip().casefold()
        if answer in all_costs:
            print(all_costs[answer])
        else:
            print("Not Found")
    elif search== "total":
        print(total)
    elif search== "category total":
        key = input("what category? >>>").strip().casefold()
        total_cost = Decimal("0")
        for cost in all_costs:
            if all_costs[cost]["category"] == key:
                total_cost += all_costs[cost]["amount"]
        print(total_cost)
    elif search== "delete":
        a = input("what do you want to delete? ...").strip().casefold()
        if a not in all_costs:
            print("already Doesn't exist")
        else:
            total -=all_costs[a]["amount"]
            del all_costs[a]
            
            print("successfully deleted")
    elif search== "exit":
        print("exiting...")
        break
    else:
        print("not found")
