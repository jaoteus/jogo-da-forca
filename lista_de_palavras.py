import random

def palavra_aleatoria():
    global lista
    lista = ["advogado", "afta", "alambique", "alcachofra", "algarismo", "almanaque", "almofariz", "almoxarife", "alquimia", "altivez", "amendoim", "amplificar",
"ampulheta", "ansioso", "aplaudir", "asterisco", "atlas", "balacobaco", "bandolim", "barulhento", "basquetebol", "beneficente", "berimbau", "bicarbonato",
"bugiganga", "bumerangue", "burocracia", "caatinga", "caboclo", "cacareco", "cacto", "calibrado", "camuflagem", "candelabro",
"cassetete", "catalisador", "catequizar", "cérebro", "chamariz", "cicatriz", "cleptomaníaco", "companhia", "condescender", "consciente", "crepúsculo", "cronologia", "deglutir", "depredar"]
    return random.choice(lista)
