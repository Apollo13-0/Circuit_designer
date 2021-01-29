# import modules

from tkinter import *

# Colors

tiber = "#112732"
deep_sea = "#0D7D65"
dark_tangerine = "#FFA618"
brown = "#B49289"
white = "#FFFFFF"

# Fonts

font1 = ("Times", 40)
font2 = ("Times", 25)
font3 = ("System", 25)


class Interfaz:
    """

    """

    def __init__(self):
        """

        """

        self.__size_x = 1200
        self.__size_y = 800

        self.__main_screen = Tk()
        self.__main_screen.title("Diseño de circuitos")
        self.__main_screen.geometry("1200x800+100+100")
        self.__main_screen.resizable(0, 0)


        #self.__main_screen.bind("<Motion>", self.mover_Elemento)



    #def __ventanaPrincipal(self):
        # Canvar for graph

        self.__graph_canva = Canvas(self.__main_screen, width=self.__size_x, height=self.__size_y, bg=white,
                                    highlightbackground=white)
        self.__graph_canva.pack()

        archi1 = PhotoImage(file="resistenciaIMG.png")
        self.__graph_canva.create_image(500, 100, image=archi1, anchor="nw", tags="movil")
        archi2 = PhotoImage(file="fuenteIMG.png")
        self.__graph_canva.create_image(400, 100, image=archi2, anchor="nw", tags="movil")
        self.__graph_canva.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.__graph_canva.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.carta_seleccionada = None
        # Canvas for inputs

        self.__input_canva = Canvas(self.__main_screen, width=300, height=800, bg=tiber, highlightbackground=tiber)
        self.__input_canva.place(x=0, y=0)

        # Text & lables
        self.__input_canva.create_text(150, 80, text="Diseño" + " \n" + "de circuitos", font=font1, fill=deep_sea)

        # Button

        run_button = Button(self.__main_screen, text="Simular", font=font2, bg=brown, activeforeground=dark_tangerine)
        run_button.place(x=20, y=730, width=260, height=50)

        BotonResis = Button(self.__main_screen, text="Resistencia", font=font2, bg=deep_sea, activeforeground=dark_tangerine, command=self.crearResistencia)
        BotonResis.place(x=20, y=530, width=260, height=50)

        mainloop()

    def crearResistencia(self):
        archi3 = PhotoImage(file="resistenciaIMG.png")
        self.__graph_canva.create_image(500, 100, image=archi3, anchor="nw", tags="movil")


    def presion_boton(self, evento):
        carta = self.__graph_canva.find_withtag(CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.__graph_canva.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)

    def mover_Elemento(self, evento):
        print(str(evento.x)+" "+str(evento.y))
