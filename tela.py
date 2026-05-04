import pygame
import sys

pygame.init()

# tamanho da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# fonte
fonte = pygame.font.SysFont("Arial", 28)

historia = [
    "Voce foi fazer um teste de perguntas...",
    "mas alguma coisa estava errada.",
    "",
    "Voce sabe o que fez?",
    "Onde esta?",
    "E quem esta te observando?",
    "",
    "Ele sabe...",
    "Obedeça o que ele diz se quiser sobreviver."
]

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(preto)

    y = 100
    for linha in historia:
        texto = fonte.render(linha, True, branco)
        tela.blit(texto, (80, y))
        y += 45

    pygame.display.update()

pygame.quit()
sys.exit()
