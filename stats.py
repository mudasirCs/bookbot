def count_number_words(text):
    words=text.split()
    return len(words)

def plot_char_dict(text):
    char_dict={}
    lower_text=text.lower()
    for char in lower_text:
        char_dict[char]= char_dict.get(char,0)+1
    return char_dict

def make_dict(char_dict):
    new_dict_list=[]
    for key,value in char_dict.items():
        new_dict_list.append({"char":key,"num":value})
    return new_dict_list

def sort_on(item):
    return item["num"]

def sort_dict(char_dict):
    new_dict=make_dict(char_dict)
    new_dict.sort(key=sort_on,reverse=True)
    return new_dict