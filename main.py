from tkinter import colorchooser
import graphviz
import mysql

from config import *

import src.RXNormVisualize as viz

from datetime import datetime

def main():
    print("> Starting program")
    viz.visualize(CUIs)
    print("> Ending program")

if __name__ == "__main__":
    main()