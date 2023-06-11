def split_and_join(line):
    # write your code here
    a = line.split(" ")
    line = "-".join(a)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)