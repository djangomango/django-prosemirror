import json
from typing import Any

from django import forms
from django.conf import settings


class ProseMirrorEditor(forms.Textarea):
    """Form widget rendering ProseMirror in place of standard textareas."""

    def __init__(self, attrs: dict[str, Any] | None = None, **kwargs: Any) -> None:
        self.config: dict[str, Any] = {}
        if hasattr(settings, "PROSEMIRROR_DEFAULTS"):
            self.config.update(settings.PROSEMIRROR_DEFAULTS)

        self.config.update(kwargs)

        if not attrs:
            attrs = {}
        attrs["data-prosemirror"] = json.dumps(self.config)

        super().__init__(attrs)

    @property
    def media(self) -> forms.Media:
        """Return static CSS and JavaScript media required for ProseMirror rendering."""
        media = forms.Media(
            css={
                "all": [
                    "prosemirror/css/editor.css",
                    "prosemirror/css/style.css",
                ]
            },
            js=["prosemirror/js/pm.min.js"],
        )
        media += forms.Media(js=["prosemirror/init.js"])
        return media
