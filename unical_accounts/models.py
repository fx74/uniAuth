import pycountry

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class User(AbstractUser):
    GENDER= (
                ( 'male', _('Maschio')),
                ( 'female', _('Femmina')),
                ( 'other', _('Altro')),
            )

    first_name = models.CharField(_('Name'), max_length=56,
                                  blank=True, null=True)
    last_name = models.CharField(_('Surname'), max_length=56,
                                 blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    email = models.EmailField('email address', blank=True, null=True)
    taxpayer_id = models.CharField(_('Taxpayer\'s identification number'),
                                      max_length=32,
                                      blank=True, null=True)
    origin = models.CharField(_('from which connector this user come from'),
                              max_length=254,
                              blank=True, null=True)

    class Meta:
        ordering = ['username']
        verbose_name_plural = _("Users")

    @property
    def uid(self):
        return self.username.split('@')[0]

    def persistent_ids(self):
        return [i.persistent_id
                for i in self.persistentid_set.filter(user=self)]

    def persistent_id(self, entityid):
        """ returns persistent id related to a recipient (sp) entity id
        """
        pid = PersistentId.objects.filter(user=self,
                                          recipient_id=entityid).last()
        if pid:
            return pid.persistent_id

    def set_persistent_id(self, recipient_id, persistent_id):

        d = dict(user = self,
                 recipient_id = recipient_id,
                 persistent_id = persistent_id)
        persistent_id = self.persistentid_set.get_or_create(**d)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PersistentId(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    persistent_id = models.CharField(_('SAML Persistent Stored ID'),
                                 max_length=254,
                                 blank=True, null=True)
    recipient_id = models.CharField(_('SAML ServiceProvider entityID'),
                                 max_length=254,
                                 blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Persistent Id')
        verbose_name_plural = _('Persistent Id')

    def __str__(self):
        return '{}: {} to {} [{}]'.format(self.user,
                                          self.persistent_id,
                                          self.recipient_id,
                                          self.created)
