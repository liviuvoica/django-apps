from django.apps import AppConfig

class BlogApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter_api'
    verbose_name = 'Newsletter subscribers'