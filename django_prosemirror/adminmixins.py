from django.contrib import admin
from django.db import models

from .widgets import ProseMirrorEditor


class ProseMirrorModelAdminMixin(admin.ModelAdmin):
    prosemirror_fields = '__all__'

    def formfield_for_dbfield(self, db_field, *args, **kwargs):

        if self.prosemirror_fields == '__all__':
            if isinstance(db_field, models.TextField):
                kwargs['widget'] = ProseMirrorEditor()
        else:
            if db_field.name in self.prosemirror_fields:
                kwargs['widget'] = ProseMirrorEditor()

        return super().formfield_for_dbfield(db_field, *args, **kwargs)
