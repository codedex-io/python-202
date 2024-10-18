# Fruit Cart 🍓
# Codédex

my_fruits = {'apple', 'banana', 'kiwi'}
friend_fruits = {'banana', 'orange', 'grape'}

union_result = my_fruits | friend_fruits
intersection_result = my_fruits & friend_fruits
difference_result = my_fruits - friend_fruits

# Uncomment to check if a fruit is <in> both list
# print('apple' in union_result)  # Output: True
# set3 = {'apple', 'orange'}
# print(set3.issubset(union_result))  # Output: True

print('Union:', union_result)
print('Intersection:', intersection_result)
print("My Fruits - Friend's Fruits:", difference_result)
