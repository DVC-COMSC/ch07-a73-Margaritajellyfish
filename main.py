

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
for i in range(len(numbers)):
    if insval < numbers[i]:
        numbers.insert(i, insval)
if len(numbers) == 5:
    numbers.append(insval)
# ******************************
# Make your Code
# ******************************

print (numbers)
