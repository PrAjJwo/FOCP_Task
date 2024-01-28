def menu_pizza():
    count = 0
    menu = {
        "Margherita": 10,
        "Pepperoni": 12,
        "Vegetarian": 11,
        "Hawaiian": 13,
        "Chicken": 10,
    }
    print("BPP Pizza Price Calculator")
    print("==========================")
    for pizza, price in menu.items():
        print(f"{count+1}) {pizza}: £{price:}")
        count +=1
    print("==========================")

    while True:
        try:
            user_choice = int(input("Select the pizza you'd like to order : "))
            # if user_choice == 0:
            #     print("Goodbye!")
            #     return None, None
            if 1 <= user_choice <= len(menu):
                pizza_name = list(menu.keys())[user_choice - 1]
                pizza_price = menu[pizza_name]
                return pizza_name, pizza_price
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def pizza_amount():
    while True:
        try:
            amount = int(input("How many Pizza ordered? "))
            if amount == 0:
                print("Please enter a valid value.")
            elif amount < 0:
                print("Please enter a positive integer!")
            else:
                return amount

        # except TypeError:
        #     print("\nPositive integers only\n")

        except ValueError:
            print("Please enter a number!")
            # amount = 1
            # break

    # return amount


def tuesday_check(amount,prize):
    while True:
        prize_1 = prize*amount
        tuesday = input("Is it Tuesday? ")
        tuesday = tuesday.lower()
        if tuesday == "y" or tuesday == "yes":
            prize_final_1 = prize_1 - (prize_1*0.5)
            return prize_final_1
        elif tuesday == "n" or tuesday == "no" or tuesday == "":
            return prize_1
        else:
            print("Please enter (Y/N)")

def app_check(prize_2):
    while True:
        tuesday = str(input("Did the customer use the app? "))
        if tuesday == "y" or tuesday == "yes":
            prize_final_2 = prize_2 - (prize_2*0.25)
            return prize_final_2
        elif tuesday == "n" or tuesday == "no" or tuesday == "":
            return prize_2
        else:
            print("Please enter (Y/N)")
def delivery_check(prize_3):
    while True:
        delivery = str(input("Is delivery required? "))
        if delivery == "y" or delivery == "yes":
            if prize_3 <= 5:
                prize_final = prize_3+2.50
                return prize_final
            else:
                return prize_3
        elif delivery == "n" or delivery == "no" or delivery == "":
            return prize_3

        else:
            print("Please enter (Y/N)")

# def total_prize(amount_final):
#     print(f"Final prize: £{amount_final}")
def billing(selected_pizza, total_bill,num_pizza):

        print("\n==========================")
        print(f"\nOrder Summary:")
        print(f"{num_pizza} {selected_pizza} pizzas: £{total_bill:}")
        print(f"Total Bill: £{total_bill:}\n")
        return total_bill






# def main():
#     while True:
#         selected_pizza, price = menu_pizza()
#
#         if selected_pizza is None:
#             break
#
# if __name__ == "__main__":
#     main()
# print("BPP Pizza Price Calculator")
# print("==========================")
selected_pizza, price = menu_pizza()
number_pizza = pizza_amount()
tuesday_delivery = tuesday_check(number_pizza,price)
app_delivery = app_check(tuesday_delivery)
pizza_delivery = delivery_check(app_delivery)
# total_prize(pizza_delivery)
billing(selected_pizza,price,pizza_delivery,number_pizza)
print("==========================")

