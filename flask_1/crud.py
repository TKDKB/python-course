from sqlalchemy import select, Text

from models import Note, session


def get_note(uuid: str) -> Note:
    with session() as conn:
        query = select(Note).where(Note.uuid == uuid)
        # (User,) - one()
        # User - scalar_one()
        return conn.execute(query).scalar_one()


def get_note_uuid(title: str) -> Note:
    with session() as conn:
        query = select(Note).where(Note.title == title)
        # (User,) - one()
        # User - scalar_one()
        return conn.execute(query).scalar_one()


def create_note(title: str, content: Text) -> Note:
    with session() as conn:
        note = Note(title=title, content=content)
        conn.add(note)  # Добавляем.
        conn.commit()  # Подтверждаем создание.
        conn.refresh(note)  # Обновляем. Для чего? Получаем созданный ID из базы.
    return note


def get_all_notes():
    with session() as conn:
        return conn.execute(select(Note)).scalars().all()

