'''
输入两个非负 10 进制整数 A 和 B (≤2^30−1)，输出 A+B 的 D (1<D≤10)进制数。

输入格式：
输入在一行中依次给出 3 个整数 A、B 和 D。
输出格式：
输出 A+B 的 D 进制数。
输入样例：
123 456 8
输出样例：
1103
'''

if __name__ == '__main__':
    A, B, D = list(map(int, input().split()))
    C = A + B
    if D == 10 or C == 0:
        print(C)
    else:
        res = ''
        while C != 0:
            res += str(C % D)
            C //= D
        print(res[::-1])
