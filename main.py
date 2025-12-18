# ===== LAMBDA MISOLLARI =====
# 1️ Sonning kvadrati
kvadrat = lambda x: x**2
print("Kvadrat(5):", kvadrat(5))

# 2 Ikki sonni qo‘shish
qoshish = lambda a, b: a + b
print("3 + 7 =", qoshish(3, 7))

# 3️ Son juft yoki toq
juftmi = lambda x: x % 2 == 0
print("6 juftmi?", juftmi(6))

# 4️ Matnni katta harflarga o‘zgartirish
katta_harf = lambda s: s.upper()
print(" 'salom' katta harf:", katta_harf("salom"))

# 5️ Uchburchak perimetri
perimetr = lambda a, b, c: a + b + c
print("Perimetr(3,4,5):", perimetr(3, 4, 5))


# ===== MAP MISOLLARI =====
# 1️ Ro‘yxatdagi sonlarning kvadrati
sonlar = [1, 2, 3, 4]
print("Kvadratlari:", list(map(lambda x: x**2, sonlar)))

# 2 Ro‘yxatdagi sonlarga 10 qo‘shish
sonlar2 = [5, 6, 7]
print("10 qo‘shilgan:", list(map(lambda x: x + 10, sonlar2)))

# 3️ Ismlarni katta harfga o‘zgartirish
ism = ["ali", "vali", "gul"]
print("Katta harf:", list(map(lambda x: x.upper(), ism)))

# 4️ Sonlarning kvadrat ildizi
sonlar3 = [1, 4, 9, 16]
print("Kvadrat ildizlari:", list(map(lambda x: x**0.5, sonlar3)))

# 5️ Musbat yoki manfiyligini tekshirish
sonlar4 = [-2, 0, 5]
print("Musbat yoki manfiyligi:", list(map(lambda x: "Musbat" if x > 0 else "Manfiy yoki 0", sonlar4)))


# ===== FILTER MISOLLARI =====
# 1️ Faqat juft sonlar
sonlar5 = [1, 2, 3, 4, 5, 6]
print("Juft sonlar:", list(filter(lambda x: x % 2 == 0, sonlar5)))

# 2 5 dan katta sonlar
sonlar6 = [2, 5, 8, 1, 10]
print("5 dan katta sonlar:", list(filter(lambda x: x > 5, sonlar6)))

# 3️ 3 harfli so‘zlar
sozlar = ["ali", "vali", "gul", "oy"]
print("3 harfli so‘zlar:", list(filter(lambda x: len(x) == 3, sozlar)))

# 4️ Manfiy sonlar
sonlar7 = [3, -1, -7, 4, 0]
print("Manfiy sonlar:", list(filter(lambda x: x < 0, sonlar7)))

# 5️ Katta harf bilan boshlanadigan so‘zlar
sozlar2 = ["Ali", "vali", "Gul", "oy"]
print("Katta harf bilan boshlanadigan so‘zlar:", list(filter(lambda x: x[0].isupper(), sozlar2)))
