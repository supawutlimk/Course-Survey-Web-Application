from flask import Flask, render_template, redirect, url_for, request, abort, g, flash

import sqlite3
import json

DATABASE = 'project_2023.db'

app = Flask(__name__)
app.secret_key = "boobie_boobie"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, isolation_level=None)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()





@app.route("/")
def home():
    return render_template("home.html")



#first page
@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        form = request.form
        try:
            get_db().cursor().execute("""
                INSERT INTO student(email)
                VALUES (?)
            """, [form.get('email')])

        except sqlite3.Error:
            pass

        try: 
            get_db().commit()
            student_id = get_db().cursor().execute("""
                SELECT student_id
                FROM student
                WHERE email=?
            """, [form.get('email')]).fetchone()[0]

            get_db().cursor().execute("""
                INSERT INTO take_course(student_id, course_id)
                VALUES (?,?)
            """, [student_id, form.get('course_id')])

            #get_db().commit()
            get_db().commit()
            take_course_id = get_db().cursor().execute("""
                SELECT take_course_id
                from take_course
                where student_id = ? and course_id = ?
                """, [student_id, form.get('course_id')]).fetchone()[0]
            
            get_db().commit()
            course_code = get_db().cursor().execute("""
                select course_code
                from course
                where course_id = ?
                """, [form.get('course_id')]).fetchone()[0]
            
            get_db().commit()
            course_id = get_db().cursor().execute("""
                SELECT course_id
                from course
                where course_id = ?
                """, [form.get('course_id')]).fetchone()[0]
            
            return redirect(url_for("take_survey", take_course_id=take_course_id, course_code = course_code, course_id = course_id))
            
        except sqlite3.Error:
            flash('You have already answered this survey!', 'danger')
            return redirect(url_for('survey'))

    title_cursor = get_db().cursor()
    title_cursor.execute("""
            select course_id as course_id, course_code as course_code, title as title
            from course
            """)
    return render_template("survey.html", titles = title_cursor)





@app.route("/survey/<course_code>/<int:course_id>/<int:take_course_id>", methods=["GET", "POST"])
def take_survey(course_code,course_id,take_course_id):
    course_code = course_code
    take_course_id = take_course_id
    course_id = course_id

    questions = get_db().cursor()
    questions.execute("""
              select question_id, question_text
            from question
             """)
    
    answers = get_db().cursor()
    answers.execute("""
            select answer_id, answer_text, answer_value
            from answer
            order by answer_id desc
            """)
    answers = answers.fetchall()

    if request.method == "POST":
        form = request.form
        try:
            for question in questions:
                answer_id = form.get(f"answer_{question['question_id']}")
                get_db().cursor().execute("""
                    INSERT INTO survey_response(question_id, answer_id, take_course_id)
                    VALUES (?, ?, ?)
                    """, [question['question_id'], answer_id, take_course_id])
                
            get_db().commit()
            flash("Survey response submitted successfully!", "success")
            return redirect(url_for('view_results', course_code = course_code, course_id = course_id))

        except sqlite3.Error:
            flash("ERROR!")



    return render_template("question.html", course_code = course_code, take_course_id = take_course_id, questions = questions, answers=answers, course_id = course_id)





@app.route("/results")
def results():
    cursor = get_db().cursor()
    cursor.execute("""
        select course_id as course_id, course_code as course_code, title as course_title
        from course      
    """)
    return render_template("results.html", courses=cursor)



@app.route("/results/<course_code>/<course_id>")
def view_results(course_code, course_id):
    course_code = course_code
    course_id = course_id

    course_title_query = get_db().cursor()
    course_title_query.execute("""
    select title
    from course
    where course_id = ?
    """, [course_id])
    course_title = course_title_query.fetchone()[0]

    student_query = get_db().cursor()
    student_query.execute("""
    select count(DISTINCT survey_response.take_course_id)
    from survey_response, course, take_course
    where survey_response.take_course_id = take_course.take_course_id
    and take_course.course_id = course.course_id
    and course.course_id = ?
    """, [course_id])
    number_student = student_query.fetchone()[0]

    view_result_query = get_db().cursor()
    view_result_query.execute("""
    select sum(answer.answer_value) as sum, count(answer.answer_value) as number_answer, (sum(answer.answer_value)*100)/(count(answer.answer_value)*5) as percent_total,   count (answer.answer_value)*5 as full_score, avg(answer_value) as avg_score_per_answer
    from survey_response, question, course, take_course, answer
    where survey_response.question_id = question.question_id 
    and take_course.course_id = course.course_id
    and survey_response.take_course_id = take_course.take_course_id
    and survey_response.answer_id = answer.answer_id
    and course.course_id = ?
    """, [course_id])
    view_result = view_result_query.fetchone()

    avg_per_survey_query = get_db().cursor()
    avg_per_survey_query.execute("""
    select sum(total_score) as score, count(take_course_id) as count_survey, avg(total_score) as avg_score, avg(total_score)*100/20 as percent_avg_total_score

    from(
    select survey_response.take_course_id as take_course_id, course.course_id, question.question_id, survey_response.answer_id, sum(answer.answer_value) as total_score
    from survey_response , question, answer, course, take_course
    where  take_course.course_id = course.course_id
    and survey_response.take_course_id = take_course.take_course_id
	and survey_response.answer_id =answer.answer_id
	and survey_response.question_id = question.question_id
	and course.course_id = ?
    group by survey_response.take_course_id)

    where total_score is not null
    """, [course_id])

    avg_per_survey = avg_per_survey_query.fetchone()

    avg_per_ques_query = get_db().cursor()
    avg_per_ques_query.execute("""
    select question.question_id as n, question.question_text as t,  avg(answer.answer_value) as v
    from survey_response , question, answer, course, take_course
    where  take_course.course_id = course.course_id
    and survey_response.take_course_id = take_course.take_course_id
	and survey_response.answer_id =answer.answer_id
	and survey_response.question_id = question.question_id
	and course.course_id = ?
	group by question.question_id
    """, [course_id])

    avg_ques = avg_per_ques_query.fetchall()

    labels_no = []
    labels_text = []
    values = []

    for row in avg_ques:
        labels_no.append(row[0])
        labels_text.append(row[1])
        values.append(row[2])
        



    return render_template("view_result.html", course_code = course_code, course_id = course_id, course_title = course_title, number_student = number_student, view_result=view_result, avg_per_survey = avg_per_survey, avg_ques = avg_ques, 
                           labels_no = json.dumps(labels_no), labels_text = json.dumps(labels_text), values = json.dumps(values) )

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

