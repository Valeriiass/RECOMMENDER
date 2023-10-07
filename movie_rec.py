import streamlit as st
import pandas as pd
import numpy as num
from PIL import Image
import base64
import streamlit as st
import sklearn

#st.title('Your best movies')
#st.title('_Streamlit_ is :blue[cool] :sunglasses:')
#[theme]



st.title("Movie rating :star:")  #:blue[star]
st.write(""" The popular movies """)




#PICTURES POP MOVIES
#images = ['Unknown.jpeg', 'images.jpeg']
#st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
import streamlit as st
from PIL import Image
from itertools import cycle

filteredImages =  ['Unknown.jpeg', 'fight.jpg', 'pulpfiction.jpg', 'LEON - French Poster by Laurent Lufroy.jpeg', '71Ke3uo-vjL._SL1500_.jpg', '918-iKMNQ3L._SL1500_.jpg', '20120704-191812.jpg.webp', 'pitch_perfect-419842614-large.jpg'] # your images here
caption = ['[ID-7361] Eternal Sunshine of the Spotless Mind (2004)', '[ID-2959] Fight Club (1999)', '[ID-296] Pulp Fiction (1994)', '[ID-293] Léon: The Professional(1994)', '[ID-84847] Emma (2009)', '[ID-96588] Toy Story 2 (1999)', '[ID-858] Godfather, The (1972)', '[ID-3114] Pitch Perfect (2012)' ] # your caption here
cols = cycle(st.columns(4)) # st.columns here since it is out of beta at the time I'm writing this
for idx, filteredImage in enumerate(filteredImages):
    next(cols).image(filteredImage, width=150, caption=caption[idx])


    


#DATA FRAME 
#df = pd.read_csv("./random_10_movies.csv")
#df = df[['movieId', 'title']]# read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Let's guess the best movie you've NEVER seen")  # add a title
#st.write(df)  # visualize my dataframe in the Streamlit app


#import pickle
#loaded_model = pickle.load(open('item_model_sav.sav', 'rb'))

NumMov = st.number_input("Chose the ID of your favourite movie from the pictures above", min_value=1, max_value=193609, value=858, step=1) #st.text_input("Log In with User ID:")

st.write("Which one do you chose for today's evening ?")




#ITEM BASED

#result_2 = pd.read_csv("./movie_data.csv")

url = "https://drive.google.com/file/d/1zNoEHDvb2eHfAoFIyFY05WMqcVQTW14o/view?usp=sharing"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
result_2 = pd.read_csv(path)



list_of_ids = (7361, 2959, 172, 296, 293,1730, 50, 96588, 4104, 84847, 413, 27831, 3114, 858)
rrr = result_2[result_2['movieId'].isin(list_of_ids)].drop_duplicates(subset='title')  
new = rrr[['movieId', 'userId', 'rating']]
user_movie_matrix = pd.pivot_table(data=new,
                                  values='rating',
                                  index='userId',
                                  columns='movieId',
                                  fill_value=0)
movie_correlations_matrix = user_movie_matrix.corr()
blonde_correlations_df = pd.DataFrame(movie_correlations_matrix[NumMov])
blonde_correlations_df = blonde_correlations_df[blonde_correlations_df.index != NumMov]
blonde_correlations_df = blonde_correlations_df.sort_values(by=NumMov, ascending=False) 

blonde_top_10_correlation = (blonde_correlations_df
                                  .head(3)
                                  .reset_index()
                                  .merge(rrr.drop_duplicates(subset='movieId'),   #subset by which column we will drop the duplicates
                                         on='movieId',
                                         how='left')
                                  [['title']]      #'movieId',
                            )   #names of columsns we will have
blonde_top_10_correlation




## USER BASED 

st.title("SPECIAL PROPOSAL for :gold[YOU] :star: :star: :star:")
NumUser = st.number_input("Please, write you user-ID", min_value=1, max_value=800, value=1, step=1) 

result_2_2 = result_2[['movieId','title', 'userId', 'rating']]
user_matrix_user = pd.pivot_table(data=result_2_2,
                                  values='rating',
                                  index='movieId',
                                  columns='userId',
                                  fill_value=0)

user_correlations_matrix_user = user_matrix_user.corr()
#user_correlations_matrix_user = pd.read_csv("./user_matrix_new.csv")

black_correlations_df = pd.DataFrame(user_correlations_matrix_user[NumUser])    #pd.DataFrame(
black_correlations_df = black_correlations_df[black_correlations_df.index != NumUser]
black_correlations_df = black_correlations_df.sort_values(by=NumUser, ascending=False) 

black_top_10_correlation = (black_correlations_df
                                  .head(1)
                                  .reset_index()
                                  .merge(result_2_2,       #.drop_duplicates(subset='movieId'),   #subset by which column we will drop the duplicates
                                         on='userId',
                                         how='left')
                                  [['title']] #names of columsns we will have
                                  )

black_top_10_correlation = black_top_10_correlation.head(1)
#black_top_10_correlation


st.write("This movie as that was needed to spend an UNFORGETTABLE evening:") 
st.title(black_top_10_correlation.iloc[0, 0])
























































#int_val = st.number_input('Seconds', min_value=1, max_value=10, value=5, step=1)


#import pandas as pd
#import streamlit as st

#data_df = pd.DataFrame(
 #   {
  #      "apps": [
   #         "https://drive.google.com/file/d/1YWv5C1QGxdBx3_aZbncxFdEtQG1Wu9ob/view?usp=sharing",
  #      ],
 #   }
#)

#st.data_editor(
#    data_df,
#    column_config={
#        "apps": st.column_config.ImageColumn(
#            "Preview Image", help="Streamlit app preview screenshots"
#        )
#    },
#    hide_index=True,
#)









#from PIL import Image

#image = Image.open('images.jpeg')
#image_2 = Image.open('Unknown.jpeg')
#st.image(image, caption='Sunrise by the mountains')
#st.image(image_2, caption='Sunrise by the mountainsssss')

#st.write("The price of the house is:", prediction)

#st.write('Hello')
#st.baloon()