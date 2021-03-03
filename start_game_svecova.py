import window.player
import svecova.player
import sebastian.player
import martins.player
import lionel.player
import janmrzilek.player
import benda.player
import vrba.player
from gomoku_tournament import GomokuTournament

playerX = svecova.player.Player(1)
playerO = benda.player.Player(-1)

tournament = GomokuTournament(playerX, playerO, 300)
winner = tournament.game()
tournament.save_logs()
print(f'winner is {winner}')
