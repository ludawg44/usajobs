import db as db
import models as models 

class Term:
    __table__ = 'terms'
    columns = ['id', 'position_id', 'travel_percentages', 'position_schedule_name', 'position_offering_type_name', 'security_clearance']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

    