# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# definimos el user manager
class UsuarioManager(BaseUserManager):
    def create_user(self, email,username,nombre,apellidos,password=None):
        if not email:
            raise ValueError('El usuario debe tener un Correo Electrónico!')
        
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,
            apellidos = apellidos
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email,username,nombre,apellidos,password=None):
               
        usuario = self.create_user(
            email,
            username = username,
            nombre = nombre,
            apellidos = apellidos,
            password=password
        )

        usuario.usuario_administrador = True

        usuario.save()
        return usuario
    
# definimos modelo User        
class Usuario(AbstractBaseUser):
    username=models.CharField('Nombre de Usuario', max_length=10, unique=True)
    email=models.EmailField('Correo Electrónico',unique=True,max_length=255)
    nombre=models.CharField('Nombre',max_length=100, blank=True, null=True)
    apellidos=models.CharField('Apellidos',max_length=100, blank=True,null=True)
    usuario_activo=models.BooleanField(default=True)
    usuario_administrador=models.BooleanField(default=False)

    objects=UsuarioManager()

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email','nombre','apellidos']

    def __str__(self):
        return f'{self.apellidos},{self.nombre}'
    
    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador

    class Meta:
        db_table='usuario'