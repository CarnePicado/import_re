from pprint import pprint
from collections import defaultdict
import csv, os, re, sys


def read_file(file_path, file_name):
  with open(os.path.join(file_path, file_name), encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return contacts_list
  

def format_number(contacts_list):
  number_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                  r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                  r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
  repl = r'+7(\4)\8-\11-\14\15\17\18\20'
  new_contacts_list = []
  for contact in contacts_list:
    str_contact = ','.join(contact)
    format_contact = re.sub(number_pattern, repl, str_contact)
    lst_contact = format_contact.split(',')
    new_contacts_list.append(lst_contact)
  return new_contacts_list


def format_name(contacts_list):
  name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
  repl = r'\1\3\10\4\6\9\7\8'
  new_contacts_list = []
  for contact in contacts_list:
    str_contact = ','.join(contact)
    format_contact = re.sub(name_pattern, repl, str_contact)
    lst_contact = format_contact.split(',')
    if lst_contact not in new_contacts_list:
      new_contacts_list.append(lst_contact)
  return new_contacts_list


def correct_text(contacts_list):
  new_list = defaultdict(list)
  for contact in contacts_list:
    key = tuple(contact[:2])
    for part in contact:
      if part not in new_list[key]:
        new_list[key].append(part)
  return list(new_list.values())


def write_file(contacts_list):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

