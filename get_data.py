from riotwatcher import TftWatcher
import requests

path = "key.txt"
with open(path) as f:
    key = f.read()

sub_region = "jp1"
region = "asia"
watcher = TftWatcher(key)
challengers_data = watcher.league.challenger(sub_region)
challengers_data = challengers_data["entries"]
# for challenger in challengers_data:
#     name = challenger["summonerName"]
#     summoner_data = watcher.summoner.by_name(sub_region, name)
#     match_id = watcher.match.by_puuid(region, summoner_data["puuid"])

name = challengers_data[0]["summonerName"]
summoner_data = watcher.summoner.by_name(sub_region, name)
match_id = watcher.match.by_puuid(region, summoner_data["puuid"])
for match in match_id:
    match_data = watcher.match.by_id(region, match)
    print(match_data)
    break