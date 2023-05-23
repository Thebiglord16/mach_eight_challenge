print("please input the list of numbers separated by commas:")
tuple_array = []
scoped_values = set()
input_values = {int(x) for x in input().split(",")}
print("please input the target sum")
target = int(input())


tuple_array = []
for i in input_values:
    if target - i in scoped_values:
        tuple_array.append((i, target-i))
        scoped_values.add(i)
    else:
        scoped_values.add(i)

print("the pairs of numbers that add up to the target sum are:")
for tuple in tuple_array:
    print(tuple)