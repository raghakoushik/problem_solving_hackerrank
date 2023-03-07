if __name__ == '__main__':
    score_list = []
    marks_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = []
        temp.append(score)
        temp.append(name)
        marks_list.append(score)
        score_list.append(temp)

    # print(marks_list)
    score_list.sort()
    marks_list.sort()
    # print(marks_list)
    marks_list = [*set(marks_list)]
    marks_list.sort()
    # print(marks_list)
    ##print(score_list)
    sec_low_scr = min(marks_list)
    # print(sec_low_scr)
    marks_list.remove(sec_low_scr)
    # print(marks_list)

    s3 = []
    # aa = marks_list[0] in [j for i in score_list for j in i]
    # print(aa)

    for i in range(len(score_list)):
        # print(score_list[i][0])
        # print(marks_list[0])
        if score_list[i][0] == marks_list[0]:
            if score_list[i][1] not in s3:
                s3.append(score_list[i][1])

    s3.sort()
    # print(s3)
    for i in range(len(s3)):
        print(s3[i])
        # print(score_list[i])
    # print(se_lo_min)
    # print(score_list)
