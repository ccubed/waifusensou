from flask import *

api = Blueprint('api', __name__)


@api.route("/create", methods=['POST'])
def create():
    return "API CREATE"


@api.route("/vote/<wid>/<choice>", methods=['POST'])
def vote(wid, choice):
    return "API VOTE"


@api.route("/<wid>", methods=['GET', 'PATCH', 'DELETE'])
def wars(wid):
    return "API GET OR UPDATE WAR"


@api.route("/waifus", defaults={'page': 1}, methods=['GET'])
@api.route("/waifus/<page>", methods=['GET'])
def waifus(page):
    return "API GET WAIFU DATA."


@api.route("/waifu/<wuuid>", methods=['GET'])
def waifu_stats(wuuid):
    return "API GET WAIFU STATISTICS FOR A CERTAIN WAIFU"
