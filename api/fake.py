from datetime import datetime
import random

import click
from flask import Blueprint
from faker import Faker

from api.app import db
from api.models import Via


fake = Blueprint('fake', __name__)
faker = Faker()


def _fluidez_aleatoria():
    return ['Leve', 'Médio', 'Pesado'][faker.random_int(0, 2)]


def _logradouro_aleatorio():
    return f"Av. Dr. {faker.first_name()}"


@fake.cli.command()
@click.argument('num', type=int)
def vias(num):
    """Cria algumas vias "fakes"."""
    for num in range(num):
        via = Via(cep=f"{faker.random_int(0, 99999):05}-{faker.random_int(0, 999):03}", 
                  datahora=faker.date_this_month(), 
                  logradouro=_logradouro_aleatorio(),
                  fluidez=_fluidez_aleatoria(),
                  ambulancia=bool(random.getrandbits(1)),
                  bombeiro=bool(random.getrandbits(1)),
                  policia=bool(random.getrandbits(1)))
        db.session.add(via)
    db.session.commit()
    print(num, 'vias adicionada(s).')
