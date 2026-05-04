import pygame
import sys

pygame.init()

#tamanho da janela
largura = 800
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Iniciar pesquisa?")
                           
# cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# fonte
fonte = pygame.font.SysFont("Arial", 28)

historia = [
    "fiz a tela kkk"
    
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
