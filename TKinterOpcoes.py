import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text='Deseja receber emails promocionais?', variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar Termos de Uso e Políticas de Privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)

def enviar():
    if var_promocoes.get():
        print('Com promoção')
    else:
        print('Sem promoção')
    if var_politicas.get():
        print('Concordou')
    else:
        print('Não concordou')


botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)

janela.mainloop()