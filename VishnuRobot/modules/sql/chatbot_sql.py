import threading

from sqlalchemy import Column, String

from VishnuRobot.modules.sql import BASE, SESSION


class VishnuChats(BASE):
    __tablename__ = "vishnu_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


VishnuChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_vishnu(chat_id):
    try:
        chat = SESSION.query(VishnuChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_vishnu(chat_id):
    with INSERTION_LOCK:
        vishnuchat = SESSION.query(VishnuChats).get(str(chat_id))
        if not vishnuchat:
            vishnuchat = VishnuChats(str(chat_id))
        SESSION.add(vishnuchat)
        SESSION.commit()


def rem_vishnu(chat_id):
    with INSERTION_LOCK:
        vishnuchat = SESSION.query(VishnuChats).get(str(chat_id))
        if vishnuchat:
            SESSION.delete(vishnuchat)
        SESSION.commit()
