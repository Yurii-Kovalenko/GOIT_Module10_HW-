from collections import UserDict

from re import sub


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        self.value = value


class Phone(Field):
    def __init__(self, value: str):
        value = sub(r'\D', '', value)
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        for exemplar_phone in self.phones:
            if str(exemplar_phone) == phone:
                    self.phones.remove(exemplar_phone)
                    break
    
    def edit_phone(self, phone_old: str, phone_new: str) -> None:
        not_found = True
        for exemplar_phone in self.phones:
            if str(exemplar_phone) == phone_old:
                exemplar_phone.value = phone_new
                not_found = False
                break
        if not_found:
            raise ValueError
    
    def find_phone(self, phone: str) -> Phone:
        not_found = True
        for exemplar_phone in self.phones:
            if str(exemplar_phone) == phone:
                not_found = False
                break
        return None if not_found else exemplar_phone

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()
    
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name_search: str) -> Record:
        for key in self.data:
            if key == name_search:
                return self.data[key]

    def delete(self, name_search: str) -> None:
        for key in self.data:
            if key == name_search:
                break
        self.data.pop(key)


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    book.delete("Jane")