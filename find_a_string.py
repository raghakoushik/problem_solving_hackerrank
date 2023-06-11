def count_substring(string, sub_string):
    num = 0
    for i in range(0, len(string)):
        num = num + string.count(sub_string, i, i + len(sub_string))
    return num


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)