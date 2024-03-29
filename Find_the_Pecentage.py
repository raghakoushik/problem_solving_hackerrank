if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # print(student_marks)
    query_name = input()

    if query_name in student_marks:
        a = sum(student_marks[query_name]) / len(student_marks[query_name])
        print("%.2f" % a)