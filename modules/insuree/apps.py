from django.apps import AppConfig


class InsureeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.insuree"
    url_prefix = 'insurees'