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
    data = input()
    data = data.split()
    try:
        a_len = int(data[0])
        b_len = int(data[1])
        a_str = data[2]
        b_str = data[3]
        ans = LCS(a_len, b_len, a_str, b_str)
        if ans:
            print(ans)

    except:
        print('輸入必須以空白間隔\n請重新輸入')
        main()

if __name__ == '__main__':
    main()
    sys.exit()
