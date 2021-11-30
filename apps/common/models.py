from django.db import models
from .middlewares import GlobalRequestMiddleware


class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager, self).get_queryset().filter(activo=True)


class BaseModel(models.Model):
    objects = BaseManager()
    original_objects = models.Manager()

    activo = models.BooleanField(default=True)
    usuario_creacion = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    usuario_actualizacion = models.CharField(max_length=50, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.audit()
        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.activo = False
        self.audit()
        super(BaseModel, self).save(*args, **kwargs)

    def audit(self):
        request = GlobalRequestMiddleware.get_request()

        if request and request.user and hasattr(request.user, 'email'):
            user = request.user
            if self.pk:
                self.usuario_actualizacion = user.email
            else:
                self.usuario_creacion = user.email


class BaseMeta():
    ordering = ['-id']
