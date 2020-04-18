# Silvio Dunst
# Analyse the Fisher's Iris Data Set

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the Fisher's Iris data set form the Internet
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Save the Fisher's Iris Data Set in a CSV file from pandas dataframe
# found this code on the website "https://datatofish.com/export-dataframe-to-csv/"
df.to_csv(r'Fishers_Iris_Dataset.csv', mode ='w', index = False, header = True)

# Save the data in a Text file and removing the index in the dataframe
# found this code on the website "https://stackoverflow.com/questions/48432326/remove-index-dataframe-pandas"
with open('Fishers_Iris_Dataset.txt', mode = 'w', newline = '') as textfile:
    textfile.write(df.to_string(index = False, header = True))
    textfile.close()

# Slice the pandas data set df in the three species "Setosa", "Versicolor" and "Virginica"
# found on website https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/
# Slice the dataframe for Iris Flower Setosa
setosa = df[0:50]

# Slice the dataframe for Iris Flower Versicolor
versicolor= df[50:100]

# Slice the dataframe for Iris Flower Viginica
virginica= df[100:150]

# research for plotting on website "https://matplotlib.org/examples/showcase/anatomy.html", https://pandas.pydata.org/ and 
# https://seaborn.pydata.org/tutorial/distributions.html
# Histogram plot for Sepal Length
sns.distplot(setosa["sepal_length"])
sns.distplot(setosa["sepal_length"],bins=20, kde=False, color='#0055FF', label='Setosa')
sns.distplot(versicolor["sepal_length"])
sns.distplot(versicolor["sepal_length"],bins=20, kde=False,color= '#FFAA00', label='Versicolor')
sns.distplot(virginica["sepal_length"])
sns.distplot(virginica["sepal_length"],bins=20, kde=False,color= '#00AA00', label='Virginica')
plt.legend()
plt.title("Sepal Length for different Species")
plt.xlabel("Sepal Length")
plt.ylabel("Distribution of Sepal length")
plt.savefig("Hist Sepal length.png")


# Histogram plot for Sepal Width
sns.distplot(setosa["sepal_width"])
sns.distplot(setosa["sepal_width"],bins=20, kde=False, color='#0055FF', label='Setosa')
sns.distplot(versicolor["sepal_width"])
sns.distplot(versicolor["sepal_width"],bins=20, kde=False,color= '#FFAA00', label='Versicolor')
sns.distplot(virginica["sepal_width"])
sns.distplot(virginica["sepal_width"],bins=20, kde=False,color= '#00AA00', label='Virginica')
plt.legend()
plt.title("Sepal Width for different Species")
plt.xlabel("Sepal Width")
plt.ylabel("Distribution of Sepal width")
plt.savefig("Hist Sepal width.png")


# Histogram plot for Petal Length
sns.distplot(setosa["petal_length"])
sns.distplot(setosa["petal_length"],bins=20, kde=False, color='#0055FF', label='Setosa')
sns.distplot(versicolor["petal_length"])
sns.distplot(versicolor["petal_length"],bins=20, kde=False,color= '#FFAA00', label='Versicolor')
sns.distplot(virginica["petal_length"])
sns.distplot(virginica["petal_length"],bins=20, kde=False,color= '#00AA00', label='Virginica')
plt.legend()
plt.title("Petal Length for different Species")
plt.xlabel("Petal Length")
plt.ylabel("Distribution of Petal length")
plt.savefig("Hist Petal length.png")


# Histogram plot for Petal Width
sns.distplot(setosa["petal_width"])
sns.distplot(setosa["petal_width"],bins=20, kde=False, color='#0055FF', label='Setosa')
sns.distplot(versicolor["petal_width"])
sns.distplot(versicolor["petal_width"],bins=20, kde=False,color= '#FFAA00', label='Versicolor')
sns.distplot(virginica["petal_width"])
sns.distplot(virginica["petal_width"],bins=20, kde=False,color= '#00AA00', label='Virginica')
plt.legend()
plt.title("Petal Width for different Species")
plt.xlabel("Petal Width")
plt.ylabel("Distribution of Petal width")
plt.savefig("Hist Petal width.png")


# found things on website "https://towardsdatascience.com/data-visualization-using-seaborn-fc24db95a850"
# Scatter plot for Sepal length vs Sepal width
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
plt.title("Sepal Length vs Sepal Width") 
plt.xlabel("Sepal Length") 
plt.ylabel("Sepal Width") 
plt.savefig("Scatter Sepal length vs Sepal width.png") 
 

# Scatter plot for Sepal length vs Petal length
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig("Scatter Sepal length vs Petal length.png")


# Scatter plot for Sepal length vs Petal width
sns.scatterplot(x='sepal_length', y='petal_width', data=df, hue='species')
plt.title("Sepal Length vs Petal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.savefig("Scatter Sepal length vs Petal width.png")


# Scatter plot for Sepal width vs Petal length
sns.scatterplot(x='sepal_width', y='petal_length', data=df, hue='species')
plt.title("Sepal Width vs Petal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Length")
plt.savefig("Scatter Sepal width vs Petal length.png")


# Scatter plot for Sepal width vs Petal width
sns.scatterplot(x='sepal_width', y='petal_width', data=df, hue='species')
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.savefig("Scatter Sepal width vs Petal width.png")


# Scatter plot for Petal length vs Petal width
sns.scatterplot(x='petal_length', y='petal_width', data=df, hue='species')
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.savefig("Scatter Petal length vs Petal width.png")



# Scatter plot for Sepal length for every species
sns.scatterplot(x='sepal_length', y='species', data=df, hue='species')
plt.title("Sepal Length for different Species") 
plt.xlabel("Sepal Length") 
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,) 
plt.savefig("Sepal length vs Species.png") 
 

# Scatter plot for Sepal width for every species
sns.scatterplot(x='sepal_width', y='species', data=df, hue='species')
plt.title("Sepal Width for different Species")
plt.xlabel("Sepal Width")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Sepal width vs Species.png")


# Scatter plot for Petal length for every species
sns.scatterplot(x='petal_length', y='species', data=df, hue='species')
plt.title("Petal Length for different Species")
plt.xlabel("Petal Length")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Petal length vs Species.png")


# Scatter plot for Petal width for every species
sns.scatterplot(x='petal_width', y='species', data=df, hue='species')
plt.title("Petal Width for different Species")
plt.xlabel("Petal Width")
plt.ylabel("Species",fontsize = 12, position = (0,1.01), color = "#0000FF", rotation = 0,)
plt.savefig("Petal width vs Species.png")


# Create three new dataframes "setosastats", "versicolorstats" and "virginicastats" for the Iris Flower statistics
setosastats = setosa.describe()
versicolorstats = versicolor.describe()
virginicastats = virginica.describe()

# Writing the Project summery statistics for each Iris Flower in a txt file
with open('Projectsummery.txt', mode ='w') as textfile:
    textfile.write("Project Summery Setosa")
    textfile.write("\n")
    textfile.write(setosastats.to_string(index = True, header = True))
    textfile.write("\n\n")
    textfile.write("Project Summery Versicolor")
    textfile.write("\n")
    textfile.write(versicolorstats.to_string(index = True, header= True))
    textfile.write("\n\n")
    textfile.write("Project Summery Virginica")
    textfile.write("\n")
    textfile.write(virginicastats.to_string(index = True, header= True))
    textfile.close()


