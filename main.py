def gam (name):
    unsv = 'y'
    f = open ('m.txt', 'a')
    f.write (name +'\n')
    print ("-----------"+ name +"--------"+'\n')
    while unsv == 'y':
        a = input("name - ")
        b = input("money - ")
        f.write (a + " - " + str(b)+'\n')
        unsv = input("next? (y / n)")
    f.write ("-----------"+ name + "---end------"+'\n')
    f.close()

gam("debet")
gam("credit")
