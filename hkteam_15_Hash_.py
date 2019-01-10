# Hashable  Cap bo nho vua du cho Chuoi va Tuple (Khong the thay doi noi dung cua nhung container nay)

#<> UnHashable Cap bo nho luu tru thua ra List (co the bo sung gia tri vao list)
b = 5
a = id(b)# Tra ve dia chi cua (5)
print(a)

s_1 = 'Hello'
s_2 = 'World'

print(id(s_1))
print(id(s_2))

s_1 =  s_1 + 'python'
s_2 =  s_2 + 'python'

print(id(s_1))
print(id(s_2))

s_1 =  s_1 + 'python'
s_2 += 'python'

print(id(s_1))
print(id(s_2))
