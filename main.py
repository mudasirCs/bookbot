from stats import count_number_words,plot_char_dict,sort_dict
import sys

def get_book_text(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        file_contents=f.read()
    return file_contents

def display_dict(file_path,char_list, num_words):
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}
----------- Word Count ----------""")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict_line in char_list:
        if dict_line["char"].isalpha():  # only letters
            print(f"{dict_line['char']}: {dict_line['num']}")

    print("--------- END -------")

def main():
    args=sys.argv    
    if(len(args)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path= args[1]
    text=get_book_text(file_path)
    num_words=count_number_words(text)
    char_dict=plot_char_dict(text)
    display_dict(file_path,sort_dict(char_dict),num_words)



if __name__=="__main__":
    main()