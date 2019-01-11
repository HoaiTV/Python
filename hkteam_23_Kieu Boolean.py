#

# Boolean la mot kieu du lieu ma cac ngon ngu lam trinh ngay nay thuongf xuyen su dung. Python cung khong phai la ngoai le.

# Boolean chi co 2 gia tri.

# Mot la True
# Mot la False


print(3>1)
print(ord('a'))
print(ord('A'))

######################## Toan tu is ###################################
#khi so sanh  ham is thi su dung ham id de so sanh

lst = [1,2,3]
lnd = [1,2,3]
_lst = lst

print(id(lst))
print(id(lnd))
print(id(_lst))

print(lst == lnd)
print(lst is lnd)
print(_lst is lst)

print('true' and 'true')

a = -4
b = 20

print(a<3<5<9<b<25) #(a<3)&(a<5)...(a<b)&(b<20)

# kiem tra 1 gia tri trong 1 list,tuple
k=6
tuple = (3,4,5)
print(k in tuple)
