import os
caselist = os.listdir('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\TEST_CASE')
for a in caselist:
    s=a.split('.')[-1]
    if s=='py':
        os.system('python C:\\Users\\Administrator\\PycharmProjects\\untitled2\\TEST_CASE\%s 1>>log11.txt 2>&1'%a)