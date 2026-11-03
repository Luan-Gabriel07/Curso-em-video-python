while True:
    print ('-'*30)
    num = int(input("Quer ver a tabuada de qual valor?  "))
    if num < 0:
        print ("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break 
    else: 
        print ('-'*30)
        for cont in range (1,10):
            print (f"{num} X {cont} = {num * cont}")