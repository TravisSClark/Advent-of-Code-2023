word_to_num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def puzzle_input():
    file = open("day1input.txt","r")
    return file.readlines()

def num_first_last(str):
    first_num = last_num = possible_word_num = ""
    for char in str:
        if char.isdigit():
            if not first_num:
                first_num = char
            else:
                last_num = char
        else:
            possible_word_num += char
            if possible_word_num in word_to_num_dict:
                if not first_num:
                    first_num = word_to_num_dict[possible_word_num]
                else:
                    last_num = word_to_num_dict[possible_word_num]
                possible_word_num = ""
            else:
                possible_word_num = check_match(possible_word_num)
    if not last_num and first_num:
        last_num = first_num
    return first_num + last_num

def check_match(possible_word_num):
    while len(possible_word_num) > 0:
        for num_word in word_to_num_dict.keys():
            if num_word.startswith(possible_word_num):
                return possible_word_num
        possible_word_num = possible_word_num[1:]
    return ""


def sum_list(list):
    sum = 0
    for str in list:
        sum = sum + int(num_first_last(str))
    return sum

def main():
    list = puzzle_input()
    print(sum_list(list))
    
if __name__ == '__main__':
    main()