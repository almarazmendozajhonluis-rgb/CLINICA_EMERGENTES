from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.medico import Medico

medico_bp = Blueprint('medico', __name__)

# LISTAR MEDICOS
@medico_bp.route('/medicos')
def listar_medicos():

    medicos = Medico.query.all()

    return render_template(
        'medicos/listar.html',
        medicos=medicos
    )


# CREAR MEDICO
@medico_bp.route('/medicos/crear', methods=['GET', 'POST'])
def crear_medico():

    if request.method == 'POST':

        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        nuevo_medico = Medico(
            nombre=nombre,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo
        )

        db.session.add(nuevo_medico)
        db.session.commit()

        return redirect(url_for('medico.listar_medicos'))

    return render_template('medicos/crear.html')


# EDITAR MEDICO
@medico_bp.route('/medicos/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):

    medico = Medico.query.get_or_404(id)

    if request.method == 'POST':

        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        medico.telefono = request.form['telefono']
        medico.correo = request.form['correo']

        db.session.commit()

        return redirect(url_for('medico.listar_medicos'))

    return render_template(
        'medicos/editar.html',
        medico=medico
    )


# ELIMINAR MEDICO
@medico_bp.route('/medicos/eliminar/<int:id>')
def eliminar_medico(id):

    medico = Medico.query.get_or_404(id)

    db.session.delete(medico)
    db.session.commit()

    return redirect(url_for('medico.listar_medicos'))