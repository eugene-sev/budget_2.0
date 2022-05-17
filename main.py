import shutil
import datetime
d = datetime.date.today()
f = open ('m.txt', 'w')
f.write (str(d)+'\n')
f.close()
def gam (name):
    c = 0
    f = open ('m.txt', 'a')
    f.write (name +'\n')
    print ("-----------"+ name +"--------"+'\n'+"tap name 'next' for the next step"+"\n")
    while True:
        a = input("name - ")
        if a == "next":
            break
        try:
            b = eval(input("money - "))
        except NameError:
            print('enter count (number)')
            b = eval(input("money - "))
        c += b
        f.write (a + " - " + str(b)+'\n')
    f.write ("SUM "+ name +'\n' + str(c) +'\n' + "---------"+'\n')
    f.close()
gam("debet")
gam("credit")

my_file = open('m.txt', 'r')
tio = my_file.readlines()
index = tio.index("SUM debet\n")
index2 = tio.index("SUM credit\n")
full = int(tio[index+1]) - int(tio[index2+1])
f = open ('m.txt', 'a')
f.write ("your many now is - " + str(full))
f.close()
shutil.copy('m.txt',str(d)+'.txt')
print ("your many now is - " + str(full))
