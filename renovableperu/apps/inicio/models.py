# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    celular = models.CharField(max_length=15)
    dni = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')
    pais = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    distrito = models.CharField(max_length=40)
    direccion_larga = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mensajes(models.Model):
    id_msj = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')
    fecha = models.DateTimeField()
    mensaje = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'mensajes'


class Portafolio(models.Model):
    ip_por = models.AutoField(primary_key=True)
    titulo_por = models.CharField(max_length=70)
    titular_p = models.CharField(max_length=130)
    descripcion_por = models.CharField(max_length=500)
    imagen_por = models.ImageField(upload_to='media')
    lugar_por = models.CharField(max_length=100)
    fecha_por = models.DateTimeField()
    calificacion_por = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'portafolio'


class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nombre_pro = models.CharField(max_length=60)
    titular_pro = models.CharField(max_length=100)
    descripcion_pro = models.CharField(max_length=300)
    imagen_pro = models.CharField(max_length=100)
    precio_pro = models.FloatField()

    class Meta:
        managed = False
        db_table = 'producto'
