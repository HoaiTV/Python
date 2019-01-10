#Duoc gio han boi cap ngoac ()
print('*************************TUPE*********************')

print('Day tupe rong')
tup = ()
print(tup) #Dau tupe rong

print('Day khong phai la tupe chi xem day la 1 bien nguyen')
tup = (1)
print(tup) # day khong phai la 

print('Tao 1 tupe = cac phan tu cach nhau bang dau , va duoc gioi han trong dau ()')
tup = (1,1,3,4,5,6,7)
print(tup) # 


print('Complehensive tuple')
a = tuple(i for i in range(10))
print(a) 

print('*********************')
a = tuple([1,2,3])
print(a) 
a = tuple((1,2,3))
print(a)

a = tuple('HELLO WORLD')
print(a)
print('***********MOT SO TOAN TU CUA TUPLE (GIONG CUA CHUOI)**********')

print('Toan tu + 2 tupe')
tup = (1,2,3)
a = tup + (4,5,6)
print(tup)
print(a)

print('Toan tu x tuple voi 1 so')

tup = (1,2,3)
a = tup * 2
print(tup)
print(a)

print('Toan tu Truy xuat index trong tuple <tuple>[<position>] => Laays gia tri cua <tuple> tai <position>' )

tup = (1,2,3)
a = tup[1] # 
print(tup)
print(a)

print('Toan tu len(<tuple>)=>Kiem tra tuple co bao nhieu phan tu')

tup = (1,2,3,(3,6))
a = len(tup)
print(tup)
print(a)

print('Toan tu Dao nguoc tuple <tuple>[::-1]=>Kiem tra tuple co bao nhieu phan tu')

tup = (1,2,3,(3,6))
a = tup[::-1]
print(tup)
print(a)

print('Toan tu <tuple>[:<position>]=> Lay nhieu phan tu trong tuple ')

print('<position> > 0 => Lay cac phan tu tu ben trai sang toi <position> ')
print('<position> < 0 => Lay cac phan tu tu ben trai  sang toi <position>  ')
print('<position> < 0 => Phan tu cuoi cung cua tuple la -1 ')



tup = (1,2,3,(3,6))
a = tup[:0]
b = tup[:1]
c = tup[:2]
d = tup[:3]
e = tup[:-1]
f = tup[:-2]
g = tup[:-3]

print(tup)
print(a)
print(b)
print(c)
print(d)

print('Print <position < 0')

print(e)
print(f)
print(g)

print('********** KHONG THE GIA TRI THAY DOI NOI DUNG TRONG TUPLE ******************')

print('*****************MA TRAN TUPLE******************************')


print('*****************PHUONG THUC CUA TUPLE******************************')

print('Phuong thuc count: <tuple>.count(<value>) => Dem xem <value> xuat hien bao nhieu lan trong <tuple>')

tup =([3,6],4,5,6)

a = tup.count(4)

print(tup)
print(a)

print('Phuong thuc index: <tuple>.index(<value>) => Lay ra vi tri xuat hienj cua <value> trong <tuple>')
print('Neu <value> khong co trong tuple => lenh nay se bao loi')

tup =([3,6],4,5,6)
a = tup.index(4)
print(tup)
print(a)

# tuple khong cho phep sua noi dung <> List cho phep sua noi dung.
# Toc do truy xuat tuple nhanh hon list.
# Dung luong chiem trong bo nho nho hon list.
# Bao ve du lieu cua ban se khong the thay doi.
# Co the dung lam key cua dictionary.


























