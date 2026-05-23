from flask import Blueprint, render_template
from app.models.consulta import Consulta

historial_bp = Blueprint('historial', __name__)

@historial_bp.route('/historial')

def historial():

    consultas = Consulta.query.all()

    return render_template(
        'historial/listar.html',
        consultas=consultas
    )