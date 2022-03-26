# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.
# users = [{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name": "Yeti"}]
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}, ]
print(f"Users: \n {users} \n")

users_from_poland = [user for user in users if user.get('country', '') == 'Poland']
print(f"Name(s) of user(s) from Poland: \n {users_from_poland} \n")


# Display sum of first ten elements starting from element 5:
# numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
sum_of_10_elements_starting_with_5 = 0
for n in range(numbers.index(5), numbers.index(5)+9):
    sum_of_10_elements_starting_with_5 += n
print(f"Sum of first ten elements starting from element 5: \n {sum_of_10_elements_starting_with_5} \n")


# Fill list with powers of 2, n [1..20]
squares = []
for n in range(1, 21):
    squares.append(n ** 2)
print(f"List of powers of 2, n [1..20]: \n"
      f"{squares}")
