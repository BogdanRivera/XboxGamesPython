"""
Este programa resuelve de una lista de juegos de Xbox aquellos que
han sido jugados de 100 a 120 horas con Pandas
"""
import pandas as pd
import graph 




def run():
    df = pd.read_csv("./DataXbox.csv")
    df = df[df['TIME'] == '100-120 hours']
    



if __name__=="__main__":
    run()