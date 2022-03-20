def main():
    # def's

    # ADIÇÃO
    def soma(A, B):
        return A + B

        # SUBTRAÇÃO


    def sub(C, D):
        return (A - B)

        # DIVISÕES


    def divi(A, B):
        return A / B


    def divix(A, B):
        return A // B


    def diviz(A, B):
        return A % B

        # MULTIPLICAÇÃO


    def mult(A, B):
        return A * B

        # FATORIAL


    def fat(A):
        if A > 1:
            fat = 1
            while A > 1:
                fat *= A
                A -= 1
            return fat
        
        # EXPONENCIAL
        
    def exp(A, B):
        if A >= 1:
            return A ** B
        elif A <= -1:
            return print("1/"(A) ** B)
        else:
            return 1

     # começo do programa
    print("\nAbaixo temos algumas opções de operações que o "
          "usuário pode fazer\n ")
    print("\n1 - Operaão de soma com entre dois números."
          "\n2 - Operação de subtração entre dois números."
          "\n3 - Operação de multiplicação entre dois números."
          "\n4 - Operção de divisão entre dois números."
          "\n5 - Operação fatorial entre um número."
          "\n6 - Operação exponencial de um número."
          "\n7 - Operação com logaritmo de um número.")
    x = int(input("\nDigite um número de qual operação você deseja:"))


    if x >= 1 or x <= 7:
        
        if x == 1:
            print("\nA operação vai ser feita da seguinte forma: A + B")
            A = int(input("Digite um valor para A:"))
            B = int(input("Digite um valor para B:"))
            soma2 = soma(A, B)
            print("\nA soma dos números", A, "e", B, "resulta em:", soma2)
        elif x == 2:
            print("\nA operação vai ser feita da seguinte forma: A - B")
            A = int(input("Digite um valor para A:"))
            B = int(input("Digite um valor para B:"))
            sub2 = sub(A, B)
            print("\nA subtração dos números", A, "e", B, "resulta em:", sub2)
        elif x == 3:
            print("\nA operação vai ser feita da seguinte forma: A * B")
            A = int(input("\nDigite um valor para A:"))
            B = int(input("\nDigite um valor para B:"))
            mult2 = mult(A, B)
            print("\nA multiplicação de", A, "com", B, "resulta em:", mult2)
        elif x == 4:
            print("\nA operação vai ser feita das seguintes formas: A / B,"
                  "\nA // B, A % B")
            A = int(input("Digite um valor para A:"))
            B = int(input("Digite um valor para B:"))
            divi2 = divi(A, B)
            divix2 = divix(A, B)
            diviz2 = diviz(A, B)
            print(divi2)
            print(divix2)
            print(diviz2)
            print("\nA divisão dos números", A, "e", B, "com ponto flutuante"
                  "\nresulta em:", divi2, ",a divisão com arredondamento"
                  "para baxio resulta em:", divix2, "e a sobra da divisão"
                  "é:", diviz2)
        elif x == 5:
            print("\nA operação vai ser feita da seguinte forma: A * A-1 *"
                  " A-2 * ... * A - A")
            A = int(input("Digite um valor para A:"))
            if A < 0:
                print("\nNão é possivel fazer a operação de fatoração"
                      "\n com n° negativos.")
            
            elif A == 0:
                print("\nO fatorial de 0 é 1.")
            
            else:
                fat2 = fat(A)
                print("\nO resultado do fatorial de", A, "é:", fat2)
        elif x == 6:
            print("\nA operação vai ser feita da seguinte forma:"
                 "\nA ^ B")
            A = int(input("\nDigite um valor para A:"))
            B = int(input("\nDigite um valor para B:"))
            exp2 = exp(A, B)
            print("\nO resultado de", A,"elevado", B,"resulta em:", exp2,
                  "\nou")
    else:
        print("\nVocê digitou um número não correspondente das operações")

main()