# A Simple Weather App

### Video Demo on Youtube: ([A Simple Weather App | Final Project For CS50's Introduction To Programming With Python](https://youtu.be/JP5eYi4u6_Q?si=HXMIFrml8LTCs8wg))

---
![](images\project-title.png)

---

## Introduction and Structure:
Namaste/Hello 🙏🏻, I'm Vijay Jadhav from Maharashtra, India. This is my CS50P Final Project, a Simple Weather App in Python with three functions and a Test File to conduct Tests.

  Project Structure:
  - project.py
  - test_project.py
  - README.md
  - requirements.txt
  - images (folder)

---
## Libraries:
I used following libraries in this project-
  1. tabulate ([https://pypi.org/project/tabulate/](https://pypi.org/project/tabulate/))
  2. pyfiglet ([https://pypi.org/project/pyfiglet/](https://pypi.org/project/pyfiglet/))
  3. requests ([https://pypi.org/project/requests/](https://pypi.org/project/requests/))
  4. datetime ([https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html))

## Libraries to be installed:
Libraries needed to be installed are
1. pyfiglet (version: 1.0.2) - To install 'pyfiglet' execute the following command in terminal:
    > pip install pyfiglet

2. tabulate (version: 0.9.0) - To install the Python library and the command line utility, run:
    > pip install tabulate

3. requests (version: 0.9.0) - To install 'requests' execute the following command in terminal:
    > pip install requests

---

## Usage :
0. In the terminal excute command :
    > python project.py

    then we get following welcome message.

![](<images\usage screenshot-1.png>)

There are 3 options available in the main menu-
1. Current Weather of a city of your choice.no
2. Current Air Quality of a city of your choice.
3. EXIT

Let's see how they work-

1. Current Weather of a City:

=> Typing '1' shows us a message ("Check current Weather of the city with its name") and then asks us to enter a city name.

 => Entering a city name shows us the weather data of that particular city in table format. (let's see the following example of Pune city)
![](<images\usage screenshot-2.png>)

=> It is again asking whether we want to search for another city's weather data (enter 'yes') or go back to the main menu (enter 'no').

=> Entering 'yes' asks for the city name; this cycle continues until we enter 'no' and goes back to the main menu.

=> If we enter an incorrect input or city name, it will alert with an alert message. See the following image:

![](<images\usage screenshot-3.png>)

=> Entering 'no', we come back to the main menu, and then it again asks us to select an option from the above three options in the main menu.

2. Current Air Quality of a City:
=> To select 2nd option, we need to enter '2', and then it shows a message ("Check the air quality of the city of your choice") and asks for the city name.

=> After entering the city name, it gives air quality data for that particular city, and again asks whether we want to search the air quality data of another city (enter 'yes') or go back to the main menu (enter 'no'). See the following image:

![](<images\usage screenshot-4.png>)

=> Entering 'yes' asks for the city name; this cycle continues until we enter 'no' and goes back to the main menu.

=> If we enter an incorrect input or city name, it will alert with an alert message. See the following image:

![](<images\usage screenshot-5.png>)

=> Entering 'no', we come back to the main menu, and then it again asks us to select an option from the above three options in the main menu.

3. EXIT :
=> To select 3rd option, we need to enter '3', and then it shows a message ("Write your suggestions for any improvement or any new feature.") and asks to enter 1 or 2.
=> Entering '1', needs to write our suggestions and pressing 'enter' button will show the thanking message. See the following image:

![](<images\usage screenshot-6.png>)

=> Thats how programme works!

---

## Functions:
  - def main():
    This is the main function obviously which displays the main part of the Weather App, like welcome message, starting menu and exit thanking message, etc.

  - def current_weather(city_name):
    This function take city_name as argument and returns the current weather data, otherwise prints an alert message for incorrect city name.

  - def get_city_lat_long(city_name='delhi'):
    The get_city_lat_long() fn will return tuple of values namely- latitude, longitude and country of the given city if the given city name is correct,
    otherwise prints 'city not found' message.

  - def air_quality(city_name):
    This Fn will print current Air Quality data of the given city if the city name is correct,
    otherwise print 'city not found' message.

---

## Authors:
  - Vijay Jadhav (Maharashtra, India)
  - You can connect with me on:
    - GitHub Profile - ([click here](https://github.com/vijay-jadhav1997))
    - LINKEDIN Profile - ([click here](https://www.linkedin.com/in/vijay-jadhav1997))

