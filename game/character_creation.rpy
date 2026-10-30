# ===== Variables por defecto =====
default genero = "femenino"

init python:
    generos = ["femenino", "masculino"]

# ===== Imágenes de fondo (vestidores) =====
image bg vestidor_femenino = "images/bg_vestidor_femenino.png"
image bg vestidor_masculino = "images/bg_vestidor_masculino.png"

# ===== Pantalla de selección con flechas =====
screen select_genero_screen():
    if genero == "femenino":
        add "bg vestidor_femenino"
    else:
        add "bg vestidor_masculino"

    add "images/player_{}.png".format(genero) xalign 0.5 yalign 0.5

    # Flecha izquierda
    textbutton "◀":
        background None
        text_size 60
        xalign 0.15
        yalign 0.5
        action [SetVariable("genero", generos[(generos.index(genero) - 1) % len(generos)]), Show("select_genero_screen")]

    # Flecha derecha
    textbutton "▶":
        background None
        text_size 60
        xalign 0.85
        yalign 0.5
        action [SetVariable("genero", generos[(generos.index(genero) + 1) % len(generos)]), Show("select_genero_screen")]

    # Botón de confirmar: CIERRA y sigue el flujo
    textbutton "Continuar":
        xalign 0.5
        yalign 0.85
        action Return()

# ===== Label que muestra la pantalla =====
label genero:
    call screen select_genero_screen
    return
label abrir_genero:
    hide screen hud
    call screen select_genero_screen
    show screen hud
    return
