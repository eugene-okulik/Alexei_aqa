class Flower:
    def __init__(self, name, colour, freshness, stem_length, price, lifespan):
        self.name = name
        self.colour = colour
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifespan = lifespan

    def __repr__(self):
        return (f"{self.name} ( цвет: {self.colour}, свежесть : {self.freshness} дней, "
                f"длина стебля: {self.stem_length} см, цена: {self.price}, "
                f"время жизни: {self.lifespan} дней)")


class Camomile(Flower):
    def __init__(self, colour, freshness, stem_length, price, lifespan):
        super().__init__("Ромашка", colour, freshness, stem_length, price, lifespan)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, price, lifespan):
        super().__init__("Лилия", color, freshness, stem_length, price, lifespan)


class Tulip(Flower):
    def __init__(self, colour, freshness, stem_length, price, lifespan):
        super().__init__("Тюльпан", colour, freshness, stem_length, price, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        else:
            return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def search_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def __repr__(self):
        return "\n".join(str(flower) for flower in self.flowers)


# Экземпляры цветов
camomile = Camomile("белый", 3, 35, 90, 6)
tulip = Tulip("желтый", 4, 30, 50, 5)
lily = Lily("розовый", 6, 45, 120, 8)

# Составляем букет
bouquet = Bouquet()
bouquet.add_flower(camomile)
bouquet.add_flower(lily)
bouquet.add_flower(tulip)

# Информация о букете
print("Букет:")
print(bouquet)
print(f"Общая стоимость букета: {bouquet.total_cost()} руб")
print(f"Среднее время увядания букета: {bouquet.average_lifespan()} дней")

# Сортировка цветов букета по свежести
bouquet.sort_by_freshness()
print("\nБукет после сортировки по свежести:")
print(bouquet)

# Ищем цветы с временем жизни 5 дней
lifespan_search = 5
print(f"\nЦветы с временем жизни {lifespan_search} дней:")
for flower in bouquet.search_by_lifespan(lifespan_search):
    print(flower)
