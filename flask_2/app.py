from flask import Flask, Response, request, render_template, redirect, url_for
from crud import get_note_by_title, get_note_by_uuid, create_note, get_all_notes
from sqlalchemy import exc
from models import create_tables, drop_tables

app = Flask(__name__, template_folder="templates", static_url_path="/static_files/")
drop_tables()
create_tables()
create_note("5", "text")
create_note("6", "text")
create_note("7", "text")

@app.route("/", methods=["GET"])
def home_page_view():
    all_notes = get_all_notes()
    # print(all_notes)  # В консоли вывод
    # return f"<h1>{str(all_notes)}</h1>"
    return render_template("home.html", all_notes=all_notes)

@app.route("/new_note", methods=["GET"])
def create_note_form():
    return render_template("new_note.html")


@app.route("/new_note", methods=["POST"])
def create_note_post():
    """Обрабатываем форму регистрации"""
    # Смотрим данные формы, отправленной пользователем.
    note_data = request.form
    # user_data это не редактируемый словарь.
    if 'submit_button' in request.form and request.form['submit_button'] == 'создать':
        note = create_note(
            title=note_data["title"],
            content=note_data["content"],
        )
        return redirect(url_for("get_note_view", search_field=note.uuid))
    else:
        return redirect(url_for("home_page_view"))


@app.route("/<search_field>", methods=["GET"])
def get_note_view(search_field: str):
    try:
        note = get_note_by_uuid(search_field)
    except exc.NoResultFound:
        return Response("No note with such uuid.", status=404)

    return render_template(
        "note.html",
        uuid=note.uuid,
        title=note.title,
        content=note.content,
        created_at=note.created_at
    )
    # return f"""
    #                     <h1>UUID{note.uuid}</h1>
    #                     <p>title: {note.title}</p>
    #                     <p>content: {note.content}</p>
    #                     <p>created_at: {note.created_at}</p>
    #                 """




if __name__ == '__main__':
    app.run()
