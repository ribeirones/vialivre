from api.app import ma
from api.models import Via


class ViaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Via
    
    cep = ma.auto_field()
    datahora = ma.auto_field()
    logradouro = ma.auto_field()
    fluidez = ma.auto_field()
    ambulancia = ma.auto_field()
    bombeiro = ma.auto_field()
    policia = ma.auto_field()
