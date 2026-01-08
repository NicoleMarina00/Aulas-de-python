import tkinter as tk
from tkinter import messagebox
from collections import Counter 


lista_vendas = []


def adicionar_venda():

    prod = entry_produto.get()
    qtd = entry_qtd.get()
    val = entry_valor.get()


    if not prod or not qtd or not val:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    

    lista_vendas.append(f"{prod};{qtd};{val.replace(',', '.')}")
    

    entry_produto.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    

    lbl_status_venda.config(text=f"Produto '{prod}' adicionado! Adicione mais ou clique em Finalizar.", fg="blue")

def finalizar_calcular():
    if not lista_vendas:
        messagebox.showerror("Erro", "Nenhuma venda registrada.")
        return


    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("produto;valor\n") # Cabeçalho
        for linha in lista_vendas:
            arquivo.write(linha + "\n")


    faturamento_total = 0
    max_qtd = -1
    prod_mais_vendido = ""

    try:
        with open("vendas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            
          
            for linha in linhas[1:]:
                partes = linha.strip().split(';')  
                
                nome = partes[0]
                qtd = int(partes[1])
                valor = float(partes[2])

                # Contas
                faturamento_total += (qtd * valor)

                if qtd > max_qtd:
                    max_qtd = qtd
                    prod_mais_vendido = nome

       
        lbl_resultado_vendas.config(
            text=f"Faturamento Total: R$ {faturamento_total:.2f}\n"
                 f"Mais Vendido: {prod_mais_vendido} ({max_qtd} un.)",
            fg="green"
        )
        lbl_status_venda.config(text="Arquivo 'vendas.txt' salvo e lido com sucesso!")
        
    except Exception as erro:
        messagebox.showerror("Erro", f"Deu erro ao ler o arquivo: {erro}")


def processar_texto():
    texto_exemplo = """O Python é uma linguagem incrível.
    O Python permite criar programas simples e complexos.
    Python é muito usado na faculdade e no trabalho.
    A linguagem Python é ótima."""

    
    with open("texto.txt", "w", encoding="utf-8") as f:
        f.write(texto_exemplo)

  
    with open("texto.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()


    conteudo_limpo = conteudo.lower().replace(".", "").replace(",", "").replace("\n", " ")
    palavras = conteudo_limpo.split() # Transforma em lista de palavras


    contador = Counter(palavras)
    
    total_palavras = len(contador)
    palavra_top, qtd_top = contador.most_common(1)[0] 

 
    with open("analise.txt", "w", encoding="utf-8") as f:
        f.write(f"{total_palavras};{palavra_top};{qtd_top}")


    lbl_resultado_texto.config(
        text=f"Total Palavras Diferentes: {total_palavras}\n"
             f"Palavra Mais Repetida: '{palavra_top}' ({qtd_top} vezes)",
        fg="green"
    )



janela = tk.Tk()
janela.title("Exercícios da Faculdade")
janela.geometry("400x600")


tk.Label(janela, text="--- EXERCÍCIO 1: VENDAS ---", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(janela, text="Nome do Produto:").pack()
entry_produto = tk.Entry(janela)
entry_produto.pack()

tk.Label(janela, text="Quantidade:").pack()
entry_qtd = tk.Entry(janela)
entry_qtd.pack()

tk.Label(janela, text="Valor Unitário:").pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()


btn_add = tk.Button(janela, text="Adicionar Produto", command=adicionar_venda, bg="#dddddd")
btn_add.pack(pady=5)


lbl_status_venda = tk.Label(janela, text="", font=("Arial", 8))
lbl_status_venda.pack()


btn_calc = tk.Button(janela, text="Finalizar e Calcular", command=finalizar_calcular, bg="lightblue")
btn_calc.pack(pady=10)


lbl_resultado_vendas = tk.Label(janela, text="Resultados aparecerão aqui...", font=("Arial", 10, "bold"))
lbl_resultado_vendas.pack(pady=10)



tk.Label(janela, text="---------------------------------").pack(pady=5)
tk.Label(janela, text="--- EXERCÍCIO 2: TEXTO ---", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(janela, text="Clique para criar arquivo, analisar e salvar:").pack()

btn_texto = tk.Button(janela, text="Executar Análise de Texto", command=processar_texto, bg="lightgreen")
btn_texto.pack(pady=10)

lbl_resultado_texto = tk.Label(janela, text="Resultados aparecerão aqui...", font=("Arial", 10, "bold"))
lbl_resultado_texto.pack(pady=10)


janela.mainloop()