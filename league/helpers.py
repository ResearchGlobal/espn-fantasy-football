
from typing import Any, Dict, List
import csv
from league.draft_types import (
    LeagueData,
    DraftResults,
    DraftPick,
    PlayerAuctionData,
    TeamV2,
    GmData,
    PositionData,
    GmDataMap,
    TeamMap,
)
from espn_api.football import League

def safe_get(lst: list, index: int, default=None) -> str | None:
    return lst[index] if 0 <= index < len(lst) else default
  
def extract_draft_data(source: LeagueData, league: League, teams: TeamMap) -> List[PlayerAuctionData]:
    draftDetails = source.get("draftDetail")
    picks = draftDetails.get("picks")
    draftResults = [extract_player_auction_data(pick, league, teams) for pick in picks]
    return draftResults
  

def extract_player_auction_data(pick: DraftPick, league: League, teams: TeamMap) -> PlayerAuctionData:
    playerMap = league.player_map
    playerId = pick.get("playerId")
    proTeam = league.player_info(None, playerId).proTeam
    position = league.player_info(None, playerId).position
    posRank = league.player_info(None, playerId).posRank
    totalPoints = league.player_info(None, playerId).total_points
    avgPoints = league.player_info(None, playerId).avg_points
    name: str = playerMap.get(playerId)
    nameSplit = name.split(" ")
    first = nameSplit[0]
    last = nameSplit[1]
    suffix = safe_get(nameSplit, 2)
    teamId = pick.get("teamId")
    teamOwner = teams.get(teamId).get("owner")
    bidAmount = pick.get("bidAmount")

    return {
        "playerId": playerId,
        "playerName": name,
        "playerFirst": first,
        "playerLast": last,
        "playerSuffix": suffix,
        "proTeam": proTeam,
        "position": position,
        "posRank": posRank,
        "totalPoints": totalPoints,
        "avgPoints": avgPoints,
        "bidAmount": bidAmount,
        "nominatingTeamId": pick.get("nominatingTeamId"),
        "memberId": pick.get("memberId"),
        "teamId": teamId,
        "teamName": teams.get(teamId).get("name"),
        "teamOwner": teamOwner,
        "teamAbbrev": teams.get(teamId).get("abbrev"),
        "keeper": pick.get("keeper"),
        "reservedForKeeper": pick.get("reservedForKeeper"),
    }

def scaffold_gm_data(pickResults: List[PlayerAuctionData], teams: TeamMap) -> GmDataMap:
    base = {}
    for key in teams:
        base[teams.get(key).get("owner")] = {
            "QB": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "RB": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "WR": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "TE": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "D/ST": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "K": {"totalBudgetSpent": 0, "numberOfPicks": 0},
        }

    for pick in pickResults:
        owner = pick.get("teamOwner")
        position = pick.get("position")
        bidAmount = pick.get("bidAmount")
        base[owner][position] = {
            "totalBudgetSpent": base[owner][position]["totalBudgetSpent"] + bidAmount,
            "numberOfPicks": base[owner][position]["numberOfPicks"] + 1,
        }

    return base
  

def write_draft_results(file_name: str, pick_results: List[PlayerAuctionData]):
    with open(file_name, 'w', newline='') as team_file:
        writer = csv.writer(team_file)
        writer.writerow([
            "playerId",
            "playerName",
            "playerFirst",
            "playerLast",
            "playerSuffix",
            "proTeam",
            "position",
            "posRank",
            "totalPoints",
            "avgPoints",
            "bidAmount",
            "nominatingTeamId",
            "memberId",
            "teamId",
            "teamName",
            "teamOwner",
            "teamAbbrev",
            "keeper",
            "reservedForKeeper",
        ])
        for pick in pick_results:
            writer.writerow(pick.values())
    

# with open(csv_teams_filename_2025, 'w', newline='') as team_file:
#   writer = csv.writer(team_file)
#   writer.writerow([
#     "abbrev","teamId","name","owner"
#   ])
#   for team in teams_2025:
#     writer.writerow(teams_2025[team].values())

# with open(csv_gmdata_filename_2025, "w", newline="") as gm_data:
#     writer = csv.writer(gm_data)
#     writer.writerow(
#         [
#             "teamOwner",
#             "QB $ Spent",
#             "QB # Picks",
#             "RB $ Spent",
#             "RB # Picks",
#             "WR $ Spent",
#             "WR # Picks",
#             "TE $ Spent",
#             "TE # Picks",
#             "D/ST $ Spent",
#             "D/ST # Picks",
#             "K $ Spent",
#             "K # Picks",
#         ]
#     )
#     for gm in gmDataMap:
#         singleGmData: GmData = gmDataMap[gm]
#         row = [gm]
#         for pos in singleGmData:
#             posData: PositionData = singleGmData[pos]
#             row.append(posData.get("totalBudgetSpent"))
#             row.append(posData.get("numberOfPicks"))
#         writer.writerow(row)
