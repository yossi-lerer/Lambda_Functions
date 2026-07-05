# part 1
# step 1 - Manager son price
manager_son_price = lambda price, is_manager_son: price * 0.8 if is_manager_son == True else price + (price * 0.17)
print(manager_son_price(100, True))
# step 2 - Final price after discount
final_price = lambda price, discount: price / 100 * (100 - discount) if 0 < discount <= 100 else None
print(final_price(100, 20))
# step 3 - Full name
full_name = lambda first_name, last_name: f"{first_name} {last_name}" 
print(full_name("Dana", "Levi"))
# step 4 - Grade status
grade_status = lambda grade: "pass" if grade >= 55 else "fail"
print(grade_status(80))
# step 5 - Larger number
larger = lambda num1, num2: num1 if num1 > num2 else num2
print(larger(10, 7))
# step 6 - Distance from 10
distance_from_10 = lambda num1: 10 - num1 if num1 < 10 else num1 - 10
print(distance_from_10(7))
# step 7 - Get item total
item_total = lambda item: f'total price of the item: {item["price"] * item["amount"]}'
print(item_total({"name": "Pen", "price": 5, "amount": 10}))
# step 8 - Turn a regular complex function into a lambda
shipping_cost = lambda weight, express: 50 if express and weight > 5 else 30 if express else 25 if weight > 5 else 10 
print(shipping_cost(3, True))
print(shipping_cost(8, True))
print(shipping_cost(8, False))
print(shipping_cost(2, False))
# step 9 - Turn a regular complex function into a lambda
access_message = lambda age, has_ticket, is_vip: "vip entrance" if is_vip else "regular entrance" if age >= 18 and has_ticket else "buy ticket" if age >= 18 else "too young"
print(access_message(25, True, False))
print(access_message(25, False, False))
print(access_message(15, True, False))