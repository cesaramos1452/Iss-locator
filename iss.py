#!/usr/bin/env python
import requests
import turtle

__author__ = 'Cesaramos1452@yahoo.com'


def in_space():
    """Send an api call to space api and extract info on
    astronauts that are currently in space!"""
    api = 'http://api.open-notify.org/astros.json'
    # Api call extracts JSON
    res = requests.get(api).json()
    names = ', '.join([dic.get('name') for dic in res['people']])
    craft = res['people'][0]['craft']
    total_inspace = res['number']
    summary = (f"""These {total_inspace} men, {names} are all astronauts who are
    currently in space on board of the {craft} spacecraft!""")
    return summary


def current_coords():
    """Sends an api call to extract the current coordinates and
    timestamp of ISS SpaceCraft!"""
    api = 'http://api.open-notify.org/iss-now.json'
    # Api call extracts JSON
    res = requests.get(api).json()
    lon = res['iss_position']['longitude']
    lat = res['iss_position']['latitude']
    return {'lon': float(lon), 'lat': float(lat), 'timestamp': res['timestamp']}


s = turtle.Screen()
s.setup(width=720, height=360)  # BOOM!
s.bgpic('map.gif')
s.setworldcoordinates(-180, -90, 180, 90)
s.addshape('iss.gif')

iss = turtle.Turtle()
indy = turtle.Turtle()

iss.shape('iss.gif')
iss.penup()
iss.goto(current_coords()['lon'], current_coords()['lat'])

indy.penup()
indy.goto(-86.148003, 39.791000)
indy.dot(5, 'yellow')
indy.hideturtle()

turtle.done()
# def main():
#     pass


# if __name__ == '__main__':
#     main()
