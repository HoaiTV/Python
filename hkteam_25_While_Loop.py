#################################### WHILE LOOP TRONG PYTHON ######################################

# Cau truc vong lap while

# while <condtion>:
	#while-block

k = 4

while k > 0:
	print('k=',k)
	k-=1

s = 'Hello World'

idx = 0

length = len(s)

while idx < length:
	print(idx,'stands for',s[idx])
	idx+=1


########################## CAU LENH BREAK KET THUC VONG LAP ####################################

five_even_numbers = []

k_number = 1

while True:
	if k_number % 2 == 0:
		five_even_numbers.append(k_number)
	if len(five_even_numbers) == 5:
		break
	k_number +=1

print(five_even_numbers)
print(k_number)

########################## CAU LENH CONTINUE KET THUC VONG LAP ####################################

five_even_numbers = []

k_number = 1

while k_number < 10:
	k_number += 1
	if k_number % 2 == 0:
		continue
	print(k_number,'La so le')

########################## CAU TRUC WHILE ELSE ####################################

k_number = 0

while k_number < 3:
	print('value of k_number la ',k_number)
	k_number += 1
	if k_number == 2:
		print('Thoat khoi vong lap While else')
		break
else:
	print('Da hoan thanh vong lap k_number < 3')




