from sqlalchemy import create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from core.settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
