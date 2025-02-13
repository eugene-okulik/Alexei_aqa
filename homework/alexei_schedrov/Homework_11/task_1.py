class Book:
    page_material = 'бумага'
    text_presence = True

    def __init__(self, title, author, page_count, isbn, is_reserved):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def __str__(self):
        reserve_state = ", зарезервирована" if self.is_reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, материал: {self.page_material}{reserve_state}"
                )


books = [
    Book('Идиот', 'Достоевский', 232, '122-355-43-0188', True),
    Book('Идиотss', 'Достоеffский', 111, '12436-3463-43-0188', False),
    Book('Robin Hood', 'Dickens', 131, '16346-346324-43-0188', False),
    Book('Capital', 'Marks', 5140, '66-34124-43-0188', False),
    Book('About me', 'Eminem', 179, '34545-34124-43-0188', False)
]

for book in books:
    print(book)


class School(Book):
    def __init__(self, title, author, page_count, isbn, is_reserved, subject, level, tasks_presence):
        super().__init__(title, author, page_count, isbn, is_reserved)
        self.subject = subject
        self.level = level
        self.tasks_presence = tasks_presence

    def __str__(self):
        reserve_state = ", зарезервирована" if self.is_reserved else ""
        return (f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.page_count}, предмет: {self.subject}, "
                f"класс: {self.level}{reserve_state}"
                )


school_books = [
    School('Математика 1-й класс',
           'Де Карт',
           44,
           '7877-146-0001',
           False,
           'Математика',
           1,
           True
           ),
    School('История 4-й класс',
           'Геродот',
           1440,
           '33782-146-0001',
           True,
           'История',
           4,
           False
           ),
    School('Математика 11-й класс',
           'Лобачевский',
           320,
           '4452-146-0001',
           False,
           'Математика',
           11,
           True
           ),
    School('Физика 7-й класс',
           'Резерфорд',
           444,
           '24416-0001',
           False,
           'Физика',
           7,
           True
           ),
    School('Астрономия 6-й класс',
           'Птолемей',
           77,
           '999845-82-146-0001',
           True,
           'Астрономия',
           4,
           False
           )
]

for book in school_books:
    print(book)
