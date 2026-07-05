# part 1
# step 1 - Manager son price
manager_son_price = lambda price, is_manager_son: price * 0.8 if is_manager_son == True else price + (price * 0.17)
# step 2 - Final price after discount
final_price = lambda price, discount: price / 100 * (100 - discount)
# step 3 - Full name
full_name = lambda first_name, last_name: f"{first_name} {last_name}" 
# step 4 - Grade status
grade_status = lambda grade: "pass" if grade >= 55 else "fail"
# step 5 - Larger number
larger = lambda num1, num2: num1 if num1 > num2 else num2
# step 6 - Distance from 10
distance_from_10 = lambda num1: 10 - num1 if num1 < 10 else num1 - 10
