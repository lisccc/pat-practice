'''
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：
- A_1 = 能被 5 整除的数字中所有偶数的和；
- A_2 = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n_1 − n_2 + n_3 - n_4 ...；
- A_3 = 被 5 除后余 2 的数字的个数；
- A_4 = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
- A_5 = 被 5 除后余 4 的数字中最大数字。

输入格式：
每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N，随后给出 N 个不超过 1000 的待分类的正整数。数字间以空格分隔。
输出格式：
对给定的 N 个正整数，按题目要求计算 A_1~A_5，并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。
若分类之后某一类不存在数字，则在相应位置输出 N。
输入样例 1：
13 1 2 3 4 5 6 7 8 9 10 20 16 18
输出样例 1：
30 11 2 9.7 9
输入样例 2：
8 1 2 4 5 6 7 9 16
输出样例 2：
N 11 2 N 9
'''

if __name__ == '__main__':
    nums = list(map(int, input().split()[1:]))
    A_nums = [[] for i in range(5)]
    for num in nums:
        if num % 5 == 0:
            if num % 2 == 0:
                A_nums[0].append(num)
        else:
            A_nums[num % 5].append(num)
    print('N' if len(A_nums[0]) == 0 else sum(A_nums[0]), end=' ')
    print('N' if len(A_nums[1]) == 0 else sum(list(map(lambda x, y: x * y, [1, -1] * int(len(A_nums[1])), A_nums[1]))),
          end=' ')
    print('N' if len(A_nums[2]) == 0 else len(A_nums[2]), end=' ')
    print('N' if len(A_nums[3]) == 0 else round(sum(A_nums[3]) / len(A_nums[3]), 1), end=' ')
    print('N' if len(A_nums[4]) == 0 else max(A_nums[4]))
