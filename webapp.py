from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographicsdata
        counties = json.load(demographicsdata)
    
    reply_list = get_state_options(counties)
    
    if 'State' in request.args:
        sel_state = request.args["State"]
        fact = fact_function()
        reply_state = sel_state
        return render_template('home.html', reply_list, fact, reply_state)
    
    return render_template('home.html', reply_list)


def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def fact_function():
    return "*interesting fact"

if __name__=="__home__":
    app.run(debug=False, port=54321)
