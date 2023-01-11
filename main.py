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
    juego = input("Ingrese un nombre para buscar: ")
    game = df[df['GAME']==juego]
    if str(game)!="Empty DataFrame":
        print("Ratio:",game['RATIO'].values)
        print("GAMERS:",game['GAMERS'].values)
        print("COMP %:",game['COMP %'].values)
        print("RATING:",game['COMP %'],values)
        print("ADDED:",game['ADDED'].values)
        print("GAMERSCORE:",game['ADDED'].values)
    else:
        print("No se encontró el juego")

    print("Se realizó la gráfica de los tres primeros juegos\n")
    graph.generate_pie_chart('Juegos',labels[0:3],values[0:3])
    




if __name__=="__main__":
    run()