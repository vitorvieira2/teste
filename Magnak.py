from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(1080,720)
janela.set_title("Magnak")
mouse = Window.get_mouse()
teclado = Window.get_keyboard()


def menu_principal():
    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(menusair):
                janela.close()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(menuiniciar):
                
                jogo()
            
        fundomenu = GameImage("fundo_menu_magnak.jpg")
        titulomenu = Sprite("titulo_magnak.png")
        menuiniciar = Sprite("menu_iniciar_magnak.png")
        menusair = Sprite("menu_sair_magnak.png")
        menuiniciar.x = janela.width - menuiniciar.width - 100 
        menuiniciar.y = janela.height/2 - menuiniciar.height/2
        menusair.x = janela.width - menusair.width - 100
        menusair.y = janela.height/2 - menusair.height/2 + menuiniciar.height
        titulomenu.x = 100
        titulomenu.y = 100
        fundomenu.draw()
        titulomenu.draw()
        menuiniciar.draw()
        menusair.draw()
        janela.update()

def jogo():
    rodando = True
    quantidadevida = 9
    while rodando:
        hudhabilidade = Sprite("hudarma.png")
        hudvidas = Sprite("vidashud.png")
        hudhabilidade.x = 50
        hudhabilidade.y = 50
        hudvidas.x = 200
        hudvidas.y = 50
        if teclado.key_pressed("ESC"):
            rodando = False
        janela.set_background_color([0,0,0])
        hudhabilidade.draw()
        hudvidas.draw()
        janela.draw_text(str(quantidadevida),230,75,size=60,color=(255,255,255,), font_name="Trajan Pro", bold=False , italic=False)
        janela.update()   

menu_principal()
