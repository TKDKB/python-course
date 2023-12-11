from flask import Flask, Response, request
from crud import get_note, create_note, get_all_notes, get_note_uuid
from sqlalchemy import exc
from models import create_tables, drop_tables

app = Flask(__name__)
drop_tables()
create_tables()
create_note("5", "text")
create_note("6", "text")
create_note("7", "text")

@app.route("/", methods=["GET"])
def home_page_view():
    all_notes = get_all_notes()
    return f"<h1>{all_notes}</h1>"

@app.route("/new_note", methods=["GET"])
def create_note_form():
    return (
        "<h1> Оставьте заметку </h1>"
        '<form action="/new_note" method="post">'  # Форма для отправки данных через метод `POST`.
        #   `action="/register"` - это путь, куда будут отправлены данные.
        #   Поля для заполнения:
        #   Атрибут `name="username"` указывает название поля.
        '   <p> Title: <input type="str" name="title"> </p>'  # `type="text"` - это поле для текста
        '   <p> Content: <input type="text" name="content"> </p>'  # `type="password"` - это сокрытое поле для текста
        '   <p> <input type="submit"> </p>'  # Кнопка подтверждения отправки формы - `type="submit"`
        '</form>'
    )


@app.route("/new_note", methods=["POST"])
def create_note_post():
    """Обрабатываем форму регистрации"""
    # Смотрим данные формы, отправленной пользователем.
    note_data = request.form
    # user_data это не редактируемый словарь.
    note = create_note(
        title=note_data["title"],
        content=note_data["content"]
    )
    return f"""
        <h1>Ваша заметка успешно создана!</h1>
    """


@app.route("/<note_uuid>", methods=["GET"])
def get_note_view(uuid: str):
    """Обрабатываем форму регистрации"""
    try:
        note = get_note(uuid)
    except exc.NoResultFound:
        return Response("No note with such uuid.", status=404)
    return f"""
            <h1>UUID{uuid}</h1>
            <p>title: {note.title}</p>
            <p>content: {note.content}</p>
        """

@app.route("/<note_title>", methods=["GET"])
def get_note_uuid(title: str):
    """Обрабатываем форму регистрации"""
    try:
        note = get_note_uuid(title)
    except exc.NoResultFound:
        return Response("No note with such uuid.", status=404)
    return f"""
            <h1>UUID{note.uuid}</h1>
            <p>title: {note.title}</p>
        """




if __name__ == '__main__':
    app.run()
