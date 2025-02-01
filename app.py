from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website!"

@app.route('/weather', methods=['GET', 'POST'])
def weather_submit():
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'c6870865e0b99fdacffb13422b023b7f'
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': api_key, 'units': 'imperial'}
        response = requests.get(base_url, params=params)
        weather_data = response.json()
        
        if weather_data['cod'] == 200:
            weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon']
            }
        else:
            weather = None

        return render_template('weather.html', weather=weather)
    
    return render_template('weather.html', weather=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
