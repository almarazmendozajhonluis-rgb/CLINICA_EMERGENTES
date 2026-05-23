from flask import Blueprint, render_template
from app.models.medico import Medico
from app.models.paciente import Paciente
from app.models.consulta import Consulta

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/reportes')

def reportes():

    total_medicos = Medico.query.count()

    total_pacientes = Paciente.query.count()

    total_consultas = Consulta.query.count()

    return render_template(
        'reportes/index.html',
        total_medicos=total_medicos,
        total_pacientes=total_pacientes,
        total_consultas=total_consultas
    )