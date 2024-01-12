def num_first_last(str):
    first_num = last_num = ""
    for char in str:
        if char.isdigit():
            if not first_num:
                first_num = char
            else:
                last_num = char
    return first_num + last_num

def main():
    print(num_first_last("shrz3vdcghblt21"))
    
if __name__ == '__main__':
    main()