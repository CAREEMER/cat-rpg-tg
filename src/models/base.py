from sqlmodel import Session, SQLModel, select

from db import engine


class BaseModel(SQLModel, table=False):
    def create(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()
            session.refresh(self)

        return self

    @classmethod
    def get_all(cls):
        with Session(engine) as session:
            return session.exec(select(cls)).fetchall()

    @classmethod
    def filter(cls, *lookup_expression):
        with Session(engine) as session:
            session.execute(select(cls).where(*lookup_expression)).fetchall()

    @classmethod
    def get_obj(cls, *lookup_expression):
        statement = select(cls).where(*lookup_expression)

        with Session(engine) as session:
            return session.exec(statement).one_or_none()

    @classmethod
    def create_obj(cls, **kwargs):
        obj = cls(**kwargs)

        with Session(engine) as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)

        return obj

    def update(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()
            session.refresh(self)

        return self
