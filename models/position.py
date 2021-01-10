import db as db
import models as models

class Position():
    __table__ = 'positions'
    columns = ['usa_jobs_id', 'position_title', 'position_url']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_title(self, position_title, cur):
        position_query = """SELECT * FROM positions WHERE position_title = %s"""
        cur.execute(position_query, (position_title,))
        record = cur.fetchone()
        return db.build_from_record(models.Position, record)
