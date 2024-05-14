from tkinter import *
from pygame import mixer, key
from PIL import Image, ImageTk
import random
import pygame.mixer


window = Tk()
window.configure(bg="black")
window.geometry("850x600+30+30")
window.title("Inicio")

mixer.init()
menu_sound = pygame.mixer.Sound("menu.mp3")
menu_sound.play(-1)


canvas_principal = Canvas(window, width=850, height=600)
canvas_principal.pack()
menuimg = PhotoImage(file="menu.png")
canvas_principal.create_image(0,0, image=menuimg, anchor="nw")
logoimg = PhotoImage(file="logo.png")
canvas_principal.create_image(400, 125, image=logoimg)

equipo1 = None
equipo2 = None
flecha_activa = True
flecha_activa_equipos = False
flecha_activa_tiradores = False




def iniciar_seleccion_equipos(ventana):
    window.unbind('<Key>')
    window.unbind('<Return>')

    vent_equipos(ventana)

def cerrar_ventana_equipos(ventana):
    global flecha_activa
    ventana.destroy()
    flecha_activa = True
    window.bind('<Key>', mover_flecha_menu)
    window.bind('<Return>', mover_flecha_menu)


def vent_equipos(ventana):
    global flecha_activa_equipos

    flecha_activa_equipos = True
    seleccionando_equipo = 1

    def seleccionar_equipo(eq):
        global equipo1, equipo2
        nonlocal seleccionando_equipo

        if seleccionando_equipo == 1:
            equipo1 = eq
            seleccionando_equipo = 2
            print("Equipo 1:", equipo1)
        elif seleccionando_equipo == 2:
            equipo2 = eq
            print("Equipo 2:", equipo2)
            cerrar_ventana_equipos(ventana)
            ventana_seleccion_tiradores()

    ventana = Toplevel(window)
    ventana.config(bg="black")
    ventana.geometry("800x400+30+30")
    ventana.title("Selección de equipos")
    ventana.focus_set()

    canvas_ventana = Canvas(ventana, width=800, height=400)
    canvas_ventana.pack()
    fondo = PhotoImage(file="fondo_seleccion.png")
    canvas_ventana.create_image(-50, 0, image=fondo, anchor="nw")

    # Seleccion Madrid
    madrid_logo = PhotoImage(file="madrid_logo.png")
    boton_madrid = Button(ventana, bg="white", width=190, height=210, image=madrid_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Real Madrid"))
    boton_madrid.place(x=50, y=100)

    # Seleccion Liverpool
    liv_logo = PhotoImage(file="liv_logo.png")
    boton_liv = Button(ventana, bg="red", width=190, height=210, image=liv_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Liverpool"))
    boton_liv.place(x=300, y=100)

    # Seleccion Inter de Milan
    int_logo = PhotoImage(file="int_logo.png")
    boton_int = Button(ventana, bg="blue", width=190, height=210, image=int_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Inter de Milan"))
    boton_int.place(x=550, y=100)


    def mover_flecha_equipos(event):
        global flecha_x, flecha_y

        if flecha_activa_equipos:
            coord_flecha = canvas_ventana.coords(flecha_equipos)
            if event.keysym == 'Left' and coord_flecha[0] > 155:
                canvas_ventana.move(flecha_equipos, -250, 0)
            elif event.keysym == 'Right' and coord_flecha[0] < 655:
                canvas_ventana.move(flecha_equipos, 250, 0)
            elif event.keysym == 'Return':
                x_flecha, y_flecha = canvas_ventana.coords(flecha_equipos)

                if x_flecha < 200:
                    seleccionar_equipo("Real Madrid")
                elif 200 <= x_flecha < 450:
                    seleccionar_equipo("Liverpool")
                elif x_flecha >= 450:
                    seleccionar_equipo("Inter de Milan")

    ventana.bind('<Key>', mover_flecha_equipos)
    ventana.bind('<Return>', mover_flecha_equipos)

    flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
    flecha_equipos = canvas_ventana.create_image(155, 50, image=flecha_img_equipos)

    ventana.mainloop()

jugadores_liv = 0
jugadores_rma = 0
jugadores_int = 0
tiradores_seleccionados = {"Liverpool": None, "Real Madrid": None, "Inter de Milan": None}



def ventana_seleccion_tiradores():
    global equipo1, equipo2, flecha_activa_tiradores, jugadores_liv, jugadores_int, jugadores_liv
    global tiros_vinicius, tiros_diaz, tiros_jude, tiros_rodrygo, tiros_salah, tiros_darwin, tiros_alexis, tiros_calhanoglu, tiros_lautaro
    global goles_vinicius, goles_diaz, goles_jude, goles_rodrygo, goles_salah, goles_darwin, goles_alexis, goles_calhanoglu, goles_lautaro

    ventana_tiradores = Toplevel(window)
    ventana_tiradores.config(bg="black")
    ventana_tiradores.geometry("800x550+30+30")
    ventana_tiradores.title("Selección de Tiradores")
    ventana_tiradores.focus_set()
    flecha_activa_tiradores = True

    tiros_vinicius = tiros_diaz = tiros_jude = tiros_rodrygo = tiros_salah = tiros_darwin = tiros_alexis = tiros_calhanoglu = tiros_lautaro = 0
    goles_vinicius = goles_diaz = goles_jude = goles_rodrygo = goles_salah = goles_darwin = goles_alexis = goles_calhanoglu = goles_lautaro = 0
    jugadores_liv = 0
    jugadores_rma = 0
    jugadores_int = 0


    canvas_tiradores = Canvas(ventana_tiradores, width=800, height=550, bg="black")
    canvas_tiradores.pack()
    fondo_jugadores = PhotoImage(file="fondo_jugadores.png")
    canvas_tiradores.create_image(0, 0, image=fondo_jugadores, anchor="nw")
    tiradores_label = Label(ventana_tiradores, text="Selecciona los tiradores", font=("pagoda-bolditalic", 20, "bold"), bg="black", fg="white")
    tiradores_label.place(x=500, y=5)


    def seleccionar_tiradores(equipo, nombre_tirador):
        global jugadores_rma, jugadores_int, jugadores_liv, tiradores_seleccionados
        tiradores_seleccionados[equipo] = nombre_tirador
        if equipo == "Liverpool" and jugadores_liv < 1:
            tiradores_seleccionados[equipo] = nombre_tirador
            jugadores_liv += 1
            print("Equipo:", equipo)
            print("Tirador seleccionado:", nombre_tirador)
        if equipo == "Real Madrid" and jugadores_rma < 1:
            tiradores_seleccionados[equipo] = nombre_tirador
            jugadores_rma += 1
            print("Equipo:", equipo)
            print("Tirador seleccionado:", nombre_tirador)
        if equipo == "Inter de Milan" and jugadores_int < 1:
            tiradores_seleccionados[equipo] = nombre_tirador
            jugadores_int += 1
            print("Equipo:", equipo)
            print("Tirador seleccionado:", nombre_tirador)

        if jugadores_int == 1 and jugadores_rma == 1:
            ventana_tiradores.destroy()
            ventana_seleccion_porteros()
        elif jugadores_rma == 1 and jugadores_liv == 1:
            ventana_tiradores.destroy()
            ventana_seleccion_porteros()
        elif jugadores_liv == 1 and jugadores_int == 1:
            ventana_tiradores.destroy()
            ventana_seleccion_porteros()

    if equipo1 == "Liverpool":
        salah_img = PhotoImage(file="salah.png")
        tirador1 = Button(ventana_tiradores, image=salah_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Mohamed Salah"))
        tirador1.place(x=50, y=70)

        nunez_img = PhotoImage(file="nuñez.png")
        tirador2 = Button(ventana_tiradores, image=nunez_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Darwin Núñez"))
        tirador2.place(x=190, y=70)

        diaz_img = PhotoImage(file="diaz.png")
        tirador3 = Button(ventana_tiradores, image=diaz_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool","Lucho Díaz"))
        tirador3.place(x=385, y=70)

        liv_label = Label(ventana_tiradores, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
        liv_label.place(x=570, y=140)

    if equipo2 == "Liverpool":
        salah_img = PhotoImage(file="salah.png")
        tirador1 = Button(ventana_tiradores, image=salah_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Mohamed Salah"))
        tirador1.place(x=50, y=300)

        nunez_img = PhotoImage(file="nuñez.png")
        tirador2 = Button(ventana_tiradores, image=nunez_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Darwin Núñez"))
        tirador2.place(x=190, y=300)

        diaz_img = PhotoImage(file="diaz.png")
        tirador3 = Button(ventana_tiradores, image=diaz_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Lucho Díaz"))
        tirador3.place(x=385, y=300)

        liv_label = Label(ventana_tiradores, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
        liv_label.place(x=570, y=350)

    if equipo1 == "Real Madrid":
        jude_img = PhotoImage(file="jude.png")
        tirador1 = Button(ventana_tiradores, image=jude_img, bg="white", fg="white",command=lambda: seleccionar_tiradores("Real Madrid", "Jude Bellingham"))
        tirador1.place(x=50, y=70)

        vini_img = PhotoImage(file="vinicius.png")
        tirador2 = Button(ventana_tiradores, image=vini_img, bg="white", width=155, fg="white",command=lambda: seleccionar_tiradores("Real Madrid", "Vinicius Jr"))
        tirador2.place(x=210, y=70)

        rodrygo_img = PhotoImage(file="rodrygo.png")
        tirador3 = Button(ventana_tiradores, image=rodrygo_img, bg="white", width=155, fg="white",command=lambda: seleccionar_tiradores("Real Madrid", "Rodrygo Goes"))
        tirador3.place(x=380, y=70)

        rma_label = Label(ventana_tiradores, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black",fg="white")
        rma_label.place(x=570, y=140)

    if equipo2 == "Real Madrid":
        jude_img = PhotoImage(file="jude.png")
        tirador1 = Button(ventana_tiradores, image=jude_img, bg="white", fg="black", command=lambda: seleccionar_tiradores("Real Madrid", "Jude Bellingham"))
        tirador1.place(x=50, y=300)

        vini_img = PhotoImage(file="vinicius.png")
        tirador2 = Button(ventana_tiradores, image=vini_img, bg="white", width=155, fg="black", command=lambda: seleccionar_tiradores("Real Madrid", "Vinicius Jr"))
        tirador2.place(x=210, y=300)

        rodrygo_img = PhotoImage(file="rodrygo.png")
        tirador3 = Button(ventana_tiradores, image=rodrygo_img, bg="white", width=155,  fg="black", command=lambda: seleccionar_tiradores("Real Madrid", "Rodrygo Goes"))
        tirador3.place(x=380, y=300)

        rma_label = Label(ventana_tiradores, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black",fg="white")
        rma_label.place(x=570, y=350)


    if equipo1 == "Inter de Milan":
        lautaro_img = PhotoImage(file="lautaro.png")
        tirador1 = Button(ventana_tiradores, image=lautaro_img, width=150, bg="blue", fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Lautaro Martínez"))
        tirador1.place(x=50, y=70)

        calhanoglu_img = PhotoImage(file="calhanoglu.png")
        tirador2 = Button(ventana_tiradores, image=calhanoglu_img, bg="blue", width=155, fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu"))
        tirador2.place(x=210, y=70)

        alexis_img = PhotoImage(file="alexis.png")
        tirador3 = Button(ventana_tiradores, image=alexis_img, bg="blue", width=155, fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Alexis Sánchez"))
        tirador3.place(x=380, y=70)

        inter_label = Label(ventana_tiradores, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black", fg="blue")
        inter_label.place(x=570, y=140)

    if equipo2 == "Inter de Milan":
        lautaro_img = PhotoImage(file="lautaro.png")
        tirador1 = Button(ventana_tiradores, image=lautaro_img, width=150, bg="blue", fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Lautaro Martínez"))
        tirador1.place(x=50, y=300)

        calhanoglu_img = PhotoImage(file="calhanoglu.png")
        tirador2 = Button(ventana_tiradores, image=calhanoglu_img, bg="blue", width=155, fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu"))
        tirador2.place(x=210, y=300)

        alexis_img = PhotoImage(file="alexis.png")
        tirador3 = Button(ventana_tiradores, image=alexis_img, bg="blue", width=155,  fg="black", command=lambda: seleccionar_tiradores("Inter de Milan", "Alexis Sánchez"))
        tirador3.place(x=380, y=300)

        inter_label = Label(ventana_tiradores, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black",fg="blue")
        inter_label.place(x=570, y=350)

    def mover_flecha_tiradores(event):
        global flecha_x, flecha_y

        if flecha_activa_tiradores:
            coords_flecha = canvas_tiradores.coords(flecha_equipos)
            #Potenciometro
            if event.keysym == 'Left':
                if coords_flecha[0] <= 120:
                    if coords_flecha[1] > 40:
                        canvas_tiradores.move(flecha_equipos, 330, -480)
                        canvas_tiradores.itemconfig(flecha_equipos, image=flecha_img_equipos)
                else:
                    canvas_tiradores.move(flecha_equipos, -165, 0)
            elif event.keysym == 'Right':
                if coords_flecha[0] >= 450:
                    if coords_flecha[1] <= 460:
                        canvas_tiradores.move(flecha_equipos, -330, 480)
                        canvas_tiradores.itemconfig(flecha_equipos, image=flecha_equipos_up)
                else:
                    canvas_tiradores.move(flecha_equipos, 165, 0)

            #Boton potenciometro
            elif event.keysym == 'Return':
                x_flecha, y_flecha = canvas_tiradores.coords(flecha_equipos)
                if equipo1 == "Liverpool":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_tiradores("Liverpool", "Mohamed Salah")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_tiradores("Liverpool", "Darwin Núñez")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_tiradores("Liverpool", "Lucho Diaz")
                if equipo1 == "Real Madrid":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_tiradores("Real Madrid", "Jude Bellingham")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_tiradores("Real Madrid", "Vinicius Jr")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_tiradores("Real Madrid", "Rodrygo Goes")
                if equipo1 == "Inter de Milan":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_tiradores("Inter de Milan", "Lautaro Martínez")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_tiradores("Inter de Milan", "Alexis Sánchez")


                    #Equipos 2
                if equipo2 == "Liverpool":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_tiradores("Liverpool", "Mohamed Salah")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_tiradores("Liverpool", "Darwin Núñez")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_tiradores("Liverpool", "Lucho Diaz")
                if equipo2 == "Real Madrid":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_tiradores("Real Madrid", "Jude Bellingham")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_tiradores("Real Madrid", "Vinicius Jr")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_tiradores("Real Madrid", "Rodrygo Goes")
                if equipo2 == "Inter de Milan":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_tiradores("Inter de Milan", "Lautaro Martínez")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_tiradores("Inter de Milan", "Alexis Sánchez")


    ventana_tiradores.bind('<Key>', mover_flecha_tiradores)
    ventana_tiradores.bind('<Return>', mover_flecha_tiradores)

    flecha_equipos_up = PhotoImage(file="flecha_equipos_up.png")
    flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
    flecha_equipos = canvas_tiradores.create_image(120, 40, image=flecha_img_equipos)


    ventana_tiradores.mainloop()





jugadores_livP = 0
jugadores_rmaP = 0
jugadores_intP = 0
porteros_liv = {"Portero": None}
porteros_rma = {"Portero": None}
porteros_int = {"Portero": None}




def ventana_seleccion_porteros():
    global equipo1, equipo2, jugadores_rmaP, jugadores_intP, jugadores_livP
    ventana_porteros = Toplevel(window)
    ventana_porteros.config(bg="black")
    ventana_porteros.geometry("800x550+30+30")
    ventana_porteros.title("Selección de Porteros")
    ventana_porteros.focus_set()

    jugadores_livP = 0
    jugadores_rmaP = 0
    jugadores_intP = 0

    canvas_porteros = Canvas(ventana_porteros, width=800, height=550, bg="black")
    canvas_porteros.pack()
    fondo_jugadores = PhotoImage(file="fondo_jugadores.png")
    canvas_porteros.create_image(0, 0, image=fondo_jugadores, anchor="nw")
    tiradores_label = Label(ventana_porteros, text="Selecciona los porteros", font=("pagoda-bolditalic", 20, "bold"), bg="black", fg="white")
    tiradores_label.place(x=500, y=5)

    def seleccionar_porteros(equipo, nombre_portero):
        global jugadores_rmaP, jugadores_intP, jugadores_livP, porteros_liv, porteros_int, porteros_rma

        if equipo == "Liverpool" and jugadores_livP < 1:
            porteros_liv["Portero"] = nombre_portero
            jugadores_livP += 1
            print("Equipo:", equipo)
            print("Portero seleccionado:", nombre_portero)
        elif equipo == "Real Madrid" and jugadores_rmaP < 1:
            porteros_rma["Portero"] = nombre_portero
            jugadores_rmaP += 1
            print("Equipo:", equipo)
            print("Portero seleccionado:", nombre_portero)
        elif equipo == "Inter de Milan" and jugadores_intP < 1:
            porteros_int["Portero"] = nombre_portero
            jugadores_intP += 1
            print("Equipo:", equipo)
            print("Portero seleccionado:", nombre_portero)

        if jugadores_intP == 1 and jugadores_rmaP == 1:
            ventana_porteros.destroy()
            mostrar_equipos()
        elif jugadores_rmaP == 1 and jugadores_livP == 1:
            ventana_porteros.destroy()
            mostrar_equipos()
        elif jugadores_livP == 1 and jugadores_intP == 1:
            ventana_porteros.destroy()
            mostrar_equipos()




    if equipo1 == "Liverpool":
        alisson_img = PhotoImage(file="alisson.png")
        portero1 = Button(ventana_porteros, image=alisson_img, width=150, bg="red", fg="black", command=lambda: seleccionar_porteros("Liverpool", "Alisson Becker"))
        portero1.place(x=50, y=70)

        kelleher_img = PhotoImage(file="kelleher.png")
        portero2 = Button(ventana_porteros, image=kelleher_img, bg="red", width=150,  fg="black", command=lambda: seleccionar_porteros("Liverpool", "Caoimhín Kelleher"))
        portero2.place(x=215, y=70)

        adrian_img = PhotoImage(file="adrian.png")
        portero3 = Button(ventana_porteros, image=adrian_img, bg="red", fg="black", command=lambda: seleccionar_porteros("Liverpool","Adrian San Miguel"))
        portero3.place(x=385, y=70)

        liv_label = Label(ventana_porteros, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
        liv_label.place(x=570, y=140)

    if equipo2 == "Liverpool":
        alisson_img = PhotoImage(file="alisson.png")
        portero1 = Button(ventana_porteros, image=alisson_img, width=150, bg="red", fg="white", command=lambda: seleccionar_porteros("Liverpool", "Alisson Becker"))
        portero1.place(x=50, y=280)

        kelleher_img = PhotoImage(file="kelleher.png")
        portero2 = Button(ventana_porteros, image=kelleher_img, bg="red", width=150, fg="white", command=lambda: seleccionar_porteros("Liverpool", "Caoimhín Kelleher"))
        portero2.place(x=215, y=280)

        adrian_img = PhotoImage(file="adrian.png")
        portero3 = Button(ventana_porteros, image=adrian_img, bg="red", fg="white", command=lambda: seleccionar_porteros("Liverpool", "Adrian San Miguel"))
        portero3.place(x=385, y=280)

        liv_label = Label(ventana_porteros, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
        liv_label.place(x=570, y=350)


    if equipo1 == "Real Madrid":
        courtois_img = PhotoImage(file="courtois.png")
        portero1 = Button(ventana_porteros, image=courtois_img, width=155, bg="white", fg="white",command=lambda: seleccionar_porteros("Real Madrid", "Thibaut Courtois"))
        portero1.place(x=50, y=70)

        lunin_img = PhotoImage(file="lunin.png")
        portero2 = Button(ventana_porteros, image=lunin_img, bg="white", width=155, fg="white",command=lambda: seleccionar_porteros("Real Madrid", "Andriy Lunin"))
        portero2.place(x=220, y=70)

        kepa_img = PhotoImage(file="kepa.png")
        portero3 = Button(ventana_porteros, image=kepa_img, bg="white", width=155, fg="white",command=lambda: seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga"))
        portero3.place(x=390, y=70)

        rma_label = Label(ventana_porteros, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black",fg="white")
        rma_label.place(x=570, y=140)

    if equipo2 == "Real Madrid":
        courtois_img = PhotoImage(file="courtois.png")
        portero1 = Button(ventana_porteros, image=courtois_img, width=155, bg="white", fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Thibaut Courtois"))
        portero1.place(x=50, y=280)

        lunin_img = PhotoImage(file="lunin.png")
        portero2 = Button(ventana_porteros, image=lunin_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Andriy Lunin"))
        portero2.place(x=220, y=280)

        kepa_img = PhotoImage(file="kepa.png")
        portero3 = Button(ventana_porteros, image=kepa_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga"))
        portero3.place(x=390, y=280)

        rma_label = Label(ventana_porteros, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="white")
        rma_label.place(x=570, y=350)


    if equipo1 == "Inter de Milan":
        sommer_img = PhotoImage(file="sommer.png")
        portero1 = Button(ventana_porteros, image=sommer_img, width=150, bg="blue", fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Yann Sommer"))
        portero1.place(x=50, y=70)

        digennaro_img = PhotoImage(file="digennaro.png")
        portero2 = Button(ventana_porteros, image=digennaro_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro"))
        portero2.place(x=210, y=70)

        audero_img = PhotoImage(file="audero.png")
        portero3 = Button(ventana_porteros, image=audero_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Emil Audero"))
        portero3.place(x=380, y=70)

        inter_label = Label(ventana_porteros, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black", fg="blue")
        inter_label.place(x=570, y=140)

    if equipo2 == "Inter de Milan":
        sommer_img = PhotoImage(file="sommer.png")
        portero1 = Button(ventana_porteros, image=sommer_img, width=150, bg="blue", fg="white",command=lambda: seleccionar_porteros("Inter de Milan", "Yann Sommer"))
        portero1.place(x=50, y=280)

        digennaro_img = PhotoImage(file="digennaro.png")
        portero2 = Button(ventana_porteros, image=digennaro_img, bg="blue", width=155, fg="white",command=lambda: seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro"))
        portero2.place(x=210, y=280)

        audero_img = PhotoImage(file="audero.png")
        portero3 = Button(ventana_porteros, image=audero_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Emil Audero"))
        portero3.place(x=380, y=280)

        inter_label = Label(ventana_porteros, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black",fg="blue")
        inter_label.place(x=570, y=350)


    def mover_flecha_porteros(event):
        global flecha_x, flecha_y

        if flecha_activa_tiradores:
            coords_flecha = canvas_porteros.coords(flecha_equipos)
            #Potenciometro
            if event.keysym == 'Left':
                if coords_flecha[0] <= 120:
                    if coords_flecha[1] > 40:
                        canvas_porteros.move(flecha_equipos, 330, -480)
                        canvas_porteros.itemconfig(flecha_equipos, image=flecha_img_equipos)
                else:
                    canvas_porteros.move(flecha_equipos, -165, 0)
            elif event.keysym == 'Right':
                if coords_flecha[0] >= 450:
                    if coords_flecha[1] <= 460:
                        canvas_porteros.move(flecha_equipos, -330, 480)
                        canvas_porteros.itemconfig(flecha_equipos, image=flecha_equipos_up)
                else:
                    canvas_porteros.move(flecha_equipos, 165, 0)

            #Boton potenciometro
            elif event.keysym == 'Return':
                x_flecha, y_flecha = canvas_porteros.coords(flecha_equipos)
                if equipo1 == "Liverpool":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_porteros("Liverpool", "Alisson Becker")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_porteros("Liverpool", "Caoimhin Kelleher")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_porteros("Liverpool", "Adrian")
                if equipo1 == "Real Madrid":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_porteros("Real Madrid", "Thibaut Courtois")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_porteros("Real Madrid", "Andriy Lunin")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga")
                if equipo1 == "Inter de Milan":
                    if 50 < x_flecha < 200 and y_flecha < 250:
                        seleccionar_porteros("Inter de Milan", "Yann Sommer")
                    elif 190 < x_flecha < 360 and y_flecha < 250:
                        seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro")
                    elif 385 < x_flecha < 550 and y_flecha < 250:
                        seleccionar_porteros("Inter de Milan", "Emil Audero")


                    #Equipos 2
                if equipo2 == "Liverpool":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_porteros("Liverpool", "Alisson Becker")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_porteros("Liverpool", "Caoimhin Kelleher")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_porteros("Liverpool", "Adrian")
                if equipo2 == "Real Madrid":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_porteros("Real Madrid", "Thibaut Courtois")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_porteros("Real Madrid", "Andriy Lunin")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga")
                if equipo2 == "Inter de Milan":
                    if 50 < x_flecha < 200 and y_flecha > 250:
                        seleccionar_porteros("Inter de Milan", "Yann Sommer")
                    elif 190 < x_flecha < 360 and y_flecha > 250:
                        seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro")
                    elif 385 < x_flecha < 550 and y_flecha > 250:
                        seleccionar_porteros("Inter de Milan", "Emil Audero")


    ventana_porteros.bind('<Key>', mover_flecha_porteros)
    ventana_porteros.bind('<Return>', mover_flecha_porteros)

    flecha_equipos_up = PhotoImage(file="flecha_equipos_up.png")
    flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
    flecha_equipos = canvas_porteros.create_image(120, 40, image=flecha_img_equipos)


    ventana_porteros.mainloop()


ventana_mostrar_equipos = None

def mostrar_equipos():
    global tiradores_seleccionados, equipo1, equipo2, porteros_int, porteros_rma, porteros_liv

    ventana_mostrar_equipos = Toplevel(window)
    ventana_mostrar_equipos.config(bg="black")
    ventana_mostrar_equipos.geometry("900x600+30+30")
    ventana_mostrar_equipos.title("Equipo 1")
    ventana_mostrar_equipos.focus_set()

    menu_sound.stop()
    mixer.music.load("himno_champions.mp3")
    mixer.music.play()

    canvas_equipos = Canvas(ventana_mostrar_equipos, width=1000, height=600)
    canvas_equipos.pack()

    madrid = PhotoImage(file="madrid_mostrar.png")
    liv = PhotoImage(file="liv_mostrar.png")
    int = PhotoImage(file="inter_mostrar.png")


    if equipo1 == "Real Madrid":
        canvas_equipos.create_image(0, 0, image=madrid, anchor="nw")
        if tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
            jude = PhotoImage(file="jude.png")
            canvas_equipos.create_image(350, 250, image=jude)
            canvas_equipos.create_text(500, 240, text="Jude Bellingham", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
            vini = PhotoImage(file="vinicius.png")
            canvas_equipos.create_image(350, 250, image=vini)
            canvas_equipos.create_text(500, 240, text="Vinicius Jr", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
            rodrygo = PhotoImage(file="rodrygo.png")
            canvas_equipos.create_image(350, 250, image=rodrygo)
            canvas_equipos.create_text(500, 240, text="Rodrygo Goes", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_rma.get("Portero") == "Thibaut Courtois":
            courtois = PhotoImage(file="courtois.png")
            canvas_equipos.create_image(350, 480, image= courtois)
            canvas_equipos.create_text(500, 480, text="Thibaut Courtois", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_rma.get("Portero") == "Andriy Lunin":
            lunin = PhotoImage(file="lunin.png")
            canvas_equipos.create_image(350, 480, image=lunin)
            canvas_equipos.create_text(500, 480, text="Andriy Lunin", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_rma.get("Portero") == "Kepa Arrizabalaga":
            kepa = PhotoImage(file="kepa.png")
            canvas_equipos.create_image(350, 480, image=kepa)
            canvas_equipos.create_text(500, 480, text="Kepa Arrizabalaga", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")


    elif equipo1 == "Liverpool":
        canvas_equipos.create_image(0, 0, image=liv, anchor="nw")
        if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
            salah = PhotoImage(file="salah.png")
            canvas_equipos.create_image(350,250, image=salah)
            canvas_equipos.create_text(500, 240, text="Mohamed Salah", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
            darwin = PhotoImage(file="nuñez.png")
            canvas_equipos.create_image(350, 250, image=darwin)
            canvas_equipos.create_text(500, 240, text="Darwin Núñez", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
            lucho = PhotoImage(file="diaz.png")
            canvas_equipos.create_image(350, 250, image=lucho)
            canvas_equipos.create_text(500, 240, text="Luis Díaz", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_liv.get("Portero") == "Alisson Becker":
            alisson = PhotoImage(file="alisson.png")
            canvas_equipos.create_image(350, 480, image= alisson)
            canvas_equipos.create_text(500, 480, text="Alisson Becker", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_liv.get("Portero") == "Caoimhin Kelleher":
            kelleher = PhotoImage(file="kelleher.png")
            canvas_equipos.create_image(350, 480, image= kelleher)
            canvas_equipos.create_text(500, 480, text="Caoihmin Kelleher", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_liv.get("Portero") == "Adrian":
            adrian = PhotoImage(file="adrian.png")
            canvas_equipos.create_image(350, 480, image= adrian)
            canvas_equipos.create_text(500, 480, text="Adrian San Miguel", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")


    if equipo1 == "Inter de Milan":
        canvas_equipos.create_image(0,0, image=int, anchor="nw")
        if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
            lautaro = PhotoImage(file="lautaro.png")
            canvas_equipos.create_image(350, 250, image=lautaro)
            canvas_equipos.create_text(500, 240, text="Lautaro Martínez", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
            hakan = PhotoImage(file="calhanoglu.png")
            canvas_equipos.create_image(350, 250, image=hakan)
            canvas_equipos.create_text(500, 240, text="Hakan Calhanoglu", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
            alexis = PhotoImage(file="alexis.png")
            canvas_equipos.create_image(350, 250, image=alexis)
            canvas_equipos.create_text(500, 240, text="Alexis Sánchez", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_int.get("Portero") == "Yann Sommer":
            sommer = PhotoImage(file="sommer.png")
            canvas_equipos.create_image(350, 480, image= sommer)
            canvas_equipos.create_text(500, 480, text="Yann Sommer", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_int.get("Portero") == "Raffaele Di Gennaro":
            digennaro = PhotoImage(file="digennaro.png")
            canvas_equipos.create_image(350, 480, image=digennaro)
            canvas_equipos.create_text(500, 480, text="Raffael Di Gennaro", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_int.get("Portero") == "Emil Audero":
            audero = PhotoImage(file="audero.png")
            canvas_equipos.create_image(350, 480, image=audero)
            canvas_equipos.create_text(500, 480, text="Emil Audero", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")


    ventana_mostrar_equipos.after(7000, mostrar_equipos2)
    ventana_mostrar_equipos.after(7000, ventana_mostrar_equipos.destroy)
    ventana_mostrar_equipos.mainloop()


def mostrar_equipos2():
    global tiradores_seleccionados, equipo1, equipo2, porteros_int, porteros_rma, porteros_liv, ventana_mostrar_equipos

    ventana_mostrar_equipos2 = Toplevel(window)
    ventana_mostrar_equipos2.config(bg="black")
    ventana_mostrar_equipos2.geometry("900x600+30+30")
    ventana_mostrar_equipos2.title("Equipo 2")
    ventana_mostrar_equipos2.focus_set()

    canvas_equipos = Canvas(ventana_mostrar_equipos2, width=1000, height=600)
    canvas_equipos.pack()

    madrid = PhotoImage(file="madrid_mostrar.png")
    liv = PhotoImage(file="liv_mostrar.png")
    int = PhotoImage(file="inter_mostrar.png")


    if equipo2 == "Real Madrid":
        canvas_equipos.create_image(0, 0, image=madrid, anchor="nw")
        if tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
            jude = PhotoImage(file="jude.png")
            canvas_equipos.create_image(350, 250, image=jude)
            canvas_equipos.create_text(500, 240, text="Jude Bellingham", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
            vini = PhotoImage(file="vinicius.png")
            canvas_equipos.create_image(350, 250, image=vini)
            canvas_equipos.create_text(500, 240, text="Vinicius Jr", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
            rodrygo = PhotoImage(file="rodrygo.png")
            canvas_equipos.create_image(350, 250, image=rodrygo)
            canvas_equipos.create_text(500, 240, text="Rodrygo Goes", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_rma.get("Portero") == "Thibaut Courtois":
            courtois = PhotoImage(file="courtois.png")
            canvas_equipos.create_image(350, 480, image= courtois)
            canvas_equipos.create_text(500, 480, text="Thibaut Courtois", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_rma.get("Portero") == "Andriy Lunin":
            lunin = PhotoImage(file="lunin.png")
            canvas_equipos.create_image(350, 480, image=lunin)
            canvas_equipos.create_text(500, 480, text="Andriy Lunin", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_rma.get("Portero") == "Kepa Arrizabalaga":
            kepa = PhotoImage(file="kepa.png")
            canvas_equipos.create_image(350, 480, image=kepa)
            canvas_equipos.create_text(500, 480, text="Kepa Arrizabalaga", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")


    elif equipo2 == "Liverpool":
        canvas_equipos.create_image(0, 0, image=liv, anchor="nw")
        if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
            salah = PhotoImage(file="salah.png")
            canvas_equipos.create_image(350,250, image=salah)
            canvas_equipos.create_text(500, 240, text="Mohamed Salah", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
            darwin = PhotoImage(file="nuñez.png")
            canvas_equipos.create_image(350, 250, image=darwin)
            canvas_equipos.create_text(500, 240, text="Darwin Núñez", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
            lucho = PhotoImage(file="diaz.png")
            canvas_equipos.create_image(350, 250, image=lucho)
            canvas_equipos.create_text(500, 240, text="Luis Díaz", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_liv.get("Portero") == "Alisson Becker":
            alisson = PhotoImage(file="alisson.png")
            canvas_equipos.create_image(350, 480, image= alisson)
            canvas_equipos.create_text(500, 480, text="Alisson Becker", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_liv.get("Portero") == "Caoimhin Kelleher":
            kelleher = PhotoImage(file="kelleher.png")
            canvas_equipos.create_image(350, 480, image= kelleher)
            canvas_equipos.create_text(500, 480, text="Caoihmin Kelleher", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_liv.get("Portero") == "Adrian":
            adrian = PhotoImage(file="adrian.png")
            canvas_equipos.create_image(350, 480, image= adrian)
            canvas_equipos.create_text(500, 480, text="Adrian San Miguel", anchor="nw",font=("pagoda-bolditalic", 35, "bold"), fill="white")


    if equipo2 == "Inter de Milan":
        canvas_equipos.create_image(0,0, image=int, anchor="nw")
        if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
            lautaro = PhotoImage(file="lautaro.png")
            canvas_equipos.create_image(350, 250, image=lautaro)
            canvas_equipos.create_text(500, 240, text="Lautaro Martínez", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
            hakan = PhotoImage(file="calhanoglu.png")
            canvas_equipos.create_image(350, 250, image=hakan)
            canvas_equipos.create_text(500, 240, text="Hakan Calhanoglu", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
            alexis = PhotoImage(file="alexis.png")
            canvas_equipos.create_image(350, 250, image=alexis)
            canvas_equipos.create_text(500, 240, text="Alexis Sánchez", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")

        if porteros_int.get("Portero") == "Yann Sommer":
            sommer = PhotoImage(file="sommer.png")
            canvas_equipos.create_image(350, 480, image= sommer)
            canvas_equipos.create_text(500, 480, text="Yann Sommer", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_int.get("Portero") == "Raffaele Di Gennaro":
            digennaro = PhotoImage(file="digennaro.png")
            canvas_equipos.create_image(350, 480, image=digennaro)
            canvas_equipos.create_text(500, 480, text="Raffael Di Gennaro", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")
        elif porteros_int.get("Portero") == "Emil Audero":
            audero = PhotoImage(file="audero.png")
            canvas_equipos.create_image(350, 480, image=audero)
            canvas_equipos.create_text(500, 480, text="Emil Audero", anchor="nw", font=("pagoda-bolditalic", 35, "bold"), fill="white")

    ventana_mostrar_equipos2.after(7000, ventana_moneda)
    ventana_mostrar_equipos2.after(7000, ventana_mostrar_equipos2.destroy)
    ventana_mostrar_equipos2.mainloop()


def ventana_moneda():
    ventana_moneda = Toplevel(window)
    ventana_moneda.config(bg="black")
    ventana_moneda.geometry("800x600+30+30")
    ventana_moneda.title("Sorteo")
    ventana_moneda.focus_set()

    canvas_juego = Canvas(ventana_moneda, width=800, height=600)
    canvas_juego.pack()
    fondo = PhotoImage(file="fondo_mostrarequipos.png")
    canvas_juego.create_image(0, 0, image=fondo, anchor="nw")


    def animacion_moneda():
        cara_img = Image.open("cara.png")
        cruz_img = Image.open("cruz.png")
        lateral_img = Image.open("lateral.png")

        cara_img_tk = ImageTk.PhotoImage(cara_img)
        cruz_img_tk = ImageTk.PhotoImage(cruz_img)
        lateral_img_tk = ImageTk.PhotoImage(lateral_img)

        resultado = random.choice([equipo1, equipo2])
        equipo_tira = "Equipo 1" if resultado == "equipo1" else "Equipo 2"
        equipo_ataja = "Equipo 2" if resultado == "equipo1" else "Equipo 1"

        if resultado == equipo1:
            if equipo1 == "Real Madrid":
                equipo_tira = equipo1
            elif equipo1 == "Liverpool":
                equipo_tira = equipo1
            elif equipo1 == "Inter de Milan":
                equipo_tira = equipo1
            if equipo2 == "Real Madrid":
                equipo_ataja = equipo2
            elif equipo2 == "Liverpool":
                equipo_ataja = equipo2
            elif equipo2 == "Inter de Milan":
                equipo_ataja = equipo2
        else:
            if equipo2 == "Real Madrid":
                equipo_tira = equipo2
            elif equipo2 == "Liverpool":
                equipo_tira = equipo2
            elif equipo2 == "Inter de Milan":
                equipo_tira = equipo2
            if equipo1 == "Real Madrid":
                equipo_ataja = equipo1
            elif equipo1 == "Liverpool":
                equipo_ataja = equipo1
            elif equipo1 == "Inter de Milan":
                equipo_ataja = equipo1


        x1 = 250
        y = 150

        for i in range(0, 300, 10):
            canvas_juego.delete("moneda")

            if i % 30 < 10:
                imagen = cara_img_tk
                x = x1
            elif i % 30 < 20:
                imagen = cruz_img_tk
                x = x1
            else:
                imagen = lateral_img_tk
                x = 350
            canvas_juego.create_image(x, y, image=imagen, anchor="nw", tag="moneda")
            ventana_moneda.update()
            ventana_moneda.after(100)

        canvas_juego.create_text(400, 300, text=f"{resultado.capitalize()}: Tira", font=("pagoda-bolditalic", 40, "bold"), fill="white")
        ventana_moneda.after(3000, crear_ventana_juego, equipo_tira, equipo_ataja)
        ventana_moneda.after(3000, ventana_moneda.destroy)


    animacion_moneda()
    ventana_moneda.mainloop()

pygame.mixer.init()
paleta_portero = 0
tirar = 0
tiros_eq1 = 0
tiros_eq2 = 0
lista_eq1 = []
lista_eq2 = []

tiros_salah = 0
goles_salah = 0
tiros_darwin = 0
goles_darwin = 0
tiros_diaz = 0
goles_diaz = 0

tiros_jude = 0
goles_jude = 0
tiros_vinicius = 0
goles_vinicius = 0
tiros_rodrygo = 0
goles_rodrygo = 0

tiros_lautaro = 0
goles_lautaro = 0
tiros_calhanoglu = 0
goles_calhanoglu = 0
tiros_alexis = 0
goles_alexis = 0



def crear_ventana_juego(equipo_tira, equipo_ataja):
    global tiradores_seleccionados, porteros_int, porteros_rma, porteros_liv, ventana_juego, paleta_portero, tirar, lista_eq2, lista_eq1
    ventana_juego = Toplevel(window)
    ventana_juego.config(bg="black")
    ventana_juego.geometry("1005x600+30+30")
    ventana_juego.title("Final")
    ventana_juego.focus_set()


    paleta_portero = 0
    tirar = 0

    ambiente_sound = pygame.mixer.Sound("ambiente.mp3")
    silbidos = pygame.mixer.Sound("silbidos.mp3")
    gol = pygame.mixer.Sound("gol.mp3")
    ambiente_sound.play(-1)

    canvas_juego = Canvas(ventana_juego, width=1005, height=600)
    canvas_juego.pack()
    fondo = PhotoImage(file="fondo_juego.png")
    canvas_juego.create_image(0,0, image=fondo, anchor="nw")


    port_rma_s = PhotoImage(file="port_rma_s.png")
    port_rma_l = PhotoImage(file="port_rma_l.png")
    port_rma_r = PhotoImage(file="port_rma_r.png")

    port_liv_s = PhotoImage(file="port_liv_s.png")
    port_liv_l = PhotoImage(file="port_liv_l.png")
    port_liv_r = PhotoImage(file="port_liv_r.png")

    port_int_s = PhotoImage(file="port_int_s.png")
    port_int_l = PhotoImage(file="port_int_l.png")
    port_int_r = PhotoImage(file="port_int_r.png")

    if equipo1 == "Real Madrid":
        if equipo_ataja == "Real Madrid":
            canvas_juego.create_text(215, 110, text="Real Madrid", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_rma.get("Portero") == "Thibaut Courtois":
                courtois = PhotoImage(file="courtois.png")
                canvas_juego.create_image(65, 110, image=courtois)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
            elif porteros_rma.get("Portero") == "Andriy Lunin":
                lunin = PhotoImage(file="lunin.png")
                canvas_juego.create_image(65, 110, image=lunin)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
            elif porteros_rma.get("Portero") == "Kepa Arrizabalaga":
                kepa = PhotoImage(file="kepa.png")
                canvas_juego.create_image(65, 110, image=kepa)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
        elif equipo_tira == "Real Madrid":
            canvas_juego.create_text(215, 110, text="Real Madrid", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                jude = PhotoImage(file="jude.png")
                canvas_juego.create_image(65, 110, image=jude)
            elif tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                vini = PhotoImage(file="vinicius.png")
                canvas_juego.create_image(65, 110, image=vini)
            elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                rodrygo = PhotoImage(file="rodrygo.png")
                canvas_juego.create_image(65, 110, image=rodrygo)
    if equipo2 == "Real Madrid":
        if equipo_ataja == "Real Madrid":
            canvas_juego.create_text(650, 110, text="Real Madrid", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_rma.get("Portero") == "Thibaut Courtois":
                courtois = PhotoImage(file="courtois.png")
                canvas_juego.create_image(927, 110, image=courtois)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
            elif porteros_rma.get("Portero") == "Andriy Lunin":
                lunin = PhotoImage(file="lunin.png")
                canvas_juego.create_image(927, 110, image=lunin)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
            elif porteros_rma.get("Portero") == "Kepa Arrizabalaga":
                kepa = PhotoImage(file="kepa.png")
                canvas_juego.create_image(927, 110, image=kepa)
                port_rma = canvas_juego.create_image(385, 309, image=port_rma_s, anchor="nw")
        elif equipo_tira == "Real Madrid":
            canvas_juego.create_text(650, 110, text="Real Madrid", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                jude = PhotoImage(file="jude.png")
                canvas_juego.create_image(927, 110, image=jude)
            elif tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                vini = PhotoImage(file="vinicius.png")
                canvas_juego.create_image(927, 110, image=vini)
            elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                rodrygo = PhotoImage(file="rodrygo.png")
                canvas_juego.create_image(927, 110, image=rodrygo)


    if equipo1 == "Liverpool":
        if equipo_ataja == "Liverpool":
            canvas_juego.create_text(215, 110, text="Liverpool", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_liv.get("Portero") == "Alisson Becker":
                alisson = PhotoImage(file="alisson.png")
                canvas_juego.create_image(65, 110, image= alisson)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
            elif porteros_liv.get("Portero") == "Caoimhin Kelleher":
                kelleher = PhotoImage(file="kelleher.png")
                canvas_juego.create_image(65, 110, image= kelleher)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
            elif porteros_liv.get("Portero") == "Adrian":
                adrian = PhotoImage(file="adrian.png")
                canvas_juego.create_image(65, 110, image= adrian)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
        elif equipo_tira == "Liverpool":
            canvas_juego.create_text(215, 110, text="Liverpool", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                salah = PhotoImage(file="salah.png")
                canvas_juego.create_image(65, 110, image=salah)
            elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                darwin = PhotoImage(file="nuñez.png")
                canvas_juego.create_image(65, 110, image=darwin)
            elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                lucho = PhotoImage(file="diaz.png")
                canvas_juego.create_image(65, 110, image=lucho)
    if equipo2 == "Liverpool":
        if equipo_ataja == "Liverpool":
            canvas_juego.create_text(650, 110, text="Liverpool", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_liv.get("Portero") == "Alisson Becker":
                alisson = PhotoImage(file="alisson.png")
                canvas_juego.create_image(927, 110, image= alisson)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
            elif porteros_liv.get("Portero") == "Caoimhin Kelleher":
                kelleher = PhotoImage(file="kelleher.png")
                canvas_juego.create_image(927, 110, image= kelleher)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
            elif porteros_liv.get("Portero") == "Adrian":
                adrian = PhotoImage(file="adrian.png")
                canvas_juego.create_image(927, 110, image= adrian)
                port_liv = canvas_juego.create_image(385, 309, image=port_liv_s, anchor="nw")
        elif equipo_tira == "Liverpool":
            canvas_juego.create_text(650, 110, text="Liverpool", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                salah = PhotoImage(file="salah.png")
                canvas_juego.create_image(927, 110, image=salah)
            elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                darwin = PhotoImage(file="nuñez.png")
                canvas_juego.create_image(927, 110, image=darwin)
            elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                lucho = PhotoImage(file="diaz.png")
                canvas_juego.create_image(927, 110, image=lucho)


    if equipo1 == "Inter de Milan":
        if equipo_ataja == "Inter de Milan":
            canvas_juego.create_text(215, 110, text="Inter de Milan", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_int.get("Portero") == "Yann Sommer":
                sommer = PhotoImage(file="sommer.png")
                canvas_juego.create_image(65, 110, image=sommer)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
            elif porteros_int.get("Portero") == "Raffaele Di Gennaro":
                digennaro = PhotoImage(file="digennaro.png")
                canvas_juego.create_image(65, 110, image=digennaro)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
            elif porteros_int.get("Portero") == "Emil Audero":
                audero = PhotoImage(file="audero.png")
                canvas_juego.create_image(65, 110, image=audero)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
        elif equipo_tira == "Inter de Milan":
            canvas_juego.create_text(215, 110, text="Inter de Milan", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                lautaro = PhotoImage(file="lautaro.png")
                canvas_juego.create_image(65, 110, image=lautaro)
            elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                hakan = PhotoImage(file="calhanoglu.png")
                canvas_juego.create_image(65, 110, image=hakan)
            elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                alexis = PhotoImage(file="alexis.png")
                canvas_juego.create_image(65, 110, image=alexis)
    if equipo2 == "Inter de Milan":
        if equipo_ataja == "Inter de Milan":
            canvas_juego.create_text(650, 110, text="Inter de Milan", font=("champions normal", 20), fill="white", anchor="nw")
            if porteros_int.get("Portero") == "Yann Sommer":
                sommer = PhotoImage(file="sommer.png")
                canvas_juego.create_image(927, 110, image=sommer)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
            elif porteros_int.get("Portero") == "Raffaele Di Gennaro":
                digennaro = PhotoImage(file="digennaro.png")
                canvas_juego.create_image(927, 110, image=digennaro)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
            elif porteros_int.get("Portero") == "Emil Audero":
                audero = PhotoImage(file="audero.png")
                canvas_juego.create_image(927, 110, image=audero)
                port_int = canvas_juego.create_image(385, 309, image=port_int_s, anchor="nw")
        elif equipo_tira == "Inter de Milan":
            canvas_juego.create_text(650, 110, text="Inter de Milan", font=("champions normal", 20), fill="white", anchor="nw")
            if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                lautaro = PhotoImage(file="lautaro.png")
                canvas_juego.create_image(927, 110, image=lautaro)
            elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                hakan = PhotoImage(file="calhanoglu.png")
                canvas_juego.create_image(927, 110, image=hakan)
            elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                alexis = PhotoImage(file="alexis.png")
                canvas_juego.create_image(927, 110, image=alexis)


    silbato_sound = pygame.mixer.Sound("silbato.mp3")


    def habilitar_paletas():
        global paleta_portero, tirar
        tirar = 1
        print("¡Ahora puedes seleccionar una paleta!")

    def paletas(event=None):
        global paleta_portero, tirar

        if event and hasattr(event, 'char'):
            key = event.char
            if key in {'1', '2', '3', '4', '5', '6'} and tirar == 0:
                return
            elif key in {'1', '2', '3', '4', '5', '6'} and tirar == 1:
                print("Paleta seleccionada por el usuario:", key)
                seleccionar_portero_imaginario(key)
                tirar = 0
            elif key == 'c' and tirar == 0:
                ventana_juego.destroy()
                seleccion_tiradores_juego()
        elif paleta_portero == 0 and tirar == 0:
            ventana_juego.after(5000, habilitar_paletas)
            ventana_juego.after(5000, lambda: pygame.mixer.Channel(1).play(silbato_sound))
            ventana_juego.after(10000, gol_fallido)


    def gol_fallido():
        global tiros_eq2,tiros_eq1, lista_eq2, lista_eq1, tirar, tiradores_seleccionados, tiros_vinicius, tiros_diaz, tiros_jude, tiros_rodrygo, tiros_salah, tiros_darwin, tiros_alexis, tiros_calhanoglu, tiros_lautaro
        if tirar == 1:
            pygame.mixer.Channel(1).play(silbidos)
            if equipo_tira == equipo1:
                if equipo1 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                if equipo1 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                if equipo1 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                tiros_eq1 += 1
                lista_eq1.append(0)
                marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
            elif equipo_tira == equipo2:
                if equipo2 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                if equipo2 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                if equipo2 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                tiros_eq2 += 1
                lista_eq2.append(0)
                marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
            if tiros_eq1 == 5 and tiros_eq2 == 5:
                if lista_eq1.count(1) == lista_eq2.count(1):
                    lista_eq1.pop()
                    lista_eq2.pop()
                    tiros_eq2 -= 1
                    tiros_eq1 -= 1
                    marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
                    marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
                else:
                    ambiente_sound.stop()
                    final()
            tirar = 0
        intercambiar_roles(equipo_ataja, equipo_tira)


    paletas()
    ventana_juego.bind("<Key>", paletas)


    gol_anotado = PhotoImage(file="gol_anotado.png")
    gol_fallado = PhotoImage(file="gol_fallido.png")
    coordenadas_goles_eq1 = [(209, 65), (251, 65), (297, 65), (342, 65), (386, 65)]
    coordenadas_goles_eq2 = [(580, 65), (625, 65), (669, 65), (714, 65), (758, 65)]

    def marcador1(canvas, lista_eq1, coordenadas):
        for i in range(min(len(lista_eq1), len(coordenadas))):
            if i < len(coordenadas):  # Verificar si el índice es válido
                if lista_eq1[i] == 1:
                    canvas.create_image(coordenadas[i], image=gol_anotado, anchor="nw")
                elif lista_eq1[i] == 0:
                    canvas.create_image(coordenadas[i], image=gol_fallado, anchor="nw")

    def marcador2(canvas, lista_eq2, coordenadas):
        for i in range(min(len(lista_eq2), len(coordenadas))):
            if i < len(coordenadas):  # Verificar si el índice es válido
                if lista_eq2[i] == 1:
                    canvas.create_image(coordenadas[i], image=gol_anotado, anchor="nw")
                elif lista_eq2[i] == 0:
                    canvas.create_image(coordenadas[i], image=gol_fallado, anchor="nw")


    def seleccionar_portero_imaginario(key):
        global paleta_portero, tiros_eq1, tiros_eq2, tiros_vinicius, tiros_diaz, tiros_jude, tiros_rodrygo, tiros_salah, tiros_darwin, tiros_alexis, tiros_calhanoglu, tiros_lautaro, goles_vinicius, goles_diaz, goles_jude, goles_rodrygo, goles_salah, goles_darwin, goles_alexis, goles_calhanoglu, goles_lautaro
        paleta_portero = random.randint(1, 6)
        if equipo_ataja == "Real Madrid":
            if 0 < paleta_portero <= 3:
                canvas_juego.itemconfig(port_rma, image=port_rma_l)
            else:
                canvas_juego.itemconfig(port_rma, image=port_rma_r)
        elif equipo_ataja == "Liverpool":
            if 0 < paleta_portero <= 3:
                canvas_juego.itemconfig(port_liv, image=port_liv_l)
            else:
                canvas_juego.itemconfig(port_liv, image=port_liv_r)
        elif equipo_ataja == "Inter de Milan":
            if 0 < paleta_portero <= 3:
                canvas_juego.itemconfig(port_int, image=port_int_l)
            else:
                canvas_juego.itemconfig(port_int, image=port_int_r)
        print("El portero se tiró en:", paleta_portero)
        if int(key) == paleta_portero:
            pygame.mixer.Channel(1).play(silbidos)
            print("¡Atajada!")
            if equipo_tira == equipo1:
                if equipo1 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                if equipo1 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                if equipo1 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                tiros_eq1 += 1
                lista_eq1.append(0)
                marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
            elif equipo_tira == equipo2:
                if equipo2 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                if equipo2 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                if equipo2 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                tiros_eq2 += 1
                lista_eq2.append(0)
                marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
            if tiros_eq2 == 5 and tiros_eq1 == 5:
                if lista_eq1.count(1) == lista_eq2.count(1):
                    lista_eq1.pop()
                    lista_eq2.pop()
                    tiros_eq2 -= 1
                    tiros_eq1 -= 1
                    marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
                    marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
                else:
                    ambiente_sound.stop()
                    final()
        else:
            pygame.mixer.Channel(1).play(gol)
            print("¡GOOOOL!")
            if equipo_tira == equipo1:
                if equipo1 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                        goles_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                        goles_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                        goles_rodrygo += 1
                if equipo1 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                        goles_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                        goles_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                        goles_darwin += 1
                if equipo1 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                        goles_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                        goles_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                        goles_alexis += 1
                tiros_eq1 += 1
                lista_eq1.append(1)
                marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
            elif equipo_tira == equipo2:
                if equipo2 == "Real Madrid":
                    if tiradores_seleccionados.get("Real Madrid") == "Vinicius Jr":
                        tiros_vinicius += 1
                        goles_vinicius += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Jude Bellingham":
                        tiros_jude += 1
                        goles_jude += 1
                    elif tiradores_seleccionados.get("Real Madrid") == "Rodrygo Goes":
                        tiros_rodrygo += 1
                        goles_rodrygo += 1
                if equipo2 == "Liverpool":
                    if tiradores_seleccionados.get("Liverpool") == "Mohamed Salah":
                        tiros_salah += 1
                        goles_salah += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Lucho Diaz":
                        tiros_diaz += 1
                        goles_diaz += 1
                    elif tiradores_seleccionados.get("Liverpool") == "Darwin Núñez":
                        tiros_darwin += 1
                        goles_darwin += 1
                if equipo2 == "Inter de Milan":
                    if tiradores_seleccionados.get("Inter de Milan") == "Lautaro Martínez":
                        tiros_lautaro += 1
                        goles_lautaro += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Hakan Calhanoglu":
                        tiros_calhanoglu += 1
                        goles_calhanoglu += 1
                    elif tiradores_seleccionados.get("Inter de Milan") == "Alexis Sánchez":
                        tiros_alexis += 1
                        goles_alexis += 1
                tiros_eq2 += 1
                lista_eq2.append(1)
                marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
            if tiros_eq2 == 5 and tiros_eq1 ==   5:
                if lista_eq1.count(1) == lista_eq2.count(1):
                    lista_eq1.pop()
                    lista_eq2.pop()
                    tiros_eq2 -= 1
                    tiros_eq1 -= 1
                    marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)
                    marcador1(canvas_juego, lista_eq1,coordenadas_goles_eq1)
                else:
                    ambiente_sound.stop()
                    final()

    def seleccion_tiradores_juego():
        global equipo1, equipo2, flecha_activa_tiradores, jugadores_rma, jugadores_int, jugadores_liv
        ventana_tiradores = Toplevel(window)
        ventana_tiradores.config(bg="black")
        ventana_tiradores.geometry("800x550+30+30")
        ventana_tiradores.title("Selección de Tiradores")
        ventana_tiradores.focus_set()
        flecha_activa_tiradores = True
        jugadores_liv = 0
        jugadores_rma = 0
        jugadores_int = 0


        canvas_tiradores = Canvas(ventana_tiradores, width=800, height=550, bg="black")
        canvas_tiradores.pack()
        fondo_jugadores = PhotoImage(file="fondo_jugadores.png")
        canvas_tiradores.create_image(0, 0, image=fondo_jugadores, anchor="nw")
        tiradores_label = Label(ventana_tiradores, text="Selecciona los tiradores", font=("pagoda-bolditalic", 20, "bold"), bg="black", fg="white")
        tiradores_label.place(x=500, y=5)

        def seleccionar_tiradores(equipo, nombre_tirador):
            global jugadores_rma, jugadores_int, jugadores_liv, tiradores_seleccionados
            tiradores_seleccionados[equipo] = nombre_tirador
            if equipo == "Liverpool" and jugadores_liv < 1:
                tiradores_seleccionados[equipo] = nombre_tirador
                jugadores_liv += 1
                print("Equipo:", equipo)
                print("Tirador seleccionado:", nombre_tirador)
            elif equipo == "Real Madrid" and jugadores_rma < 1:
                tiradores_seleccionados[equipo] = nombre_tirador
                jugadores_rma += 1
                print("Equipo:", equipo)
                print("Tirador seleccionado:", nombre_tirador)
            elif equipo == "Inter de Milan" and jugadores_int < 1:
                tiradores_seleccionados[equipo] = nombre_tirador
                jugadores_int += 1
                print("Equipo:", equipo)
                print("Tirador seleccionado:", nombre_tirador)

            if jugadores_int == 1 and jugadores_rma == 1:
                ventana_tiradores.destroy()
                seleccion_porteros_juego()
            elif jugadores_rma == 1 and jugadores_liv == 1:
                ventana_tiradores.destroy()
                seleccion_porteros_juego()
            elif jugadores_liv == 1 and jugadores_int == 1:
                ventana_tiradores.destroy()
                seleccion_porteros_juego()

        if equipo1 == "Liverpool":
            salah_img = PhotoImage(file="salah.png")
            tirador1 = Button(ventana_tiradores, image=salah_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Mohamed Salah"))
            tirador1.place(x=50, y=70)

            nunez_img = PhotoImage(file="nuñez.png")
            tirador2 = Button(ventana_tiradores, image=nunez_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Darwin Núñez"))
            tirador2.place(x=190, y=70)

            diaz_img = PhotoImage(file="diaz.png")
            tirador3 = Button(ventana_tiradores, image=diaz_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Lucho Díaz"))
            tirador3.place(x=385, y=70)

            liv_label = Label(ventana_tiradores, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
            liv_label.place(x=570, y=140)

        if equipo2 == "Liverpool":
            salah_img = PhotoImage(file="salah.png")
            tirador1 = Button(ventana_tiradores, image=salah_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Mohamed Salah"))
            tirador1.place(x=50, y=300)

            nunez_img = PhotoImage(file="nuñez.png")
            tirador2 = Button(ventana_tiradores, image=nunez_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Darwin Núñez"))
            tirador2.place(x=190, y=300)

            diaz_img = PhotoImage(file="diaz.png")
            tirador3 = Button(ventana_tiradores, image=diaz_img, bg="red", fg="white", command=lambda: seleccionar_tiradores("Liverpool", "Lucho Díaz"))
            tirador3.place(x=385, y=300)

            liv_label = Label(ventana_tiradores, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black",
                              fg="red")
            liv_label.place(x=570, y=350)

        if equipo1 == "Real Madrid":
            jude_img = PhotoImage(file="jude.png")
            tirador1 = Button(ventana_tiradores, image=jude_img, bg="white", fg="white",command=lambda: seleccionar_tiradores("Real Madrid", "Jude Bellingham"))
            tirador1.place(x=50, y=70)

            vini_img = PhotoImage(file="vinicius.png")
            tirador2 = Button(ventana_tiradores, image=vini_img, bg="white", width=155, fg="white",
                              command=lambda: seleccionar_tiradores("Real Madrid", "Vinicius Jr"))
            tirador2.place(x=210, y=70)

            rodrygo_img = PhotoImage(file="rodrygo.png")
            tirador3 = Button(ventana_tiradores, image=rodrygo_img, bg="white", width=155, fg="white",
                              command=lambda: seleccionar_tiradores("Real Madrid", "Rodrygo Goes"))
            tirador3.place(x=380, y=70)

            rma_label = Label(ventana_tiradores, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black",
                              fg="white")
            rma_label.place(x=570, y=140)

        if equipo2 == "Real Madrid":
            jude_img = PhotoImage(file="jude.png")
            tirador1 = Button(ventana_tiradores, image=jude_img, bg="white", fg="black",
                              command=lambda: seleccionar_tiradores("Real Madrid", "Jude Bellingham"))
            tirador1.place(x=50, y=300)

            vini_img = PhotoImage(file="vinicius.png")
            tirador2 = Button(ventana_tiradores, image=vini_img, bg="white", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Real Madrid", "Vinicius Jr"))
            tirador2.place(x=210, y=300)

            rodrygo_img = PhotoImage(file="rodrygo.png")
            tirador3 = Button(ventana_tiradores, image=rodrygo_img, bg="white", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Real Madrid", "Rodrygo Goes"))
            tirador3.place(x=380, y=300)

            rma_label = Label(ventana_tiradores, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black",
                              fg="white")
            rma_label.place(x=570, y=350)

        if equipo1 == "Inter de Milan":
            lautaro_img = PhotoImage(file="lautaro.png")
            tirador1 = Button(ventana_tiradores, image=lautaro_img, width=150, bg="blue", fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Lautaro Martínez"))
            tirador1.place(x=50, y=70)

            calhanoglu_img = PhotoImage(file="calhanoglu.png")
            tirador2 = Button(ventana_tiradores, image=calhanoglu_img, bg="blue", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu"))
            tirador2.place(x=210, y=70)

            alexis_img = PhotoImage(file="alexis.png")
            tirador3 = Button(ventana_tiradores, image=alexis_img, bg="blue", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Alexis Sánchez"))
            tirador3.place(x=380, y=70)

            inter_label = Label(ventana_tiradores, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"),
                                bg="black", fg="blue")
            inter_label.place(x=570, y=140)

        if equipo2 == "Inter de Milan":
            lautaro_img = PhotoImage(file="lautaro.png")
            tirador1 = Button(ventana_tiradores, image=lautaro_img, width=150, bg="blue", fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Lautaro Martínez"))
            tirador1.place(x=50, y=300)

            calhanoglu_img = PhotoImage(file="calhanoglu.png")
            tirador2 = Button(ventana_tiradores, image=calhanoglu_img, bg="blue", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu"))
            tirador2.place(x=210, y=300)

            alexis_img = PhotoImage(file="alexis.png")
            tirador3 = Button(ventana_tiradores, image=alexis_img, bg="blue", width=155, fg="black",
                              command=lambda: seleccionar_tiradores("Inter de Milan", "Alexis Sánchez"))
            tirador3.place(x=380, y=300)

            inter_label = Label(ventana_tiradores, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"),
                                bg="black", fg="blue")
            inter_label.place(x=570, y=350)

        def mover_flecha_tiradores(event):
            global flecha_x, flecha_y

            if flecha_activa_tiradores:
                coords_flecha = canvas_tiradores.coords(flecha_equipos)
                # Potenciometro
                if event.keysym == 'Left':
                    if coords_flecha[0] <= 120:
                        if coords_flecha[1] > 40:
                            canvas_tiradores.move(flecha_equipos, 330, -480)
                            canvas_tiradores.itemconfig(flecha_equipos, image=flecha_img_equipos)
                    else:
                        canvas_tiradores.move(flecha_equipos, -165, 0)
                elif event.keysym == 'Right':
                    if coords_flecha[0] >= 450:
                        if coords_flecha[1] <= 460:
                            canvas_tiradores.move(flecha_equipos, -330, 480)
                            canvas_tiradores.itemconfig(flecha_equipos, image=flecha_equipos_up)
                    else:
                        canvas_tiradores.move(flecha_equipos, 165, 0)

                # Boton potenciometro
                elif event.keysym == 'Return':
                    x_flecha, y_flecha = canvas_tiradores.coords(flecha_equipos)
                    if equipo1 == "Liverpool":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_tiradores("Liverpool", "Mohamed Salah")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_tiradores("Liverpool", "Darwin Núñez")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_tiradores("Liverpool", "Lucho Diaz")
                    if equipo1 == "Real Madrid":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_tiradores("Real Madrid", "Jude Bellingham")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_tiradores("Real Madrid", "Vinicius Jr")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_tiradores("Real Madrid", "Rodrygo Goes")
                    if equipo1 == "Inter de Milan":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_tiradores("Inter de Milan", "Lautaro Martínez")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_tiradores("Inter de Milan", "Alexis Sánchez")

                        # Equipos 2
                    if equipo2 == "Liverpool":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_tiradores("Liverpool", "Mohamed Salah")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_tiradores("Liverpool", "Darwin Núñez")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_tiradores("Liverpool", "Lucho Diaz")
                    if equipo2 == "Real Madrid":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_tiradores("Real Madrid", "Jude Bellingham")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_tiradores("Real Madrid", "Vinicius Jr")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_tiradores("Real Madrid", "Rodrygo Goes")
                    if equipo2 == "Inter de Milan":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_tiradores("Inter de Milan", "Lautaro Martínez")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_tiradores("Inter de Milan", "Hakan Calhanoglu")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_tiradores("Inter de Milan", "Alexis Sánchez")

        ventana_tiradores.bind('<Key>', mover_flecha_tiradores)
        ventana_tiradores.bind('<Return>', mover_flecha_tiradores)

        flecha_equipos_up = PhotoImage(file="flecha_equipos_up.png")
        flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
        flecha_equipos = canvas_tiradores.create_image(120, 40, image=flecha_img_equipos)

        ventana_tiradores.mainloop()

    def seleccion_porteros_juego():
        global equipo1, equipo2, jugadores_rmaP, jugadores_intP, jugadores_livP
        ventana_porteros = Toplevel(window)
        ventana_porteros.config(bg="black")
        ventana_porteros.geometry("800x550+30+30")
        ventana_porteros.title("Selección de Porteros")
        ventana_porteros.focus_set()
        jugadores_livP = 0
        jugadores_rmaP = 0
        jugadores_intP = 0

        canvas_porteros = Canvas(ventana_porteros, width=800, height=550, bg="black")
        canvas_porteros.pack()
        fondo_jugadores = PhotoImage(file="fondo_jugadores.png")
        canvas_porteros.create_image(0, 0, image=fondo_jugadores, anchor="nw")
        tiradores_label = Label(ventana_porteros, text="Selecciona los porteros", font=("pagoda-bolditalic", 20, "bold"), bg="black", fg="white")
        tiradores_label.place(x=500, y=5)

        def seleccionar_porteros(equipo, nombre_portero):
            global jugadores_rmaP, jugadores_intP, jugadores_livP, porteros_liv, porteros_int, porteros_rma

            if equipo == "Liverpool" and jugadores_livP < 1:
                porteros_liv["Portero"] = nombre_portero
                jugadores_livP += 1
                print("Equipo:", equipo)
                print("Portero seleccionado:", nombre_portero)
            elif equipo == "Real Madrid" and jugadores_rmaP < 1:
                porteros_rma["Portero"] = nombre_portero
                jugadores_rmaP += 1
                print("Equipo:", equipo)
                print("Portero seleccionado:", nombre_portero)
            elif equipo == "Inter de Milan" and jugadores_intP < 1:
                porteros_int["Portero"] = nombre_portero
                jugadores_intP += 1
                print("Equipo:", equipo)
                print("Portero seleccionado:", nombre_portero)

            if jugadores_intP == 1 and jugadores_rmaP == 1:
                ventana_porteros.destroy()
                crear_ventana_juego(equipo_tira, equipo_ataja)
            elif jugadores_rmaP == 1 and jugadores_livP == 1:
                ventana_porteros.destroy()
                crear_ventana_juego(equipo_tira, equipo_ataja)
            elif jugadores_livP == 1 and jugadores_intP == 1:
                ventana_porteros.destroy()
                crear_ventana_juego(equipo_tira, equipo_ataja)

        if equipo1 == "Liverpool":
            alisson_img = PhotoImage(file="alisson.png")
            portero1 = Button(ventana_porteros, image=alisson_img, width=150, bg="red", fg="black",
                              command=lambda: seleccionar_porteros("Liverpool", "Alisson Becker"))
            portero1.place(x=50, y=70)

            kelleher_img = PhotoImage(file="kelleher.png")
            portero2 = Button(ventana_porteros, image=kelleher_img, bg="red", width=150, fg="black",
                              command=lambda: seleccionar_porteros("Liverpool", "Caoimhín Kelleher"))
            portero2.place(x=215, y=70)

            adrian_img = PhotoImage(file="adrian.png")
            portero3 = Button(ventana_porteros, image=adrian_img, bg="red", fg="black",
                              command=lambda: seleccionar_porteros("Liverpool", "Adrian San Miguel"))
            portero3.place(x=385, y=70)

            liv_label = Label(ventana_porteros, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black",
                              fg="red")
            liv_label.place(x=570, y=140)

        if equipo2 == "Liverpool":
            alisson_img = PhotoImage(file="alisson.png")
            portero1 = Button(ventana_porteros, image=alisson_img, width=150, bg="red", fg="white",
                              command=lambda: seleccionar_porteros("Liverpool", "Alisson Becker"))
            portero1.place(x=50, y=280)

            kelleher_img = PhotoImage(file="kelleher.png")
            portero2 = Button(ventana_porteros, image=kelleher_img, bg="red", width=150, fg="white",
                              command=lambda: seleccionar_porteros("Liverpool", "Caoimhín Kelleher"))
            portero2.place(x=215, y=280)

            adrian_img = PhotoImage(file="adrian.png")
            portero3 = Button(ventana_porteros, image=adrian_img, bg="red", fg="white", command=lambda: seleccionar_porteros("Liverpool", "Adrian San Miguel"))
            portero3.place(x=385, y=280)

            liv_label = Label(ventana_porteros, text="Liverpool", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="red")
            liv_label.place(x=570, y=350)

        if equipo1 == "Real Madrid":
            courtois_img = PhotoImage(file="courtois.png")
            portero1 = Button(ventana_porteros, image=courtois_img, width=155, bg="white", fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Thibaut Courtois"))
            portero1.place(x=50, y=70)

            lunin_img = PhotoImage(file="lunin.png")
            portero2 = Button(ventana_porteros, image=lunin_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Andriy Lunin"))
            portero2.place(x=220, y=70)

            kepa_img = PhotoImage(file="kepa.png")
            portero3 = Button(ventana_porteros, image=kepa_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga"))
            portero3.place(x=390, y=70)

            rma_label = Label(ventana_porteros, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="white")
            rma_label.place(x=570, y=140)

        if equipo2 == "Real Madrid":
            courtois_img = PhotoImage(file="courtois.png")
            portero1 = Button(ventana_porteros, image=courtois_img, width=155, bg="white", fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Thibaut Courtois"))
            portero1.place(x=50, y=280)

            lunin_img = PhotoImage(file="lunin.png")
            portero2 = Button(ventana_porteros, image=lunin_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Andriy Lunin"))
            portero2.place(x=220, y=280)

            kepa_img = PhotoImage(file="kepa.png")
            portero3 = Button(ventana_porteros, image=kepa_img, bg="white", width=155, fg="white", command=lambda: seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga"))
            portero3.place(x=390, y=280)

            rma_label = Label(ventana_porteros, text="Real Madrid", font=("pagoda-bolditalic", 35, "bold"), bg="black", fg="white")
            rma_label.place(x=570, y=350)

        if equipo1 == "Inter de Milan":
            sommer_img = PhotoImage(file="sommer.png")
            portero1 = Button(ventana_porteros, image=sommer_img, width=150, bg="blue", fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Yann Sommer"))
            portero1.place(x=50, y=70)

            digennaro_img = PhotoImage(file="digennaro.png")
            portero2 = Button(ventana_porteros, image=digennaro_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro"))
            portero2.place(x=210, y=70)

            audero_img = PhotoImage(file="audero.png")
            portero3 = Button(ventana_porteros, image=audero_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Emil Audero"))
            portero3.place(x=380, y=70)

            inter_label = Label(ventana_porteros, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black", fg="blue")
            inter_label.place(x=570, y=140)

        if equipo2 == "Inter de Milan":
            sommer_img = PhotoImage(file="sommer.png")
            portero1 = Button(ventana_porteros, image=sommer_img, width=150, bg="blue", fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Yann Sommer"))
            portero1.place(x=50, y=280)

            digennaro_img = PhotoImage(file="digennaro.png")
            portero2 = Button(ventana_porteros, image=digennaro_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro"))
            portero2.place(x=210, y=280)

            audero_img = PhotoImage(file="audero.png")
            portero3 = Button(ventana_porteros, image=audero_img, bg="blue", width=155, fg="white", command=lambda: seleccionar_porteros("Inter de Milan", "Emil Audero"))
            portero3.place(x=380, y=280)

            inter_label = Label(ventana_porteros, text="Inter de Milan", font=("pagoda-bolditalic", 30, "bold"), bg="black", fg="blue")
            inter_label.place(x=570, y=350)

        def mover_flecha_porteros(event):
            global flecha_x, flecha_y

            if flecha_activa_tiradores:
                coords_flecha = canvas_porteros.coords(flecha_equipos)
                # Potenciometro
                if event.keysym == 'Left':
                    if coords_flecha[0] <= 120:
                        if coords_flecha[1] > 40:
                            canvas_porteros.move(flecha_equipos, 330, -480)
                            canvas_porteros.itemconfig(flecha_equipos, image=flecha_img_equipos)
                    else:
                        canvas_porteros.move(flecha_equipos, -165, 0)
                elif event.keysym == 'Right':
                    if coords_flecha[0] >= 450:
                        if coords_flecha[1] <= 460:
                            canvas_porteros.move(flecha_equipos, -330, 480)
                            canvas_porteros.itemconfig(flecha_equipos, image=flecha_equipos_up)
                    else:
                        canvas_porteros.move(flecha_equipos, 165, 0)

                # Boton potenciometro
                elif event.keysym == 'Return':
                    x_flecha, y_flecha = canvas_porteros.coords(flecha_equipos)
                    if equipo1 == "Liverpool":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_porteros("Liverpool", "Alisson Becker")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_porteros("Liverpool", "Caoimhin Kelleher")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_porteros("Liverpool", "Adrian")
                    if equipo1 == "Real Madrid":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_porteros("Real Madrid", "Thibaut Courtois")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_porteros("Real Madrid", "Andriy Lunin")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga")
                    if equipo1 == "Inter de Milan":
                        if 50 < x_flecha < 200 and y_flecha < 250:
                            seleccionar_porteros("Inter de Milan", "Yann Sommer")
                        elif 190 < x_flecha < 360 and y_flecha < 250:
                            seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro")
                        elif 385 < x_flecha < 550 and y_flecha < 250:
                            seleccionar_porteros("Inter de Milan", "Emil Audero")

                        # Equipos 2
                    if equipo2 == "Liverpool":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_porteros("Liverpool", "Alisson Becker")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_porteros("Liverpool", "Caoimhin Kelleher")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_porteros("Liverpool", "Adrian")
                    if equipo2 == "Real Madrid":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_porteros("Real Madrid", "Thibaut Courtois")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_porteros("Real Madrid", "Andriy Lunin")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_porteros("Real Madrid", "Kepa Arrizabalaga")
                    if equipo2 == "Inter de Milan":
                        if 50 < x_flecha < 200 and y_flecha > 250:
                            seleccionar_porteros("Inter de Milan", "Yann Sommer")
                        elif 190 < x_flecha < 360 and y_flecha > 250:
                            seleccionar_porteros("Inter de Milan", "Raffaele Di Gennaro")
                        elif 385 < x_flecha < 550 and y_flecha > 250:
                            seleccionar_porteros("Inter de Milan", "Emil Audero")

        ventana_porteros.bind('<Key>', mover_flecha_porteros)
        ventana_porteros.bind('<Return>', mover_flecha_porteros)

        flecha_equipos_up = PhotoImage(file="flecha_equipos_up.png")
        flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
        flecha_equipos = canvas_porteros.create_image(120, 40, image=flecha_img_equipos)

        ventana_porteros.mainloop()

    def madrid_gana():
        global lista_eq2, lista_eq1

        ventana_madrid = Toplevel(window)
        ventana_madrid.config(bg="black")
        ventana_madrid.geometry("1005x600+40+40")
        ventana_madrid.title("REAL MADRID GANA")
        ventana_madrid.focus_set()

        lista_eq2 = []
        lista_eq1 = []

        canvas_juego = Canvas(ventana_madrid, width=1005, height=600)
        canvas_juego.pack()
        fondo = PhotoImage(file="madrid_gana.png")
        canvas_juego.create_image(0, 0, image=fondo, anchor="nw")
        madrid_campeon = PhotoImage(file="madrid_campeon.png")
        canvas_juego.create_image(70, 100, image=madrid_campeon, anchor="nw")

        mixer.music.load("gana_madrid.mp3")
        mixer.music.play()
        ventana_madrid.after(20000, lambda: [ventana_madrid.destroy(), menu_sound.play(1)])

        ventana_madrid.mainloop()

    def liverpool_gana():
        global lista_eq2, lista_eq1
        ventana_liverpool = Toplevel(window)
        ventana_liverpool.config(bg="black")
        ventana_liverpool.geometry("1005x600+40+40")
        ventana_liverpool.title("LIVERPOOL GANA")
        ventana_liverpool.focus_set()

        lista_eq2 = []
        lista_eq1 = []
        canvas_juego = Canvas(ventana_liverpool, width=1005, height=600)
        canvas_juego.pack()
        fondo = PhotoImage(file="liverpool_gana.png")
        canvas_juego.create_image(0, 0, image=fondo, anchor="nw")
        canvas_juego.create_text(100, 40, text="LIVERPOOL CAMPEON", anchor="nw", font=("pagoda-bolditalic", 70, "bold"), fill="white")

        mixer.music.load("liverpool_gana.mp3")
        mixer.music.play()
        ventana_liverpool.after(27000, lambda: [ventana_liverpool.destroy(), menu_sound.play(1)])

        ventana_liverpool.mainloop()

    def inter_gana():
        global lista_eq2, lista_eq1
        ventana_inter = Toplevel(window)
        ventana_inter.config(bg="black")
        ventana_inter.geometry("1005x600+40+40")
        ventana_inter.title("INTER DE MILAN GANA")
        ventana_inter.focus_set()

        lista_eq2 = []
        lista_eq1 = []

        canvas_juego = Canvas(ventana_inter, width=1005, height=600)
        canvas_juego.pack()
        fondo = PhotoImage(file="int_gana.png")
        canvas_juego.create_image(0, 0, image=fondo, anchor="nw")
        int_campeon = PhotoImage(file="int_campeon.png")
        canvas_juego.create_image(70, 40, image=int_campeon, anchor="nw")

        mixer.music.load("int_gana.mp3")
        mixer.music.play()
        ventana_inter.after(16000, lambda: [ventana_inter.destroy(), menu_sound.play(1)])


        ventana_inter.mainloop()


    def final():
        global tiros_eq2, tiros_eq1, lista_eq2, lista_eq1

        mixer.music.stop()
        unos_eq1 = lista_eq1.count(1)
        unos_eq2 = lista_eq2.count(1)
        if unos_eq1 > unos_eq2:
            if equipo1 == "Liverpool":
                print("Ha ganado", equipo1)
                ventana_juego.destroy()
                liverpool_gana()
            if equipo1 == "Real Madrid":
                print("Ha ganado", equipo1)
                ventana_juego.destroy()
                madrid_gana()
            if equipo1 == "Inter de Milan":
                print("Ha ganado", equipo1)
                ventana_juego.destroy()
                inter_gana()
        elif unos_eq1 < unos_eq2:
            if equipo2 == "Liverpool":
                print("Ha ganado", equipo2)
                ventana_juego.destroy()
                liverpool_gana()
            elif equipo2 == "Real Madrid":
                print("Ha ganado", equipo2)
                ventana_juego.destroy()
                madrid_gana()
            elif equipo2 == "Inter de Milan":
                print("Ha ganado", equipo2)
                ventana_juego.destroy()
                inter_gana()







    marcador1(canvas_juego, lista_eq1, coordenadas_goles_eq1)
    marcador2(canvas_juego, lista_eq2, coordenadas_goles_eq2)


    ventana_juego.mainloop()




    intercambiar_roles(equipo_ataja, equipo_tira)

def intercambiar_roles(equipo_ataja, equipo_tira):
    global ventana_juego
    equipo_tira, equipo_ataja = equipo_ataja, equipo_tira
    ventana_juego.after(3000, lambda: cambiar_ventana(equipo_tira, equipo_ataja))


def cambiar_ventana(equipo_tira, equipo_ataja):
    ventana_juego.destroy()
    crear_ventana_juego(equipo_tira, equipo_ataja)






def informacion():
    ventana_info = Toplevel(window)
    ventana_info.config(bg="black")
    ventana_info.geometry("660x500+30+30")
    ventana_info.title("About")
    ventana_info.focus_set()

    canvas_info = Canvas(ventana_info, width=660, height=500, bg="black")
    canvas_info.pack()
    fondo_info = PhotoImage(file="fondo_jugadores.png")
    canvas_info.create_image(0, 0, image=fondo_info, anchor="nw")
    canvas_info.create_text(320, 20, text="Fundamentos de Sistemas Computacionales", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 80, text="Steven Loaiza Aguirre", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 120, text="2024182376", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 180, text="Jean Carlo Medaglia Quirós", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 220, text="2024062836", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 280, text="2024", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 340, text="Version: Alpha", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")
    canvas_info.create_text(320, 380, text="Alpha 1.0", anchor="n", font=("pagoda-bolditalic", 20, "bold"), fill="white")

    def vent_estadisticas(equipo):
        global tiros_vinicius, tiros_diaz, tiros_jude, tiros_rodrygo, tiros_salah, tiros_darwin, tiros_alexis, tiros_calhanoglu, tiros_lautaro, goles_vinicius, goles_diaz, goles_jude, goles_rodrygo, goles_salah, goles_darwin, goles_alexis, goles_calhanoglu, goles_lautaro, tiros, goles
        ventana = Toplevel(window)
        ventana.config(bg="black")
        ventana.geometry("800x400+30+30")
        ventana.title("Estadisticas")
        ventana.focus_set()

        def reiniciar_estadisticas():
            nonlocal equipo
            global tiros_vinicius, tiros_diaz, tiros_jude, tiros_rodrygo, tiros_salah, tiros_darwin, tiros_alexis, tiros_calhanoglu, tiros_lautaro
            global goles_vinicius, goles_diaz, goles_jude, goles_rodrygo, goles_salah, goles_darwin, goles_alexis, goles_calhanoglu, goles_lautaro

            tiros_vinicius = tiros_diaz = tiros_jude = tiros_rodrygo = tiros_salah = tiros_darwin = tiros_alexis = tiros_calhanoglu = tiros_lautaro = 0
            goles_vinicius = goles_diaz = goles_jude = goles_rodrygo = goles_salah = goles_darwin = goles_alexis = goles_calhanoglu = goles_lautaro = 0
            ventana.destroy()
            vent_estadisticas(equipo)

            if equipo == "Liverpool":
                canvas_est.itemconfig(tiros, text=f"Tiros: {tiros_liv}", font=("pagoda-bolditalic", 20, "bold"),fill="white")
                canvas_est.itemconfig(goles, text=f"Goles: {goles_liv}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            elif equipo == "Real Madrid":
                canvas_est.itemconfig(tiros, text=f"Tiros: {tiros_rma}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
                canvas_est.itemconfig(goles, text=f"Goles: {goles_rma}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            elif equipo == "Inter de Milan":
                canvas_est.itemconfig(tiros, text=f"Tiros: {tiros_int}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
                canvas_est.itemconfig(goles, text=f"Goles: {goles_int}", font=("pagoda-bolditalic", 20, "bold"), fill="white")

        liv_img = PhotoImage(file="liv_logo.png")
        rma_img = PhotoImage(file="madrid_logo.png")
        int_img = PhotoImage(file="int_logo.png")

        tiros_liv = tiros_diaz + tiros_salah + tiros_darwin
        goles_liv = goles_darwin + goles_salah + goles_diaz

        tiros_rma = tiros_vinicius + tiros_jude + tiros_rodrygo
        goles_rma = goles_vinicius + goles_jude + goles_rodrygo

        tiros_int = tiros_alexis + tiros_calhanoglu + tiros_lautaro
        goles_int = goles_calhanoglu + goles_alexis + goles_lautaro

        canvas_est = Canvas(ventana, width=800, height=400, bg="black")
        canvas_est.pack()



        if equipo == "Liverpool":
            canvas_est.create_image(30, 40, image=liv_img, anchor="nw")
            tiros = canvas_est.create_text(400, 100, text=f"Tiros: {tiros_liv}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            goles = canvas_est.create_text(400, 200, text=f"Goles: {goles_liv}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            reiniciar_estadisticas = Button(canvas_est, text="Reiniciar", bg="red", fg="white", height=1, width=10, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=reiniciar_estadisticas)
            reiniciar_estadisticas.place(x=50, y=320)
        elif equipo == "Real Madrid":
            canvas_est.create_image(30, 40, image=rma_img, anchor="nw")
            tiros = canvas_est.create_text(400, 100, text=f"Tiros: {tiros_rma}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            goles = canvas_est.create_text(400, 200, text=f"Goles: {goles_rma}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            reiniciar_estadisticas = Button(canvas_est, text="Reiniciar", bg="red", fg="white", height=1, width=10, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=reiniciar_estadisticas)
            reiniciar_estadisticas.place(x=50, y=320)
        elif equipo == "Inter de Milan":
            canvas_est.create_image(30, 40, image=int_img, anchor="nw")
            tiros = canvas_est.create_text(400, 100, text=f"Tiros: {tiros_int}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            goles = canvas_est.create_text(400, 200, text=f"Goles: {goles_int}", font=("pagoda-bolditalic", 20, "bold"), fill="white")
            reiniciar_estadisticas = Button(canvas_est, text="Reiniciar", bg="red", fg="white", height=1, width=10, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=reiniciar_estadisticas)
            reiniciar_estadisticas.place(x=50, y=320)
        ventana.mainloop()


    def vent_equipos_est():
        global flecha_activa_equipos
        flecha_activa_equipos = True
        seleccionando_equipo = 1

        def seleccionar_equipo(eq):
            global equipo1
            nonlocal seleccionando_equipo
            if seleccionando_equipo == 1:
                equipo1 = eq
                print("Equipo:", eq)
                ventana.destroy()
                vent_estadisticas(eq)





        ventana = Toplevel(window)
        ventana.config(bg="black")
        ventana.geometry("800x400+30+30")
        ventana.title("Selección de equipos")
        ventana.focus_set()

        canvas_ventana = Canvas(ventana, width=800, height=400)
        canvas_ventana.pack()
        fondo = PhotoImage(file="fondo_seleccion.png")
        canvas_ventana.create_image(-50, 0, image=fondo, anchor="nw")

        # Seleccion Madrid
        madrid_logo = PhotoImage(file="madrid_logo.png")
        boton_madrid = Button(ventana, bg="white", width=190, height=210, image=madrid_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Real Madrid"))
        boton_madrid.place(x=50, y=100)

        # Seleccion Liverpool
        liv_logo = PhotoImage(file="liv_logo.png")
        boton_liv = Button(ventana, bg="red", width=190, height=210, image=liv_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Liverpool"))
        boton_liv.place(x=300, y=100)

        # Seleccion Inter de Milan
        int_logo = PhotoImage(file="int_logo.png")
        boton_int = Button(ventana, bg="blue", width=190, height=210, image=int_logo, relief="raised", borderwidth=8, cursor="hand2", command=lambda: seleccionar_equipo("Inter de Milan"))
        boton_int.place(x=550, y=100)

        def mover_flecha_equipos(event):
            global flecha_x, flecha_y

            if flecha_activa_equipos:
                coord_flecha = canvas_ventana.coords(flecha_equipos)
                if event.keysym == 'Left' and coord_flecha[0] > 155:
                    canvas_ventana.move(flecha_equipos, -250, 0)
                elif event.keysym == 'Right' and coord_flecha[0] < 655:
                    canvas_ventana.move(flecha_equipos, 250, 0)
                elif event.keysym == 'Return':
                    x_flecha, y_flecha = canvas_ventana.coords(flecha_equipos)
                    if x_flecha < 200:
                        seleccionar_equipo("Real Madrid")
                    elif 200 <= x_flecha < 450:
                        seleccionar_equipo("Liverpool")
                    elif x_flecha >= 450:
                        seleccionar_equipo("Inter de Milan")

        ventana.bind('<Key>', mover_flecha_equipos)
        ventana.bind('<Return>', mover_flecha_equipos)

        flecha_img_equipos = PhotoImage(file="flecha_equipos.png")
        flecha_equipos = canvas_ventana.create_image(155, 50, image=flecha_img_equipos)

        ventana.mainloop()


    boton_estadisticas = Button(canvas_info, text="Estadísticas", bg="red", fg="white", height=1, width=10, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=vent_equipos_est)
    boton_estadisticas.place(x=50, y=420)


# Botón Iniciar
boton_iniciar = Button(canvas_principal, text="Jugar", bg="red", fg="white", height=1, width=7, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=lambda: iniciar_seleccion_equipos(window))
boton_iniciar.place(x=620, y=250)

#Boton Opciones
boton_opciones = Button(canvas_principal, text="About",  bg="red", fg="white", height=1, width=9, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", cursor="hand2", command=informacion)
boton_opciones.place(x=606, y=360)

# Botón Salir
boton_salir = Button(canvas_principal, text="Salir",  bg="red", fg="white", height=1, width=7, font=("pagoda-bolditalic", 23, "bold"), pady=1, bd=5, activebackground="white", command= window.destroy, cursor="pirate")
boton_salir.place(x=620, y=470)



def mover_flecha_menu(event):
    global flecha_x, flecha_y

    if flecha_activa:
        coords_flecha = canvas_principal.coords(flecha)
        if event.keysym == 'Up' and coords_flecha[1] > 275:
            canvas_principal.move(flecha, 0, -112)
        elif event.keysym == 'Down' and coords_flecha[1] < 499:
            canvas_principal.move(flecha, 0, 112)
        elif event.keysym == 'Return':
            x_flecha, y_flecha = canvas_principal.coords(flecha)

            posiciones_botones = [(620, 250), (606, 360), (620, 470)]

            distancias = []
            for pos_x, pos_y in posiciones_botones:
                distancia = ((x_flecha - pos_x) ** 2 + (y_flecha - pos_y) ** 2) ** 0.5
                distancias.append(distancia)

            indice_bot_cercano = distancias.index(min(distancias))

            if indice_bot_cercano == 0:
                boton_iniciar.invoke()
            elif indice_bot_cercano == 1:
                boton_opciones.invoke()
            elif indice_bot_cercano == 2:
                boton_salir.invoke()


flecha_img = PhotoImage(file="flecha.png")
flecha = canvas_principal.create_image(570, 275, image=flecha_img)

window.bind('<Key>', mover_flecha_menu)
window.bind('<Return>', mover_flecha_menu)


window.mainloop()
