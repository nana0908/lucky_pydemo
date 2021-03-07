'''
编写后台管理员管理前台会员信息系统:
1. 后台管理员只有一个用户: admin, 密码: admin
2. 当管理员登陆成功后， 可以管理前台会员信息.
3. 会员信息管理包含:
     添加会员信息
     删除会员信息
     查看会员信息
     退出
界面如下，输入相应的数字进入相应的功能
**********操作目录**********
           1.添加会员信息
           2.删除会员信息
           3.查看会员信息
           4.退出

- 添加用户:
   1). 判断用户是否存在?
   2).  如果存在， 报错；
   3).  如果不存在，添加用户名和密码分别到列表中;

- 删除用户
   1). 判断用户名是否存在
   2). 如果存在，删除；
   3). 如果不存在， 报错；
'''


# user,password = input('请输入用户名和密码：（空格分开）').split(' ')
# if user == 'admin' and password == 'admin':
#     print('''
#     **********操作目录**********
#            1.添加会员信息
#            2.删除会员信息
#            3.查看会员信息
#            4.退出''')
# user_list = []
# while True:
#     num = int(input('请选择操作（输入相应的数字进入相应的功能）：'))
#     if num == 1:
#         member_name = input('请输入需要添加的会员姓名：')
#         member_age = input('请输入会员年龄：')
#         member_occupation = input('请输入会员职业：')
#         name_list = []
#         for i in range(0, len(user_list)):
#             name_list.append(user_list[i]['会员姓名'])
#             #print('当前会员姓名：',name_list)
#         if member_name in name_list:
#             print('用户已存在，请重新输入')
#         else:
#             member_dict = {'会员姓名': member_name, '会员年龄': member_age, '会员职业': member_occupation}
#             user_list.append(member_dict)
#         #print(user_list)
#
#     elif num == 2:
#         member_name = input('请输入需要删除的会员姓名：')
#         name_list = []
#         for i in range(0, len(user_list)):
#             name_list.append(user_list[i]['会员姓名'])
#             #print('当前会员姓名：',name_list)
#         if member_name in name_list:
#             index = name_list.index(member_name)
#             #print(index)
#             user_list.pop(index)
#             print('会员删除成功')
#             #print(user_list)
#         else:
#             print('用户不存在，请重新输入')
#     elif num == 3:
#         if len(user_list) != 0:
#             for i in range(0, len(user_list)):
#                 print(user_list[i])
#         else:
#             print('当前会员信息为null')
#     elif num == 4:
#         break
#     else:
#         print('无对应操作事项，请重新输入')
# else:
#     print('用户名或密码错误，请重新登录')
#
# print(user_list)

root_name = input('请输入用户名：')
root_password = input('请输入密码：')
user = ['admin']
password = ['admin']
while True:
    if root_name == 'admin':
        if root_password == 'admin':
            print('''
                **********操作目录**********
                       1.添加会员信息
                       2.删除会员信息
                       3.查看会员信息
                       4.退出''')
            option = input('请输入您的选择：')
            if option == '1':
                print('************添加会员信息************')
                add_user = input('请输入需要添加的会员名称：')
                add_password = input('请输入会员密码：')
                if add_user in user:
                    print('添加会员失败，该用户已经存在！')
                else:
                    user.append(add_user)
                    password.append(add_password)
                    print(f'恭喜，会员{add_user}添加成功！')
            elif option == '2':
                print('************删除会员信息************')
                del_user = input('请输入需要删除的会员名称：')
                if del_user in user:
                    del_index = user.index(del_user)
                    user.remove(del_user)
                    del password[del_index]
                    print(f'会员{del_user}删除成功！')
                else:
                    print(f'用户{del_user}不存在')
            elif option == '3':
                for i in range(0,len(user)):
                    print(f'用户名：{user[i]}，密码：{password[i]}')
            elif option == '4':
                print('************退出系统************')
                exit()
            else:
                print('请输入正确的操作指令。')

        else:
            print(f'用户{root_name}密码不正确')
    else:
        print(f'用户{root_name}不存在')


