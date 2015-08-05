import sys


def LCS(a_len, b_len, a, b):
    Ans = [[0 for j in range(b_len+1)] for i in range(a_len+1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                Ans[i+1][j+1] = Ans[i][j]+1
            else:
                Ans[i+1][j+1] = 0

    max_len = -1
    max_index = -1
    for i in range(a_len):
        for j in range(b_len):
            if Ans[i+1][j+1] > max_len:
                max_len = Ans[i+1][j+1]
                max_index = i+1

    return a[max_index-max_len:max_index]


def main():
    str_length = input()
    str_length = str_length.split()
    try:
        a_len = int(str_length[0])
        b_len = int(str_length[1])
    except:
        print("字串長度應為整數型態")
        main()
    a_str = input()
    b_str = input()
    ans = LCS(a_len, b_len, a_str, b_str)
    if ans:
        print(ans)


if __name__ == '__main__':
    main()
    sys.exit()
