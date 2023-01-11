"""
Este programa resuelve de una lista de juegos de Xbox aquellos que
han sido jugados de 100 a 120 horas con Pandas
"""
import pandas as pd
import graph 
import menu
#GAME, RATIO

def run():
    opc = 0
    df = pd.read_csv("./DataXbox.csv")
    df = df[df['TIME'] == '100-120 hours']
    labels = df['GAME'].values
    values = df['RATIO'].values
    while opc != 3 and opc<3:
        menu.imprime()
        try:
            opc = int(input("Por favor elige una opcion: "))
        except ValueError as error: 
            print(error)
            opc=0
    if opc>=0 and opc<=4:
        if opc==1:
            print(df)
            opc = 0
        elif opc==2:
            x = buscar(df)
            print(x)
            opc = 0  
        elif opc==3:
            graph.generate_bar_chart('Juegos',labels[0:7],values[0:7])
            opc = 0
        else:
            return 
    else:
        opc = 0
            

def buscar(data):
    juego = input("Ingresa el nombre de un juego: ")
    x = data[data['GAME']==juego]
    return x



if __name__=="__main__":
    run()