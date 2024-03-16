# Для начала убедитесь, что ваш исходный файл с улицами находится в том же каталоге, что и этот скрипт,
# или укажите полный путь к файлу.

def process_streets(input_file, output_file):
    unique_streets = set()

    # Чтение и обработка каждой строки файла
    with open(input_file, 'r') as file:
        for line in file:
            # Удаление цифр и текста после запятой
            street_name = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line.split(',')[0])).strip()
            unique_streets.add(street_name)

    # Сортировка и запись уникальных названий улиц в новый файл
    with open(output_file, 'w') as file:
        file.write("[\n")
        for street in sorted(unique_streets):
            # file.write(f'    {{ name: "{street}", group:  }},\n')
            file.write(f' {street}\n')
        file.write("]")

# Пример использования:
input_file = '4.txt'  # Замените на путь к вашему файлу
output_file = 'unique_streets.txt'  # Выходной файл будет создан в том же каталоге

process_streets(input_file, output_file)

# После выполнения этого кода, проверьте файл unique_streets.json для списка уникальных улиц.
