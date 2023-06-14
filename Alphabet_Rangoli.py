def print_rangoli(size):
    # your code goes here
    list_1 = list(map(chr, range(97, 123)))

    x = list_1[n - 1:: -1] + list_1[1:n]
    m = len("-".join(x))

    for i in range(1, n):
        print('-'.join(list_1[n - 1:n - i:-1] + list_1[n - i: n]).center(m, '-'))
    for i in range(n, 0, -1):
        print('-'.join(list_1[n - 1:n - i:-1] + list_1[n - i: n]).center(m, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)