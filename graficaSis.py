import pygraphviz as pgv
import csv
import sys

# Create main function where data is loaded and ensures functionability
def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python graficaSis.py FILENAME.csv")

    #ask user how many years to plot and ensure it's a number
    while True:
        try:
            num = int(input("How many years to plot? "))
        except ValueError:
            print("please enter positive integer")
            continue
        else:
            if num < 1 or num > 26:
                print("please enter positive integer")                
            else:
                break
    
    
    print("Years available range from 2024 to 2050")
    for i in range(1, num + 1):
        #ask user for year to plot
        while True:
            try: 
                year= int(input("Choose year "+str(i)+" to graph: "))
            except ValueError:
                print("please enter year between 2024 and 2050")
                continue
            else:
                if year < 2024 or year > 2050:
                    print("please enter year between 2024 and 2050")
                else:
                    break

        #load and preprocess data
        year= str(year)
        lines = load_data(sys.argv[1], year)
        
        # Graph data
        create_graph(lines, year)

#Function that reads file and load data
def load_data(data, year):
    # Read items into memory
    lines = []
    with open(data) as file:
        reader = csv.DictReader(file)
        for row in reader:
            #Removes word "220 kv" from begining and format a nested list of node1 - node2
            #Check if node duplicated as "node C1" or "node C2" and removes duplicate
            if row["Lineas"][-2:] == "C1" or row["Lineas"][-2:] == "C2":
                line = row["Lineas"][7:-3].split(" - ")    
            else:
                line = row["Lineas"][7:].split(" - ")
            line.append(round(float(row[year]),2))
            lines.append(line)
            
    return lines

#Function that draws nodes reading data
def create_graph(lineas,year):
    Grafico = pgv.AGraph(splines = 'ortho', fontname='Helvetica', nodesep = '0.5')
    Grafico.node_attr['shape'] = 'rect'
    Grafico.node_attr['style'] = 'filled'
    
    
    for i in range(len(lineas)):
        if lineas[i][2] == 0:
            color = "grey"
        elif lineas[i][2] > 0.9:
            color = "red"
        else:
            color = "black"
        Grafico.add_edge(lineas[i][0], lineas[i][1], headlabel = lineas[i][2], color = color, labelfloat = 'true', penwidth = '2.0')
    Grafico.layout(prog='dot')
    Grafico.draw("grafico_"+year+".png")
    return
            
if __name__ == "__main__":
    main()