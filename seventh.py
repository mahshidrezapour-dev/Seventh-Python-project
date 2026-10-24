# پروژه هفتم
# سیستم مدیریت هزینه ها
def costs(title=None):
    if title is None:

        title = input("title>>")
    amount = int(input("amount>>"))
    category = input("category>>>")
    money = {
        "title": title,
        "amount": amount,
        "category": category
    }
    return money


all_costs = {}
i = int(input("how many categories do you have : "))
total = 0
for number in range(i):
    outgo = costs()
    all_costs[outgo["title"]] = outgo
    total += outgo["amount"]
    # menue=
    # add
# show all
# search
# total مجموع همه هزینه ها
# category total مجموع هزینه های یک دسته خاص
# delete
# exit

while True:
    search = input("what you looking for? >>>")
    if search.lower() == "add":
        name = input("what do you want to add? >>>")
        if name in all_costs:
            print("already exists")
        else:
            outgo = costs(name)
            all_costs[outgo["title"]] = outgo
            total += outgo["amount"]
    elif search.lower() == "show all":
        print(all_costs)
    elif search.lower() == "search":
        answer = input("what >>>")
        if answer in all_costs:
            print(all_costs[answer])
        else:
            print("Not Found")
    elif search.lower() == "total":
        print(total)
    elif search.lower() == "category total":
        key = input("what category? >>>")
        total_cost = 0
        for cost in all_costs:
            if all_costs[cost]["category"] == key:
                total_cost += all_costs[cost]["amount"]
        print(total_cost)
    elif search.lower() == "delete":
        a = input("what do you want to delete? ...")
        if a not in all_costs:
            print("already Doesn't exist")
        else:
            total -=all_costs[a]["amount"]
            del all_costs[a]
            
            print("successfully deleted")
    elif search.lower() == "exit":
        print("exiting...")
        break
    else:
        print("not found")