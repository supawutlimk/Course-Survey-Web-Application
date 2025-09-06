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

![imagealt](https://github.com/supawutlimk/Course-Survey-Web-Application/blob/e298bbccd49b1dfc135a54696f9bc4ae7dd0bd43/Relational_Schema.png)

## Tech Stack

Backend: Python (Flask)

Database: SQLite

Frontend: HTML, Bootstrap, Chart.js

Tools: VS Code, DB Browser for SQLite
