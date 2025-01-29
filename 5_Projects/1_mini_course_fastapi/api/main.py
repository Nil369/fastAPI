from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from enum import Enum
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:*",
    "http://localhost:8080",
    "http://localhost:5500",
    "http://localhost:5500",
    "http://127.0.0.1:5500/"
]
#  Handling CORS errors & Enabling CORS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# creating enum for course category
class CourseCategory(str, Enum):
    web_dev = "Web Development"
    data_science = "Data Science"
    ai = "Artificial Intelligence"
    cloud = "Cloud Computing"
    cyber_security = "Cyber Security"

# pydantic model for course
class Course(BaseModel):
    id:int
    title:str
    price:float
    teacher:str
    description:str


# Fake Database:
courseDB = []


@app.post("/add-courses/")
def create_course(course:Course):
    # check if id exits:
    for existing_course in courseDB:
        if existing_course.id == course.id:
            raise HTTPException(status_code=400, detail="Course ID already exists")

    courseDB.append(course)
    return {"message":"Course Created Successfully!","course":course}


@app.get("/courses/")
def get_courses():
    return {"courses": courseDB}


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    for course in courseDB:
        if course.id == course_id:
            return {"course": course}
    raise HTTPException(status_code=404, detail="Course not found")


@app.put("/courses/{course_id}")
def update_course(course_id: int, updated_course: Course):
    for index, course in enumerate(courseDB):
        if course.id == course_id:
            courseDB[index] = updated_course
            return {"message": "Course updated successfully!", "course": updated_course}
    
    raise HTTPException(status_code=404, detail="Course not found")


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    for index, course in enumerate(courseDB):
        if course.id == course_id:
            deleted_course = courseDB.pop(index)
            return {"message": "Course deleted successfully!", "course": deleted_course}
    
    raise HTTPException(status_code=404, detail="Course not found")
