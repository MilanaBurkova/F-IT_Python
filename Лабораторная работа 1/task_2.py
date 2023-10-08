# TODO Найдите количество книг, которое можно разместить на дискете

BYTES_ONE_CHARACTER = 4  # объем для хранения кода одного символа в байтах

floppy_disk_capacity = 1.44 * 1024 * 1024  # информационный объем дискеты в байтах
number_of_pages = 100
number_of_lines = 50
number_of_character = 25

bytes_one_book = BYTES_ONE_CHARACTER * number_of_character * number_of_lines * number_of_pages
number_of_books = int(floppy_disk_capacity // bytes_one_book)

print("Количество книг, помещающихся на дискету:", number_of_books)
