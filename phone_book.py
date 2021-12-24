import re
import csv

def phone_book(raw_data, chang_data):
    with open(raw_data, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        name_pattern = r"^([\w]+)(\s)?([\w]+)?(\s)?([\w]+)?,([\w]+)?(\s)?([\w]+)?,([\w]+)?"
        name_regex = re.compile(name_pattern)
        phone_pattern = r"((\+7)|8)\s?\(?([\d]{3}?)(\)|\s|-)?\s?([\d]{3}?)(\s|-)?([\d]{2}?)(\s|-)?([\d]{2}?)(\s\(?(доб\.)?\s?([\d]*)\)?)?"
        phone_regex = re.compile(phone_pattern)
        contacts_list_chang = []

        for contact in contacts_list:
            contact = ','.join(contact)
            contact = name_regex.sub(r"\1,\3\6,\5\8\9", contact)
            contact = phone_regex.sub(r"+7(\3)\5-\7-\9 \11\12", contact)
            contact = contact.split(',')
            contacts_list_chang.append(contact)
    contacts = []
    for contact in contacts_list_chang:
        entrance = (contact[0], contact[1])
        contacts.append(entrance)
    contacts = set(contacts)
    phone_book_chang = []

    for entrance in contacts:
        new_input = ['', '', '', '', '', '', '']
        for contact in contacts_list_chang:
            if entrance[0] and entrance[1] in contact:
                i = -1
                for field in contact:
                    i += 1
                    if new_input[i] != contact[i]:
                        new_input[i] += contact[i]
        phone_book_chang.append(new_input)
    phone_book_chang.sort()

    with open(chang_data, "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phone_book_chang)
    return print(f'исходный файл {raw_data} изменён и записан в {chang_data}')