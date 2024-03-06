import canvasapi
import openai
from dotenv import load_dotenv
import os

print(load_dotenv())


# load .env variables
load_dotenv()

# retrieve env vars
canvas_api_key = os.getenv('CANVAS_API')
openai_api_key = os.getenv('OPENAI_API_KEY')

CANVAS_URL = "https://canvas.nus.edu.sg/"
print(canvas_api_key)
canvas = canvasapi.Canvas(CANVAS_URL, canvas_api_key)
courses = canvas.get_courses()
c_arr = []
for course in courses:
    try:
        print(course.name)
        c_arr.append(course)
    except:
        continue

# specify the course id
course_id = c_arr[0].id

# get the course by id
course = canvas.get_course(course_id)

# get the files of the course
files = course.get_files()

# print the files
for file in files:
    print(f"File: {file.display_name} - {file.id} - {file.url}")