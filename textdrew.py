from os import name
from tkinter import *
from tkinter import filedialog
from tkinter import font


root = Tk()
root.title('Code Drew')
root.geometry("1200x660")

# Função que cria um novo arquivo
def creat_file():
    text1.delete("1.0", END)
    root.title("Novo Arquivo - Code Drew")
    status.config(text="Novo Arquivo        ")

# Função que Abre o arquivo selecionado
def open_file():
    text1.delete("1.0", END)
    # Tipo de Arquivo
    text_file = filedialog.askopenfilename(title="Abrir Arquivo", filetypes=(("Arquivos de texto", "*.txt"), ("Arquivos Python", "*.py"), ("Todos os Arquivos", "*.*")))
    # troca na barra de estatus
    nome = text_file
    status.config(text=f'{nome}'       )
    nome = nome.replace("Abriu arquivo", "")
    root.title(f'{nome} - Code Drew')

    # Abrir Arquivo
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Adicionando arquivo para caixa de texto
    text1.insert(END, stuff)
    # Fechando arquivo aberto
    text_file.close()

def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Salvar Arquivo", filetypes=(("Arquivo de texto", "*.txt"), ("Arquivo Python", "*.py"), ("Todos os arquivos", "*.*")))
    if text_file:
        # Atualizando barra de status
        nome = text_file
        status.config(text=f'Salvo {nome}')
        root.title(f'{nome} - Code Drew')

        # Salva o arquivo
        text_file = open(text_file, 'w')
        text_file.write(text1.get(1.0, END))
        text_file.close()

# Cria um Main Frame
mframe = Frame(root)
mframe.pack(pady=5)

# Cria um Scrollbar
text_scroll = Scrollbar(mframe)
text_scroll.pack(side=RIGHT, fill=Y)

# Cria um text box
text1 = Text(mframe, width=97, height=25, font=("helvetica, 16"), selectbackground="yellow",
selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
text1.pack()

# Confuguração do Scrollbar
text_scroll.config(command=text1.yview)

# Criando menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Adicionando arquivos no menu
arq_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Arquivo", menu=arq_menu)
arq_menu.add_command(label="Novo", command=creat_file)
arq_menu.add_command(label="Abrir", command=open_file)
arq_menu.add_command(label="Salvar")
arq_menu.add_command(label="Salvar Como", command=save_as)
arq_menu.add_separator()
arq_menu.add_command(label="Sair", command=root.quit)

# Adicionar
editor_menu = Menu(my_menu)
my_menu.add_cascade(label="Editar", menu=editor_menu)
editor_menu.add_command(label="Cortar")
editor_menu.add_command(label="Copiar")
editor_menu.add_command(label="Voltar")

# Adicionar barra de estados em baixo do programa
status = Label(root, text="Pronto        ", anchor=E)
status.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()