import db as db
import models as models

class Application:
    __table__ = 'applications'
    columns = ['id', 'position_id', 'publication_start_date', 'application_close_date']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

            