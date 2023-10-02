# for num in range(1, 21):
#     print(num)

# for num in range(1, 1_000_001):
#     print(num)

# one_million = list(range(1, 1_000_001))
# print(f"The smallest number in the list is {min(one_million)}, and the largest is {max(one_million)}")
# print(f"The sum of all numbers from one to a million is {sum(one_million)}.")

# odd = list(range(1, 21, 2))
# for _ in odd:
#     print(_,sep="",end=" ")

# threes = list(range(3, 31, 3))
# for _ in threes:
#     print(_,sep="",end=" ")

# cubes = list(range(1, 11))
# for _ in cubes:
#     print(_ ** 3, end = " ")

## write as a list comprehension
cubes = [cube**3 for cube in range(1, 11)]
for cube in cubes:
    print(cube)