class RadarDragon:
	region1: int
	region2: int
	def __init__(self, region1: int, region2: int):
		self.region1=region1
		self.region2=region2
	
	def buscar_esferas(self):
		esferas_en_posesion=3
		esferas_encontradas=self.region1+self.region2
		esferas_en_posesion+=esferas_encontradas
		total_esferas=esferas_en_posesion


radar_bulma=RadarDragon(3,2)

