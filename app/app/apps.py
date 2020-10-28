from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = "app"

    def ready(self):
        from polaris.integrations import register_integrations
        from .integrations import MyRailsIntegration

        register_integrations(
            rails=MyRailsIntegration()
        )

