import time

import streamlit as st
import requests
import random

# NASA API key
API_KEY = 'Xw8AUhfbqSqn5TxTRvrPrjeJZKTNpBnVFiArC3gu'

def get_random_image():
    # Fetch today's Astronomy Picture of the Day from the NASA API
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count=5")
    dataTEMP = response.json()

    # Choose a random image from the list
    index = random.randint(0, len(dataTEMP)-1)
    image_data = dataTEMP[index]

    return image_data

def main():
    image_data = get_random_image()

    # Display the image
    if image_data['media_type'] == 'image':
        image_url = image_data['url']
        st.image(image_url, caption=image_data['title'], use_column_width=True)

        # Display the title and explanation of the image
        st.write(f"# {image_data['title']}")
        st.write(image_data['explanation'])
    else:
        st.write("Sorry, this media type is not supported.")

    # Rerun the app every 5 seconds
    time.sleep(20)
    st.experimental_rerun()

if __name__ == '__main__':
    main()
