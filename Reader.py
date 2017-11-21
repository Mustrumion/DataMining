import pandas as pd
import numpy as np

class Reader:
	def __init__(self):
		self.DefaultTestUsedNames = ("id","region_id","category_id","subregion_id","district_id",\
				"city_id","accurate_location","user_id","sorting_date","created_at_first",\
				"valid_to","title","description","full_description","has_phone","params",\
				"private_business","has_person","photo_sizes","paidads_id_index","paidads_valid_to",\
				"predict_sold","predict_replies","predict_views","reply_call","reply_sms","reply_chat",\
				"reply_call_intent","reply_chat_intent")
		self.DefaultQueriesUsedNames = ("phrase", "category_id", "sessions_count")
		self.UsedNames = None
		self.DataFrame = None
		

	def LoadTestAds(self, year, month):
		if self.UsedNames is None:
			self.UsedNames = self.DefaultTestUsedNames
		path = "AdsTraining\\ads_%d_%s_01\\001_anonimized" % (year, str(month).zfill(2))
		pd.read_csv(path, names = self.UsedNames, delimiter = ",", low_memory = False)

	def LoadQueries(self, year, month, day):
		if self.UsedNames is None:
			self.UsedNames = self.DefaultQueriesUsedNames
		path = "Queries\\search_queries_%d_%s_%s.csv" % (year, str(month).zfill(2), str(day).zfill(2))
		pd.read_csv(path, names = self.UsedNames, delimiter = ",", low_memory = False, header = None)