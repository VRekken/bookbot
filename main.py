import sys
from stats import count_words, count_unique_characters, rearrange_dict


def main(sys_input):
    for arg in sys_input:
        if len(sys_input) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        elif arg == sys_input[0]:
            pass
        else:
            text = get_book_text(arg)
            character_dict = count_unique_characters(text)
            #print(character_dict)
            #print(rearrange_dict(character_dict))
            new_list = rearrange_dict(character_dict)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {arg}")
            print("----------- Word Count ----------")
            count_words(text)
            print("--------- Character Count -------")
            print_each_character(new_list)
            print("============= END ===============")


def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()


def print_each_character(dict_list):
    for item in dict_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            pass

main(sys.argv)