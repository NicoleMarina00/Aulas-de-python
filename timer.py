import tkinter as tk
from tkinter import messagebox, ttk
import time
import threading

def timer():
    while True:
        try:
            num = int(input("Entre um número: "))
            if num <= 0:
                print("Coloque um número maior que 0.")
                return


            for count in range(num+1):
                print(count)
                time.sleep(1)
        except ValueError:
            print("Número inválido. Coloque apenas números inteiros.")
        except Exception as e:
            print(f"Erro: {e}")



def start():
    try:
        num = int(entry_number.get())

        if num <= 0:
            messagebox.showerror("Número inválido. Coloque apenas números inteiros.", "Coloque um número maior que 0.")
            return

        
        button_start.config(state=tk.DISABLED)

        
        progress_bar['value'] = 0
        progress_bar['maximum'] = num+1
        label_output.config(text="")

        def run_countdown():
            for i in range(num+1):
                label_output.config(text=str(i))
                progress_bar['value'] = i+1
                time.sleep(1)
            label_output.config(text="Contagem finalizada")
            progress_bar['value'] = num+1  # Full bar at end
            

        threading.Thread(target=run_countdown).start()

    except ValueError:
        messagebox.showerror("Número inválido. Coloque apenas números inteiros.", "Coloque um número maior que 0.")



root = tk.Tk()
root.title("Timer")
root.geometry("350x300")


tk.Label(root, text="Insira o número").pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack(pady=5)


button_start = tk.Button(root, text="Começar timer", command=start)
button_start.pack(pady=10)

# Output label
label_output = tk.Label(root, text="", font=("Helvetica", 24))
label_output.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=250, mode='determinate')
progress_bar.pack(pady=10)


if __name__ == "__main__":
    root.mainloop()