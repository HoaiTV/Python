# Kieu du lieu SET

# Duoc gioi han boi  {}

# Cac phan tu cach nhau boi dau <,>

# SET khong chua nhieu hon 1 phan tu trung lap

# SET chi chua Hashable Object nhung no khong phai Hashable object, Do do khong chua 1 set trong 1 set.

set_1 = {1,4}
set_2 = {'Hello World','Hello World'}
print(set_1)
print(type(set_1))
print(set_2)
print(type(set_2))

# Su dung comprehension Set

print('Su dung Comprehension SET')
set_3 = {i for i in range(4)}
print(set_3)
print(type(set_3))

# Su dung contracter for set.
print('Su dung Contracter for Set')


set_2 = set((1,2,3))
print(set_2)
print(type(set_2))

set_2 = set(('Hello World'))
print(set_2)
print(type(set_2))

print('******************Toan tu trong SET****************')

print('Toan tu <value>in{<set>}=> kiem tra <value> co trong <set> hay khong? if have => return True; If ')

print(2 in {6,7,8,3,2,6,8})
print((3,4) in {5,3,4,(3,4)})

print('Toan tu tru  <set_1>-<set_2> => tao ra 1 set moi ma cos phan tu cho ton taij trong <set_1> ma khong co trong <set_2>')

print({1,2,3,4}- {2,3})

print('Toan tu &  <set_1>&<set_2> => tao ra 1 set moi ma cos phan tu trong vua ton tai trong <set_1> va <set_2>')
print({1,2,3,4} & {2,3})

print('Toan tu |  <set_1>|<set_2> => tao ra 1 set moi ma bao gom cac phan tu  trong <set_1> va <set_2>')
print({1,2,3,4}|{2,3})

print('Toan tu XOR  <set_1>^<set_2> => tao ra 1 set moi ma bao gom cac phan tu CHI TON TAI   trong <set_1> va <set_2>')
print({1,2,3,4}^{2,3})

print('***************************Phuong thuc Trong SET******************')

print('Phuong thuc clear')

set1 = {1,2,3}

set1.clear()

print('Phuong thuc <set>.pop()=> lay ra trong set phan tu dau tien va xoa phan tu nay trong <set>')

set1 = {1,2,3}
print(set1)
print(set1.pop())

print('Phuong thuc <set>.remove(<value>)=> Xoa phan tu <value> co trong <set>')

set1 = {1,2,3}
set1.remove(2)
print(set1)

print('Phuong thuc <set>.discard(<value>)=> loai bo <value> neu co trong <set>')

set1 = {1,2,3}
set1.discard(4)
print(set1)

print('Phuong thuc <set>.copy()=> loai bo <value> neu co trong <set>')

set1 = {1,2,3}
set2 = set1.copy()
print(set1)
print(set2)

print('Phuong thuc <set>.add(<value>)=> Them <value> neu co trong <set>')

set1 = {1,2,3}
set1.add(4)
print(set1)
print(set2)






