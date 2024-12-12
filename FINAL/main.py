import tkinter as tk
from cliente.vista import Frame, barra_menu


def main():
    ventana=tk.Tk()
    ventana.title("Listado Peliculas")
    ventana.iconbitmap('img/camaraVideo.ico')
    ventana.resizable(0,0)
    
    barra_menu(ventana)
    app=Frame(root=ventana)

    ventana.mainloop()


if __name__=='__main__':
    main()  