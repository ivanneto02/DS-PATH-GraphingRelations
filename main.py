import graphviz
import mysql

from config import *

import src.RXNormVisualize as viz

def main():
    # connect to database, return connection
    connection = viz.connect(
        host = mysql_host,
        database = mysql_database,
        user = mysql_username,
        password = mysql_password)

    queries = viz.get_queries(CUIs)
    results = viz.send_queries(queries, connection)

    # # Printing out the results
    # for i in range(len(results)):
    #     print(f"Printing result {i}...")
    #     for row in results[i][:LIMIT_ROWS]:
    #         print(row)

    for i in range(len(results)):
        gra = graphviz.Digraph()
        gra.node(i, results[i][0])
        # Create graph

    # will disconnect the connection
    viz.disconnect(connection)

if __name__ == "__main__":
    main()