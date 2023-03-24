
import requests
import streamlit as st

url = "https://api.nasa.gov/planetary/apod?api_key=Xw8AUhfbqSqn5TxTRvrPrjeJZKTNpBnVFiArC3gu"

response = requests.get(url)
content = response.json()
image = content["hdurl"]

# Display the image in the Streamlit app
# st.image(response.content, caption='Image from the internet')
st.image(image, caption='Image from the internet')
st.subheader(content["title"])
st.write(content["explanation"])

