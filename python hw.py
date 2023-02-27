def main():
    t1,t2,t3,t4,t5,avg = calc_average()
    grading (t1)
    print('score 1: ' + str(t1) + letgrade)
    grading (t2)
    grading (t3)
    grading (t4)
    grading (t5)
def calc_average():
    print('insert test score')
    test1 = int(input('test score 1'))
    test2 = int(input('test score 2'))
    test3 = int(input('test score 3'))
    test4 = int(input('test score 4'))
    test5 = int(input('test score 5'))
    testavg = (int(test1)) + (int(test2)) + (int(test3)) + (int(test4)) + int(test5)
    testavg = testavg / 5
    return test1,test2,test3,test4,test5,testavg


letgrade = 'kay'
def grading(testimpt):
    i = 0
    while i != 1:
        if 90 <= testimpt <= 100:
            i = i + 1
            letgrade = ('A')
        elif 89 >= testimpt > 79:
            i = i + 1
            letgrade = ('B')
        elif 79 >= testimpt > 69:
            i = i + 1
            letgrade = ('C')
        elif 69 >= testimpt > 59:
            i = i + 1
            letgrade = ('D')
        else:
            i = i + 1
            letgrade =('F')

main()


    
