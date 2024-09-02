from django.conf import settings


class PortfolioRouter:
    """
    A router to control all database operations on models in the
    portfolio application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read, cycling models go to portfolio.
        """
        if model._meta.app_label == "portfolio":
            return "cycling"
        return None

    def db_for_write(self, model, **hints):
        """
        Do not allow attempts to write
        """
        if model._meta.app_label == "portfolio":
            return "cycling"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the portfolio app.
        """
        if obj1._meta.app_label == "portfolio" and obj2._meta.app_label == "portfolio":
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Allow migrations only to appropriate databases
        """
        if getattr(settings, "TESTS_RUN", False):
            return True
