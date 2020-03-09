
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

# User Based Imports
from flask_login import current_user
from notificadorHSteste.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    enrollment = IntegerField('Matrícula', validators=[DataRequired()])
    username = StringField('Nome', validators=[DataRequired()])
    last_name = StringField('Último nome', validators=[DataRequired()])
    cellphone = StringField('Celular com DDD', validators=[DataRequired()])

    level = SelectField(u'Nível', choices=[('lv1', 'Iniciante'), ('lv2', 'Intermediário'), ('lv3', 'Avançado')],
                        validators=[DataRequired()])

    age = SelectField(u'Idade', choices=[('inf', 'Até 13 anos'), ('ado', '14 a 18 anos'), ('jov', '19 a 30 anos'),
                                                ('adul', '31 a 50 anos'), ('meia_id', '50 a 60 anos'), ('ido', 'Acima de 60')],
                                                validators=[DataRequired()])

    franchise = SelectField(u'Unidade', choices=[('alec', 'Alecrins'), ('f_santana', 'Feira de Santana'),
                                                 ('gru', 'Guarulhos'), ('join', 'Joinville'), ('lapa', 'Lapa'),
                                                 ('natal', 'Natal'), ('nv_europa', 'Nova Europa'), ('paca', 'Pacaembu'),
                                                 ('perd', 'Perdizes'), ('pin', 'Pinheiros'), ('tatu', 'Tatuapé'),
                                                 ('vl_pru', 'Vila Prudente'), ('vix', 'Vitória')],
                                                 validators=[DataRequired()])

    password = PasswordField('Senha', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])

    pass_confirm = PasswordField('Confirmar senha', validators=[DataRequired()])

    notifications = BooleanField('Autorizo receber notificações')

    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Seu email já está registrado.')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first() and User.query.filter_by(last_name=field.data).first():
            raise ValidationError('Desculpe, usuário existente. Contate a adminstradora.')


class UpdateUserForm(FlaskForm):
    # username = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    cellphone = StringField('Celular com DDD', validators=[DataRequired()])

    level = SelectField(u'Nível', choices=[('lv1', 'Iniciante'), ('lv2', 'Intermediário'), ('lv3', 'Avançado')],
                        validators=[DataRequired()])

    age = SelectField(u'Faixa etária',
                      choices=[('inf', 'Até 13 anos'), ('ado', '14 a 18 anos'), ('jov', '19 a 30 anos'),
                               ('adul', '31 a 50 anos'), ('meia_id', '50 a 60 anos'), ('ido', 'Acima de 60')],
                                validators=[DataRequired()])

    franchise = SelectField(u'Unidade', choices=[('alec', 'Alecrins'), ('f_santana', 'Feira de Santana'),
                                                 ('gru', 'Guarulhos'), ('join', 'Joinville'), ('lapa', 'Lapa'),
                                                 ('natal', 'Natal'), ('nv_europa', 'Nova Europa'), ('paca', 'Pacaembu'),
                                                 ('perd', 'Perdizes'), ('pin', 'Pinheiros'), ('tatu', 'Tatuapé'),
                                                 ('vl_pru', 'Vila Prudente'), ('vix', 'Vitória')],
                                                    validators=[DataRequired()])

    notifications = BooleanField('Autorizo receber notificações')

    submit = SubmitField('Atualizar')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')
    #
    # def check_username(self, field):
    #     # Check if not None for that username!
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Sorry, that username is taken!')


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Apagar usuário !')
