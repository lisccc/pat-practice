'''
正整数 A 的“D_A（为 1 位整数）部分”定义为由 A 中所有 D_A 组成的新整数 P_A。
例如：给定 A=3862767，D_A = 6，则 A 的“6 部分” P_A 是 66，因为 A 中有 2 个 6。
现给定 A、D_A、B、D_B，请编写程序计算 P_A + P_B。

输入格式：
输入在一行中依次给出 A、D_A、B、D_B ，中间以空格分隔，其中 0<A,B<10^9。

输出格式：
在一行中输出 P_A + P_B 的值。
输入样例 1：
3862767 6 13530293 3
输出样例 1：
399
输入样例 2：
3862767 1 13530293 8
输出样例 2：
0
'''

if __name__ == '__main__':
    A, DA, B, DB = input().split()
    Px = lambda x, dx: int(dx * x.count(dx)) if dx in x else 0
    print(Px(A, DA) + Px(B, DB))
