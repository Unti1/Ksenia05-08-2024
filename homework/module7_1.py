class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category 
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'homework/products.txt'
    def get_products(self):
        all=''
        with open(self.__file_name, 'r',encoding='utf-8') as file:
            return file.read()
    def add(self, *products):
        all = []
        with open(self.__file_name, 'r',encoding='utf-8') as file:
            for x in file:
                all.append(x.lower().split(',')[0].strip())
            
        with open(self.__file_name, 'a',encoding='utf-8') as file:
            for x in products:
                x.name = x.name.lower()
                if x.name not in all:
                    file.write(str(x.name+ '\n'))
                    all.append(x.name)
                    print('Продукт добавлен')
                else:
                    print('Продукт уже есть')

            
shop = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Spaghetti', 3.4, 'Groceries')
p6 = Product('potato', 5.5, 'Vegetables')
shop.add(p6)





print(shop.get_products())








