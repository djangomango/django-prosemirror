# Django-Prosemirror

A rich text editing package providing form widgets and ModelAdmin mixins for Django powered by ProseMirror.

---

## Installation

```bash
pip install git+https://github.com/djangomango/django-prosemirror.git@0.1.0
```

Or add to your `requirements.txt`:

```txt
git+https://github.com/djangomango/django-prosemirror.git@0.1.0
```

Add `django_prosemirror` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "django_prosemirror",
    ...
]
```

---

## Usage

### 1. Form Field Widget

Attach the `ProseMirrorEditor` widget to form fields:

```python
from django import forms
from django_prosemirror.widgets import ProseMirrorEditor


class ArticleForm(forms.Form):
    content = forms.CharField(widget=ProseMirrorEditor())
```

In your template:

```html
<head>
    {{ form.media }}
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ form.content }}
        <button type="submit">Save</button>
    </form>
</body>
```

### 2. ModelAdmin Mixin

Automatically render ProseMirror editors for specified fields in the Django Admin:

```python
from django.contrib import admin
from django_prosemirror.adminmixins import ProseMirrorModelAdminMixin
from .models import Article


@admin.register(Article)
class ArticleAdmin(ProseMirrorModelAdminMixin, admin.ModelAdmin):
    prosemirror_fields = ["content"]
```

---

## Build (Optional)

To rebuild bundled ProseMirror assets using Docker:

```bash
docker-compose -f docker-compose.yml run node npm run build
```

---

## License & Credits

- Licensed under the **GNU Lesser General Public License v3 (LGPLv3)**.
- Integrates [ProseMirror](https://prosemirror.net/).