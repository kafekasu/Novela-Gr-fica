#Variables
default confianza = 0
default sospecha_amigo = False

# PERSONAJES
define ju = Character("[name_p]", color="#91b7ff")
define amigo = Character("Kalet")
define sombra = Character("??", color="#653489")
define enfermera = Character("Enfermera", color = "#284692")


transform mareado:
    blur 8
    xoffset 0
    linear 1.0 xoffset 8
    linear 1.0 xoffset -8
    repeat

default pista_maleta = False
default pista_recibo = False
default pista_foto = False
default pistas = 0
default personajes = {
    "kalet": {"conocido": False, "foto": None, "nombre": "Kalet", "info": "Tu mejor amigo."},
}


label start:
    python:
        for p in personajes.values():
            p["conocido"] = False
    # --- BIENVENIDA (pausada) ---
    scene black
    with fade
    centered "Bienvenido" with dissolve
    pause 1.0
    centered "Antes de comenzar, creemos tu personaje." with dissolve
    pause 1.0

    # --- PASO 1: Elegir género ---
    centered "Primero, elige el género de tu personaje." with dissolve
    pause 0.5
    call genero

    # --- PASO 2: Elegir nombre ---
    centered "Perfecto." with dissolve
    pause 0.8
    centered "Ahora, ¿cómo te llamas?" with dissolve
    pause 0.5
    $ name_p = renpy.input("Ingresa tu nombre:")
    centered "Bienvenid[ 'o' if genero == 'masculino' else 'a'], [name_p]." with dissolve
    pause 1.0

    # --- TRANSICIÓN PAUSADA a la historia ---
    centered "Tu historia comienza ahora..." with dissolve
    # Recién aquí aparece el HUD
    show screen hud
    jump inicio

label inicio:
    scene black
    with fade

    centered "{size=+12}Hay cosas en la vida que resultan difíciles de entender{/size}"
    centered "{size=+12}porque ni nosotros mismos nos entendemos aún{/size}"
    centered "{size=+12}Sobre todo, cuando no sabemos que nuestra vida ha sido construida por alguien más{/size}" 
    centered "{size=+12}como una red{/size}"
    centered "{size=+12}Y algunas redes comienzan a construirse mucho antes de que notes que estás atrapado{/size}"
    centered "{size=+12}Para cuanto nos damos cuenta, ya no podemos huir{/size}" 

    pause 2.0

    centered "{size=+8}A menos que, estemos listos para enfrentar el pasado{/size}"

    pause 3.0

    scene black
    with fade

    jump introduccion


# INTRODUCCIÓN


label introduccion:

    scene black_room
    with fade

    "No puedo moverme"

    "¿En dónde estoy?"

    scene sombra
    with fade

    sombra "                      "
    pause 0.5
    sombra "                          "
    pause 0.5
    sombra "                          "
    ju "¿Qué eres?"

label bg_darkhospital:
    scene hospital_dia
    with fade
    "???"
    "Es la misma camilla, la misma habitación"
    ju "Aghh"
    "¿Qué fue eso?"
    "Creo que fue una pesadilla"
    show enfermera3 at left
    enfermera "Buenos días ['joven' if genero == 'masculino' else 'señorita']. Que bueno que despierta."
    ju "Disculpe... no sé que hago aquí, no puedo recordar nada y me duele la cabeza."
    hide enfermera 3
    show enfermera1
    enfermera "Se desmayó y tuvo una mala caída."
    hide enfermera1
    show enfermera2
    enfermera "Tranquil['o' if genero == 'masculino' else 'a'], con el tiempo tal vez logre recodar algo importante."
    hide enfermera2
    show enfermera3
    ju "N-no entiendo ¿Qué debo recordar?"
    hide enfermera3
    show enfermera2
    enfermera "Tenga paciencia. No es bueno forzar la mente."
    hide enfermera2
    show enfermera3
    enfermera "Alguien estuvo esperando toda la noche a que recobrara la conciencia."
    enfermera "Ahora vuelvo, iré a avisarle que esta despiert[ 'o' if genero == 'masculino' else 'a']."
    hide enfermera3
    ju "¡E-espere!"
    ju "¿Por qué..."
    ju "...no puedo recordar nada?"
    
    pause 1.0

# Contexto de lo sucedido
    scene hospital_dia
    with fade
    show amigo at left
    show enfermera at right
    pause 3.0
    "¿Kalet?"
    "..."
    enfermera "Por favor sea cuidadoso, aún está en shock. Hablaré con el doctor para que l['o' if genero == 'masculino' else 'a'] dé de alta."
    amigo "Muchas gracias."
    $ personajes["kalet"]["conocido"] = True


    enfermera "Los dejo solos. Con permiso"
    hide enfermera
    hide amigo
    show kalet_escena1 at left with fade 
    amigo "¿Cómo te sientes?"
    ju "¿Qué fue lo que pasó?"
    amigo "..."
    amigo "¿En serio no recuerdas nada?"
    ju "No..."
    ju "No entiendo que está pasando !Por favor, dime qué está pasando!"
    amigo "Ayer me pediste que fuera a verte. Estabas muy triste y no sabía como consolarte."
    amigo "No te sentías muy bien. Te desmayaste, no logré sostenerte y recibiste un golpé muy fuerte."
    amigo "Perdón. Si me hubiera dado cuenta de lo grave que estabas te habría traído al hospital cuanto antes."
    ju "N-no es tu culpa, hiciste lo mejor que podías ¡Incluso me trajiste aquí!"
    ju "No recuerdo nada, pero, gracias por esperar. Seguro ni siquiera dormiste bien."

    ju "¿Mis padres saben que estoy aquí? Deben de estar muy preocupados."
    amigo "..."
    amigo "...Ellos no saben que te desmayaste. No estaban en casa cuando eso paso."
    amigo "No tengo sus números así que, no pude contactarlos."
    ju "...¿En serio?"
    ju "¿Sabes dónde está mi teléfono? Deben de estar muy preocupados."
    amigo "Probablemente lo dejaste en casa. En cuanto el doctor te dé de alta te llevaré a casa ¿De acuerdo?"
    ju "Está bien."
    pause 1.0

# Escena del auto
    scene bg_auto
    with fade 
    show amgigo at left 
    ju "No entiendo porque mis padres no hay intentado buscarme ¿A dónde vamos?" 
    amigo "Te llevo a casa"
    ju "¿Era por aquí?"
    amigo "Sí, es tu ruta normal ¿Te acuerdas de cuando nos quedamos atorados en el estacionamiento de la escuela? Tardamos unas dos horas en salir de ahí. "
    ju "No lo recuerdo."
    amigo "Está bien, es normal"
    ju "...¿Por qué no me acuerdo de ti?"
    amigo "Sí me recuerdas."
    ju "No me acuerdo de eso."
    amigo "El doctor dijo que es normal, ya te acordarás."
    ju "Kalet..."
    amigo "No te preocupes por eso ahora, si sigues tu rutina de siempre será más fácil recordar todo. "
    ju "Prestáme tu teléfono, quiero llamar a mis padres."
    amigo "Recuerdas sus números?"
    ju "..."
    ju "¿Dónde está mi telefono?"
    amigo "Seguro lo dejaste en casa. Necesitas descansar."
    menu: 
        "¡Lo que necesito es mi teléfono!":
            $confianza = 0
            amigo ""
        "Sólo me gustaría hablar con ellos":
            $confianza = 0
        "Perdón, esto es demasiado para mí":
            $confianza += 1
    
# ============================================================
# De vuelta a casa
# ============================================================
    scene bg_street
    with fade
    "El doctor dijo que debía guardar reposo. Al parecer tuve una contusión leve. Pero mis dolores de cabeza continúan."
    show amigo at center
    amigo"Necesitas guardar reposo por un tiempo. No te sobreesfuerces"
    pause 2.0
    ju "Pensé que mis padres estarían aquí."
    amigo "Tal vez sea por el trabajo. No te preocupes, ve a descansar."
    menu: 
        "No me siento bien, no creo que pueda descansar.":
            $ confianza += 1
            amigo "Ve a recostarte, te llevaré el medicamento."
            jump escene_room
        "Tal vez tengas razón":
            amigo "Sí, así que ve a descansar."
            amigo "¿Quieres que lleve el medicamento a tu habitación?"
            menu:
                "Está bien, intentaré dormir.":
                    $ confianza += 1
                    jump escene_room
                "No, ya has hecho mucho. Lo tomaré ahora.":
                    $ confianza = 0
                    menu: 
                        "Ir por el medicamento":
                            hide amigo
                            call screen pomo_interactivo
                            "Aghh. Espero que con esto deje de dolerme la cabeza."
                            jump escena_teléfono
        "Necesito llamar a mis padres":
            $ confianza += 1
            amigo "[name_p], e-espera. Necesitas tomar tus medicamentos."
            ju "Lo encontré"
            camera:
                xoffset 0
                yoffset 0
                linear 0.05 xoffset 15
                linear 0.05 xoffset -15
                linear 0.05 yoffset 15
                linear 0.05 yoffset -15
                linear 0.05 xoffset 15
                linear 0.05 xoffset -15
                linear 0.05 yoffset 15
                linear 0.05 yoffset -15
                linear 0.05 xoffset 15
                linear 0.05 xoffset -15
                linear 0.05 yoffset 15
                linear 0.05 yoffset -15
                linear 0.05 xoffset 15
                linear 0.05 xoffset -15
                linear 0.05 yoffset 15
                linear 0.05 yoffset -15
                linear 0.05 xoffset 0
                linear 0.05 yoffset 0
            show bg street at mareado
            "¡AGHH!"
            amigo "!tranquil['o' if genero == 'masculino' else 'a'], iré por el medicamento!"
            pause 3.0 
            "¿Qué es esto?, ¿porqué me duele tanto de repente?"
            scene bg street
            amigo "Necesitas descansar, puedes… llamarlos después. Ahora solo te harás mal."
            ju "..."
            ju "Está bien. Iré a mi habitación."
            jump escena_teléfono

label escena_teléfono:
    show amigo at center
    amigo "¿Quieres que me quede?" 
    menu:
        "No, estaré bien":
            $ confianza -= 1
            $ sospecha_amigo = True
            amigo "De todos modos, llámame si necesitas algo más, ¿Okey?"
            ju "Esta bien."
            hide amigo
        "Está bien":
            $ confianza += 1
            amigo "Bien, dormiré en el sofá. Estaré aquí por si me necesitas"
            ju "Gracias."
            hide amigo
        "No quiero ser una molestia":
            $ confianza +=2
            amigo "No lo eres. Estaré para apoyarte, como siempre."
            ju "…"
            amigo "Ve a dormir. Debes de estar exhaust['o' if genero == 'masculino' else 'a']"
            ju "Está bien, y gracias, por todo lo de hoy."
            amigo "No te preocupes, es lo que hacen los amigos."
            hide amigo
    jump scene_room 
    
label scene_room:
    scene room
    with fade
    "Que extraño se siente estar aquí"
    ju "Sólo fue un mal día"
    camera:
        xoffset 0
        yoffset 0
        linear 0.05 xoffset 15
        linear 0.05 xoffset -15
        linear 0.05 yoffset 15
        linear 0.05 yoffset -15
        linear 0.05 xoffset 15
        linear 0.05 xoffset -15
        linear 0.05 yoffset 15
        linear 0.05 yoffset -15
        linear 0.05 xoffset 15
        linear 0.05 xoffset -15
        linear 0.05 yoffset 15
        linear 0.05 yoffset -15
        linear 0.05 xoffset 15
        linear 0.05 xoffset -15
        linear 0.05 yoffset 15
        linear 0.05 yoffset -15
        linear 0.05 xoffset 0
        linear 0.05 yoffset 0
     
    "¡ugh!"
    pause 3.0
    "¿Acabo de tropezar con algo?"
    ju "¿Una maleta? ¿Qué hace una maleta en mi habitación?"
    show room at mareado
    "Agh… Me duele la cabeza. No sé qué me está pasando"
    scene room
    "¿Por qué rayos hay una maleta en mi habitación?"
    
return
