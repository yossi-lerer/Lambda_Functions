# part 1
# step 1 - Manager son price
manager_son_price = lambda price, is_manager_son: price * 0.8 if is_manager_son == True else price + (price * 0.17)
# step 2 - Final price after discount
final_price = lambda price, discount: price / 100 * (100 - discount)
print(final_price(200, 10))