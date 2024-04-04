for x in range(5):
    print(x)
for x in range(1,5):
    print(x)

# x = 5
# while (True):
#     print(x)
#     x += 1
#     if (x >= 10):
#         break

# 因数
# 18的因数有哪些?
# 1.对于任意一个数字而言,1和本身都是其约数
# 2.从1开始遍历到数字本身,凡是可以除尽的就是约数
# 3.利用列表存放因数
# num = int(input())
# dibisor = []
# num1 = 18
# for n in range(1,num1 + 1):
#     if num1 % n == 0:
#         dibisor.append(n)
# print(dibisor)

# 100以内6的倍数有哪些？
# 1.一个数的额倍数是无限多的，所以求倍数时一定要有一定的范围
# 2.从6开始遍历到100，凡是可以被6除尽的就是6的倍数
# 3.利用列表盛放100以内6的倍数
# multiple = []
# num2 = 6
# for n in range(num2,101):
#     if n % num2 == 0:
#         multiple.append(n)
# print(multiple)

#完美数
# 一个数，除了自身以外的因数之和恰好等于它本身
# 例如6的因数除了自身之外有1、2、3  6=1+2+3
# 找出100以内的所有完美数
# 1.遍历所有100以内的数字
# 2.求出每一个数除以自身以外的所有因数之和
# 3.如果因数之和与自身相等，则是一个完美数
# 4.用列表盛放所有的完美数
# perfect = []
# for x in range(1,100):
#     sum = 0
#     for y in range(1,x):
#         if x % y == 0:
#             sum += y
#     if sum == x:
#         perfect.append(x)
# print(perfect)

# 公因数
# 如果一个整数同时是几个整数的因数，称这个整数为它们的”公因数“
# 例如：6可以同时被24,36整除，则6就是24和36的公因数
# # 公因数可以有多个，最大的那一个称为最大公因数
# 1.遍历从1开始到较小数字的所有数字
# 2.利用列表盛放可以同时整除两个数字的所有数字
# 3.列表中的数字就是公因数，列表中最大的数字就是最大公因数
# n1 = 24
# n2 = 36
# factor = []
# for x in range(1,min(n1,n2)):
#     if n1 % x == 0 and n2 % x == 0:
#         factor.append(x)
# print(factor)
# print(max(factor))

# 穷举法计算最大公因数
# 要求解数字m和n的最大公因数时：
# 1.设定变量temp为m或n其中的任意一个值
# 2.如果temp可以被m和n整除，则temp就是最大公因数
# 3.如果temp不能，就让temp的值减一，然后再次判断此时的temp是否可以被m和n整除。重复这个步骤，直到找到一个temp
# 4.即使m和n为互质数，它们也有一个公约数1
# m = int(input("m:"))
# n = int(input("n:"))
# temp = m
# while True:
#     if m % temp == 0 and n % temp == 0:
#         break
#     else:
#         temp -= 1
# print("最大公因数为：",temp)

# 数字特性计算最大公因数
# 要求解数字m和n的最大公因数时：
# 1.让m对n求余，如果可以除尽，则n就是最大公约数
# 2.如果m不能整除n，则让m等于n的值，n等于每一步计算的余数。继续让m对n求余，如果可以除尽，则此时的n就是最大公约数。否则继续重复执行第二步
# 3.即使m和n为互质数，它们也有一个公约数1
# m = int(input("m:"))
# n = int(input("n:"))
# while True:
#     if m % n == 0:
#         break
#     else:
#         m,n = n,m % n
#         # t = m
#         # m = n
#         # n = t % n
# print("最大公因数为：",n)

# 裁纸
# m = 135
# n = 105
# while True:
#     if m % n == 0:
#         break
#     else:
#         m, n = n, m % n
# print("最大正方形的边长：",n)
# print("最多可以裁剪：：",(135/n) , (105/n))

# 分水果
# 50个梨，75个橘子，100个苹果，这些水果最多可以平均分配给几个小朋友？
# 实际就是在求解50，75，100这三个数字的最大公约数
# m = 50
# n = 75
# p = 100
# temp = min(m,n,p)
# while True:
#     if m % temp == 0 and n % temp == 0 and p % temp == 0:
#         break
#     else:
#         temp -= 1
# print("最多可以分给小朋友的个数:",temp)