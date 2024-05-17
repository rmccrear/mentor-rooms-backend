from flask import Flask, render_template, request, jsonify
from setup_db import reset_db

app = Flask('app')

from replit import db
import json
from flask_cors import CORS

app = Flask('app')

CORS(app)

@app.route('/reset-db')
def reset():
  reset_db()
  return "done"


@app.route('/')
def hello():
  return render_template('front-page.html')
  
@app.route('/mentors')
def mentor_dashboard():
    user_name=request.headers['X-Replit-User-Name']
    mentor = None
    if user_name:
      mentors = fetchMentors()
      print(mentors)
      mentor = findMentor(user_name, mentors)
    else: 
      mentor = False
    return render_template(
        'index.html',
        mentor=mentor,
        user_id=request.headers['X-Replit-User-Id'],
        user_name=request.headers['X-Replit-User-Name'],
        user_roles=request.headers['X-Replit-User-Roles'],
        user_bio=request.headers['X-Replit-User-Bio'],
        user_profile_image=request.headers['X-Replit-User-Profile-Image'],
        user_teams=request.headers['X-Replit-User-Teams'],
        user_url=request.headers['X-Replit-User-Url']
    )

def fetchDbJson(key):
  data = db[key]
  if not data:
    return None
  else:
    return json.loads(data)

def putDbJson(key, val):
  db[key] = val

def fetchMentors():
  mentors = fetchDbJson("mentor-data")
  if not mentors:
    return []
  else:
    return mentors

def putMentors(mentors):
  db["mentor-data"] = json.dumps(mentors)

def findMentor(username, mentors):
  for mentor in mentors:
    if mentor["username"] == username:
      return mentor
  return None

@app.route('/get-status')
def get_status():
  mentors = fetchMentors()
  return mentors

@app.route('/clock-in')
def clock_in_out():
  user_name=request.headers['X-Replit-User-Name']
  if(not user_name):
    return {"error": "not signed in"}
  else:
    mentors = fetchMentors()
    mentor = findMentor(user_name, mentors)
    if not mentor:
      return {"error": "not a registered mentor"}
    else:
      mentor["availableNow"] = not mentor["availableNow"]
      putMentors(mentors)
      return jsonify(mentor)

@app.route('/toggle-full')
def room_full():
  user_name=request.headers['X-Replit-User-Name']
  if(not user_name):
    return {"error": "not signed in"}
  else:
    mentors = fetchMentors()
    mentor = findMentor(user_name, mentors)
    if not mentor:
      return {"error": "not a registered mentor"}
    else:
      mentor["roomFull"] = not mentor["roomFull"]
      putMentors(mentors)
      return jsonify(mentor)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

