

def split_and_join(line):
    strng = line.split(" ")
    # print(strng)
    
    return "-".join(strng)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
