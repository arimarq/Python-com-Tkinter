# importacoes de modulos
from tkinter import * # importando tkinter
from tkcalendar import DateEntry # importanto o calendario
from tkinter import ttk # importanto a função de tabela para o frame direita
from tkinter import messagebox # importando messagebox
from view import * # importando codigo do arquivo view .py

# cores
cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = "#e06636"  # - profit
cor6 = "#038cfc"  # azul
cor7 = "#ef5350"  # vermelha
cor8 = "#263238"  # + verde
cor9 = "#e9edf5"  # skyblue

# criando janela
janela = Tk()
janela.title('')
janela.iconbitmap('bandeira.ico')
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)  # bloqueia tamanho da janela

# variavel tree global
global tree

# funcao inserir
def inserir():
    # obtem o valor digitado nos campos
    nome = ent_nome.get()
    email = ent_email.get()
    telefone = ent_telefone.get()
    data = ent_data.get()
    estado = ent_estado.get()
    sobre = ent_sobre.get()

    lista = [nome, email, telefone, data, estado, sobre]

    if nome == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio!')
    else:
        inserir_registro(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

        # limpa a digitacao dos campos
        ent_nome.delete(0, 'end')
        ent_email.delete(0, 'end')
        ent_telefone.delete(0, 'end')
        ent_data.delete(0, 'end')
        ent_estado.delete(0, 'end')
        ent_sobre.delete(0, 'end')

    # apagando dados na frame direita
    for widget in frame_direita.winfo_children():
        widget.destroy()

    # reexibindo a frame direita
    mostrar()


# funcao atualizar
def atualizar():
    try:
        tree_dados = tree.focus() # obtem os dados clicados na frame direita
        tree_dicionario = tree.item(tree_dados) # converte os dados para formato dicionario
        tree_lista = tree_dicionario['values'] # grava os valores numa lista
        id_dado = tree_lista[0] # pega o valor do indice 0 na lista (ou seja, o id do registro)

        # limpa a digitacao dos campos
        ent_nome.delete(0, 'end')
        ent_email.delete(0, 'end')
        ent_telefone.delete(0, 'end')
        ent_data.delete(0, 'end')
        ent_estado.delete(0, 'end')
        ent_sobre.delete(0, 'end')

        # insere os dados da tree_lista nos campos
        ent_nome.insert(0, tree_lista[1])
        ent_email.insert(0, tree_lista[2])
        ent_telefone.insert(0, tree_lista[3])
        ent_data.insert(0, tree_lista[4])
        ent_estado.insert(0, tree_lista[5])
        ent_sobre.insert(0, tree_lista[6])

        def gravar():
            # obtem o valor digitado nos campos
            nome = ent_nome.get()
            email = ent_email.get()
            telefone = ent_telefone.get()
            data = ent_data.get()
            estado = ent_estado.get()
            sobre = ent_sobre.get()

            lista = [nome, email, telefone, data, estado, sobre, id_dado]

            if nome == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio!')
            else:
                atualizar_registro(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram alterados com sucesso!')

                # limpa a digitacao dos campos
                ent_nome.delete(0, 'end')
                ent_email.delete(0, 'end')
                ent_telefone.delete(0, 'end')
                ent_data.delete(0, 'end')
                ent_estado.delete(0, 'end')
                ent_sobre.delete(0, 'end')

            # apagando dados na frame direita
            for widget in frame_direita.winfo_children():
                widget.destroy()

            # apaga o botao confirma no frame baixo
            bt_confirma.destroy()

            # reexibe a frame direita
            mostrar()

        # criar botao confirma
        bt_confirma = Button(frame_baixo, text='Confirma', command=gravar, width=10, font='Ivy 9 bold', bg=cor2, fg=cor1, overrelief='ridge')
        bt_confirma.place(x=110, y=360)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha na tabela!')


# funcao deletar
def deletar():
    try:
        tree_dados = tree.focus() # obtem os dados clicados na frame direita
        tree_dicionario = tree.item(tree_dados) # converte os dados para formato dicionario
        tree_lista = tree_dicionario['values'] # grava os valores numa lista
        id_dado = [tree_lista[0]] # pega o valor do indice 0 na lista (ou seja, o id do registro)

        # deleta os dados da linha selecionada
        deletar_registro(id_dado)

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

        # apagando dados na frame direita
        for widget in frame_direita.winfo_children():
            widget.destroy()

        # reexibe a frame direita
        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma linha na tabela!')


# criando as frames
frame_cima = Frame(janela, width=310, height=50, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=733, height=403, bg=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0)
frame_direita.grid_rowconfigure(0, weight=1) # faz com que a linha 0 "rowconfigure(0...)" ocupe toda a frame "rowconfigure(... weight=1)"

# criando titulo no frame cima
app_nome = Label(frame_cima, text='Agendamento de Consultas', font=('Ivy', '13', 'bold'), bg=cor2, fg=cor1, relief='flat')
app_nome.place(x=10, y=20, anchor=NW)

# criando widgets no frame baixo
lbl_nome = Label(frame_baixo, text='Nome *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
lbl_nome.place(x=10, y=10, anchor=NW)
ent_nome.place(x=15, y=40)

lbl_email = Label(frame_baixo, text='E-mail *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
lbl_email.place(x=10, y=70, anchor=NW)
ent_email.place(x=15, y=100)

lbl_telefone = Label(frame_baixo, text='Telefone *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
lbl_telefone.place(x=10, y=130, anchor=NW)
ent_telefone.place(x=15, y=160)

lbl_data = Label(frame_baixo, text='Data da Consulta *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_data = DateEntry(frame_baixo, locale='pt_br', width=12, background='blue', foreground='white', borderwidth=2)
lbl_data.place(x=10, y=190, anchor=NW)
ent_data.place(x=15, y=220)

listaEstadoCons = ['Normal', 'Urgente', 'Urgentissima']
lbl_estado = Label(frame_baixo, text='Estado da Consulta *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_estado = ttk.Combobox(frame_baixo, values=listaEstadoCons, width=15, justify='left')
lbl_estado.place(x=160, y=190, anchor=NW)
ent_estado.place(x=165, y=220)

lbl_sobre = Label(frame_baixo, text='Consulta Sobre *', font=('Ivy', '10', 'bold'), bg=cor1, fg=cor4, relief='flat')
ent_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
lbl_sobre.place(x=10, y=250, anchor=NW)
ent_sobre.place(x=15, y=280)

# criando botoes no frame baixo
bt_inserir = Button(frame_baixo, text='Inserir', command=inserir, width=10, font=('Ivy', '9', 'bold'), bg=cor6, fg=cor1, overrelief='ridge')
bt_inserir.place(x=15, y=330)

bt_atualizar = Button(frame_baixo, text='Atualizar', command=atualizar, width=10, font=('Ivy', '9', 'bold'), bg=cor2, fg=cor1, overrelief='ridge')
bt_atualizar.place(x=110, y=330)

bt_deletar = Button(frame_baixo, text='Deletar', command=deletar, width=10, font=('Ivy', '9', 'bold'), bg=cor7, fg=cor1, overrelief='ridge')
bt_deletar.place(x=205, y=330)


def mostrar():
    global tree
    # criando lista para exibir no frame direita
    lista = mostrar_registros()

    # lista para cabecario
    tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # criar a vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # criar a horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    # aplicando as scrollbar (hor e ver) na tela
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # exibindo os widgets na frame direita
    tree.grid(column=0, row=0, sticky='nsew') # a funcao sticky "estende" o widget na direcao apontada (nsew = norte, sul, etc)
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # #### EXIBINDO OS DADOS NO FRAME DIREITA

    # definindo os parametros de alinhamento para o cabecalho e coluna de dados
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 90, 80, 100]
    n = 0

    # exibindo o cabecalho e colunas de dados com os parametros acima
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    # exibindo os dados da lista
    for item in lista:
        tree.insert('', 'end', values=item)


# chamando a funcao mostrar
mostrar()

# executando e exibindo a janela na tela
janela.mainloop()
