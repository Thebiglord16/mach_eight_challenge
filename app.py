print("please input the list of numbers separated by commas:")
input_values = input()
input_values = [int(x) for x in input_values.split(",")]
print("please input the target sum")
target = int(input())

scoped_values = []
tuple_array = []
for i in input_values:
    if 12 - i in scoped_values:
        tuple_array.append((i, 12-i))
        scoped_values.append(i)
    else:
        scoped_values.append(i)

print("the pairs of numbers that add up to the target sum are:")
for tuple in tuple_array:
    print(tuple)