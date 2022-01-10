import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#Fonction : 
def graphique_norm(dataframe):
	  taille = len(dataframe.columns)
	  fig, ax = plt.subplots( figsize = (3*taille,6))
	  for i in range(0,taille):
	    col = dataframe.columns[i]
	    #BoxPlot : 
	    ax1 = plt.subplot2grid((2,taille),(0,i)) 
	    dataframe[[col]].boxplot()
	    plt.tick_params(axis = "x",labelsize=20)
	    #Histogrammes : 
	    ax2 = plt.subplot2grid((2,taille),(1,i)) 
	    ax2.hist(dataframe[col],color="cornflowerblue")
	  return st.pyplot(ax1.figure)

#Entête : 
st.markdown("<h1 style='text-align: center; color: royalblue;'>Quête Streamlit</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: cornflowerblue;'>Build and share data apps!</h1>", unsafe_allow_html=True)
st.write("DataFrame source sur les voitures : https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)
st.write("")

df_graphique = df

#Question 2 :
st.sidebar.markdown("<h1 style = 'color:cornflowerblue;'>Question 2 :</h3>", unsafe_allow_html=True)
if st.sidebar.button("ALL"):
    df_graphique = df
if st.sidebar.button("EUROPE"):
    df_graphique = df[df["continent"]==" Europe."]
if st.sidebar.button("JAPON"):
    df_graphique = df[df["continent"]==" Japan."]
if st.sidebar.button("US"):
    df_graphique = df[df["continent"]==" US."]
    
df_graphique

#Question 1 : 
st.markdown("<h3 style = 'color:cornflowerblue;'>Question 1 :</h3>", unsafe_allow_html=True)
graphiques = st.selectbox("Choisissez le graphique désiré : ", 
                     ['Analyse de la corrélation entre les variables', 'Analyse de la distribution des valeurs']) 


if graphiques == "Analyse de la corrélation entre les variables":
	col1, col2 = st.columns(2)
	with col1:
		corrélation = sns.heatmap(df_graphique.corr(),
								  center = 0,
								  cmap = sns.diverging_palette(255,0,sep=77, as_cmap=True))
		corrélation.set_title("Heatmap")
		st.pyplot(corrélation.figure)
	with col2:
		st.markdown('<p style="color:#7a95ed;">Cylinders, Cubicinches, Hp et Weightlbs sont corrélés positivement entre eux</p>'
              		'<p style="color:#7a95ed;">Cylinders, Cubicinches, Hp et Weightlbs sont corrélés négativement avec mpg</p>'
                	'<p style="color:#7a95ed;">Time-to-60 est correlée négativement avec HP</p>',unsafe_allow_html=True) #font-size:24px;


elif graphiques == "Analyse de la distribution des valeurs":
	col1, col2 = st.columns(2)
	with col1:
		graphique_norm(df_graphique[["mpg","cylinders","cubicinches","hp","weightlbs","time-to-60","year"]])
	with col2:
		st.write("<p style='color:#7a95ed;'>Il n'y a pas d'Outlier</p>"
           		 "<p style='color:#7a95ed;'>'Time-to-60' a une distribution normale</p>"
                 "<p style='color:#7a95ed;'>'Year' a une distribution uniform <p>", unsafe_allow_html=True)