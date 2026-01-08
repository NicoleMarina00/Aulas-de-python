import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

lista_produtos = []


def registros():

    prod = entry_produto.get()
    val = entry_valor.get()


    if not prod or not val:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    lista_produtos.append(f"{prod};{val.replace(',', '.')}")
    

    lbl_status_venda.config(text=f"Produto '{prod}' adicionado! Adicione mais ou clique em Finalizar.", fg="blue")

    if not lista_produtos:
        messagebox.showerror("Erro", "Nenhuma venda registrada.")
        return


    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        for linha in lista_produtos:
            arquivo.write(linha + "\n")


    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
          
            for linha in linhas[1:]:
                partes = linha.strip().split(';')  
                
                nome = partes[0]
                valor = partes[1]

        lbl_status_venda.config(text="Arquivo 'produtos.txt' salvo e lido com sucesso!")
        
    except Exception as erro:
        messagebox.showerror("Erro", f"Deu erro ao ler o arquivo: {erro}")

def ler():
    leitura = Toplevel(janela)  
    leitura.title("Produtos")
    leitura.geometry("250x150")  
    text_widget = tk.Text(leitura, wrap="word", width=40, height=10)
    text_widget.pack(pady=10)


    with open("produtos.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
        text_widget.delete(1.0, tk.END)  
        text_widget.insert(tk.END, conteudo)
    


janela = tk.Tk()
janela.title("Exercícios da Faculdade")
janela.geometry("300x250")


tk.Label(janela, text="Nome do Produto:").pack()
entry_produto = tk.Entry(janela)
entry_produto.pack(pady=10)

tk.Label(janela, text="Valor Unitário:").pack()
entry_valor = tk.Entry(janela)
entry_valor.pack(pady=10)


btn_add = tk.Button(janela, text="Adicionar Produto", command=registros, bg="#dddddd")
btn_add.pack(pady=10)


lbl_status_venda = tk.Label(janela, text="", font=("Arial", 8))
lbl_status_venda.pack()


btn_calc = tk.Button(janela, text="Mostrar registros", command=ler, bg="lightblue")
btn_calc.pack(pady=10)


janela.mainloop()


