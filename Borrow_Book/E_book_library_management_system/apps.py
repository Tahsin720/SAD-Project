from django.apps import AppConfig


class EBookLibraryManagementSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'E_book_library_management_system'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'
    
    def ready(self):
        from . import signals