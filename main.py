from re_phonebook import*

script_dir = os.path.dirname(sys.argv[0])
if __name__ == '__main__':
    contacts = read_file(script_dir, "phonebook_raw.csv")
    contacts = format_number(contacts)
    contacts = format_name(contacts)
    contacts = correct_text(contacts)
    write_file(contacts)
