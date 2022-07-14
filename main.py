from tkinter import colorchooser
import graphviz
import mysql

from config import *

import src.RXNormVisualize as viz

from datetime import datetime

def main():
    # connect to database, return connection
    connection = viz.connect(
        host = mysql_host,
        database = mysql_database,
        user = mysql_username,
        password = mysql_password)

    relations_queries = viz.get_relations_queries(CUIs)
    relations_results = viz.send_relations_queries(relations_queries, connection)
    get_strings_dic = viz.get_strings_dic(relations_results, connection)

    stop_letters = None

    for i in range(len(relations_results)):
        print(f"> Creating graph {i+1}...")
        gra = graphviz.Digraph(format="png", node_attr={"colorscheme" : "gnbu9", "style" : "filled"})
        gra.node(str(i), str(relations_results[i][0][0])+'\n'+str(get_strings_dic[relations_results[i][0][0]])[:stop_letters])
        for j in range(len(relations_results[i])):
            gra.node(f"{i}{j}", str(relations_results[i][j][2])+'\n'+str(get_strings_dic[relations_results[i][j][2]])[:stop_letters])
            gra.edge(str(i), f"{i}{j}", label=str(relations_results[i][j][1]))
        gra = gra.unflatten(stagger=10)
        gra.render(image_save_path + f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{relations_results[i][0][0]}')

    # will disconnect the connection
    viz.disconnect(connection)

if __name__ == "__main__":
    main()