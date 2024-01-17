import tkinter as tk


janela=tk.Tk()

var_aviao = tk.IntVar()

botao_classeeconomica = tk.Radiobutton(text='Classe Econômica', variable=var_aviao, value='Classe Economica')
botao_classeexecutiva = tk.Radiobutton(text='Classe Executiva', variable=var_aviao, value='Classe Executiva')
botao_primeiraclasse = tk.Radiobutton(text='Primeira Classe', variable=var_aviao, value='Primeira Classe')
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)

def enviar():
    print(var_aviao.get())

janela.mainloop()

