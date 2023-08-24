from .models import SubMenu, Menu, Noticia, Servicio, Contrato, TipoContrato, Cliente, Empleado, Imagen
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
class EmpleadoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
    list_filter = ('nombre',)

class ClienteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
    list_filter = ('nombre',)

class ImagenAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class TipoContratoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)

class ContratoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ncontrato',)
    search_fields = ('id', 'ncontrato',)
    list_filter = ('ncontrato',)
class ServicioAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class NoticiaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
class SubMenuInline(admin.TabularInline):
    model = SubMenu

class SubMenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)

class MenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'titulo',)
    search_fields = ('id', 'titulo',)
    list_filter = ('titulo',)
    inlines = [SubMenuInline]

admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(TipoContrato, TipoContratoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Imagen, ImagenAdmin)