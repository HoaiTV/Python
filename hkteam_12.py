# List trong python
# List duoc gioi han boi cap ngoac []
# Cac phan tu cua list cach nhau boi dau ,
# List co kha nang chua moi gia tri cua python vd: int,string,list

a =[1,2,3,'abc']

b = [[1,2,3,[2,3]],[],[]]
print(a)
print(b)
print('Hello world')

# su dung list comprehension
# cong thuc vong lap tuong duong voi c for (int i=0;i++;i<30)
a = [[i*2,i*4] for i in range(4)]
print(a)

# su dung  list constructor
# chuoi va list la 2 iterable(1 dang cau truc tap hop)
a = list('Hello World')
print(a)
### Mot so toan tu voi list
#Cong 2 list voi nhau
a = [1,2]
a+=[3,4]
print(a)
#phep nhan list. CHi nhan list voi 1 so
a = [1,2]
a = a* 2
print(a)

# Toan tu in la kiem tra 1 gia tri co nam trong 1 list hay khong
b = 1 in a # 1 co nam trong a hay khong dung la true sai false
print(b)

##Lay  gia tri trong 1 list

a =[1,2,3,4,'a','b','c',[1,2]]
print( 'Neu dau [<vi tri1>:<vi tri2>]=> Lay 1 chuoi tu <vi tri1> toi <vi tri2>')
b = a[3:6]
print(b)

# Su dung dau ': 'de thuc hien viec goi lay chuoi

print( 'Neu dau [:<vi tri>] ddung truoc thi lay toan bo cac gia tri truoc < vi tri>')
b = a[:2]# lay tat ca cac gia tri truoc vi tri thu 2
print(b)

print('Neu dung [<vi tri>:] dung sau < vi tri trong list> => lay tat ca cac gia tri bat dau tu <vi tri>')
b = a[2:]
print(b)

print('Neu dung [::] => Hien thi toan to list ')
b = a[::]
print(b)

# Thay doi gia tri cua chuoi

print('Thay doi 1 phan tu cua list')

a[1]='Hello' # Gan phan tu thu 2 la hello

print(a)

# Matrix la mot list nam trong 1 list 
print('*******MATRIX*********')
a = [[5,6,8],[3,4,7],[1,2,9]]
print(a[0])
print(a[1])
print(a[2])
print('TRuy cap phan tu trong ma tran')

print(a[0][0])
print(a[1][0])
print(a[2][0])

print('****NHung luu y khi su dung list******')

print(' Khong thuc hien viec gan list nay* sang list khac **')

a = [1,2,3]
b = a
print(a)
print(b)
b[0] =  'Hello World'
print('Gia tri cua b[0]=a[0]')
print(a)
print(b)


print('Su dung phuong thuc list() de gan 1 list ')

a = [1,2,3]
b = list(a)
print(a)
print(b)
b[0] =  'Hello World'
print('Gia tri cua b[0]=a[0]')
print(a)
print(b)

print('')

a = [[1,2,3],[4,5,6],[7,8,9]]
b = list(a)
print(a)
print(b)
b[0][0] =  'Hello World'
print('Gia tri cua b[0]=a[0]')
print(a)
print(b)

