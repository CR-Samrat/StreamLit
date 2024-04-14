import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns

dataframe = pd.DataFrame(np.random.randn(20,4), columns=["Col1","Col2","Col3","Col4"])

st.title("Line chart")
st.line_chart(dataframe)
st.title("Bar chart")
st.bar_chart(dataframe)
st.title("Area chart")
st.area_chart(dataframe)

# working with iris dataset
st.title("Iris dataset")
df = load_iris()
iris_df = pd.DataFrame(df.data, columns=df.feature_names)
iris_df["Target"] = df.target
target_names = {0:'setosa', 1:'versicolor', 2:'virginica'}
iris_df["Target"] = iris_df["Target"].apply(lambda x: target_names[x])

st.write(iris_df)

# knowing the differences about all 3 classes
st.title("Grouping by Classes")
level_2_df = iris_df.groupby("Target").mean()
st.write(level_2_df)

st.title("Setosa details")
st.bar_chart(level_2_df.iloc[0, :])
st.title("versicolor details")
st.bar_chart(level_2_df.iloc[1, :])
st.title("virginica details")
st.bar_chart(level_2_df.iloc[2, :])

# distribution plot of all independent variables
st.title("Distribution of all independent variables")
fig1 = plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
sns.distplot(iris_df["sepal length (cm)"])
plt.subplot(2,2,2)
sns.distplot(iris_df["sepal width (cm)"])
plt.subplot(2,2,3)
sns.distplot(iris_df["petal length (cm)"])
plt.subplot(2,2,4)
sns.distplot(iris_df["petal width (cm)"])
st.pyplot(fig1)

st.title("Variation of data WRT Classes")
fig2 = plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
sns.barplot(data=level_2_df, x="Target", y="sepal length (cm)")
plt.subplot(2,2,2)
sns.barplot(data=level_2_df, x="Target", y="sepal width (cm)")
plt.subplot(2,2,3)
sns.barplot(data=level_2_df, x="Target", y="petal length (cm)")
plt.subplot(2,2,4)
sns.barplot(data=level_2_df, x="Target", y="petal length (cm)")
st.pyplot(fig2)