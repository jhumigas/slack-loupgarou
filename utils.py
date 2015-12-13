import json
from player import Player
from random import *
from slackclient import SlackClient

#Ce fichier contient toutes les fonctions utilitaires


#Retourne la liste des noms des gens sur le chan (les gens sur le chan au debut de la 
#partie sont ceux qui participent au loup-garou)
def get_members(sc, channel_id):
	users = []

	users_id = json.loads(sc.api_call("channels.info", channel=channel_id))["channel"]["members"]
	for user_id in users_id:
		name = json.loads(sc.api_call("users.info", user=user_id))["user"]["name"]
		if name != "maitre_du_jeu":
			users.append(Player(user_id,name))
		
		
	return users
	
#Reparti les loups-garous
#Retourne : le nombre de loups-garous crees
def generate_wolves(players, sc):
	wolves_number = 1
	#Repartitions des joeurs
	if len(players)<6:
		#1 seul loup-garou
		wolves_number = 1
	elif len(players)==6 and len(players)<9:
		#2 loups-garous
		wolves_number = 2
	elif len(players)==9 and len(players)<13:
		#3 loups-garous
		wolves_number = 3
	elif len(players)==13 and len(players)<17:
		#4 loups-garous (Wahoo ca en fait du monde qui joue !!)
		wolves_number = 4
	elif len(players) >= 17:
		#TODO :Nombre de loups proportionnel
		wolves_number = 5
		
	for i in range (wolves_number):
		create_wolf(players, sc)
		
		
	return wolves_number

#Trouve un villageois aleatoirement et le definit comme loup-garou
def create_wolf(players, sc):
	go_on = True
	
	while go_on:
		new_wolf = choice(players)
		if new_wolf.type == "Villageois":
			new_wolf.type = "Loup-Garou"
			go_on = False
			
			#Il faut prevenir le joueur que c'est un loup-garou
			#sc.api_call("chat.postMessage", channel= get_id_of_pm(new_wolf.id, sc), text="Hello " + new_wolf.name + ", juste pour te dire que tu as ete designe comme loup-garou pour cette nouvelle partie !", as_user="true")
			#Finalement utilisation d'une nouvelle fonction pour prevenir tout le monde
			print new_wolf.name, ' est un loup-garou'

#Retourne l'id de la conversation privee avec l'utilisateur ayant pour id user_id
def get_id_of_pm(user_id, sc):
	return json.loads(sc.api_call("im.open", user=new_wolf.id, as_user="true"))["channel"]["id"]
	
	
def inform_players_of_role(players, sc):
	for player in players:
		c.api_call("chat.postMessage", channel= get_id_of_pm(new_wolf.id, sc), text="Hello " + new_wolf.name + ", juste pour te dire que tu as ete designe comme " + player.type + " pour cette nouvelle partie !", as_user="true")
			
	
	