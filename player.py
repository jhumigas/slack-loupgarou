class Player:

	def __init__(self, user_id, user_name):
		self.name = user_name
		self.id = user_id
		self.is_alive = True
		self.type = "Villageois" #Types possibles : Villageois, Sorciere, Voyante, Loup-Garou, Cupidon, Chasseur
		self.is_mayor = False
		
		