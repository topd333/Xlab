class RobustGridRouter(object):
    """
    A router to control all database operations on models in the
    grid_core application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read grid_core models go to robust_grid.
        """
        if model._meta.app_label == 'grid_core':
            return 'robust_grid'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write grid_core models go to robust_grid.
        """
        if model._meta.app_label == 'grid_core':
            return 'robust_grid'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the grid_core app is involved.
        """
        if obj1._meta.app_label == 'grid_core' or obj2._meta.app_label == 'grid_core':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the grid_core app only appears in the 'grid_core'
        database.
        """
        if db == 'robust_grid':
            return model._meta.app_label == 'grid_core'
        elif model._meta.app_label == 'grid_core':
            return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure the grid_core apps only appears on the robust_grid db"""
        if model._meta.app_label in ['south']:
            return True
        if db == 'robust_grid':
            return model._meta.app_label == 'grid_core'
        elif model._meta.app_label == 'grid_core':
            return False
        return None

class StagingRouter(object):
    """
    A router to control all database operations on models in the
    grid_staging application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read grid_staging models go to staging.
        """
        if model._meta.app_label == 'grid_staging':
            return 'staging'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write grid_staging models go to staging.
        """
        if model._meta.app_label == 'grid_staging':
            return 'staging'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the grid_staging app is involved.
        """
        if obj1._meta.app_label == 'grid_staging' or obj2._meta.app_label == 'grid_staging':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the grid_staging app only appears in the 'staging'
        database.
        """
        if db == 'staging':
            return model._meta.app_label == 'grid_staging'
        elif model._meta.app_label == 'grid_staging':
            return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure the grid_staging apps only appears on the staging db"""
        if model._meta.app_label in ['south']:
            return True
        if db == 'staging':
            return model._meta.app_label == 'grid_staging'
        elif model._meta.app_label == 'grid_staging':
            return False
        return None

class EstatesRouter(object):
    """
    A router to control all database operations on models in the
    grid_estates application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read grid_estates models go to grid_estates.
        """
        if model._meta.app_label == 'grid_estates':
            return 'estates'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write grid_estates models go to estates.
        """
        if model._meta.app_label == 'grid_estates':
            return 'estates'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the grid_estates app is involved.
        """
        if obj1._meta.app_label == 'grid_estates' or obj2._meta.app_label == 'grid_estates':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the grid_estates app only appears in the 'estates'
        database.
        """
        if db == 'estates':
            return model._meta.app_label == 'grid_estates'
        elif model._meta.app_label == 'grid_estates':
            return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure the grid_estates apps only appears on the estates db"""
        if model._meta.app_label in ['south']:
            return True
        if db == 'estates':
            return model._meta.app_label == 'grid_estates'
        elif model._meta.app_label == 'grid_estates':
            return False
        return None


class SpaceRouter(object):
    """
    A router to control all database operations on models in the
    grid_space application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read grid_space models go to grid_space.
        """
        if model._meta.app_label == 'grid_space':
            return 'grid_space'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write grid_space models go to grid_space.
        """
        if model._meta.app_label == 'grid_space':
            return 'grid_space'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the grid_space app is involved.
        """
        if obj1._meta.app_label == 'grid_space' or obj2._meta.app_label == 'grid_space':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the grid_space app only appears in the 'grid_space'
        database.
        """
        if db == 'grid_space':
            return model._meta.app_label == 'grid_space'
        elif model._meta.app_label == 'grid_space':
            return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure the grid_space apps only appears on the grid_space db"""
        if model._meta.app_label in ['south']:
            return True
        if db == 'grid_space':
            return model._meta.app_label == 'grid_space'
        elif model._meta.app_label == 'grid_space':
            return False
        return None

    def allow_syncdb(self, db, model):
        """Make sure the grid_estates apps only appears on the grid_space db"""
        if model._meta.app_label in ['south']:
            return True
        if db == 'grid_space':
            return model._meta.app_label == 'grid_space'
        elif model._meta.app_label == 'grid_space':
            return False
        return None
