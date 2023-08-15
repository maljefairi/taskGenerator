from flask import Flask, render_template
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, 'generated_activities.json')

app = Flask(__name__)

@app.route('/')
def activities_table():
    print("Trying to open file at:", JSON_PATH)
    with open(JSON_PATH, 'r') as file:
        activities = json.load(file)

    # Primary regular expression pattern
    pattern1 = re.compile(r'Activity Name: (.*?) RS [pP]oints:')
    # Fallback regular expression pattern
    pattern2 = re.compile(r'Activity Name: (.*)')

    for activity in activities:
        match = pattern1.search(activity["Activities"])
        if match:
            activity["Activities"] = match.group(1).strip()
        else:
            match = pattern2.search(activity["Activities"])
            if match:
                activity["Activities"] = match.group(1).strip()
            else:
                activity["Activities"] = re.split(r'\t|\d', activity["Activities"])[0].replace('"', '').replace("'", '').strip()

    return render_template('table_template.html', activities=activities)

if __name__ == '__main__':
    app.run(debug=True)
