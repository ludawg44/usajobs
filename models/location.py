import db as db
import models as models

class Location:
    __table__ = 'locations'
    columns = ['id', 'position_id', 'country_code', 'country_sub_division_code', 'city_name', 'longitude', 'latitude']
    
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}'
        for k, v in kwargs.items():
            setattr(self, k, v)

