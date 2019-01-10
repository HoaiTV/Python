# Cac phuong thuc cua list trong python

a = [1,2,3,4,5,1,7,8,9]

# Phuong thcu count

print('phuong thuc count(<bien_dem_xuat_hien_list>)=> tra ve so lan xuat hien cua bien <bien_dem_xuat_hien_list> trong list a')

c = a.count(1)

print(c)


print('phuong thuc index(<bien_vi_tri_xuat_hien_list>)=> tra ve so lan xuat hien cua bien <bien_vi_tri_xuat_hien_list> trong list a')

c = a.index(1,1)

print(c)

# Cac phuong thuc cap nhat
print('******************Phuong thuc cap nhat ************')

a = [1,2,3]

print('phuong thuc append<value_add_list>  => bo sung gia tri <value_add_list> vao list ')

a.append(4)

print(a)

print('phuong thuc extend<value_add_list>  => bo sung tung  gia tri <value_add_list> vao list (neu la 1 list thi add tung phan tu cua list moi vao list duoc extend)')

a.extend([4,5])

print(a)

print('phuong thuc insert<position,value_add_list>  => them gia tri <value_add_list> vao vi tri <position> ')

a.insert(4,9)

print(a)

print('phuong thuc pop(<position>)  =>  bo di phan tu thu position> trong list ')

a.pop(4)

print(a)

print('phuong thuc remove(<value>)  =>  bo di phan tu dau tien trong list co gia tri la <value> trong list ')
#Neu <value> khong ton tai trong list thi ket qua bao loi
a.remove(4)

print(a)

print('phuong thuc reverse()=> Sap xep list nguoc lai ')

a.reverse()

print(a)

print('phuong thuc sort()=> Sap xep list,  ')
#Mac dinh tu nho toi lon
#chi su dung duoc neu list cung kieu data
#Sap xep tu be den lon
a.sort(reverse = False)
print(a)
#Sap xep tu nguoc, tu lon xuong be reserve = True
a.sort(reverse = True)
print(a)








