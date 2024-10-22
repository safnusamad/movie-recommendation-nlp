# -*- coding: utf-8 -*-
"""movie_recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VrsTQCWLzpePbVzxklKWljy-TZ1O9-hC

## Importing the dataset and library
"""

!kaggle datasets download -d tmdb/tmdb-movie-metadata

!unzip /content/tmdb-movie-metadata.zip

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# for hiding the unwanted warning
import warnings
warnings.filterwarnings('ignore')

movies=pd.read_csv('/content/tmdb_5000_movies.csv')
credits=pd.read_csv('/content/tmdb_5000_credits.csv')

movies.head(2)

credits.head(1)

"""## Merging both the dataframe"""

movies.shape

credits.shape

df=movies.merge(credits,on='title')

df.head(2)

#genres
#id
#keywords
#title
#overview
#cast
#crew

df=df[['movie_id','title','overview','genres','keywords','cast','crew']]
df.head()

#checking for missing data
df.isnull().sum()

#dropping the missing data
df.dropna(inplace=True)
df.head()

df.isnull().sum()

#checking for duplicate
df.duplicated().sum()

"""## Data Preprocessing"""

df.iloc[0].genres

# reformating the columns for tagging

#approch 1

def convv(data):
  l=[]
  for x in data:
    l.append(x['name'])
  return l

df['genres']=df['genres'].apply(convv)

# reformating the columns for tagging

#approch 2

import ast
def convert(data):
  list=[]
  for i in ast.literal_eval(data):
    list.append(i['name'])
  return list

# using approch 2

# keywords for genres
df['genres']=df['genres'].apply(convert)
df.head(2)

# keywords for keywords
df['keywords']=df['keywords'].apply(convert)
df.head(2)

#approch 2
# mordifying for cast

# import ast
def convert_cast(data):
  list=[]
  counter=0
  for i in ast.literal_eval(data):
    if counter!=5:
      list.append(i['name'])
      counter+=1
    else:
      break
  return list

df['cast']=df['cast'].apply(convert_cast)
df.head(2)

df['crew'].iloc[0]

# function for fetching director from crew
def fetch_director(data):
  list=[]
  for i in ast.literal_eval(data):
    if i['job']=='Director':
      list.append(i['name'])
      break
  return list

df['crew']=df['crew'].apply(fetch_director)

df.head(2)

# converting the overview also into list
df['overview']=df['overview'].apply(lambda x:x.split())
df.head(2)

#replacing the space in the geners,keywords,cast,crew to create a token
df['genres']=df['genres'].apply(lambda x:[i.replace(" ","") for i in x])
df['keywords']=df['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
df['cast']=df['cast'].apply(lambda x:[i.replace(" ","") for i in x])
df['crew']=df['crew'].apply(lambda x:[i.replace(" ","") for i in x])
df.head()

# concating the data to make a single token
df['tags']=df['overview']+df['genres']+df['keywords']+df['cast']+df['crew']
df.head(2)

# converting the tags to string
df['tags']=df['tags'].apply(lambda x:" ".join(x))
df.head(2)

df['tags'][0]

# final dataframe for proceeding
final_df=df[['movie_id','title','tags']]
final_df.head()

# converting the tags to lower case
final_df['tags']=final_df['tags'].apply(lambda x:x.lower())
final_df.head()

"""### Text Vectorization for the tags

"""

# we are approching the technique know as "bag of words" which comes under "Text Vectorization"

# we will be removing the stop words before vectorization:
# stop words are those words which doesnt as meaning to a sentence like "is, of, the, are,etc"
# we will be using the sklearn library for this feature

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000,stop_words='english')

cv.fit_transform(final_df['tags']).toarray().shape

vectors=cv.fit_transform(final_df['tags']).toarray()

vectors[0]

cv.get_feature_names_out()

# it is noted that there are so many similar type of words are there like actions and action etc.
# to fix this we will use the technique Stemming
# what is does it if we have a array like ['loving','loved','love'] it will convert it to ['','','']
# this process uses libriry nltk which is a famous NLP model

# importing the library
!pip install nltk
import nltk

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def stem(text):
  lst=[]
  for x in text.split():
    lst.append(ps.stem(x))
  return " ".join(lst)

# testing
stem('dancing'), stem('loving'),stem('loved'),stem('love'),stem('action'),stem('actions')

final_df['tags'][0]

# testing
stem('in the 22nd century, a paraplegic marine is dispatched to the moon pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. action adventure fantasy sciencefiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d samworthington zoesaldana sigourneyweaver stephenlang michellerodriguez jamescameron')

new_df_tags=final_df['tags'].apply(stem)
new_df_tags

# after going the stemming we will calculate the vector
new_vectors=cv.fit_transform(new_df_tags).toarray()
cv.get_feature_names_out().size

# we fill find the distance between the movies for recomendation
# as the dimentionality is high we will not go for the eucliden distance instead we will go for the cosine distance

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity(vectors)

cosine_similarity(vectors).shape

similarity=cosine_similarity(vectors)

similarity[2]

# testing the logic to find the index position of the movie using the movie name
final_df[final_df['title']=='Avatar'].index[0],final_df[final_df['title']=='Raymond Did It'].index[0]

# for recommendation we need to find next movies.
# for that we will require to sort the array.
sorted(similarity[0])
# the issue with above sort is that when we are sorting it like this
# we are loosing the index value
# (i.e similarity of movie1 with movie2 and movie1 with movie3 and movie1 with movie4 etc)
# because by similarity[0] has arraged value like that. so to maintain that we need to

sorted(similarity[0],reverse=True)[0:6]
# here we got the values/similarity which are closest to the orginal value
# here i have taken top 5. value=1.0 is the movie which we searched
# below are the values which are recomended

# include the index position also with the similarity value
sorted(list(enumerate(similarity[0])),reverse=True)[0:6]
# in above code the sorting happend based on index postion where as we wanted based on similiraty

sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]
# here we have achived what we wanted

# function for recommendation #testing
def recommend(movie):
  movie_idx=final_df[final_df['title']==movie].index[0]
  distance=similarity[movie_idx]
  movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[0:6]
  for x in movie_list:
    print(x[0]," ",final_df.iloc[x[0]].title)

final_df.columns

# checking using a random movie name
final_df['title'].sample(n=1).iloc[0]

recommend('The 5th Wave')

final_df[final_df['title']=='Allegiant'].index[0]

# final function for recommendation of the movie
def recommend(movie):
  movie_idx=final_df[final_df['title']==movie].index[0]
  distance=similarity[movie_idx]
  movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
  for x in movie_list:
    print(x[0])

# now we will pass the list of movies from here to vs code for that we will use pickle
import pickle

pickle.dump(final_df,open('movies.pkl','wb'))
# when we are sending the dataframe we are getting error instead of stending the dataframe
#  we will send the dictionary

# passing the movies list as dictinary

# Assuming final_df is your DataFrame
final_df_dict = final_df.to_dict()

with open('movies_dict.pkl', 'wb') as file:
    pickle.dump(final_df_dict, file)

pickle.dump(similarity,open('similarity.pkl','wb'))