from typing import TypedDict, List, Dict, Any, TypeAlias, Literal

# Define type for notification settings
class NotificationSetting(TypedDict):
    enabled: bool
    id: str
    type: str

# Define type for league members
class Member(TypedDict):
    displayName: str
    firstName: str
    id: str
    isLeagueCreator: bool
    isLeagueManager: bool
    lastName: str
    notificationSettings: List[NotificationSetting]

# Define type for draft picks (with optional 'memberId')
class DraftPick(TypedDict, total=False):
    autoDraftTypeId: int
    bidAmount: int
    id: int
    keeper: bool
    lineupSlotId: int
    nominatingTeamId: int
    overallPickNumber: int
    playerId: int
    reservedForKeeper: bool
    roundId: int
    roundPickNumber: int
    teamId: int
    tradeLocked: bool
    memberId: str

# Define type for draft details
class DraftDetail(TypedDict):
    completeDate: int
    drafted: bool
    inProgress: bool
    picks: List[DraftPick]

# Define type for team record parts (away, division, home, overall)
class TeamRecordPart(TypedDict):
    gamesBack: float
    losses: int
    percentage: float
    pointsAgainst: float
    pointsFor: float
    streakLength: int
    streakType: str
    ties: int
    wins: int

# Define type for team record
class TeamRecord(TypedDict):
    away: TeamRecordPart
    division: TeamRecordPart
    home: TeamRecordPart
    overall: TeamRecordPart

# Define type for transaction counter
class TransactionCounter(TypedDict):
    acquisitionBudgetSpent: int
    acquisitions: int
    drops: int
    matchupAcquisitionTotals: Dict[int, int]
    misc: int
    moveToActive: int
    moveToIR: int
    paid: int
    teamCharges: int
    trades: int

# Define type alias for values by stat (stat ID to integer value)
ValuesByStat: TypeAlias = Dict[int, int]

# Define type for teams
class TeamV2(TypedDict):
    abbrev: str
    currentProjectedRank: int
    divisionId: int
    draftDayProjectedRank: int
    id: int
    isActive: bool
    logo: str
    logoType: str
    name: str
    owners: List[str]
    playoffSeed: int
    points: float
    pointsAdjusted: float
    pointsDelta: float
    primaryOwner: str
    rankCalculatedFinal: int
    rankFinal: int
    record: TeamRecord
    transactionCounter: TransactionCounter
    valuesByStat: ValuesByStat
    waiverRank: int
    watchList: List[Any]

# Define type for league data
class LeagueData(TypedDict):
    draftDetail: DraftDetail
    gameId: int
    id: int
    members: List[Member]
    scoringPeriodId: int
    seasonId: int
    segmentId: int
    settings: Dict[str, Any]
    status: Dict[str, Any]
    teams: List[TeamV2]
    
class PlayerAuctionData(TypedDict):
    playerId: int
    playerName: str
    playerFirst: str
    playerLast: str
    playerSuffix: str | None
    bidAmount: int
    proTeam: str
    position: str
    nominatingTeamId: int
    memberId: str
    teamId: int
    teamName: str
    teamOwner: str
    teamAbbrev: str
    keeper: bool
    reservedForKeeper: bool

class DraftResults(TypedDict):
    roster: Dict[int, PlayerAuctionData]
    teamName: str
    teamAbbrev: str
    teamId: int
    
class DraftResultsByYear(TypedDict):
    Dict[int, DraftResults]

class TeamMapDetail(TypedDict):
    abbrev: str
    teamId: int
    name: str
    owner: str

class TeamMap(TypedDict):
    Dict[int, TeamMapDetail]
    

Position: TypeAlias = Literal["QB","RB","WR","TE","D/ST","K"]

class PositionData(TypedDict):
    totalBudgetSpent: int
    numberOfPicks: int

class GmData(TypedDict):
    Dict[Position,PositionData]
    
class GmDataMap(TypedDict):
    Dict[str,GmData]

    