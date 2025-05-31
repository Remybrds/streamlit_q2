import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_list = ['anagrams.csv'
                , 'anscombe.csv'
                , 'attention.csv'
                , 'brain_networks.csv'
                , 'car_crashes.csv'
                , 'diamonds.csv'
                , 'dots.csv'
                , 'dowjones.csv'
                , 'exercise.csv'
                , 'flights.csv'
                , 'fmri.csv'
                , 'geyser.csv'
                , 'glue.csv'
                , 'healthexp.csv'
                , 'iris.csv'
                , 'mpg.csv'
                , 'penguins.csv'
                , 'planets.csv'
                , 'seaice.csv'
                , 'taxis.csv'
                , 'tips.csv'
                , 'titanic.csv']

type_list = ['bar_chart', 'line_chart', 'scatter_chart']

st.header("Manipulation de données et création de graphiques")

csv = st.selectbox("Quel dataset veux-tu utiliser", dataset_list)
data = pd.read_csv(csv)

st.dataframe(data=data)

x = st.selectbox("Choisissez la colonne X", data.columns)
y = st.selectbox("Choisissez la colonne Y", data.columns)
graph_type = st.selectbox("Quel graphique veux-tu utiliser?", type_list)

if graph_type == "bar_chart" :
    st.bar_chart(data, x=x, y=y)
elif graph_type == "line_chart" :
    st.line_chart(data, x=x, y=y)
elif graph_type == "scatter_chart" :
    st.scatter_chart(data, x=x, y=y)

check = st.checkbox("Afficher la matrice de corrélation")

if check :
    corr = data.select_dtypes('number').corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, ax=ax, annot=True)
    st.pyplot(fig)