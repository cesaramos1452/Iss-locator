#!/usr/bin/env python
import requests
import turtle
import time

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
    summary = (f"""These {total_inspace} astronauts, {names} are all astronauts who are
    currently in space on board of the {craft} spacecraft!""")
    print(summary)


def current_coords():
    """Sends an api call to extract the current coordinates and
    timestamp of ISS SpaceCraft!"""
    api = 'http://api.open-notify.org/iss-now.json'
    # Api call extracts JSON
    res = requests.get(api).json()
    lon = res['iss_position']['longitude']
    lat = res['iss_position']['latitude']
    return {'lon': float(lon), 'lat': float(lat),
            'timestamp': res['timestamp']}


def over_indy():
    """Make an api call to get the estimation
    time of when The ISS will be overhead Indy"""
    api = 'http://api.open-notify.org/iss-pass.json'
    payload = {'lat': 39.791000, 'lon': -86.148003}
    res = requests.get(api, params=payload).json()
    next_pass = time.ctime(int(res['request']['datetime']))
    return next_pass


def draw_iss():
    """Creates a world map using turtle module
    that displays current Location of ISS
    SpaceCraft and display Indianapolis, Indiana!"""
    # Turtle setup
    s = turtle.Screen()
    s.setup(width=720, height=360)
    s.bgpic('map.gif')
    s.setworldcoordinates(-180, -90, 180, 90)
    s.addshape('iss.gif')
    # Iss Craft turtle and Indy turtle setup
    iss = turtle.Turtle()
    indy = turtle.Turtle()

    iss.shape('iss.gif')
    iss.penup()
    iss.goto(current_coords()['lon'], current_coords()['lat'])

    indy.penup()
    indy.goto(-86.148003, 39.791000)
    indy.dot(5, 'yellow')
    indy.color('turquoise')
    indy.write(over_indy(), align='center',
               font=("Arial", 10, 'normal',
                     'bold', 'italic', 'underline'))
    indy.hideturtle()

    turtle.done()


def main():
    in_space()
    draw_iss()


if __name__ == '__main__':
    main()
