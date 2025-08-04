import json
from typing import Any, Dict, List
from league.draft_types import (
    LeagueData,
    DraftResults,
    DraftPick,
    PlayerAuctionData,
    TeamV2,
    GmData,
    PositionData,
    GmDataMap,
)
from espn_api.football import Team
from league.constant import teams_2024

from espn_api.football import League

input_filename_2024 = "output/draft-detail-2024.json"
output_filename = "output/test.json"

league = League(
    league_id=1809145,
    year=2024,
    espn_s2="AEAb0%2FC10zP7SYtNgakwQ43vCfN8SBJWbas5bkmZpYtCi4ssMvB5gbi5xbG5K5D0EJWoMxpZUA0mKqaUKdauEdzP3srhQXVzjF%2BZjIAnVL8%2BxqGgXoAuCdMsZrtmZhIKsYzGwqb5fph4aaTTCb9U0L%2F9nWXBlZgkIj%2Feuqis%2FWTd8sPTR0T7EZZQx%2BmFynYBNt0VCLH4UV8n6V5Kg%2FVAR8MK0QMEPR0BkJVyF6kgPjxFn4QpM%2BFWnqtHkUlgJI8aOArxevvR3MZ4Q8UNvWmIYEVjx0zY8%2Fq2YkMbrVIaekmaZYdyOyoTiIlIqCoatRdf7vU%3D",
    swid="{C5575E3E-3B10-4280-975E-3E3B10A280F8}",
)

playerMap = league.player_map
teams = league.teams
team = teams[0]

with open(input_filename_2024, "r") as file:
    draft_json_2024: Dict[str, Any] = json.load(file)

with open(input_filename_2024, "r") as file:
    draft_json_2024: Dict[str, Any] = json.load(file)



def safe_get(lst: list, index: int, default=None) -> str | None:
    return lst[index] if 0 <= index < len(lst) else default


def extract_draft_data(source: LeagueData) -> List[PlayerAuctionData]:
    draftDetails = source.get("draftDetail")
    picks = draftDetails.get("picks")
    draftResults = [extract_player_auction_data(pick) for pick in picks]
    return draftResults


def extract_player_auction_data(pick: DraftPick) -> PlayerAuctionData:
    playerId = pick.get("playerId")
    proTeam = league.player_info(None, playerId).proTeam
    position = league.player_info(None, playerId).position
    name: str = playerMap.get(playerId)
    nameSplit = name.split(" ")
    first = nameSplit[0]
    last = nameSplit[1]
    suffix = safe_get(nameSplit, 2)
    teamId = pick.get("teamId")

    teamOwner = teams_2024.get(teamId).get("owner")
    bidAmount = pick.get("bidAmount")

    return {
        "playerId": playerId,
        "playerName": name,
        "playerFirst": first,
        "playerLast": last,
        "playerSuffix": suffix,
        "proTeam": proTeam,
        "position": position,
        "bidAmount": bidAmount,
        "nominatingTeamId": pick.get("nominatingTeamId"),
        "memberId": pick.get("memberId"),
        "teamId": teamId,
        "teamName": teams_2024.get(teamId).get("name"),
        "teamOwner": teamOwner,
        "teamAbbrev": teams_2024.get(teamId).get("abbrev"),
        "keeper": pick.get("keeper"),
        "reservedForKeeper": pick.get("reservedForKeeper"),
    }


pickResults = extract_draft_data(draft_json_2024)

def scaffold_gm_data(pickResults: List[PlayerAuctionData]) -> GmDataMap:
    base = {}
    for key in teams_2024:
        base[teams_2024.get(key).get("owner")] = {
            "QB": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "RB": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "WR": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "TE": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "D/ST": {"totalBudgetSpent": 0, "numberOfPicks": 0},
            "K": {"totalBudgetSpent": 0, "numberOfPicks": 0},
        }
    
    for pick in pickResults:
        owner = pick.get('teamOwner')
        position = pick.get('position')
        bidAmount = pick.get('bidAmount')
        base[owner][position] = {
          'totalBudgetSpent': base[owner][position]['totalBudgetSpent'] + bidAmount,
          'numberOfPicks': base[owner][position]['numberOfPicks'] + 1
        }
    
    return base

gmDataMap = scaffold_gm_data(pickResults)

print(gmDataMap)


with open(output_filename, 'r+') as file:
  json.dump({'2024': {'picks': pickResults, 'teamByTeam': gmDataMap}}, file, indent=2)
