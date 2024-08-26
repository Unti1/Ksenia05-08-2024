immutable_var = (15, 10, 16)
immutable_var1 = ("Привет", "мир", "25")
immutable_var3 = (10, "Привет", 25, 29)
print(immutable_var1) 
print(immutable_var) 
print(immutable_var3) 

# tuple - это кортеж и его изменить нельзя. 
# print(immutable_var)
# immutable_var.append(4)
# print(immutable_var)


mutable_list = [15, 10, 16]
mutable_list1 = ["Привет", "мир", "25"]
mutable_list2= [10, "Привет", 25, 29]
mutable_list1.append(4)
print(mutable_list) 
print(mutable_list1) 
print(mutable_list2) 

frukt = ["Яблоко","Апельсин","Мандарин","Дыня","Арбуз"]
frukt.append("Киви") #frukt.insert(5,"Киви")
frukt[1] = "Банан"
frukt.remove("Арбуз") #frukt.pop(5)
print(frukt)

s1 = [1,2,4,6]
s2 = [3,5,3,9]
s1.extend(s2)
ss = s1.count(7)
print(ss)
print(s1[0:3])

cveta = ["Красный","Синий","Черный"]
cveta.insert(1,"Зеленый")
print(cveta)

s3 = [3, 1, 4, 1, 5, 9, 2, 6, 5] 
s3.sort()
print(s3)

slovar = {
    "Яблоко":["Красный","Зеленый","Желтый"],
    "Банан": ["Желтый","Оранжевый"],
    "Киви":["Зеленый","Черный"]
    }
slovar.setdefault("Дыня", ["Желтый","Белый"])  # Вопрос: можем ли мы изменить одно значение в ключе, не задавая ключю полностью новое? 
print(slovar)
slovar["Яблоко"] = "Голубой", "Черный"
slovar.pop("Яблоко")
print(slovar)
print(slovar.keys())
print(slovar.values())
print(slovar.get("Апельсин", "Нету"))

slovar1 = {
    "Анна":[18],
    "Ксения":[26],
    "Елена":[33] 
    }
print(slovar1)
print(f"Анне {slovar1.get("Анна")}лет")
slovar.update(slovar1)
print(slovar)

kniga = {
    "Название":["Маленький принц"],
    "Автор":["Антуан де Сент-Экзюпери"],
    "Год издания":[1943]
}
print(f"Автор книги - {kniga.get("Автор")}")