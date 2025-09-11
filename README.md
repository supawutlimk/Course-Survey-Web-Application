# Course Survey Web Application

## Overview

This project was developed as part of the EBA3420 Databases course at BI Norwegian Business School (Spring 2023). The goal was to design and implement a web application for course evaluations that allows students to take surveys and view summarized results.

The project demonstrates skills in:

- Database design (ER & relational models)

- SQL (DDL & DML)

- Web development with Flask

- Data collection and visualization

## Features

- Homepage with welcome message and navigation.

- Take a Survey:
  - Email input (non-anonymous survey).
  - Course selection from dropdown.
  - Four evaluation questions with Likert-scale answers.
  - Duplicate submission prevention.

- View Survey Results:

- Course list with links.

- Summary of survey results per course (statistics + visualizations).

## Database Design

Entities: Student, Course, Question, Answer, Survey Response, Take_Course.

Constraints:

- Each student has one unique email.

- A student can take multiple surveys, but only once per course.

- Course ID uniquely identifies course code and title.

![imagealt](https://github.com/supawutlimk/Course-Survey-Web-Application/blob/1180398df3c243fa4979cbdfa3e0d6abfeb97feb/images/ER_Diagram.png)

![imagealt](https://github.com/supawutlimk/Course-Survey-Web-Application/blob/f8a1a88b020e035056596f4b634445165db16df7/images/Relational_Schema.png)

## Design Decisions & Assumptions

The database schema could have been reduced to fewer tables (e.g., student, course, survey_response).

However, I intentionally kept additional tables such as take_course to improve usability:

- This allows the system to quickly check whether a student has already taken a survey by only filling out their email and selecting a course.

- Without this, students would need to fill out their email, select a course, and answer all questions just to find out they already submitted a response.

- This design choice prioritizes user experience and data integrity over minimal schema size.

## Tech Stack

Backend: Python (Flask)

Database: SQLite

Frontend: HTML, Bootstrap, Chart.js

Tools: VS Code, DB Browser for SQLite

## Example
![imagealt](https://github.com/supawutlimk/Course-Survey-Web-Application/blob/f5572708e82c1b39e9f76851b473aecbbb80aaf7/images/Interface.png)

## Example Survey Questions

1. I have got a clear idea of what is expected of me in this course.
2. The lecturer(s) presented the course contents well.
3. The course literature supported my learning.
4. I have acquired new and relevant knowledge.
   
## Learning Outcomes
- Applied database normalization (3NF) in schema design.
- Built a relational database and integrated it with Flask.
- Created a full workflow: data entry → storage → analysis → visualization.
- Gained experience in building reproducible and documented analytics projects.
