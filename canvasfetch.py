import canvasapi
import openai
from dotenv import load_dotenv
import os
import requests

print(load_dotenv())


# load .env variables
load_dotenv()

# retrieve env vars
canvas_api_key = os.getenv('CANVAS_API')
openai_api_key = os.getenv('OPENAI_API_KEY')

CANVAS_URL = "https://canvas.nus.edu.sg/"
canvas = canvasapi.Canvas(CANVAS_URL, canvas_api_key)
courses = canvas.get_courses()

courses = [course for course in courses if hasattr(course, 'name')]
print(", ".join([course.name for course in courses]))

for course in courses:
    files = iter(course.get_files())
    os.makedirs(f"Docs/{course.name}", exist_ok=True)
    while True:
            try:
                file = next(files)
                if hasattr(file, 'url') and file.display_name.endswith('.pdf'):
                    file_path = f"Docs/{course.name}/{file.display_name}"
                    if os.path.exists(file_path):
                        print(f"File {file.display_name} already exists.")
                        continue
                    else:
                        response = requests.get(file.url)
                        if response.status_code == 200:
                            print("Success", file.display_name)
                            with open(f"Docs/{course.name}/{file.display_name}", 'wb') as f:
                                f.write(response.content)
                        else:
                            print("Failed:",file.display_name)
            except (canvasapi.exceptions.Unauthorized, canvasapi.exceptions.Forbidden):
                print("Unauthorized to access file or request error:", file.display_name)
                continue
            except StopIteration:
                break
    if len(os.listdir(f"Docs/{course.name}")) == 0:
        os.rmdir(f"Docs/{course.name}")


""" c_arr = []
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
file_arr = []
for file in files:
    file_arr.append((file.display_name, file.id, file.url))
    print(f"File: {file.display_name} - {file.id} - {file.url}")

response = requests.get(file_arr[0][2])

if response.status_code == 200:
    print("Success")
    _, file_extension = os.path.splitext(file_arr[0][0])
    with open(f"test{file_extension}", 'wb') as f:
        f.write(response.content) """