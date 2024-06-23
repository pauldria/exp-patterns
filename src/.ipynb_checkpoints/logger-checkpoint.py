from   datetime import datetime
import pandas as pd

class Logger:

    def __init__(self):
        self.visit_log    = []
        self.exposure_log = []
        self.metrics_log  = []

    def add_to_visit_log(self, user_id):
        self.visit_log.append((user_id, datetime.now()))

    def add_to_exposure_log(self, user_id, variant_name):
        self.exposure_log.append((user_id, variant_name, datetime.now()))

    def get_visit_log(self, columns = ("user_id", "visit_timestamp")):
        return pd.DataFrame(data = self.visit_log, columns = columns)

    def get_exposure_log(self, columns = ("user_id", "variant_name", "exposure_timestamp")):
        return pd.DataFrame(data = self.exposure_log, columns = columns)