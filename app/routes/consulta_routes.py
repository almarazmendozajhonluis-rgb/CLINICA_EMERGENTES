from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.consulta import Consulta
from app.models.medico import Medico
from app.models.paciente import Paciente

consulta_bp = Blueprint('consulta', __name__)

# LISTAR CONSULTAS
@consulta_bp.route('/consultas')
def listar_consultas():

    consultas = Consulta.query.all()

    return render_template(
        'consultas/listar.html',
        consultas=consultas
    )


# CREAR CONSULTA
@consulta_bp.route('/consultas/crear', methods=['GET', 'POST'])
def crear_consulta():

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':

        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        nueva_consulta = Consulta(
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            id_medico=id_medico,
            id_paciente=id_paciente
        )

        db.session.add(nueva_consulta)
        db.session.commit()

        return redirect(url_for('consulta.listar_consultas'))

    return render_template(
        'consultas/crear.html',
        medicos=medicos,
        pacientes=pacientes
    )


# EDITAR CONSULTA
@consulta_bp.route('/consultas/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):

    consulta = Consulta.query.get_or_404(id)

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':

        consulta.diagnostico = request.form['diagnostico']
        consulta.tratamiento = request.form['tratamiento']
        consulta.id_medico = request.form['id_medico']
        consulta.id_paciente = request.form['id_paciente']

        db.session.commit()

        return redirect(url_for('consulta.listar_consultas'))

    return render_template(
        'consultas/editar.html',
        consulta=consulta,
        medicos=medicos,
        pacientes=pacientes
    )


# ELIMINAR CONSULTA
@consulta_bp.route('/consultas/eliminar/<int:id>')
def eliminar_consulta(id):

    consulta = Consulta.query.get_or_404(id)

    db.session.delete(consulta)
    db.session.commit()

    return redirect(url_for('consulta.listar_consultas'))