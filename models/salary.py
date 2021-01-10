import db as db
import models as models

class Salary():
    __table__ = 'salary'
    columns = ['id', 'position_id', 'minimum', 'maximum', 'rate_interval']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
            for k, v in kwargs.items():
                setattr(self, k, v)

    def salary_info(self, cur):
        query_str = "SELECT * FROM salary WHERE position_id = %s"
        cur.execute(query_str, (self.position_id,))
        record = cur.fetchone()
        return db.build_from_record(models.Salary, record)

    