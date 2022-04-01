name = str(input('what is your name')) # input your name
reversed_name = name[:: -1] #slicng method, takes the entire string and reverse it
print(reversed_name)#result

another_name = str(input('input any string'))
reversed_another_name = ''
for i in another_name:
    reversed_another_name = i + reversed_another_name
    print(reversed_another_name)
print(reversed_another_name)



