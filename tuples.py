# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    # print(n)
    tuple_elements = tuple(map(int, input().split()))
    print(hash(tuple_elements))
