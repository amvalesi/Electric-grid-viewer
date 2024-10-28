# Electrical system graph
#### Video Demo:  <URL HERE>
#### Description:
The following project consists of making a Python script that graphs (makes diagram) a list of names that represent the line's names of an electrical system. In the diagram the substations are represented as nodes and the electrical lines are represented as lines. It also includes a label with the percentage of the line's loading level.
To run the script is necesary to type "python graficaSis.py FILENAME.csv" to the terminal, where FILENAME is a CSV file containing the data to graph.

#### Requirements:
The script uses the Pygraphviz library that requires Python, Graphviz, and a C/C++ Compiler as [stated here](https://pygraphviz.github.io/).
For Pygraphviz documentation [check here.](https://pygraphviz.github.io/documentation/latest/)

## Introduction
In certain areas of electrical engineering, engineers must project the future behavior of electrical power systems to plan for upcoming expansions, such as new substations, generating plants, or loads. These studies aim to assess both economic and technical outcomes. On the technical side, the focus is on evaluating system stability and determining whether new consumption or generation will cause congestion.

The software used for system modeling and calculations typically generates large amounts of data, often with graphical visualizations. However, these tools can be less practical when many simulations are required or when specific results need to be verified quickly. This has led to the idea of developing a simpler tool that can graphically represent the system more efficiently.

## Project's files
The project consists of one Python script, one CSV file and it will generate PNG files as required

### Line_Data.csv
This file contain the data to graph. The data distribution is designed in matrix format, where the first columns contain an index and the Line's name and the following columns different years with the data of the line's loading level.

### graficaSis.py
This Python script requires pygraphviz, csv and sys Python libraries and is divided into 3 functions:
#### main():
It is expected to run the script on the terminal as "python graficaSis.py FILENAME.csv" so it first check if the required number of comand lines were typed. After that it asks the user how many year to graph, and wich ones. It was assumed that the entered file contains data of years from 2024 to 2050 because the studies are usually made in that year range, but if this is required for a more generic data set it could check the range of data within the file. In any case, it is verified that the data is numerical within the specified range
Once the years are entered it just calls the "load_data()" function to load and preprocess the data and then calls the "create_graph()" to finally plot the data inside a loop for each year.

#### load_data(data, year):
This function uses the DictReader() function to read the CSV file into memory, assuming the column with the lines's name is called "Lineas" it gets the name of each node that make up the line by spliting the string when detecting a dash symbol (-), and stores them with the loading level data in a nested list, so each index of the list will have the two nodes composing the line and its data.
In the file, the name of the line includes the tension level in kilo Watts (kW) at the begining, because is not needed for the graph this is removed.
In addition, some of the lines come with "C1" or "C2" in the name wich indicates whether it belongs to circuit number one or two of the line. This is also removed from the name but it is kept within the list, because the pygraphviz library allows duplicate objects without the need to graph them but it can be changed if needed.
After procesing the data it returns the created list.

#### create_graph(lineas):
This function creates and configures the canvas to start ploting the data. As a basic design it configures every node as a gray square that is joined by orthogonal lines. This design resembles typical [single line diagrams](https://en.wikipedia.org/wiki/Single-line_diagram) representing an electrical system but focusing on the node's name instead of every component.
Then, some other configurations are made depending on the data to plot:
- If the line data is zero the line is gray indicating that the line has no flow so it may be disconnected.
- If the data is greater than 0.9 the line is red indicating a possible overload.

As the imputed list is being traversed by a for loop, every node is created with its data as a label to then be distributed with the "dot" Graphviz algorithm, which is the one that most closely resembles the desired design.
