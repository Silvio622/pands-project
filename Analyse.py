# Silvio Dunst
# Analyse the Fisher's Iris Data Set

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Import the Fisher's Iris data set form the Internet
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Save the Fisher's Iris Data Set in a CSV file from pandas dataframe
# found this code on the website "https://datatofish.com/export-dataframe-to-csv/"
df.to_csv(r'Fishers_Iris_Dataset.csv', mode ='w', index = False, header = True)

# Save the data in a Text file and removing the index in the dataframe
# found this code on the website "https://stackoverflow.com/questions/48432326/remove-index-dataframe-pandas"
with open('Fishers_Iris_Dataset.txt', 'w') as textfile:
    textfile.write(df.to_string(index = False))
    textfile.close()

# research for plotting on website "https://matplotlib.org/examples/showcase/anatomy.html", https://pandas.pydata.org/ and 
# https://matplotlib.org/3.2.0/api/_as_gen/matplotlib.pyplot.hist.html
# Histogram plot for Sepal Length
plt.hist(df['sepal_length'], histtype = 'bar',rwidth = 0.8,color= '#0000FF')
plt.title("Sepal Length for different Species")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Distribution of Sepal length")
plt.savefig("Hist Sepal length.png")
plt.show()

# Histogram plot for Sepal Width
plt.hist(df['sepal_width'], histtype = 'bar',rwidth = 0.8,color= '#0000FF')
plt.title("Sepal Width for different Species")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Distribution of Sepal Width")
plt.savefig("Hist Sepal width.png")
plt.show()

# Histogram plot for Petal Length
plt.hist(df['petal_length'], histtype = 'bar',rwidth = 0.8,color= '#0000FF')
plt.title("Petal Length for different Species")
plt.xlabel("Petal Length in cm")
plt.ylabel("Distribution of Petal length")
plt.savefig("Hist Petal length.png")
plt.show()

# Histogram plot for Petal Width
plt.hist(df['petal_width'], histtype = 'bar',rwidth = 0.8,color= '#0000FF')
plt.title("Petal Width for different Species")
plt.xlabel("Petal Width in cm")
plt.ylabel("Distribution of Petal Width")
plt.savefig("Hist Petal width.png")
plt.show()

# Scatter plot for Sepal length vs Sepal width
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Sepal Width in cm")
plt.savefig("Scatter Sepal length vs Sepal width.png")
plt.show()

# Scatter plot for Sepal length vs Petal length
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Petal Length in cm")
plt.savefig("Scatter Sepal length vs Petal length.png")
plt.show()

# Scatter plot for Sepal length vs Petal width
sns.scatterplot(x='sepal_length', y='petal_width', data=df, hue='species')
plt.title("Sepal Length vs Petal Width")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Petal Width in cm")
plt.savefig("Scatter Sepal length vs Petal width.png")
plt.show()

# Scatter plot for Sepal width vs Petal length
sns.scatterplot(x='sepal_width', y='petal_length', data=df, hue='species')
plt.title("Sepal Width vs Petal Length")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Petal Length in cm")
plt.savefig("Scatter Sepal width vs Petal length.png")
plt.show()

# Scatter plot for Sepal width vs Petal width
sns.scatterplot(x='sepal_width', y='petal_width', data=df, hue='species')
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Petal Width in cm")
plt.savefig("Scatter Sepal width vs Petal width.png")
plt.show()

# Scatter plot for Petal length vs Petal width
sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species')
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length in cm")
plt.ylabel("Petal Width in cm")
plt.savefig("Scatter Petal length vs Petal width.png")
plt.show()


# Scatter plot for Sepal length for every species
sns.scatterplot(x='sepal_length', y='species', data=df, hue='species')
plt.title("Sepal Length for different Species")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Sepal length vs Species.png")
plt.show()

# Scatter plot for Sepal width for every species
sns.scatterplot(x='sepal_width', y='species', data=df, hue='species')
plt.title("Sepal Width for different Species")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Sepal width vs Species.png")
plt.show()

# Scatter plot for Petal length for every species
sns.scatterplot(x='petal_length', y='species', data=df, hue='species')
plt.title("Petal Length for different Species")
plt.xlabel("Petal Length in cm")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Petal length vs Species.png")
plt.show()

# Scatter plot for Petal width for every species
sns.scatterplot(x='petal_width', y='species', data=df, hue='species')
plt.title("Petal Width for different Species")
plt.xlabel("Petal Width in cm")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Petal width vs Species.png")
plt.show()


# Summery of each variable into a text file "Summery"
summery = []
summery = df.describe()
print(summery)

print(summery['petal_length'])
sepallengthsummery = (summery['sepal_length'])
sepalwidthsummery = (summery['sepal_width'])
petallengthsummery = (summery['petal_length'])
petalwidthsummery = (summery['petal_width'])

summerydic = {}
summerydic = df.describe()
print(summerydic)

with open("Summery.txt", mode = 'w', newline ='') as writeon: 
    # Sepal Length 
    writeon.write("stats") 
    writeon.write("\t") 
    writeon.write("Sepal Length")
    writeon.write("\n")
    writeon.write("\t")     
    for line in sepallengthsummery:
        writeon.writelines(str(line))
        writeon.write("\n")
        writeon.write("\t")
    writeon.write("\n") 
    # Sepal Width
    writeon.write("stats") 
    writeon.write("\t") 
    writeon.write("Sepal Width")
    writeon.write("\n")
    writeon.write("\t")     
    for line in sepalwidthsummery:
        writeon.writelines(str(line))
        writeon.write("\n")
        writeon.write("\t")
    writeon.write("\n") 
    # Petal Length 
    writeon.write("stats") 
    writeon.write("\t") 
    writeon.write("Petal Length")
    writeon.write("\n")
    writeon.write("\t")     
    for line in petallengthsummery:
        writeon.writelines(str(line))
        writeon.write("\n")
        writeon.write("\t")
    writeon.write("\n") 
    # Petal Width
    writeon.write("stats") 
    writeon.write("\t") 
    writeon.write("Petal Width")
    writeon.write("\n")
    writeon.write("\t")     
    for line in petalwidthsummery:
        writeon.writelines(str(line))
        writeon.write("\n")
        writeon.write("\t")
    writeon.write("\n") 


# working until here

#sepaldescr = df.describe(include=['object'])
#print(sepaldescr.values)
#print(sepaldescr)
#working until here

#np.savetxt('Project Summery.tx',df.describe,fmt='%d',delimiter="\t",header="\tsepal_length\tsepal_width\tpetal_length\tpetal_width")
#np.savetxt('Project Summery.txt',df.values,fmt='%d',delimiter="\t",header="\tsepal_length\tsepal_width\tpetal_length\tpetal_width")



with open("Project Summery.txt", mode = 'w', newline ='') as writein:  
    writein.write("stats") 
    writein.write("\t")     
    for line in summery:
        writein.write(str(line))
        writein.write("\t")
    writein.write("\n") 

    writein.write("count") 
    writein.write("\t")  
    for count in df.count():        
        writein.write(str(count))
        writein.write("\t")  
    writein.write("\n")

    writein.write("mean") 
    writein.write("\t")  
    for mean in df.mean():        
        writein.write(str(mean))
        writein.write("\t")  
    writein.write("\n")

    writein.write("std") 
    writein.write("\t")  
    for std in df.std():        
        writein.write(str(std))
        writein.write("\t")  
    writein.write("\n")

    writein.write("min") 
    writein.write("\t")  
    for minimum in df.min():        
        writein.write(str(minimum))
        writein.write("\t")  
    writein.write("\n")

# 25%,50%,75%

    writein.write("max") 
    writein.write("\t")  
    for maximum in df.max():        
        writein.write(str(maximum))
        writein.write("\t")  
    writein.write("\n")




# write the project Summery in a Text file
#import csv
#from itertools import zip_longest
#d=[summery]
#export_data = zip_longest(*d, fillvalue ='')
#with open ("Project Summery.txt", mode = 'w',newline ='') as SummeryFile:
    #filewriter = csv.writer(SummeryFile, delimiter = '\t',quotechar = '"')
    #filewriter.writerow(("sepal_length","sepal_width","petal_length","petal_width"))
    #filewriter.writerows(export_data)
    #SummeryFile.close()
      

# Seaborn


print("Finshed")

