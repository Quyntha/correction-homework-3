import json

class Model:
	title = 0
	text = 0
	author = 0

	def save(self):
		list(filter(lambda x: not x.startswith('_'), dir(Model)))
		js = json.dumps(self.__dict__)
		print(js)
		
ml = Model()
ml.title = '2'
ml.text = '1'
ml.author = '4'
ml.save()