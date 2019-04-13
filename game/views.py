from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from .models import Game
from urllib.parse import urlencode
import json

____ = None


# helper function to redirect to home page and show error message
def redir_index(err_msg):
    return HttpResponseRedirect('{}?{}'.format(reverse('game:index'), urlencode({'err_msg': err_msg})))


# helper function to redirect to the game page
def redir_game(game_id):
    return HttpResponseRedirect(reverse('game:show_game', kwargs={'game_id': game_id}))


# home page
def index(request):
    # set err_msg as an empty string
    err_msg = ''

    # if request method is GET and err_msg is in GET parameters, update err_msg
    if ____:
        ____

    # render index.html with the argument err_msg
    ____


# create a new game, and jump to the game page
def new_game(request):
    # create a game instance, save it, get its id and redirect to the game page
    ____
    ____
    ____
    ____


# check the game id and jump to the game page
def load_game(request):
    # if request method is not GET or game_id is not in GET parameters, redirect to the home page with err_msg
    if ____:
        ____

    # get game_id from GET parameters
    game_id = ____

    # try to convert game_id from str to int
    try:
        game_id = ____

    # if try fails with ValueError exception, redirect to the home page with err_msg
    except ValueError:
        ____

    # if game_id is negative, redirect to the home page with err_msg
    if ____:
        ____

    # redirect to the game page
    ____


# read the game and show it
def show_game(request, game_id):
    # try to get the game from Game objects
    try:
        game = ____

    # if try fails with Game.DoesNotExist exception, redirect to the home page with err_msg
    except Game.DoesNotExist:
        ____

    # get board from game and convert the json string to 2-d list
    board = ____

    # render game.html with arguments game and board
    ____


# mark the game board
def mark(request, game_id):
    # try to get the game from Game objects
    try:
        game = ____

    # if try fails with Game.DoesNotExist exception, redirect to the home page with err_msg
    except Game.DoesNotExist:
        ____

    # if request method is not POST or row or col is not in in POST parameters, redirect to the game page
    # Note:
    #   GET parameters are appended in the request URL
    #   POST parameters are in the request body with the same format as GET
    #   reference: https://stackoverflow.com/questions/14551194/how-are-parameters-sent-in-an-http-post-request
    if ____:
        ____

    # get row and col from POST parameters
    row = ____
    col = ____

    # try to convert row and col from str to int
    try:
        row = ____
        col = ____

    # if try fails with ValueError exception, redirect to the game page
    except ValueError:
        ____

    # if row and col are not between 0 and BOARD_SIZE - 1, redirect to the game page
    if ____:
        ____

    # mark on the board and change the game status
    mark_on_board(game, row, col)

    # redirect to the game page
    ____


# mark on the board and change the game status
def mark_on_board(game, row, col):
    # get board from game and convert the json string to 2-d list
    board = ____

    # if the cell to be marked is marked already, return
    if ____:
        return

    # mark the cell on the board
    board[row][col] = ____
    # convert board from list to json string and store in game.board
    ____

    # increase turn count by 1
    ____

    # if the board is full (determined by turn_count), change the game status to draw
    if ____:
        ____

    # before checking win conditions, determine the next possible status based on who is the current player
    if ____:
        next_status = ____
    else:
        next_status = ____

    # if all cells on the row of the marked cell are of the current player, change game status to next_status
    if ____:
        ____

    # if all cells on the col of the marked cell are of the current player, change game status to next_status
    if ____:
        ____

    # if the cell is on the top-left to bottom-right diagonal, and all cells on the diagonal are of the current player,
    # change game status to next_status
    if ____:
        ____

    # if the cell is on the top-right to bottom-left diagonal, and all cells on the diagonal are of the current player,
    # change game status to next_status
    if ____:
        ____

    # switch current player
    if ____:
        ____
    else:
        ____

    # save game
    ____
