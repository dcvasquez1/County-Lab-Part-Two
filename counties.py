from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def get_2014_population(counties, selected_state):
    total = 0
    for c in counties:
        if c["State"] == selected_state:
            total_population += c["Population"]["2014 Population"]
    return str(total_population)


if __name__=="__home__":
    app.run(debug=False, port=54321)

@app.route("/")
def render_main():
    with open('static/county_demographics.json') as demographicsdata
        counties = json.load(demographicsdata)
    if 'State' in request.args:
        sel_state = request.args["State"]
        return render_template('home.html', response_options = get_state_options(counties), response_population = get_2014_population(counties, sel_state), response_state = sel_state)
    return render_template('home.html', response_options = get_state_options(counties))