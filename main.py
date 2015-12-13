#IMPORTANT, il faut renseigner le token du bot dans private.py
#Il est identifie par la variable "token"
#Pour des raisons evidentes de securite ne commitez pas le token du bot, pensez au .gitignore s'il vous plait
#
#Pour plus d'infos n'hesitez pas a joigner le chan loupgarou-dev
#
#Made with love by the DTY team, add your name here :
#@ronan
#
#This is fucking open source so enjoy, no Microsoft techno out there !
#Okay, the first lines were written using Visual Studio Code...

import private
import time
import json
from utils import *
from player import Player
from slackclient import SlackClient


#ID du chan loupgarou-dev, a recuperer de maniere plus propre
channel_id = "C0GEPSV38"

#Liste des joueurs
players = []

sc = SlackClient(token)

#On verifie que l'appel a l'API fonctionne
print sc.api_call("api.test")


#Dire bonjour a tous parce que c'est bonne ambiance !
sc.api_call("chat.postMessage", channel=channel_id, text="Bienvenue pour une nouvelle partie de Loup Garou !", as_user="true")

#Recuperation des joeurs
players = get_members(sc, channel_id)

#Construction du message d'annonce
message = 'Il y a ' + str(len(players)) + ' joueurs qui jouent : '
for player in players:
	message += player.name + ', '
	
sc.api_call("chat.postMessage", channel=channel_id, text=message, as_user="true")

#Generation des loups-garous
wolves_number = generate_wolves(players, sc)

sc.api_call("chat.postMessage", channel=channel_id, text=str(wolves_number)+" loups-garous ont ete designes, ils ont recu un message prive.", as_user="true")




