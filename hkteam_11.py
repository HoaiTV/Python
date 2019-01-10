# phuong thuc cau chuoi trong python
a = 'hello world I AM PYTHON eo oi'
# voi phuong thuc nay ta xem la cat chuoi ben trai
b= a.split('l',1)
print(a)
print(b)
# cat chuoi tu phia ben phai
print('cat chuoi ben phai')
b = a.rsplit(' ',1)
print(a)
print(b)

# # cat chuoi tu phia ben trai
# b = a.lsplit(' ',2)
# print(a)
# print(b)


# PHuong thuc partion
print('Cat 1 chuoi ra lam 3 phan')
b = a.partition('w')
print(a)
print(b)

print('Phuong thuc rpartition => Cat 1 chuoi tu ben phai ra lam 3 phan')
b = a.rpartition('w')
print(a)
print(b)

# PHuong thuc count.
print('phuong thuc count')
b = a.count('e')
print(a)
print(b)
# Dem ky tu trong mot khoang 
print('phuong thuc count')
b = a.count('e',0,10)# bat dau, va ket thuc
print(a)
print(b)

# PHuong thuc startwith

print('phuong thuc startwith => kiem tra xem bat dau 1 chuoi la 1 ky tu hoac la 1 chuoi, gia tri tra ve la true or false ')
b = a.startswith('h')
print(a)
print(b)

# PHuong thuc endswith

print('phuong thuc startwith => kiem tra xem bat dau 1 chuoi la 1 ky tu hoac la 1 chuoi, gia tri tra ve la true or false ')
b = a.endswith('h')
print(a)
print(b)

# tim chuoi trong mot chuoi

print('phuong thuc FIND ******* => kiem tra xem co 1 chuoi la 1 ky tu hoac la 1 chuoi, so luong ')
b = a.find('e',4)
print(a)
print(b)

#phuong thuc rindex 

#phuong thuc islower

print('co phai mot chuoi viet thuong hay khong=> gia tri tra ve neu ')
b = a.islower()
print(a)
print(b)

#phuong thuc isupper
print('co phai mot chuoi viet Hoa hay khong=> gia tri tra ve neu ')
b = a.isupper()
print(a)
print(b)

# Phuong thuc kiem tra xem 1 chuoi co phai la so hay khong

print('phuong thuc kiem tra xem 1 chuoi co phai la so hay khong => gia tri tra ve TRUE OR FALSE ')
b = a.isdigit()
print(a)
print(b)

# Phuong thuc kiem tra xem 1 chuoi co phai la space hay khong

print('Phuong thuc kiem tra xem 1 chuoi co phai la space hay khong => gia tri tra ve TRUE OR FALSE ')
b = a.isspace()
print(a)
print(b)


# Bai tap cung co
A = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
b = A.find('o',20)
print(b)
A = A.title()
a = (A.split('oaa',1))
#a = a.rsplit('oaa',1)
b = a[1].rsplit('aaaaaaa',1)
print(a)
print(b)







