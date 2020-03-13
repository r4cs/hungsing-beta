from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from notificadorHSproject.models import User
from flask import request


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    enrollment = IntegerField('Matrícula', validators=[DataRequired()])

    username = StringField('Nome', validators=[DataRequired()])

    last_name = StringField('Sobrenome', validators=[DataRequired()])

    cellphone = StringField('Celular com DDD', validators=[DataRequired()])

    # level = BooleanField(u'Nível', choices=[
    #     ('lv1', 'Iniciante'),
    #     ('lv2', 'Intermediário'),
    #     ('lv3', 'Avançado')
    # ],
    #                     validators=[DataRequired()])

    begginer = BooleanField(u'Iniciante')

    interm = BooleanField(u"Intermediário")

    adv = BooleanField(u"Avançado")


    age = SelectField(u'Idade', choices=[
        ('ado', '14 a 18 anos'),
        ('jov', '19 a 30 anos'),
        ('adul', '31 a 50 anos'),
        ('meia_id', '50 a 60 anos'),
        ('ido', 'Acima de 60')
    ],
                      validators=[DataRequired()]
                      )

    password = PasswordField('Senha', validators=[
        DataRequired(),
        EqualTo('pass_confirm', message='As senhas devem coincidir!')
    ]
                             )

    pass_confirm = PasswordField('Confirmar senha', validators=[DataRequired()])

    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Seu email já está registrado.')

    def check_enrollment(self, field):
        # Check if not None for that username!
        if User.query.filter_by(enrollment=field.data).first():
            raise ValidationError('Desculpe, matrícula já cadastrsada. Contate a adminstradora.')


class UpdateUserForm(FlaskForm):
    # username = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    cellphone = StringField('Celular com DDD', validators=[DataRequired()])

    begginer = BooleanField(u'Iniciante')

    interm = BooleanField(u"Intermediário")

    adv = BooleanField(u"Avançado")

    # level = SelectField(u'Nível', choices=[
    #     ('lv1', 'Iniciante'),
    #     ('lv2', 'Intermediário'),
    #     ('lv3', 'Avançado')
    # ],
    #                     validators=[DataRequired()])

    age = SelectField(u'Idade', choices=[
        ('ado', '14 a 18 anos'),
        ('jov', '19 a 30 anos'),
        ('adul', '31 a 50 anos'),
        ('meia_id', '50 a 60 anos'),
        ('ido', 'Acima de 60')
    ],
                      validators=[DataRequired()])

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
