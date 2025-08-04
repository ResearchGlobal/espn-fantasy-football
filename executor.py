
import json
from typing import Any, Dict, List
from draft_types import LeagueData, DraftResults, DraftPick, PlayerAuctionData, Team

from espn_api.football import League

input_filename = 'output/draft-detail-2024.json'
output_filename = 'output/test.json'

league = League(league_id=1809145, year=2024, espn_s2='AEAb0%2FC10zP7SYtNgakwQ43vCfN8SBJWbas5bkmZpYtCi4ssMvB5gbi5xbG5K5D0EJWoMxpZUA0mKqaUKdauEdzP3srhQXVzjF%2BZjIAnVL8%2BxqGgXoAuCdMsZrtmZhIKsYzGwqb5fph4aaTTCb9U0L%2F9nWXBlZgkIj%2Feuqis%2FWTd8sPTR0T7EZZQx%2BmFynYBNt0VCLH4UV8n6V5Kg%2FVAR8MK0QMEPR0BkJVyF6kgPjxFn4QpM%2BFWnqtHkUlgJI8aOArxevvR3MZ4Q8UNvWmIYEVjx0zY8%2Fq2YkMbrVIaekmaZYdyOyoTiIlIqCoatRdf7vU%3D', swid='{C5575E3E-3B10-4280-975E-3E3B10A280F8}')

playerMap = league.player_map
teams: List[Team] = league.teams
team = teams[0]
# print(playerMap)

def printTeam(localTeam: Team):
  print(dir(localTeam))
  print(localTeam.team_abbrev)
  # for key, value in vars(localTeam).items():
  #     print(f"{key}: {value}")
  # print(json.dumps(localTeam))
  # print(type(localTeam))
  # for key, value in localTeam.items():
  #       print(f"{key}: {value}")
printTeam(team)

with open(input_filename,'r') as file:
  draft_json: Dict[str, Any] = json.load(file)
    
def safe_get(lst: list, index: int, default=None) -> str | None:
  return lst[index] if 0 <= index < len(lst) else default
    
def extract_draft_data(source: LeagueData) -> DraftResults:
  draftDetails = source.get('draftDetail')
  # print(extract_player_auction_data(draftDetails.get('picks')[0]))
  return

def extract_player_auction_data(pick: DraftPick) -> PlayerAuctionData: 
  playerId = pick.get('playerId')
  name: str = playerMap.get(playerId)
  nameSplit = name.split(' ')
  first = nameSplit[0]
  last = nameSplit[1]
  suffix = safe_get(nameSplit, 2)
  pick.get('')
  return {
    'playerId': playerId,
    'playerName': name,
    'playerFirst': first,
    'playerLast': last,
    'playerSuffix': suffix,
    'bidAmount': pick.get('bidAmount'),
    'nominatingTeamId': pick.get('nominatingTeamId'),
    'memberId': pick.get('memberId'),
    'teamId': pick.get('teamId'),
    'keeper': pick.get('keeper'),
    'reservedForKeeper': pick.get('reservedForKeeper'),
  }


extract_draft_data(draft_json)

# print(draft_json)












# print(league.p)
# print(league.player_info(None, 4241389).)

# league_data = json.loads(json.dumps(league.draft, default=make_serializable))

# with open(filename, 'w') as file: 
#   json.dump(league, file, indent=2)

# print(league_json)

# def make_serializable(obj):
#     # Handle common non-serializable types
#     if hasattr(obj, '__dict__'):
#         return obj.__dict__  # Convert custom objects to dict
#     elif isinstance(obj, (set, tuple)):
#         return list(obj)  # Convert sets/tuples to lists
#     elif hasattr(obj, 'isoformat'):  # For datetime objects
#         return obj.isoformat()
#     else:
#         return str(obj)  # Fallback: convert to string
      
# def extract_draft_data(obj):
#   return
