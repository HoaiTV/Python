########################## VONG LAP FOR ##########################

## Cu phap for variable_1,variable_2,....,variable_n in sequence:

	# for-block

iter_ = (x for x in range(3))

for value in iter_:
	print('->',value)

for value,value2,value3 in iter_:
	print('->',value)
	# print('->',value2)
	# print('->',value3)

howkteam = {'name':'Kteam','kter':69}



############3 Cau lenh Break va Continue ########################


for key, value in howkteam.items():
	print(key,'=>',value)
	if key == 'name':
			print('Dictionary have key name')
			break
	else:
		print('Hello World')

#################3 Continue ###############
s = 'Hello World'
for ch in s:
	if ch == ' ':
		continue
	else:
		print('Hello World')


################# Vong lap FOR ELSE ###############

for k in (1,2,3):
	print(k)
else:
	print('Done')

for k in (1,2,3):
	print(k)
	if k %2 == 0:
		break #  thoat han vaong lap For else
else:
	print('Done')

################# Vong lap FOR ELSE ###############

for k in (1,2,3):
	print(k)
else:
	print('Done')

for k in (1,2,3):
	if k %2 == 0:
		print(k)
		continue #  Van chay toi ELSE
else:
	print('Done')

###################################  DAY SO TRONG #######################################

#########################range()##################

k = range(5) # Tao ra 1 danh sach 0->4

print(type(k))
print(k[1])

####################3 Tao 1 day so bat dau bang start va

# cu phap range(start,stop-step,step)

print(list(range(2,5)))
print(list(range(2,-3,-1)))

# Toan tu in kiem tra 1 gia tri trong list hay khong

# cu phap <variable> in <range> => kiem tra <variable> co ton tai trong <range> hay khong. Co return Tre; KHoong return False 

k = range(5)
print(1 in k)
print(6 in k)


lst = [5, (1,2,3),{'abc','xyz'}]

for i in range(len(lst)):
	print(lst[i])

############### Su khac nhau sequence scan

lst =  [1,2,3]
for value in lst:
	value +=1

print(lst)


######indexing scan

lst =  [1,2,3]
for value in range(len(lst)):
	lst[value] +=1

print(lst)


################ Complehension ##########################

# Cu phap: [output-expression for statement optional predicate]

############## output-expression #########################			   ##################statement optional predicate #########
lst =['--'.join((a.capitalize(),b.upper()+c.lower())) for a,b,c in [('hello','World','Planet'),('chung','ta','la mot')]]
print(lst)
 ########## 1 Cach thong thuong nhu sau

danhsach = []

for a,b,c in [('hello','World','Planet'),('chung','ta','la mot')]:
 	a = a.capitalize()
 	b = b.upper()
 	c.lower()
 	danhsach.append('**'.join((a,b+c))) ##Python program to demonstrate the use of join function to join list elements with a character. noi cac phan tu bang ky tu '--'

print(danhsach)

lst ={key:value +1 for key,value in (('Kteam',69),('Teo',50),('Zona',23),('HB',2018)) if value %2 !=0}
print(lst)

###############################
# enumerate(iterable[, start])

studien_list = ['Hello','World','BK','VN']

gen = enumerate(studien_list)
print(list(gen))

for index, student in enumerate(studien_list):
	print(index,'=>',student)
























