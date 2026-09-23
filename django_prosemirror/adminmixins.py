from typing import Any

from django.contrib import admin
from django.db import models
from django.forms import Field

from .widgets import ProseMirrorEditor


class ProseMirrorModelAdminMixin(admin.ModelAdmin):
    """Admin mixin replacing text fields with ProseMirror editor widgets."""

    prosemirror_fields: str | list[str] | tuple[str, ...] = "__all__"

    def formfield_for_dbfield(
        self, db_field: models.Field, *args: Any, **kwargs: Any
    ) -> Field | None:
        """Attach ProseMirror widget for configured fields."""
        if self.prosemirror_fields == "__all__":
            if isinstance(db_field, models.TextField):
                kwargs["widget"] = ProseMirrorEditor()
        elif db_field.name in self.prosemirror_fields:
            kwargs["widget"] = ProseMirrorEditor()

        return super().formfield_for_dbfield(db_field, *args, **kwargs)
