import json
from typing import Any, Dict

from espn_api.football import Team
from league.constant import teams
from league.helpers import (extract_draft_data, scaffold_gm_data, write_draft_results)
from espn_api.football import League

input_filename_2021 = "output/draft-detail-2021.json"
input_filename_2022 = "output/draft-detail-2022.json"
input_filename_2024 = "output/draft-detail-2024.json"
input_filename_2025 = "output/draft-detail-2025.json"
output_filename = "output/test.json"
csv_picks_filename_2021="output/draft-results-2021.csv"
csv_picks_filename_2022="output/draft-results-2022.csv"
csv_picks_filename = "output/test.csv"
csv_picks_filename_2025="output/draft-results-2025.csv"
csv_teams_filename_2024 = "output/team-map.csv"
csv_teams_filename_2025 = "output/team-map-2025.csv"
csv_gmdata_filename = "output/gm-data.csv"
csv_gmdata_filename_2025 = "output/gm-data-2025.csv"

league = League(
    league_id=1809145,
    year=2021,
    espn_s2="AEAb0%2FC10zP7SYtNgakwQ43vCfN8SBJWbas5bkmZpYtCi4ssMvB5gbi5xbG5K5D0EJWoMxpZUA0mKqaUKdauEdzP3srhQXVzjF%2BZjIAnVL8%2BxqGgXoAuCdMsZrtmZhIKsYzGwqb5fph4aaTTCb9U0L%2F9nWXBlZgkIj%2Feuqis%2FWTd8sPTR0T7EZZQx%2BmFynYBNt0VCLH4UV8n6V5Kg%2FVAR8MK0QMEPR0BkJVyF6kgPjxFn4QpM%2BFWnqtHkUlgJI8aOArxevvR3MZ4Q8UNvWmIYEVjx0zY8%2Fq2YkMbrVIaekmaZYdyOyoTiIlIqCoatRdf7vU%3D",
    swid="{C5575E3E-3B10-4280-975E-3E3B10A280F8}",
)


with open(input_filename_2021, "r") as file:
    draft_json: Dict[str, Any] = json.load(file)

pick_results = extract_draft_data(draft_json, league, teams)

# gmDataMap = scaffold_gm_data(pick_results, teams)

write_draft_results(csv_picks_filename_2021, pick_results)
