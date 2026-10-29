
import customtkinter as ctk
from tkinter import messagebox, ttk
import psycopg
from PIL import Image
from pathlib import Path

DB_CONFIG = {
    "dbname": "cinema",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}

BASE_DIR = Path(__file__).resolve().parent

FILEIRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
COLUNAS = list(range(1,21))

def selecionar_cadeira(cadeira):
    if cadeira.cget("fg_color") == "#745B6B":
        cadeira.configure(fg_color="#C5AAB2")
    else:
        cadeira.configure(fg_color="#745B6B")
    
def criar_cadeiras(frame):
    botoes = []

    for linha, letra in enumerate(FILEIRAS):
        for coluna, numero in enumerate(COLUNAS):
            cadeira = ctk.CTkButton(
                frame,
                text=f"{letra}{numero}",
                width=48,
                height=40,
                fg_color="#C5AAB2",
                hover_color="#8C6980",
                text_color="#1A1518",
                corner_radius=8
            )

            cadeira.configure(
                command=lambda c=cadeira: selecionar_cadeira(c)
            )

            cadeira.grid(
                row=linha,
                column=coluna,
                padx=4,
                pady=4,
                sticky="nsew" #esticar para todos os lados
            )

            botoes.append(cadeira)

    return botoes


def esconder_todas_as_telas():
    frame_inicial.pack_forget()
    frame_historico.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()
    frame_sala4.pack_forget()
    frame_sala5.pack_forget()

def mostrar_inicio():
    esconder_todas_as_telas()
    frame_inicial.pack(fill="both", expand=True)

def mostrar_historico():
    esconder_todas_as_telas()
    frame_historico.pack(fill="both", expand=True)

def mostrar_sala1():
    esconder_todas_as_telas()
    frame_sala1.pack(fill="both", expand=True)

def mostrar_sala2():
    esconder_todas_as_telas()
    frame_sala2.pack(fill="both", expand=True)

def mostrar_sala3():
    esconder_todas_as_telas()
    frame_sala3.pack(fill="both", expand=True)

def mostrar_sala4():
    esconder_todas_as_telas()
    frame_sala4.pack(fill="both", expand=True)

def mostrar_sala5():
    esconder_todas_as_telas()
    frame_sala5.pack(fill="both", expand=True)

#def reservar():
    #fazer

#def cancelar():
    #fazer

#---------------------------------------------------------------------------------------------------------------------
#janela - cinema
ctk.set_appearance_mode("dark")

cinema = ctk.CTk()
cinema.title("cinema ruby")
cinema.geometry("1600x800")

frame_inicial = ctk.CTkFrame(cinema, fg_color="transparent")
frame_inicial.pack(fill="both", expand=True)

titulo = ctk.CTkLabel(
    frame_inicial,
    text="CINEMA RUBY",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(10, 10), anchor="w", padx=25)

btn_historico = ctk.CTkButton(
    frame_inicial,
    text="📜 HISTÓRICO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=140,
    height=35,
    command=mostrar_historico
)

btn_historico.place(x=1518, anchor="e", y=40)

label_inicio = ctk.CTkLabel(
    frame_inicial,
    text="INÍCIO",
    font=("Arial", 18, "bold"),
    text_color="#F7D9ED"
)
label_inicio.place(x=1360, anchor="e", y=40)

label_escolha = ctk.CTkLabel(
    frame_inicial,
    text="ESCOLHA SUA SALA: ",
    font=("Arial", 20, "bold"),
    text_color="#FFFFFF"
)

label_escolha.place(x=38, y=640)

#------------------------------------------------------------------------------------------------------------------------
#imagens
frame_imagens = ctk.CTkFrame(frame_inicial, height=550, width=1500, fg_color="#463940")
frame_imagens.pack()

frame_imagens.grid_propagate(False)

#odisseia
imagem_odisseia = Image.open("a_odisseia.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_odisseia, dark_image=imagem_odisseia, size=(280,500))

label_odisseia_imagem = ctk.CTkLabel(frame_imagens, text="", image=imagem_ctk)
label_odisseia_imagem.grid(row=0, column=0, padx=10, pady=20)

#obsessao
imagem_obsessao_imagem = Image.open("obsessao.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_obsessao_imagem, dark_image=imagem_obsessao_imagem, size=(280,500))

label_obsessao_imagem = ctk.CTkLabel(frame_imagens, text="", image=imagem_ctk)
label_obsessao_imagem.grid(row=0, column=1, padx=10, pady=20)

#homem aranha
imagem_homem_aranha = Image.open("homem_aranha.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_homem_aranha, dark_image=imagem_homem_aranha, size=(280,500))

label_homem_aranha_imagem = ctk.CTkLabel(frame_imagens, text="", image=imagem_ctk)
label_homem_aranha_imagem.grid(row=0, column=2, padx=10, pady=20)

#toy story 5
imagem_toy_story_5 = Image.open("toy_story_5.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_toy_story_5, dark_image=imagem_toy_story_5, size=(280,500))

label_toy_story_5_imagem = ctk.CTkLabel(frame_imagens, text="", image=imagem_ctk)
label_toy_story_5_imagem.grid(row=0, column=3, padx=10, pady=20)

#um cabra bom de bola
imagem_um_cabra_bom_de_bola = Image.open("um_cabra_bom_de_bola.png")
imagem_ctk = ctk.CTkImage(light_image=imagem_um_cabra_bom_de_bola, dark_image=imagem_um_cabra_bom_de_bola, size=(280,500))

label_um_cabra_bom_de_bola_imagem = ctk.CTkLabel(frame_imagens, text="", image=imagem_ctk)
label_um_cabra_bom_de_bola_imagem.grid(row=0, column=4, padx=10, pady=20)

#--------------------------------------------------------------------------------------------------------------------------------------
#frame odisseia
frame_odisseia = ctk.CTkFrame(frame_inicial, height=130, width=270, fg_color="#D19ABE")
frame_odisseia.place(x=35, y=680)

frame_odisseia.pack_propagate(False)

label_odisseia = ctk.CTkLabel(frame_odisseia, text="🎬\nA ODISSEIA", font=("Arial", 18, "bold"), justify="left")
label_odisseia.place(x=15, y=15)

botao_odisseia = ctk.CTkButton(
    frame_odisseia,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    width=100,
    height=35,
    command=mostrar_sala1
)
botao_odisseia.place(x=15, y=70)

#frame obsessao
frame_obsessao = ctk.CTkFrame(frame_inicial, height=130, width=270, fg_color="#CC91AE")
frame_obsessao.place(x=335, y=680)

frame_obsessao.pack_propagate(False)

label_obsessao = ctk.CTkLabel(frame_obsessao, text="🍿\nA OBSESSAO", font=("Arial", 18, "bold"), justify="left")
label_obsessao.place(x=15, y=15)

botao_obsessao = ctk.CTkButton(
    frame_obsessao,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    width=100,
    height=35,
    command=mostrar_sala2
)
botao_obsessao.place(x=15, y=70)

#frame homem aranha
frame_homem_aranha = ctk.CTkFrame(frame_inicial, height=130, width=270, fg_color="#B8789C")
frame_homem_aranha.place(x=635, y=680)

frame_homem_aranha.pack_propagate(False)

label_homem_aranha = ctk.CTkLabel(frame_homem_aranha, text="🎥\n HOMEM ARANHA", font=("Arial", 18, "bold"), justify="left")
label_homem_aranha.place(x=15, y=15)

botao_homem_aranha = ctk.CTkButton(
    frame_homem_aranha,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    width=100,
    height=35,
    command=mostrar_sala3
)
botao_homem_aranha.place(x=15, y=70)

#frame toy story
frame_toy_story_5 = ctk.CTkFrame(frame_inicial, height=130, width=270, fg_color="#A4608A")
frame_toy_story_5.place(x=935, y=680)

frame_toy_story_5.pack_propagate(False)

label_toy_story_5 = ctk.CTkLabel(frame_toy_story_5, text="📹\n TOY STORY 5", font=("Arial", 18, "bold"), justify="left")
label_toy_story_5.place(x=15, y=15)

botao_toy_story_5 = ctk.CTkButton(
    frame_toy_story_5,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    width=100,
    height=35,
    command=mostrar_sala4
)
botao_toy_story_5.place(x=15, y=70)

#frame um cabra bom de bola
frame_um_cabra_bom_de_cabra = ctk.CTkFrame(frame_inicial, height=130, width=270, fg_color="#8F4B77")
frame_um_cabra_bom_de_cabra.place(x=1235, y=680)

frame_um_cabra_bom_de_cabra.pack_propagate(False)

label_um_cabra_bom_de_cabra = ctk.CTkLabel(frame_um_cabra_bom_de_cabra, text="🎞️\n UM CABRA BOM DE BOLA", font=("Arial", 18, "bold"), justify="left")
label_um_cabra_bom_de_cabra.place(x=15, y=15)

botao_um_cabra_bom_de_cabra = ctk.CTkButton(
    frame_um_cabra_bom_de_cabra,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    width=100,
    height=35,
    command=mostrar_sala5
)
botao_um_cabra_bom_de_cabra.place(x=15, y=70)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#historico
frame_historico = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_historico,
    text="HISTÓRICO",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=35)

botao_inicio = ctk.CTkButton(
    frame_historico,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1500, anchor="e", y=40)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#salas
frame_sala1 = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_sala1,
    text="A ODISSEIA",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=80)

botao_inicio = ctk.CTkButton(
    frame_sala1,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1480, anchor="e", y=40)

frame_tela = ctk.CTkFrame(
    frame_sala1,
    width=1400,
    height=50,
    fg_color="#463940",
    corner_radius=10
)

frame_tela.place(x=80, y=90)

label_tela = ctk.CTkLabel(
    frame_tela,
    text="TELA",
    font=("Arial", 18, "bold"),
    text_color="#D19ABE"
)

label_tela.place(x=665, y=10)

frame_cadeiras = ctk.CTkFrame(
    frame_sala1,
    width=1400,
    height=580,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras.place(x=80, y=160)

botao_reservar = ctk.CTkButton(
    frame_sala1,
    text="🎟️ RESERVAR CADEIRAS",
    font=("Arial", 14, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=300,
    height=50,
    corner_radius=10
    #command=reservar
)

botao_reservar.place(x=435, y=760)


botao_cancelar = ctk.CTkButton(
    frame_sala1,
    text="❌ CANCELAR RESERVAS",
    font=("Arial", 14, "bold"),
    fg_color="#463940",
    hover_color="#643352",
    text_color="#D19ABE",
    width=300,
    height=50,
    corner_radius=10
    #command=cancelar
)

botao_cancelar.place(x=775, y=760)

frame_cadeiras_sala1 = ctk.CTkFrame(
    frame_cadeiras,
    width=1200,
    height=560,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras_sala1.place(x=150, y=40)
frame_cadeiras_sala1.grid_propagate(False)

botoes_sala1 = criar_cadeiras(frame_cadeiras_sala1)

#------------------------------------------------------------------------------------------------------------------------------------
frame_sala2 = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_sala2,
    text="OBSESSÃO",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=80)

botao_inicio = ctk.CTkButton(
    frame_sala2,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#643352",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1480, anchor="e", y=40)

frame_tela = ctk.CTkFrame(
    frame_sala2,
    width=1400,
    height=50,
    fg_color="#463940",
    corner_radius=10
)

frame_tela.place(x=80, y=90)

label_tela = ctk.CTkLabel(
    frame_tela,
    text="TELA",
    font=("Arial", 18, "bold"),
    text_color="#D19ABE"
)

label_tela.place(x=665, y=10)

frame_cadeiras = ctk.CTkFrame(
    frame_sala2,
    width=1400,
    height=580,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras.place(x=80, y=160)

botao_reservar = ctk.CTkButton(
    frame_sala2,
    text="🎟️ RESERVAR CADEIRAS",
    font=("Arial", 14, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=300,
    height=50,
    corner_radius=10
    #command=reservar
)

botao_reservar.place(x=435, y=760)


botao_cancelar = ctk.CTkButton(
    frame_sala2,
    text="❌ CANCELAR RESERVAS",
    font=("Arial", 14, "bold"),
    fg_color="#463940",
    hover_color="#643352",
    text_color="#D19ABE",
    width=300,
    height=50,
    corner_radius=10
    #command=cancelar
)

botao_cancelar.place(x=775, y=760)

frame_cadeiras_sala2 = ctk.CTkFrame(
    frame_cadeiras,
    width=1200,
    height=560,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras_sala2.place(x=150, y=40)
frame_cadeiras_sala2.grid_propagate(False)

botoes_sala2 = criar_cadeiras(frame_cadeiras_sala2)

#------------------------------------------------------------------------------------------------------------------------------------
frame_sala3 = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_sala3,
    text="HOMEM-ARANHA",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=80)

botao_inicio = ctk.CTkButton(
    frame_sala3,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1480, anchor="e", y=40)

frame_tela = ctk.CTkFrame(
    frame_sala3,
    width=1400,
    height=50,
    fg_color="#463940",
    corner_radius=10
)

frame_tela.place(x=80, y=90)

label_tela = ctk.CTkLabel(
    frame_tela,
    text="TELA",
    font=("Arial", 18, "bold"),
    text_color="#D19ABE"
)

label_tela.place(x=665, y=10)

frame_cadeiras = ctk.CTkFrame(
    frame_sala3,
    width=1400,
    height=580,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras.place(x=80, y=160)

botao_reservar = ctk.CTkButton(
    frame_sala3,
    text="🎟️ RESERVAR CADEIRAS",
    font=("Arial", 14, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=300,
    height=50,
    corner_radius=10
    #command=reservar
)

botao_reservar.place(x=435, y=760)


botao_cancelar = ctk.CTkButton(
    frame_sala3,
    text="❌ CANCELAR RESERVAS",
    font=("Arial", 14, "bold"),
    fg_color="#463940",
    hover_color="#643352",
    text_color="#D19ABE",
    width=300,
    height=50,
    corner_radius=10
    #command=cancelar
)

botao_cancelar.place(x=775, y=760)

frame_cadeiras_sala3 = ctk.CTkFrame(
    frame_cadeiras,
    width=1200,
    height=560,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras_sala3.place(x=150, y=40)
frame_cadeiras_sala3.grid_propagate(False)

botoes_sala3 = criar_cadeiras(frame_cadeiras_sala3)

#------------------------------------------------------------------------------------------------------------------------------------
frame_sala4 = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_sala4,
    text="TOY STORY 5",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=80)

botao_inicio = ctk.CTkButton(
    frame_sala4,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1480, anchor="e", y=40)

frame_tela = ctk.CTkFrame(
    frame_sala4,
    width=1400,
    height=50,
    fg_color="#463940",
    corner_radius=10
)

frame_tela.place(x=80, y=90)

label_tela = ctk.CTkLabel(
    frame_tela,
    text="TELA",
    font=("Arial", 18, "bold"),
    text_color="#D19ABE"
)

label_tela.place(x=665, y=10)

frame_cadeiras = ctk.CTkFrame(
    frame_sala4,
    width=1400,
    height=580,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras.place(x=80, y=160)

botao_reservar = ctk.CTkButton(
    frame_sala4,
    text="🎟️ RESERVAR CADEIRAS",
    font=("Arial", 14, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=300,
    height=50,
    corner_radius=10
    #command=reservar
)

botao_reservar.place(x=435, y=760)


botao_cancelar = ctk.CTkButton(
    frame_sala4,
    text="❌ CANCELAR RESERVAS",
    font=("Arial", 14, "bold"),
    fg_color="#463940",
    hover_color="#643352",
    text_color="#D19ABE",
    width=300,
    height=50,
    corner_radius=10
    #command=cancelar
)

botao_cancelar.place(x=775, y=760)

frame_cadeiras_sala4 = ctk.CTkFrame(
    frame_cadeiras,
    width=1200,
    height=560,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras_sala4.place(x=150, y=40)
frame_cadeiras_sala4.grid_propagate(False)

botoes_sala4 = criar_cadeiras(frame_cadeiras_sala4)

#------------------------------------------------------------------------------------------------------------------------------------
frame_sala5 = ctk.CTkFrame(cinema, fg_color="#1A1518")

titulo = ctk.CTkLabel(
    frame_sala5,
    text="UM CABRA BOM DE BOLA",
    font=("Arial", 46, "bold"),
    bg_color="transparent",
    fg_color="transparent",
    text_color="#D19ABE"
)
titulo.pack(pady=(15, 10), anchor="w", padx=80)

botao_inicio = ctk.CTkButton(
    frame_sala5,
    text="⌂ INÍCIO",
    font=("Arial", 13, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=100,
    height=35,
    command=mostrar_inicio
)
botao_inicio.place(x=1480, anchor="e", y=40)

frame_tela = ctk.CTkFrame(
    frame_sala5,
    width=1400,
    height=50,
    fg_color="#463940",
    corner_radius=10
)

frame_tela.place(x=80, y=90)

label_tela = ctk.CTkLabel(
    frame_tela,
    text="TELA",
    font=("Arial", 18, "bold"),
    text_color="#D19ABE"
)

label_tela.place(x=665, y=10)

frame_cadeiras = ctk.CTkFrame(
    frame_sala5,
    width=1400,
    height=580,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras.place(x=80, y=160)

botao_reservar = ctk.CTkButton(
    frame_sala5,
    text="🎟️ RESERVAR CADEIRAS",
    font=("Arial", 14, "bold"),
    fg_color="#8F4D75",
    hover_color="#713A5D",
    text_color="white",
    width=300,
    height=50,
    corner_radius=10
    #command=reservar
)

botao_reservar.place(x=435, y=760)


botao_cancelar = ctk.CTkButton(
    frame_sala5,
    text="❌ CANCELAR RESERVAS",
    font=("Arial", 14, "bold"),
    fg_color="#463940",
    hover_color="#643352",
    text_color="#D19ABE",
    width=300,
    height=50,
    corner_radius=10
    #command=cancelar
)

botao_cancelar.place(x=775, y=760)

frame_cadeiras_sala5 = ctk.CTkFrame(
    frame_cadeiras,
    width=1200,
    height=560,
    fg_color="#2B2026",
    corner_radius=10
)

frame_cadeiras_sala5.place(x=150, y=40)
frame_cadeiras_sala5.grid_propagate(False)

botoes_sala5 = criar_cadeiras(frame_cadeiras_sala5)

cinema.mainloop()
