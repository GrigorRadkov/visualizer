import PySimpleGUI as sg
import pygame
import numpy as np
from draw import *
from pygame import *
from bubblesort import *
from quicksort import *

BAR_SPACING, BAR_WIDTH, OFFSET = 12, 10, 5
GRAPH_SIZE = 450

graph_layout = [[sg.Graph(
            canvas_size=(2000, 600),
            graph_bottom_left=(0, 0),
            graph_top_right=(2000, 600),
            key="graph")], [sg.Button('Sort')],
            [sg.T('Speed    Faster'), 
            sg.Slider((0,20), orientation='h', default_value=10, key='-SPEED-'), 
            sg.T('Slower')]]

#graph_layout = [[graph],[sg.T('Speed    Faster'), sg.Slider((0,20), orientation='h', default_value=10, key='-SPEED-'), sg.T('Slower')]]


select_layout = [[sg.Text("Select Algorithm")], [sg.Button("BubbleSort")], [sg.Button("SelectionSort")],
[sg.Button("QuickSort")],[sg.Button("Exit")]]

select_window = sg.Window(title = "Sorting Visualizer", layout = select_layout)

alg_layout = [[sg.Text('Enter array size'), sg.InputText()],
            [sg.Text('Enter max element size'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Close')]]

alg_window = sg.Window(title = "Sorting Visualizer", layout = alg_layout)



def main():
    
    #sg.ChangeLookAndFeel('DarkAmber') Doesnt work????

    while True:

        event, values = select_window.read()
        select_window.Maximize()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "BubbleSort":

            select_window.close()
            event, values = alg_window.read()
            alg_window.Maximize()

            arr_size = int(values[0])
            num_cap = int(values[1])

            if event == "Close" or event == sg.WIN_CLOSED:
                break

            if event == "Ok":
                
                alg_window.close()

                arr = np.random.randint(1, num_cap, arr_size)

                graph_window = sg.Window("Sorting Visualizer", graph_layout, finalize= True)

                graph = graph_window.Element('graph')

                draw_bars(graph, arr, BAR_SPACING, BAR_WIDTH, OFFSET)
                graph_window.Maximize()

                event, values = graph_window.read()

                timeout = 1

                if event == 'Sort':

                    sorted_array = bubblesort(arr)

                    for partially_sorted_array in sorted_array:
                        event, values = graph_window.read(timeout=timeout)
                        if event is None:
                            break
                        graph.Erase()
                        draw_bars(graph, partially_sorted_array, BAR_SPACING, BAR_WIDTH, OFFSET)
                        timeout = int(values['-SPEED-'])

                    sg.popup('Sorted!')
                    #graph_window.close()

                while True:
                    event, values = graph_window.Read()
                    if event in (sg.WIN_CLOSED):
                        break
                

                
                #print(sorted_array)

        if event == "SelectionSort":

            select_window.close()
            event, values = alg_window.read()
            alg_window.Maximize()

            arr_size = int(values[0])
            num_cap = int(values[1])

            if event == "Close" or event == sg.WIN_CLOSED:
                break

            if event == "Ok":
                
                alg_window.close()

                arr = np.random.randint(1, num_cap, arr_size)

                graph_window = sg.Window("Sorting Visualizer", graph_layout, finalize= True)

                graph = graph_window.Element('graph')

                draw_bars(graph, arr, BAR_SPACING, BAR_WIDTH, OFFSET)
                graph_window.Maximize()

                event, values = graph_window.read()

                timeout = 1

                if event == 'Sort':

                    sorted_array = selectionsort(arr)

                    for partially_sorted_array in sorted_array:
                        event, values = graph_window.read(timeout=timeout)
                        if event is None:
                            break
                        graph.Erase()
                        draw_bars(graph, partially_sorted_array, BAR_SPACING, BAR_WIDTH, OFFSET)
                        timeout = int(values['-SPEED-'])

                    sg.popup('Sorted!')
                    #graph_window.close()

                while True:
                    event, values = graph_window.Read()
                    if event in (sg.WIN_CLOSED):
                        break

        if event == "QuickSort":

            select_window.close()
            event, values = alg_window.read()
            alg_window.Maximize()

            arr_size = int(values[0])
            num_cap = int(values[1])

            if event == "Close" or event == sg.WIN_CLOSED:
                break

            if event == "Ok":
                
                alg_window.close()

                arr = np.random.randint(1, num_cap, arr_size)

                graph_window = sg.Window("Sorting Visualizer", graph_layout, finalize= True)

                graph = graph_window.Element('graph')

                draw_bars(graph, arr, BAR_SPACING, BAR_WIDTH, OFFSET)
                graph_window.Maximize()

                event, values = graph_window.read()

                timeout = 1

                if event == 'Sort':

                    sorted_array = quicksort(arr, 0, (len(arr) - 1))

                    for partially_sorted_array in sorted_array:
                        event, values = graph_window.read(timeout=timeout)
                        if event is None:
                            break
                        graph.Erase()
                        draw_bars(graph, partially_sorted_array, BAR_SPACING, BAR_WIDTH, OFFSET)
                        timeout = int(values['-SPEED-'])

                    sg.popup('Sorted!')
                    #graph_window.close()

                while True:
                    event, values = graph_window.Read()
                    if event in (sg.WIN_CLOSED):
                        break


main()