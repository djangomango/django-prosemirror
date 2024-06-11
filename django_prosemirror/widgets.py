import json

from django import forms
from django.conf import settings


class ProseMirrorEditor(forms.Textarea):
    """
    Form widget that renders as a standard <textarea> but also includes the
    relevant static files that convert it into a ProseMirror editor.
    """

    def __init__(self, attrs=None, **kwargs):
        self.config = {}
        if hasattr(settings, 'PROSEMIRROR_DEFAULTS'):
            self.config.update(settings.PROSEMIRROR_DEFAULTS)

        self.config.update(kwargs)

        if not attrs:
            attrs = {}
        attrs['data-prosemirror'] = json.dumps(self.config)

        super().__init__(attrs)

    @property
    def media(self):
        media = forms.Media(
            css={
                'all': [
                    "prosemirror/css/editor.css",
                    "prosemirror/css/style.css",
                ]
            },
            js=[f"prosemirror/js/pm.min.js"]
        )

        media += forms.Media(js=['prosemirror/init.js'])

        return media
