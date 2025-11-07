def count_words(text):
    print(f"Found {len(text.split())} total words")


def count_unique_characters(text):
    dict = {}
    text = text.lower()
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    #print(dict)
    return dict

def sort_on_num(items):
    return items["num"]

def rearrange_dict(dict):
    dict_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        dict_list.append(new_dict)
    dict_list.sort(key=sort_on_num, reverse=True)
    return dict_list