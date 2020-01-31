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

BARCHART:
Used for comparison of different points and takes both the values to be plotted (X-coordinates) and its corresponding height(Y-Coordinates)

Parameters:
colors:Colors for each bar
aligh:where the values has to be aligned(left,right or center)

HISTOGRAM:
For categorising a distribution of data into bins.Each bin will have a subset of data and with that we can actually see the progression of data from one bin to another.

Parameters:
x:data points
range:The range which we are actually concerned about.Outside the range all values will be treated as outliers.
color:we can control the color of the bins
histtype:This could be a bar chart(default),stepped bar chart,filled stepped graph
align:alignment of the bars(of the bins)along the baseline.
label:label for the histogram and call to plt.legend():label will not be defined until a call to the legend is done.

BOXPLOT:
Depicts a group of numbers through quartiles (three points dividing a group into four equal parts).There can be lines called whiskers indicating data outside the upper and lower quartiles.They are called outliers.

Parameters:
data:data points 
notch: True/False whether to display the notched box plot which is actually measured by calculating the notch Height = median +/- 1.57 x IQR/sqrt of n. Any random sample data inside the InterQuartileRange will have similar median.If the shapes and the ranges match then it implies that their variance is equal.

if the notches overlap then the data is from the similar population.Otherwise its from a different population.
