array = input("digite o array")
array = array.split(" ")

"""for number in array: 
    number = int(number)
    print(type(number))"""

for i  in range (len(array)):
    array[i] = int(array[i])

for i in range (len(array)):
    print(array[i])
    print(type(array[i]))


    
