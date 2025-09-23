from typing import TypedDict, List, Dict, Any, TypeAlias, Literal

# inputs:
class TeamMatchupData(TypedDict):
  teamId: int
  totalPoints: float

class WeeklyMatchup(TypedDict):
  away: TeamMatchupData
  home: TeamMatchupData
  matchupPeriodId: int
  
#outputs
class TopScoringMatchupWinner(TypedDict):
  week: int # matchupPeriodId
  winner: int # teamId of winner
  winner_score: float # score of winner
  loser: int # teamID of loser
  loser_score: float # score of loser
  
class TopScoringMatchupWinnersBySeason(TypedDict):
  _2020: List[TopScoringMatchupWinner]
  _2021: List[TopScoringMatchupWinner]
  _2022: List[TopScoringMatchupWinner]
  _2023: List[TopScoringMatchupWinner]
  _2024: List[TopScoringMatchupWinner]
  