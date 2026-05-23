from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.paciente import Paciente

paciente_bp = Blueprint('paciente', __name__)

# LISTAR PACIENTES
@paciente_bp.route('/pacientes')
def listar_pacientes():

    pacientes = Paciente.query.all()

    return render_template(
        'pacientes/listar.html',
        pacientes=pacientes
    )


# CREAR PACIENTE
@paciente_bp.route('/pacientes/crear', methods=['GET', 'POST'])
def crear_paciente():

    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        nuevo_paciente = Paciente(
            nombre=nombre,
            edad=edad,
            direccion=direccion,
            telefono=telefono
        )

        db.session.add(nuevo_paciente)
        db.session.commit()

        return redirect(url_for('paciente.listar_pacientes'))

    return render_template('pacientes/crear.html')


# EDITAR PACIENTE
@paciente_bp.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):

    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':

        paciente.nombre = request.form['nombre']
        paciente.edad = request.form['edad']
        paciente.direccion = request.form['direccion']
        paciente.telefono = request.form['telefono']

        db.session.commit()

        return redirect(url_for('paciente.listar_pacientes'))

    return render_template(
        'pacientes/editar.html',
        paciente=paciente
    )


# ELIMINAR PACIENTE
@paciente_bp.route('/pacientes/eliminar/<int:id>')
def eliminar_paciente(id):

    paciente = Paciente.query.get_or_404(id)

    db.session.delete(paciente)
    db.session.commit()

    return redirect(url_for('paciente.listar_pacientes'))