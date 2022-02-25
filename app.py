import streamlit as st
import geopandas as gpd
import requests
'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string).
# Or as with this paragraph using the `st.` functions
# ''')
st.title('Taxi Fares in New York City')
# '''
# ## Here we would like to add some controllers in order to ask the user
# # to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
date = st.date_input('Pickup Date')
time = st.time_input('Pickup Time')
pickup_location = st.text_input('Pickup Location')
dropoff_location = st.text_input('Dropoff Location')
passenger_count = st.slider('Number of Passengers', 0,6)
pickup_longitude, pickup_latitude = gpd.tools.geocode(pickup_location)
dropoff_longitude, dropoff_latitude = gpd.tools.geocode(dropoff_location)
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to
know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''
2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if url == 'https://taxifare.lewagon.ai/predict':


    url = 'https://taxifare.lewagon.ai/predict'

    query = dict(datetime = (date+time), pickup_longitude=pickup_longitude,
                            pickup_latitude=pickup_latitude,
                            dropoff_longitude=dropoff_longitude,
                            dropoff_latitude=dropoff_latitude,
                            passenger_count =passenger_count)

    response = requests.get(url, params = query)

st.markdown(f'Fare: f{response.json()}')
