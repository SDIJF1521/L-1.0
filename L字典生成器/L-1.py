文件 = input("请定义文件名称：")
while len(文件) == False:
    print('文件名称不能为空')
    文件 = input("请定义文件名称：")
A1 = input("请输入最小密码数值：")            #定义最小密码数值
A = int(A1)
while A <0 :                                   #判断密码长度是否大于等于0
    print("最小数值必须大于等于0")
    A1 = input("请输入最小密码数值：")
    A = int(A1)
B1 = input("请输入最大密码数值：")            #定义最大密码数值
B = int(B1)
while B<A :
    print("数值必须大于或小于最小数值")        #判断最大密码数值是否大于或者等于最小密码数值
    B1 = input("请输入最大密码数值")
    B = int(B1)
file = open(文件,'w')
C=str(A1)
file.write(C)                                 
file.write('\r')                         
A2 = list(A1)                                
while A < B :                               
    A = A + 1                                 
    C=str(A)                                
    C1 = list(C)                             
    CD = len(C1)                              
    CD1 = len(A2)                             
    CD1 = int(CD1)
    LB = []
    LB1 = ['0']
    CD2 = len(LB)
    CD2 = int(CD2)
    CD3 = CD1 -CD
    while CD3  > CD2 :
        LB.extend(LB1[0])
        CD2 = len(LB)
        CD = list(C)
    LB.extend(C)
    C = ''.join(LB)
    print(C)
    file.write(C)                             #写入密码
    file.write("\r")                        #换行
