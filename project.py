from pyfiglet import Figlet
from tabulate import tabulate
import requests

from datetime import datetime


#? Simple Weather App with following features
#? 1) current weather data for any location
#? 2) Get the solar data by particular location and calculate energy generation!
#? 3) Air Pollution data


def main():
    figlet = Figlet(font='ogre')
    print(figlet.renderText("Welcome To The Weather App"))
    option = '1'
    while option != '3' :
        print(
            "\nSelect what would you prefer to search from following => ",
            "1) Current weather of a city of your choice.",
            "2) Current Air quality of a city of your choice.",
            "3) EXIT ", sep="\n"
        )
        option = input("# Enter 1, 2 or 3. => ").strip()
        if option == '1':
            back = 'yes'
            while back != 'no':
                if back == 'yes':
                    print("\n Check Weather of the city with its name 💯")
                    city = input("# Enter a city name: ").strip().title()
                    weather_data = current_weather(city)
                    print(weather_data)
                    print(
                        "\n1) Enter 'yes' to search another city weather data.",
                        "2) Enter 'no' to go back to Main Menu", sep='\n'
                    )
                else:
                    print(
                        "\n 🤔 Oops! ❌❌ Invalid input ❌❌.",
                        "👉🏻 Please Enter valid response",
                        "1) Enter 'yes' to search another/same city weather data.",
                        "2) Enter 'no' to go back to Main Menu", sep='\n'
                    )
                back = input("Enter 'yes' or 'no' => ").strip().lower()
        elif option == '2':
            back = 'yes'
            while back != 'no':
                if back == 'yes':
                    print("\n Check Air Quality of the city with its name 💯")
                    city = input("# Enter city name: ").strip().title()
                    air_quality_data = air_quality(city)
                    print(air_quality_data[0], air_quality_data[1], sep='\n')
                    print(
                        "\n1) Enter 'yes' to search another city Air Quality data.",
                        "2) Enter 'no' to go back to Main Menu", sep='\n'
                    )
                else:
                    print(
                        "\n 🤔 Oops! ❌❌ Invalid input ❌❌.",
                        "👉🏻 Please Enter valid response",
                        "1) Enter 'yes' to search another city Air Quality data.",
                        "2) Enter 'no' to go back to Main Menu", sep='\n'
                    )
                back = input("Enter 'yes' or 'no' => ").strip().lower()
        else:
            print("\n 📝 => Write your suggestions for any improvement or/and any new feature.", "1) If any suggestion", "2) No suggestions", sep="\n")

            suggestion = input("# Enter 1 or 2 => ")
            if suggestion == '1':
                input("✏ # Your suggestions => ")
                print("\n 🙏🏻 We're thankful to you for your noteworthy suggestions! 🙏🏻 \n")
            figlet = Figlet(font='doom')
            print(figlet.renderText("Feel free to visit Again !!"))



#* Access current weather data of any location:
def current_weather(city_name):
    """
    This functions returns current weather data of the given city if the city name is correct,
    otherwise returns 'city not found' message.

    Args:
        city_name (str): The name of the city
    """
    metric = "metric"
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=a73d68f9bcb2329ef697a7b1f304b10b&units={metric}")
        data = response.json()
        if response.status_code == 200:
            weather_data_lists = [
                ["City Name", data['name']],
                ["Country", data['sys']['country']],
                ["Date ", datetime.fromtimestamp(data['dt']).strftime(r"%d-%m-%Y") ],
                ["Time ", datetime.fromtimestamp(data['dt']).strftime(r"%H:%M") ],
                ["Weather", data['weather'][0]['description']],
                ["Temperature", f"{data['main']['temp']} ॰C"],
                ["Feels-like Temp", f"{data['main']['feels_like']} ॰C"],
                ["Min Temp", f"{data['main']['temp_min']} ॰C"],
                ["Max Temp", f"{data['main']['temp_max']} ॰C"],
                ["Pressure", f"{data['main']['pressure']}hPa"],
                ["Humidity", f"{data['main']['humidity']}%"],
                ["Wind Speed", f"{round(data['wind']['speed'] * (3.6), 2)}km/h"],
                ["Visibility", f"{round((data['visibility']/1000), 2)}km"],
                ["Sunrise", datetime.fromtimestamp(data['sys']['sunrise']).strftime(r"%H:%M")],
                ["Sunset", datetime.fromtimestamp(data['sys']['sunset']).strftime(r"%H:%M")],
            ]
            return tabulate(weather_data_lists, tablefmt="grid")
        else:
           return "\n City not found ❌; Please, enter correct city name!"
    except :
        return "\nOops🧐, Please check your network connection ❌🔄"



#* get_city_lat_long() fn returns latitude and longitude of the given city
def get_city_lat_long(city_name='delhi'):
    """
    get_city_lat_long() fn will return tuple of values namely- latitude, longitude and country of the given city if the given city name is correct,
    otherwise print 'city not found' message.

    Args:
        city_name (str): The name of the city
    """
    try:
        city_response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid=a73d68f9bcb2329ef697a7b1f304b10b")
        city_data = city_response.json()
        if city_response.status_code == requests.codes.ok and city_data != []:
            return (city_data[0]["lat"], city_data[0]["lon"], city_data[0]["country"], city_data[0]["name"])
        else:
            print("\n🧐 City Not Found!❌ Please enter correct city name.")
    except:
        print("\nOops🧐, Please check your network connection ❌🔄")




#* air_quality function prints Air Quality status of the given city
def air_quality(city_name):
    """
        This Fn retuns current Air Quality data of the given city if the city name is correct,
        otherwise print 'city not found' message.

        Args:
            city_name (str): The name of the city
    """
    try:
        lat, lon, country, city = get_city_lat_long(city_name)
        response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid=a73d68f9bcb2329ef697a7b1f304b10b")
        data = response.json()
        if response.status_code == 200 :
            air_purity= ['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor']
            air_quality_data_lists = [
                ["City Name", city],
                ["Country", f"{country}"],
                ["Date ", datetime.fromtimestamp(data['list'][0]['dt']).strftime(r"%d-%m-%Y") ],
                ["Time ", datetime.fromtimestamp(data['list'][0]['dt']).strftime(r"%H:%M") ],
                ["Air Quality", air_purity[data['list'][0]['main']['aqi'] - 1]],
            ]
            pollutants_data_lists = [
                ["Carbon monoxide (co)", data['list'][0]['components']['co']],
                ["Nitrogen monoxide (No)", data['list'][0]['components']['no']],
                ["Nitrogen dioxide (No2)", data['list'][0]['components']['no2']],
                ["Ozone (o3)", data['list'][0]['components']['o3']],
                ["Sulphur dioxide (so2)", data['list'][0]['components']['so2']],
                ["Particulate matter (pm2_5)", data['list'][0]['components']['pm2_5']],
                ["Particulate matter (pm10)", data['list'][0]['components']['pm10']],
                ["NH3", data['list'][0]['components']['nh3']],
            ]
            headers =  ["Components", 'Pollutant concentration in µg/m3']
            return (tabulate(air_quality_data_lists, tablefmt="grid"), tabulate(pollutants_data_lists, headers, tablefmt="pretty"))
    except:
        return ("", "")




if __name__ == "__main__":
    main()
