from tkinter import *




#estrutura da janela
calculadora = Tk ()
calculadora.title ('Calculadora')
calculadora.geometry ('480x500')
calculadora.resizable (width = False, height = False)
calculadora.config ( background = "#426F42")


def btNumeros (numero):
    pegaNumero = campoNumeros.get()
    campoNumeros.delete (0, END)
    campoNumeros.insert (0, str(pegaNumero) + str(numero))
    return


def limpaCampo():
    campoNumeros.delete (0, END)
    return


def soma():
    pegaNumeros = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'soma'
    primeiroNumero = int(pegaNumeros)
    campoNumeros.delete (0, END)
    return


def subtracao():
    pegaNumeros = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'subtracao'
    primeiroNumero = int(pegaNumeros)
    campoNumeros.delete (0, END)
    return


def divisao():
    pegaNumeros = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'divisao'
    primeiroNumero = int(pegaNumeros)
    campoNumeros.delete (0, END)
    return


def multiplicacao():
    pegaNumeros = campoNumeros.get()
    global primeiroNumero
    global operacao
    operacao = 'multiplicacao'
    primeiroNumero = int(pegaNumeros)
    campoNumeros.delete (0, END)
    return


def igual ():
    pegaNumero = campoNumeros.get()
    campoNumeros.delete (0, END)
    if operacao == 'soma':
        campoNumeros.insert(0, primeiroNumero + int(pegaNumero))
    elif operacao == 'subtracao':
        campoNumeros.insert (0, primeiroNumero - int(pegaNumero))
    elif operacao == 'divisao':
        campoNumeros.insert (0, primeiroNumero / int(pegaNumero))  
    elif operacao == 'multiplicacao':
        campoNumeros.insert (0, primeiroNumero * int(pegaNumero))
    return    


#entry
campoNumeros = Entry(calculadora, width = 50, )
campoNumeros.place(x = 100, y = 50)


#botoes
Bt7 = Button (calculadora, text = '7',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (7))
Bt7.place (x = 50, y = 150)


Bt8 = Button (calculadora, text = '8',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (8))
Bt8.place (x = 150, y = 150)


Bt9 = Button (calculadora, text = '9',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (9))
Bt9.place (x = 250, y = 150)


Btx = Button (calculadora, text = 'x',relief = FLAT,  width = 10, height = 3, command = multiplicacao)
Btx.place (x = 350, y = 150)


Bt4 = Button (calculadora, text = '4',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (4))
Bt4.place (x = 50, y = 225)


Bt5 = Button (calculadora, text = '5',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (5))
Bt5.place (x = 150, y = 225)


Bt6 = Button (calculadora, text = '6',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (6))
Bt6.place (x = 250, y = 225)


Btmenos = Button (calculadora, text = '-',relief = FLAT,  width = 10, height = 3, command = subtracao)
Btmenos.place (x = 350, y = 225)


Bt1 = Button (calculadora, text = '1',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (1))
Bt1.place (x = 50, y = 300)


Bt2 = Button (calculadora, text = '2',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (2))
Bt2.place (x = 150, y = 300)


Bt3 = Button (calculadora, text = '3',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (3))
Bt3.place (x = 250, y = 300)


Btmais = Button (calculadora, text = '+',relief = FLAT,  width = 10, height = 3, command = soma)
Btmais.place (x = 350, y = 300)


Btc = Button (calculadora, text = 'C',relief = FLAT,  width = 10, height = 3, command = limpaCampo)
Btc.place (x = 50, y = 375)


Bt0 = Button (calculadora, text = '0',relief = FLAT,  width = 10, height = 3, command = lambda : btNumeros (0))
Bt0.place (x = 150, y = 375)


Btdivisao = Button (calculadora, text = '÷',relief = FLAT,  width = 10, height = 3, command = divisao)
Btdivisao.place (x = 250, y = 375)


Btigual = Button (calculadora, text = '=',relief = FLAT,  width = 10, height = 3, command = igual)
Btigual.place (x = 350, y = 375)



calculadora.mainloop()
