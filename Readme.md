JuPyter Lab Notebook and Mathplotlib are used as the Web UI - as such it can be hosted on any web platform. ANother possibility is to use the Django widget for Mathplotlib

the plot of individual timeseries contains a side effect consisting of extra horizontal line due to the previous two invocations of matplotlib for the visualization of all timeseries 
and apparently retained context/state. Due to the shortage of time there was no suffcient time to debug this issue (reinitilizing mathplotliub has been tried in a few ways)

Due to shortage of time, JuPyter Widget with multiple selection of list items has not been implemented (currently only one specific or all timeseries from a chosen dataset can be selected)
from the 2 dedicated Combobox UI Widgets, but it should be already clear that the support for multiple selection and slicing of group of of time 
series is implemented in the code of the python lib supporting the JuPyter Notebook
