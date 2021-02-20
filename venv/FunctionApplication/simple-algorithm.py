#简单小算法
#有一个列表：[80,13,66,202,0,-13],把列表种的最大数和列表种的第一个元素交换位置
#即最终结果：[202,13,66,80,0,-13]
list01 = [80, 13, 66, 202, 0, -13]
max_value_index = list01.index(max(list01))#找出最大值的下标
list01[0],list01[max_value_index] = list01[max_value_index],list01[0]#通过下标交换最大元素和第一个元素
print(list01)

#求100以内的质数（质数：质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。）
list02 = []
for i in range(2,101):#1不为质数，因此从2开始
    for j in range(2,i):
        if i % j == 0:
#            print(f'{i}不为质数')
            break
    else:
#        print(f'{i}为质数')
        list02.append(i)
print('100以内质数列表',list02)