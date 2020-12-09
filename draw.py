import PySimpleGUI as sg

# draws all the bars for all values across screen
def draw_bars(graph, items, bar_spacing, bar_width, offset):  
    
    for i, item in enumerate(items):
        graph.DrawRectangle(top_left=(i * bar_spacing + offset, item),
                            bottom_right=(i *  bar_spacing + offset + bar_width, 0), fill_color='#76506d')