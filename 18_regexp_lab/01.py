import re
import sys

file_path = sys.argv[1]
key = sys.argv[2]

def get_file_as_list(filepath):
    str1 = []
    with open(filepath, "r") as rows:
        for row in rows:
            str1 += [row]
    return str1


def get_dictionary_from_list(list_):
    dict_temp = {}
    for n in list_:
        txt = re.search(r'(\w+)\s*=\s*(\w+)', n)
        if txt is not None:
            dict_temp.setdefault(txt.group(1),  txt.group(2))
    return dict_temp

lst = get_file_as_list(file_path)
dictionary = get_dictionary_from_list(lst)

print dictionary[key]
