# Generated by Django 2.2.7 on 2020-03-02 15:21

from django.db import migrations

# se copian y adaptan algunos métodos directamente del modelo User ya que no se pueden acceder
# en medio de la migracion de datos


def get_supervisor_profile(user):
    supervisor_profile = None
    if hasattr(user, 'supervisorprofile'):
        supervisor_profile = user.supervisorprofile
    return supervisor_profile


def get_is_supervisor_customer(user):
    supervisor = get_supervisor_profile(user)
    if supervisor and supervisor.is_customer:
        return True
    return False


def get_is_administrador(user):
    supervisor = get_supervisor_profile(user)
    if supervisor and supervisor.is_administrador:
        return True
    elif user.is_staff:
        return True
    return False


def crear_grupos_roles_predefinidos(apps, schema_editor):
    # se crean los roles predefinidos como grupos
    Group = apps.get_model("auth", "Group")
    # User.ADMINISTRADOR
    administradores = Group.objects.create(name='Administrador')
    # User.GERENTE
    gerentes = Group.objects.create(name='Gerente')
    # User.SUPERVISOR
    Group.objects.create(name='Supervisor')
    # User.REFERENTE
    referentes = Group.objects.create(name='Referente')
    # User.AGENTE
    agentes = Group.objects.create(name='Agente')
    # User.CLIENTE_WEBPHONE
    clientes_webphone = Group.objects.create(name='Cliente Webphone')
    # se asignan los usuario existentes a los nuevos grupos creados
    User = apps.get_model("ominicontacto_app", "User")
    SupervisorProfile = apps.get_model("ominicontacto_app", "SupervisorProfile")
    for user in User.objects.all():
        supervisor_profile = get_supervisor_profile(user)
        if user.is_agente:
            user.groups.set([agentes])
        elif user.is_cliente_webphone:
            user.groups.set([clientes_webphone])
        elif get_is_supervisor_customer(user):
            user.groups.set([referentes])
        elif get_is_administrador(user):
            # es un admin pero de tipo staff (sin perfil de supervisor)
            # por lo tanto se agrega al grupo 'Administradores'
            # y se le crea un perfil de supervisor
            user.groups.set([administradores])
            if supervisor_profile is None:
                SupervisorProfile.objects.create(user=user, sip_extension=user.id + 1000,
                                                 is_administrador=True)
        else:
            # es un supervisor gerente, se le asigna el grupo 'Gerentes'
            user.groups.set([gerentes])


def eliminar_grupos_roles_predefinidos(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0053_elimina_ringall_queue'),
    ]

    operations = [
        migrations.RunPython(
            crear_grupos_roles_predefinidos, reverse_code=eliminar_grupos_roles_predefinidos),
    ]