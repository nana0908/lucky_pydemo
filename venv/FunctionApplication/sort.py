'''
冒泡排序
 1. 从当前元素起，向后依次比较每一对相邻元素，若逆序则交换 */
 2. 对所有元素均重复以上步骤，直至最后一个元素 */
'''
arr01 = [2, 4, 3, 5, 9, 8, 6, 4, 2, 1, 8, 19, 22, 28, 28, 16, 12]
arr01.sort()# 方法1：直接使用排序函数
print(arr01)
#print(len(arr01))
for i in range(1,len(arr01)):#冒泡排序
    for j in range(0,len(arr01)-i):
        if arr01[j] > arr01[j+1]:
            arr01[j],arr01[j+1] = arr01[j+1],arr01[j]
print(arr01)

#思路2 排序，定义null列表，通过每次取出最小值放入null列表中进行排序
arr02 = []
while True:
    if len(arr01) != 0:
        arr02.append(min(arr01))#每次取出列表中的最小值放入空列表中
        #print(arr02)
        arr01.remove(min(arr01))#然后源列表移除最小值
    else:
        break
print(arr02)

arr01 = [2, 4, 3, 5, 9, 8, 6, 4, 2, 1, 8, 19, 22, 28, 28, 16, 12]
arr02 = []
for i in range(len(arr01)):
    arr02.append(min(arr01))  # 每次取出列表中的最小值放入空列表中
    # print(arr02)
    arr01.remove(min(arr01))  # 然后源列表移除最小值
print(arr02)

'''
选择排序：将列表分为有序区和无序区
'''
arr01 = [2, 4, 3, 5, 9, 8, 6, 4, 2, 1, 8, 19, 22, 28, 28, 16, 12]
for i in range(len(arr01)-1):
    index = arr01.index( min(arr01[i:]))#从无序区找出最小值的下标
    if index < i:
        index = i
        for j in range(i+1,len(arr01)-1) :
            if arr01[j] < arr01[index]:
                index = j
    if index != i:
        arr01[i],arr01[index] = arr01[index],arr01[i]#最小值依次放入有序区
print(arr01)

arr01 = [2, 4, 3, 5, 9, 8, 6, 4, 2, 1, 8, 19, 22, 28, 28, 16, 12]
for i in range(len(arr01)-1):
    index = i#假设第一个值为最小值的下标
    for j in range(i,len(arr01)-1):
        if arr01[j+1] < arr01[index]:#从下一个位置开始和最小值对比，若小于最小值，则交换
            index = j+1
    arr01[i], arr01[index] = arr01[index], arr01[i]
print(arr01)

arr01 = [2, 4, 3, 5, 9, 8, 6, 4, 2, 1, 8, 19, 22, 28, 28, 16, 12]
for i in range(len(arr01)-1):
    index = arr01.index( min(arr01[i:]),i )#从i开始，这样已经排序的下标就不会影响找出来的下标了
    arr01[i], arr01[index] = arr01[index], arr01[i]
print(arr01)


