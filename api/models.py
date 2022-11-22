import sqlalchemy as sqla

from api.app import db


class Via(db.Model):
    """Representa o estado de uma Via."""
    __tablename__ = 'TB_VIA'

    cep = sqla.Column('cep', sqla.String, primary_key=True)
    datahora = sqla.Column('datahora', sqla.DateTime)
    logradouro = sqla.Column('logradouro', sqla.String)
    fluidez = sqla.Column('fluidez', sqla.String)
    ambulancia = sqla.Column('ambulancia', sqla.Boolean)
    bombeiro = sqla.Column('bombeiro', sqla.Boolean)
    policia = sqla.Column('policia', sqla.Boolean)
