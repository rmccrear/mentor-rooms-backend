from replit import db
import json

mentor_list = [
  "rmccrear",
  "kimbrow1",
  "briankimbrow",
  "rolazaraberin",
  "fernandolopez93"
]

mentor_data = [
  {
    "username": "rmccrear",
    "displayName": "Robert",
    "meetLink": "https://meet.google.com/dbb-vibo-nov",
    "availableNow": False,
    "roomFull": False
  },
  {
    "username": "RafaelSequeiros",
    "displayName": "Rafael",
    "meetLink": "https://meet.google.com/oto-vgwk-dag",
    "availableNow": False,
    "roomFull": False
  },
  {
    "username": "rolazaraberin",
    "displayName": "Rolazar",
    "meetLink": "https://meet.google.com/nhf-ehvv-fiz",
    "availableNow": False,
    "roomFull": False
  },
  {
    "username": "kimbrow1",
    "displayName": "Brian",
    "meetLink": "https://meet.google.com/imh-koyz-onm",
    "availableNow": False,
    "roomFull": False
  },
  {
    "username": "briankimbrow",
    "displayName": "Brian Kimbrow",
    "meetLink": "https://meet.google.com/imh-koyz-onm",
    "availableNow": False,
    "roomFull": False
  },
  {
    "username": "fernandolopez93",
    "displayName": "Fernando",
    "meetLink": "https://meet.google.com/bob-kayi-rrn",
    "availableNow": False,
    "roomFull": False
  }
]

def reset_db():
  print(db)
  db["mentor-list"] = mentor_list
  db["mentor-data"] = json.dumps(mentor_data)

if __name__ == "__main__":
  db["mentor-list"] = mentor_list
  db["mentor-data"] = json.dumps(mentor_data)

