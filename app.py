# to start the app use "steamlit run app.py"
# to stop the the app press "ctrl+c"

# first pip install streamlit (in terminal)



import streamlit as st
import pickle as pk
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e77cb77abc6b8d45c3686cffad8a2cdc&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# function for recommendation movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# def recommend(movie):
#   movie_idx=movies[movies['title']==movie].index[0]
#   distance=similarity[movie_idx]
#   movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
#   recommended_movies=[]
#   recommended_movie_poster=[]
#   for x in movie_list:
#     movie_id=movies.iloc[x[1]].movie_id
#     recommended_movies.append(movies.iloc[x[0]].title)
#     recommended_movie_poster.append(fetch_poster(movie_id))
#   return recommended_movies



movie_dictinary=pk.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dictinary)

similarity=pk.load(open('similarity.pkl','rb'))



st.title("Movie Recommendation System")
selected_movie_name = st.selectbox("Select a movie to Recommend",movies['title'].values)

# if st.button('Recommend Movies'):
#     recommendations=recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5,gap="small")
    with col1:
        st.markdown(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.markdown(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.markdown(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.markdown(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.markdown(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])