# MATPLOTLIB
Matplot lib ,magic functions

MATPLOTLIB library contains the functions that could be used to provide a graphical representation of the numerical data using many plots.

The code we type is the frontend and then we have a list of backends that do all the processing to print the data in a graphical format. The list of backends that could be given to the %matplotlib are inline, notebook,gtk,qt,qt4,qt5,tk and wx.

There are two types of backends: user interface backends (for use in pygtk, wxpython, tkinter, qt4, or macosx; also referred to as "interactive backends") and hardcopy backends to make image files (PNG, SVG, PDF, PS; also referred to as "non-interactive backends").

Embed function: used to load an image from another location inside our notebook.
SoftLinked: Dynamic Loading helps in loading the image dynamically which means that if the original image is changed in that location this gets updated.

PIECHART:
Is used when we want to understand how the individual data elements are contributing to the whole.

Parameters:
values : values to be plotted
colors : colors to differentiate each value
labels : labels for each data element.
explode : When u want to show one wedge (one data element seperately) from the whole pie .The explode value corresponding to that will be higher and the rest will be 0.We can do that for several values.
counterlock : direction of the wedges
shadow : shadow for each wedge
autopct: %1.1f%% when u want to specify a format for the percentage of each data element.

