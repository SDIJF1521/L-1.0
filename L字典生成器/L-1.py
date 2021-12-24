文件 = input("请定义文件名称：")
while 文件 == False:
    print('文件名称不能为空')
    文件 = input("请定义文件名称：")
number1 = input('请输入最小密码数值：')
C = number1
number1 = int(number1)
while number1 < -1:
    print('最小密码数值必须大于等于0')
    number1 = input('请输入最小密码数值：')
    C = number1
    number1 = int(number1)
step = int(input('请设置步长：'))
while step < 1:
    print('步长必须大于等于1')
    step = int(input('请设置步长：'))
number2 = int(input('请输入最大密码数值：'))+1
while number2 < number1:
    print('最大密码数值不能小于最小密码数值')
    numer2 = int(input('请输入最大密码数值：'))+1
file = open(文件, 'w')
for i in range(number1,number2,step):     #生成原始密码
    mima= str(i)
    mima1 = list(mima)
    ZD = []
    ZD1=['0']
    CD1 = int(len(mima1))
    z = list(C)
    CD2 = int(len(z))
    CD = CD2 - CD1
    while CD != 0:                 #补全前端0位
        ZD.extend(ZD1[0])
        CD2 = len(ZD)
        CD = CD-1
    ZD.extend(mima1)              #生成密码
    Y = ''.join(ZD)               #去除多余符号
    print(Y)
    file.write(Y)  # 写入密码      #存入字典文件
    file.write("\r")
