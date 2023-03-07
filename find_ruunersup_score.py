if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sort_arr = list(arr)
    sort_arr.sort(reverse=True)
    s2 = []
    for i in sort_arr:
        # print(i)
        if i not in s2:
            s2.append(i)
    print(s2[1])
