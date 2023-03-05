import csv, os, re, sys

def read_file(file_path, file_name):
  with open(os.path.join(file_path, file_name), encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return contacts_list


def format_number(contacts_list):
  number_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
  r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})' \
  r'(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
  repl = r'+7(\4)\8-\11-\14\15\17\18\19\20'
  new_contacts_list = []
  for contact in contacts_list:
    str_contact = ','.join(contact)
    format_contact = re.sub(number_pattern, repl, str_contact)
    lst_contact = format_contact.split(',')
    new_contacts_list.append(lst_contact)
  return new_contacts_list


def format_name(contacts_list):
  name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)' \
    r'(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
  repl = r'\1\3\10\4\6\9\7\8'
  new_contacts_list = []
  for contact in contacts_list:
    str_contact = ','.join(contact)
    format_contact = re.sub(name_pattern, repl, str_contact)
    lst_contact = format_contact.split(',')
    new_contacts_list.append(lst_contact)
  return new_contacts_list


def correct_text(contacts_list):
  for i in contacts_list:
    for j in contacts_list:
      if i[0] == j[0] and i[1] == j[1] and i is not j:
        if i[2] == '':
          i[2] = j[2]
        if i[3] == '':
          i[3] = j[3]
        if i[4] == '':
          i[4] = j[4]
        if i[5] == '':
          i[5] = j[5]
        if i[6] == '':
          i[6] = j[6]
  new_contacts_list = []
  for contact in contacts_list:
    if contact not in new_contacts_list:
      new_contacts_list.append(contact)
  return new_contacts_list


def write_file(contacts_list):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

