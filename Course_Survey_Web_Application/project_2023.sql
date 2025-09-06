PRAGMA foreign_keys=ON;
BEGIN;


CREATE TABLE student
(
  student_id INTEGER NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (student_id),
  UNIQUE (email)
);

CREATE TABLE course
(
  course_id INTEGER NOT NULL,
  course_code VARCHAR(255) NOT NULL,
  title VARCHAR(255) NOT NULL,
  PRIMARY KEY (course_id),
  UNIQUE (title)
);

CREATE TABLE take_course
(
  take_course_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  PRIMARY KEY (take_course_id)
  FOREIGN KEY (course_id) REFERENCES course(course_id)
  FOREIGN KEY (student_id) REFERENCES student(student_id)
  UNIQUE (student_id, course_id)
);


CREATE TABLE question
(
  question_id INTEGER NOT NULL,
  question_text INTEGER NOT NULL,
  PRIMARY KEY (question_id)
);

CREATE TABLE answer
(
  answer_id INTEGER NOT NULL,
  answer_text VARCHAR(255) NOT NULL,
  answer_value INTEGER,
  PRIMARY KEY (answer_id)
);


CREATE TABLE survey_response
(
  take_course_id INTEGER NOT NULL,
  question_id INTEGER NOT NULL,
  answer_id INTEGER NOT NULL,
  PRIMARY KEY (take_course_id, question_id),
  FOREIGN KEY (question_id) REFERENCES question(question_id),
  FOREIGN KEY (answer_id) REFERENCES answer(answer_id),
  FOREIGN KEY (take_course_id) REFERENCES take_course(take_course_id),
  UNIQUE (question_id, take_course_id)
);


insert into student (student_id,email) values (1,"s1@bi.no");

insert into student (student_id,email) values (2,"s2@bi.no");

insert into student (student_id,email) values (3,"s3@bi.no");

insert into student (student_id,email) values (4,"s4@bi.no");

insert into student (student_id,email) values (5,"s5@bi.no");



insert into course (course_id, course_code, title) values (1,"EBA3400","Programming Data Extraction & Visualization");

insert into course (course_id, course_code, title) values (2,"EBA1800","Mathematics for Data Science");

insert into course (course_id, course_code, title) values (3,"EBA3420","Databases (SQL)");

insert into course (course_id, course_code, title) values (4,"EBA3420","Databases (Web Programming)" );

insert into course (course_id, course_code, title) values (5,"EBA2904","Statistics with Programming");



insert into take_course (take_course_id, course_id, student_id) values (1,1,1);
insert into take_course (take_course_id, course_id, student_id) values (2,1,2);


insert into question (question_id, question_text) values (1, "I have got a clear idea of what is expected of me in this course.");

insert into question (question_id, question_text) values (2, "The lecturer(s) in this course presented the course contents well.");

insert into question (question_id, question_text) values (3, "The course literature has supported my learning.");

insert into question (question_id, question_text) values (4, "I have acquired new and relevant knowledge in the course area.");


insert into answer (answer_id, answer_text) values (0, "I don’t know");

insert into answer (answer_id, answer_text, answer_value) values (1, "Strongly disagree", 1);

insert into answer (answer_id, answer_text, answer_value) values (2, "Disagree", 2);

insert into answer (answer_id, answer_text, answer_value) values (3, "Neutral", 3);

insert into answer (answer_id, answer_text, answer_value) values (4, "Agree", 4);

insert into answer (answer_id, answer_text, answer_value) values (5, "Strongly agree", 5);


insert into survey_response (take_course_id, question_id, answer_id) values (1,1,5);
insert into survey_response (take_course_id, question_id, answer_id) values (1,2,5);
insert into survey_response (take_course_id, question_id, answer_id) values (1,3,4);
insert into survey_response (take_course_id, question_id, answer_id) values (1,4,5);

insert into survey_response (take_course_id, question_id, answer_id) values (2,1,4);
insert into survey_response (take_course_id, question_id, answer_id) values (2,2,5);
insert into survey_response (take_course_id, question_id, answer_id) values (2,3,4);
insert into survey_response (take_course_id, question_id, answer_id) values (2,4,5);


COMMIT;