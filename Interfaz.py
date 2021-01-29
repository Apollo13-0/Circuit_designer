# import modules

from tkinter import *
from tkinter import messagebox

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
    Es la clase encargada del manejo de toda la interfaz y eventos del raton y teclado
    """

    def __init__(self):
        """
        Es el constructor de la clase Interfaz, genera la ventana y asiga las funciones a cada boton
        """

        self.__size_x = 1200
        self.__size_y = 800

        self.__main_screen = Tk()
        self.__main_screen.title("Diseño de circuitos")
        self.__main_screen.geometry("1200x800+100+100")
        self.__main_screen.resizable(0, 0)


        self.__graph_canva = Canvas(self.__main_screen, width=self.__size_x, height=self.__size_y, bg=white,
                                    highlightbackground=white)
        self.__graph_canva.pack()

        self.__graph_canva.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
        self.__graph_canva.tag_bind("movil", "<Button1-Motion>", self.mover)
        self.__graph_canva.tag_bind("movil", "<ButtonPress-3>", self.presion_union)
        self.__graph_canva.tag_bind("movil", "<ButtonPress-2>", self.cambioNombre)

        self.ele_seleccionada = None
        # Canvas for inputs

        self.__input_canva = Canvas(self.__main_screen, width=300, height=800, bg=tiber, highlightbackground=tiber)
        self.__input_canva.place(x=0, y=0)

        # Text & lables
        self.__input_canva.create_text(150, 80, text="Diseño" + " \n" + "de circuitos", font=font1, fill=deep_sea)

        # Button

        run_button = Button(self.__main_screen, text="Simular", font=font2, bg=brown, activeforeground=dark_tangerine)
        run_button.place(x=20, y=730, width=260, height=50)

        BotonResis = Button(self.__main_screen, text="Resistencia", font=font2, bg=deep_sea,
                            activeforeground=dark_tangerine, command=self.crearResistencia)
        BotonResis.place(x=20, y=530, width=260, height=50)

        BotonFuente = Button(self.__main_screen, text="Fuente", font=font2, bg=deep_sea,
                             activeforeground=dark_tangerine, command=self.crearFuente)
        BotonFuente.place(x=20, y=430, width=260, height=50)

        mainloop()

    def cambioNombre(self, evento):
        """
        Este metodo se encarga de llamar a otra ventana que solicita en nuevo nombre y valor de la resistencia
        :param evento: event
        :return: ventana de nombre y valor
        """
        MiniInterfaz()

    def crearResistencia(self):
        """
        Crea un objeto que relaciona una resistencia
        :return: un rectangulo que representa una resiostencia
        """
        self.__graph_canva.create_rectangle(550, 550, 610, 610, fill=brown, outline=brown, tags="movil")

    def crearFuente(self):
        """
        Crea un objeto que relaciona una fuente de poder
        :return: crea un circulo que representa la fuente de poder
        """
        self.__graph_canva.create_oval(530, 530, 600, 600, outline=dark_tangerine, fill=dark_tangerine, width=2,
                                       tags="movil")

    def crearLinea(self, pos1, pos2):
        """
        Este metodo se encarga de unir dos elementos con una line, represenando los cables
        :param pos1: posicion del primer elemento
        :param pos2: posicion del segundo elemento
        :return: crea una linea con las coordenada dadas
        """
        self.__graph_canva.create_line(pos1[0], pos1[1], pos2[0], pos2[1], fill="#000000", width=15, tags="linea")
        global primerPos, segundObjBoole, primerObjBoole, segundPos
        primerObjBoole = None
        segundObjBoole = None
        primerPos = None
        segundPos = None

    def presion_union(self, evento):
        """
        Este metodo se encarga de validar la seleecion de dos elementos
        :param evento: event
        :return: en caso de seleccionar dos elementos llama al creador de lineas
        """
        ele = self.__graph_canva.find_withtag(CURRENT)
        global primerObjBoole, segundObjBoole, primerPos, segundPos
        if primerObjBoole:
            segundObjBoole = True
            segundPos = (evento.x, evento.y)
            self.crearLinea(primerPos, segundPos)
        else:
            primerObjBoole = True
            primerPos = (evento.x, evento.y)

    def presion_boton(self, evento):
        """
        este metodo valida que el mouse se encuentra encima del elemento
        :param evento: event
        :return:
        """
        ele = self.__graph_canva.find_withtag(CURRENT)
        self.ele_seleccionada = (ele, evento.x, evento.y)

    def mover(self, evento):
        """
        este metodo se encarga de mover los elementos cuando el mouse lo arrastra
        :param evento: event
        :return:
        """
        x, y = evento.x, evento.y
        ele, x1, y1 = self.ele_seleccionada
        self.__graph_canva.move(ele, x - x1, y - y1)
        self.ele_seleccionada = (ele, x, y)

    def fijar(self, evento):
        """
        este metodo se encarga de fijar el elemento a la ultima posicion donde la carta lo soltó
        :param evento: event
        :return:
        """
        ele = self.__graph_canva.find_withtag(CURRENT)
        self.ele_seleccionada = (ele, evento.x, evento.y)
        self.ele_seleccionada.ele


class MiniInterfaz:
    """
    esta clase se encarga de mostra una pequeña interfaz donde se pueda modificar el nombre y valor de los elementos
    """
    def __init__(self):
        """
        Es el constructor de la clase MiniInterfaz, genera la ventana y asiga las funciones a cada boton
        """
        self.__size_x = 500
        self.__size_y = 400

        self.__name_screen = Tk()
        self.__name_screen.title("Insertar nombre")
        self.__name_screen.geometry("500x400+200+200")
        self.__name_screen.resizable(0, 0)

        self.__name_canva = Canvas(self.__name_screen, width=self.__size_x, height=self.__size_y, bg=deep_sea,
                                   highlightbackground=deep_sea)
        self.__name_canva.pack()

        namelabel = Label(self.__name_screen, text="Inserte nombre y valor", font=font3, fg=tiber, bg=deep_sea)
        namelabel.place(x=80, y=10)

        nameEle = Label(self.__name_screen, text="Nombre", font=font3, fg=dark_tangerine, bg=deep_sea)
        nameEle.place(x=200, y=60)

        name_entry = Entry(self.__name_screen, font=font2, bd=2)
        name_entry.place(x=135, y=100, width=230, height=50)

        valorEle = Label(self.__name_screen, text="Valor", font=font3, fg=dark_tangerine, bg=deep_sea)
        valorEle.place(x=200, y=150)

        v_entry = Entry(self.__name_screen, font=font2, bd=2)
        v_entry.place(x=135, y=190, width=230, height=50)

        save_button = Button(self.__name_screen, text="Guardar", font=font2, bg=brown, activeforeground=dark_tangerine,
                             command=lambda x=name_entry, y=v_entry, z=self.__name_screen: self.saveName(x, y, z))
        save_button.place(x=135, y=260, width=230, height=50)

    def saveName(self, name, valor, ventana):
        """
        este metodo se encarga de guardar el nuevo nombre y valor, ademas notifica al usuario el cambio
        :param name: str
        :param valor: int
        :param ventana: tk()
        :return: messagebox indicando que se guardaron correctamente
        """
        Elemento(name.get(), int(valor.get()))
        messagebox.showinfo(title="Nombre guardado", message="El nombre y el valor han sido guardados exitosamente")
        ventana.destroy()


class Elemento:
    """
    esta clase se encarga de crear elementod de resistencias y fuentes de poder
    """
    num = 1

    def __init__(self, type: str, value: int):
        """
        Es el constructor de la clase almacena la info del elemento
        :param type: str
        :param value: int
        """
        self.id = type + str(Elemento.num)
        self.value = value
        Elemento.num += 1

    def get_id(self):
        """
        retorna el id del elemento
        :return: str
        """
        return self.id

    def get_value(self):
        """
        retorna el valor del elemento
        :return: int
        """
        return self.value
