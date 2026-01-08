import tkinter as tk
import sqlite3
from tkinter import messagebox

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Criação de Alunos")

        # Cria ou conecta ao banco de dados
        self.conn = sqlite3.connect("escola.db")
        self.cursor = self.conn.cursor()

        # Cria a tabela se ela não existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            stclass TEXT,
            marks REAL
        )''')
        self.conn.commit()

        # Interface
        self.name_label = tk.Label(root, text="Nome:")
        self.name_label.pack(anchor="center", padx=30)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.position_label = tk.Label(root, text="Matéria:")
        self.position_label.pack()

        self.stclass_entry = tk.Entry(root)
        self.stclass_entry.pack()

        self.salary_label = tk.Label(root, text="Notas:")
        self.salary_label.pack()

        self.marks_entry = tk.Entry(root)
        self.marks_entry.pack()

        self.add_button = tk.Button(root, text="Adicionar estudante", command=self.add_student)
        self.add_button.pack()

        self.student_listbox = tk.Listbox(root)
        self.student_listbox.pack()

        self.load_students()

        self.update_button = tk.Button(root, text="Atualizar estudante", command=self.update_student)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Excluir estudante", command=self.delete_student)
        self.delete_button.pack()

    def add_student(self):
        name = self.name_entry.get()
        stclass = self.stclass_entry.get()
        marks = self.marks_entry.get()
        if name and stclass and marks:
            #self.cursor.execute("INSERT INTO students (name, class, marks) VALUES (?, ?, ?)", (name, class, marks))
            self.cursor.execute("INSERT INTO students (name, stclass, marks) VALUES (?, ?, ?)", (name, stclass, marks))
            self.conn.commit()
            self.load_students()
            self.clear_entries()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def load_students(self):
        self.student_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()
        for row in students:
            self.student_listbox.insert(tk.END, f"{row[0]}. {row[1]}, {row[2]}, {'%.2f' % float(row[3])}")


    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.stclass_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

    def update_student(self):
        selected_student = self.student_listbox.get(tk.ACTIVE)
        if selected_student:
            student_id = int(selected_student.split(".")[0])
            name = self.name_entry.get()
            stclass = self.stclass_entry.get()
            marks = self.marks_entry.get()
            if name and stclass and marks:
                self.cursor.execute("UPDATE students SET name=?, stclass=?, marks=? WHERE id=?", (name, stclass, marks, student_id))
                self.conn.commit()
                self.load_students()
                self.clear_entries()
            else:
                messagebox.showwarning("Aviso", "Preencha todos os campos.")
        else:
            messagebox.showwarning("Aviso", "Selecione o estudante para atualizar.")

    def delete_student(self):
        selected_student = self.student_listbox.get(tk.ACTIVE)
        if selected_student:
            student_id = int(selected_student.split(".")[0])
            self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            self.conn.commit()
            self.load_students()
            self.clear_entries()
        else:
            messagebox.showwarning("Aviso", "Escolha um estudante para deletar.")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("340x400")
    app = CRUDApp(root)
    root.mainloop()
