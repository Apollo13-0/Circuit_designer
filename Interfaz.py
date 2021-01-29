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

global primerPos, primerObjBoole, segundObjBoole, segundPos
primerObjBoole = False
segundObjBoole = False

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


        self.__graph_canva.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.__graph_canva.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.__graph_canva.tag_bind("movil", "<ButtonPress-3>", self.presion_union)
        self.__graph_canva.tag_bind("movil", "<ButtonPress-2>", self.cambioNombre)

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

        BotonFuente = Button(self.__main_screen, text="Fuente", font=font2, bg=deep_sea,
                            activeforeground=dark_tangerine, command=self.crearFuente)
        BotonFuente.place(x=20, y=430, width=260, height=50)

        mainloop()

    def cambioNombre(self, evento):
        MiniInterfaz()

    def crearResistencia(self):
        self.__graph_canva.create_rectangle(550, 550, 610, 610, fill=brown, outline=brown, tags="movil")

    def crearFuente(self):
        self.__graph_canva.create_oval(530, 530, 600, 600, outline=dark_tangerine, fill=dark_tangerine, width=2, tags="movil")

    def crearLinea(self, pos1, pos2):
        self.__graph_canva.create_line(pos1[0],pos1[1],pos2[0],pos2[1],fill="#000000",width=15, tags="linea")
        global primerPos, segundObjBoole, primerObjBoole,segundPos
        primerObjBoole = None
        segundObjBoole = None
        primerPos = None
        segundPos = None


    def presion_union(self,evento):
        carta = self.__graph_canva.find_withtag(CURRENT)
        #self.carta_seleccionada = (carta, evento.x, evento.y)
        global primerObjBoole, segundObjBoole, primerPos, segundPos
        if primerObjBoole:
            segundObjBoole = True
            segundPos = (evento.x, evento.y)
            self.crearLinea(primerPos,segundPos)
        else:
            primerObjBoole = True
            primerPos = (evento.x, evento.y)


    def presion_boton(self, evento):
        carta = self.__graph_canva.find_withtag(CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        carta, x1, y1 = self.carta_seleccionada
        self.__graph_canva.move(carta, x - x1, y - y1)
        self.carta_seleccionada = (carta, x, y)

    def fijar(self,evento):
        carta = self.__graph_canva.find_withtag(CURRENT)
        self.carta_seleccionada = (carta, evento.x, evento.y)
        self.carta_seleccionada.carta

    def mover_Elemento(self, evento):
        print(str(evento.x)+" "+str(evento.y))

class MiniInterfaz:
    def __init__(self):
        self.__size_x = 500
        self.__size_y = 400

        self.__name_screen = Tk()
        self.__name_screen.title("Insertar nombre")
        self.__name_screen.geometry("500x400+200+200")
        self.__name_screen.resizable(0, 0)

        self.__name_canva = Canvas(self.__name_screen, width=self.__size_x, height=self.__size_y, bg=white,
                                    highlightbackground=white)
        self.__name_canva.pack()

        namelabel = Label(self.__name_screen, text="Inserte nombre y valor", font=font3, fg=tiber, bg=tiber)
        namelabel.place(x=320, y=750)
        # disp_var.set("Displacement: " + str(thrustSim.thrust))

        # Entry

        mass_entry = Entry(self.__name_screen, font=font2, bd=3)
        mass_entry.place(x=20, y=200, width=260, height=50)
