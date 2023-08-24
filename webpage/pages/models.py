from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Menu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class SubMenu(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.DO_NOTHING,
        verbose_name="Menu",
        help_text="Menu",
        blank=True, null=True
    )
    url = models.TextField(
        verbose_name='URL Document',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    descripcion = RichTextField()
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    campo1 = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="campo1",
        help_text="campo1",
    )
    campo2 = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="campo2",
        help_text="campo2",
    )

    month = models.CharField(
        null=True, blank=True, max_length=300,
        verbose_name="redirigir",
        help_text="redirigir",
    )
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo

class TipoContrato(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Tipo de contrato"
        verbose_name_plural = "Tipos de contratos"
    def __str__(self):
        return self.titulo
class Contrato(models.Model):

    ano = models.DateTimeField(verbose_name='año')
    ncontrato = models.CharField(
        max_length=20, blank=True,
        verbose_name='N° de Contrato',
        null=True)
    tipocontrato = models.ForeignKey(
        TipoContrato, on_delete=models.DO_NOTHING,
        verbose_name="Tipo de Contrato",
        help_text="Tipo de contrato",
        blank=True, null=True)
    valor = models.CharField(
        max_length=20, blank=True,
        verbose_name='valor',
        null=True)
    contrato = models.BooleanField(
        verbose_name='Contrato',
        blank=True,null=True)
    actainicio = models.BooleanField(
        verbose_name='Acta de inicio',
        blank=True, null=True)
    actafinal = models.BooleanField(
        verbose_name='Acta final',
        blank=True, null=True)
    pagina = models.CharField(
        max_length=70, blank=True,
        verbose_name='pagina', null=True)
    secop = models.CharField(
        max_length=70, blank=True,
        verbose_name='SECOP', null=True)
    Finicio = models.DateTimeField(verbose_name='Fecha Inicio')
    Fterminacion = models.DateTimeField(verbose_name='Fecha Final')
    descripcion = models.TextField(
        verbose_name='Descripcion',
        null=True, blank=True)
    rup = models.TextField(
        verbose_name='RUP',
        null=True, blank=True)
    archivo = models.FileField(
        verbose_name='URL Document',
        upload_to='upload/documento',
        blank=True, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return self.ncontrato


class Servicio(models.Model):
    titulo = models.TextField(
        null=True, blank=True,
        verbose_name="Titulo",
        help_text="Titulo",
    )
    slug = models.CharField(
        null=True, blank=True,
        verbose_name="Slug",
        help_text="Slug", max_length=100
    )
    descripcion = RichTextField()
    imagen = models.ImageField(
        null=False, blank=False,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo


class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    posicion = models.CharField(max_length=255)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ["id"]
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    TIPO_CHOICES = [
        ('PN', 'Persona Natural'),
        ('PJ', 'Persona Jurídica')
    ]

    tipo_cliente = models.CharField(max_length=2, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=255, blank=True, null=True)  # Opcional para persona jurídica
    apellido = models.CharField(max_length=255, blank=True, null=True)  # Opcional para persona jurídica
    fecha_nacimiento = models.DateField(blank=True, null=True)  # Opcional para persona jurídica
    dni = models.CharField(max_length=10, blank=True, null=True)  # Opcional para persona jurídica
    nombre_empresa = models.CharField(max_length=255, blank=True, null=True)  # Opcional para persona natural
    ruc = models.CharField(max_length=11, blank=True, null=True)  # Opcional para persona natural
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    class Meta:
        ordering = ["id"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    titulo = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='imagenes/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo or str(self.id)
