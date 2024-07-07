#Imports
import streamlit as st
from PIL import Image
import numpy as np
import os

#Page Setup
st.set_page_config(page_title = 'Photo Labeling Website', page_icon = ':national_park:', layout = 'wide')
directory = "C:/Users/space/Desktop/CS Projects/AI Photo Rater/Landscape Photos"
extensions = ('jpg', 'jpeg', 'png')
file_list = os.listdir(directory)
counter_path = "C:/Users/space/Desktop/CS Projects/AI Photo Rater/counter.txt"
#Counter Read-in
try:
    with open(counter_path, 'r') as file:
        counter = int(file.read().strip())  # Read the content and strip any surrounding whitespace
except Exception as e:
    print(f"An error occurred: {e}")
#Image Array Creation
@st.cache_data
def createImageArray(directory, extensions):
    images = []
    for filename in file_list:
        if filename.lower().endswith(extensions):
            images.append(os.path.join(directory, filename))
    return images

images = createImageArray(directory, extensions)
    
#Completion Check
if counter >= len(images):
    print('Labeling Complete')
    st.info("There are no more images to label. Thank you for you help!")
    st.stop()

#Header and explanation
st.subheader('Welcome to the Image Labeling Website')
st.write('This website allows users to label images for use in machine learning datasets. When labeling please select one of the options provided for each image shown.')
st.write('---')

#Image Display
image_column, rating_column = st.columns((0.6, 0.4))
with image_column:
    st.image(images[counter])
with rating_column:
    options = np.arange(0, 10.1, 0.1)
    options = np.round(options, 1)
    rating = st.select_slider(label = 'Image Rating', options = options, value = 5)
    
    #Button Press
    if st.button('Next Image'):
        label_directory = "C:/Users/space/Desktop/CS Projects/AI Photo Rater/Landscape Labels/"
        label_name = label_directory + file_list[counter].split('.')[0] + '.txt'
        try:
            with open(counter_path, 'w') as file:
                counter = file.write(str(counter + 1)) # Read the content and strip any surrounding whitespace
        except Exception as e:
            print(f"An error occurred: {e}")
        try:
            with open(label_name, 'w') as file:
                file.write(str(rating))
                print(f"Label file '{label_name}' created with rating: {rating}")
        except Exception as e:
            print(f"An error occurred: {e}")
        st.rerun()
        
