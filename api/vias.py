from flask import Blueprint, abort
from apifairy import response, other_responses

from api import db
from api.models import Via
from api.schemas import ViaSchema


vias = Blueprint('vias', __name__)
via_schema = ViaSchema()
vias_schema = ViaSchema(many=True)


@vias.route('/vias', methods=['GET'])
@response(vias_schema)
def all():
    """Retorna todoas as vias."""
    return db.session.scalars(Via.select())

@vias.route('/vias/<int:cep>', methods=['GET'])
@other_responses({404: 'CEP não encontrado'})
@response(via_schema)
def get(cep):
    """Retorna os dados sobre uma via pelo CEP."""
    return db.session.get(Via, cep) or abort(404)
