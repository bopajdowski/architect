```bash
export DJANGO_SETTINGS_MODULE=project.settings
python manage.py migrate
architect partition --module alignment_table.models
python manage.py partition
 python manage.py search
```
