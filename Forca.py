import tkinter as tk
import random
import lista_de_palavras

def escolher_palavra_aleatoria():
    global palavra_escolhida
    palavra_escolhida = lista_de_palavras.palavra_aleatoria()
escolher_palavra_aleatoria() # --> escolhendo a palavra aleatoria

# Função para verificar o palpite do usuário
def verificar_palpite(palpite):
    palpites.append(palpite)
    if palpite in palavra_escolhida:
        atualizar_palavra_oculta()
    else:
        palpites_errados.append(palpite)
        letras_erradas_var.set(" ".join(palpites_errados))
        desenhar_boneco(len(palpites_errados))  # Desenha uma parte do boneco para cada erro
    verificar_vitoria_derrota()
    entrada_palpite.delete(0, tk.END)  # Limpa a caixa de entrada

# Função para desenhar o boneco
def desenhar_boneco(erros):
    # A cada erro, desenha uma parte do boneco: cabeça, tronco, braços e pernas
    partes_boneco = [cabeça, tronco, braço_esquerdo, braço_direito, perna_esquerda, perna_direita]
    if erros <= len(partes_boneco):
        canvas.create_oval(partes_boneco[erros-1], width=2, outline="black")

# Função para atualizar a palavra oculta
def atualizar_palavra_oculta():
    global palavra_escolhida
    palavra_oculta = ""
    for letra in palavra_escolhida:
        if letra in palpites:
            palavra_oculta += letra + " "
        else:
            palavra_oculta += "_ "
    palavra_var.set(palavra_oculta)

# Função para verificar se o jogador ganhou ou perdeu
def verificar_vitoria_derrota():
    global palavra_escolhida
    if all(letra in palpites for letra in palavra_escolhida):
        palavra_var.set(f"A palavra era {palavra_escolhida}. Você ganhou!")
    elif len(palpites_errados) >= 6:
        palavra_var.set("Você perdeu!")

# Cria a janela principal
janela = tk.Tk()
janela.title('Jogo da Forca')
janela.geometry('600x600')
janela.resizable(False, False)

# Variáveis para controle
palpites = []
palpites_errados = []
palavra_var = tk.StringVar()
palavra_var.set("_ " * len(palavra_escolhida))
letras_erradas_var = tk.StringVar()
letras_erradas_var.set("")

# Widgets
canvas = tk.Canvas(janela, width=200, height=200)  # Canvas para desenhar a forca e o boneco
canvas.pack(pady=20)

# Coordenadas para desenhar o boneco
cabeça = (140, 40, 160, 60)  # Ajustando a posição da cabeça
tronco = (150, 60, 150, 100)  # Ajustando a posição do tronco
braço_esquerdo = (140, 70, 150, 70)  # Ajustando a posição do braço esquerdo
braço_direito = (160, 70, 150, 70)  # Ajustando a posição do braço direito
perna_esquerda = (145, 120, 150, 100)  # Ajustando a posição da perna esquerda
perna_direita = (155, 120, 150, 100)  # Ajustando a posição da perna direita



# Cria a forca
canvas.create_line((100, 20, 100, 140), width=2)
canvas.create_line((100, 20, 150, 20), width=2)
canvas.create_line((150, 20, 150, 40), width=2)

palavra_label = tk.Label(janela, textvariable=palavra_var, font=("Helvetica", 16))
palavra_label.pack(pady=20)

entrada_palpite = tk.Entry(janela)
entrada_palpite.pack(pady=20)
entrada_palpite.bind("<Return>", lambda event: verificar_palpite(entrada_palpite.get()))  # Liga a tecla Enter ao palpite

palpite_button = tk.Button(janela, text="Palpite", command=lambda: verificar_palpite(entrada_palpite.get()))
palpite_button.pack(pady=20)

letras_erradas_label = tk.Label(janela, textvariable=letras_erradas_var, font=("Helvetica", 16), fg="red")
letras_erradas_label.pack(pady=20)

# Função para reiniciar o jogo
def reiniciar_jogo():
    global palavra_escolhida, palpites, palpites_errados
    canvas.delete("boneco")  # Remove o boneco do canvas
    # escolher_palavra_aleatoria()
    escolher_palavra_aleatoria()
    palpites = []  # Limpa os palpites
    palpites_errados = []  # Limpa os palpites errados
    palavra_var.set("_ " * len(palavra_escolhida))  # Reseta a palavra oculta
    letras_erradas_var.set("")  # Limpa as letras erradas
    entrada_palpite.config(state=tk.NORMAL)  # Reabilita a entrada de texto
    palpite_button.config(state=tk.NORMAL)  # Reabilita o botão de palpite

# Botão de Reiniciar
reiniciar_button = tk.Button(janela, text="Reiniciar", command=reiniciar_jogo)
reiniciar_button.pack(pady=20)

def desenhar_boneco(erros):
    # A cada erro, desenha uma parte do boneco: cabeça, tronco, braços e pernas
    partes_boneco = [cabeça, tronco, braço_esquerdo, braço_direito, perna_esquerda, perna_direita]
    if erros <= len(partes_boneco):
        canvas.create_oval(partes_boneco[erros-1], width=2, outline="black", tags="boneco")

# Inicia o loop principal (A janela)
janela.mainloop()