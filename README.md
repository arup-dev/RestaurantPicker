# RestaurantPicker
Python script that returns details of top 10 restaurants of a given city 

#**Requirements to use**
1.A Google API key with Google Places API and Geocoding API enabled
2.A stable version of Python 
3.Install required binaries called "requests" by using "pip install requests" as it used for querying

#**Instructions on how to use**
1. Either pull the files or extract the contents of the zip folder to a directory of your choice.
2. Then create a file called config.json in the directory and add your api key to it in the following format-

> {
    "api_key": "YOUR API KEY HERE"
  }

3.Save the file and close it
4.Run RestaurantPicker.py
5.A json file having the name "top_10_restaurants_(city name here)" will be generated containing all the details
