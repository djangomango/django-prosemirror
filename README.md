# Django-Prosemirror

This package provides widgets for the basic ProseMirror example.

### Installation

1. Pip install or add to your requirements.txt:

    ```bash
    pip install git+https://github.com/djangomango/django-prosemirror.git@main
    ```

2. Add to INSTALLED_APPS:

    ```bash
    INSTALLED_APPS = [
        ...
        'django_prosemirror',
    ]
    ```

3. Add to form and template:

   ```python
   from django import forms
   from django_prosemirror.widgets import ProseMirrorEditor
   
   class Form(forms.Form):
       field = forms.CharField(widget=ProseMirrorEditor())
   ```
   ```html
   <html>
      <head>
         {{ form.media.js }}
         {{ form.media.css }}
      </head>
      <body>
         {{ form.field|safe }}
      </body>
   </html>
   ```

### Build (optional)

Feel free to pull this repository and rebuild the prosemirror assets. You can do so using Docker & docker-compose:

```bash
docker-compose -f docker-compose.yml run node npm run build
```