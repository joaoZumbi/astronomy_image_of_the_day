import streamlit as st
import requests
import datetime
from PIL import Image

# NASA API key
API_KEY = "Xw8AUhfbqSqn5TxTRvrPrjeJZKTNpBnVFiArC3gu"

# Load previous date from a file, or start at today if file doesn't exist
try:
    with open('last_date.txt', 'r') as f:
        last_date = f.read()
        last_date = datetime.datetime.strptime(last_date, '%Y-%m-%d').date()
except FileNotFoundError:
    last_date = datetime.date.today() - datetime.timedelta(days=2)

# Check if a day has passed since the last visit
today = datetime.date.today()
if today > last_date:
    # Fetch today's Astronomy Picture of the Day from the NASA API
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
    data = response.json()

    # Display the image
    if data['media_type'] == 'image':
        image_url = data['url']
        image = Image.open(requests.get(image_url, stream=True).raw)
        st.image(image, caption=data['title'], use_column_width=True)
        # Display the title and explanation of the image
        st.write(f"# {data['title']}")
        st.write(data['explanation'])
    else:
        st.write("Sorry, this media type is not supported.")

    # Save the current date
    with open('last_date.txt', 'w') as f:
        f.write(str(today))

    # Save the current image URL
    with open('last_image_url.txt', 'w') as f:
        f.write(data['url'])

else:
    # Display the image from the last visit
    with open('last_image_url.txt', 'r') as f:
        last_image_url = f.read()
    if last_image_url:
        last_title = last_image_url.split('/')[-1]
        image = Image.open(requests.get(last_image_url, stream=True).raw)
        st.image(image, caption=last_title, use_column_width=True)
    else:
        st.write("No image available.")


