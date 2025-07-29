import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/tipsters/api/pinnacle-odds'

mcp = FastMCP('pinnacle-odds')

@mcp.tool()
def list_of_periods(sport_id: Annotated[Union[int, float], Field(description='Sport id Default: 1 Minimum: 1 Maximum: 29')]) -> dict: 
    '''Get a list of periods'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/meta-periods'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def event_details(event_id: Annotated[Union[int, float], Field(description='Event id Default: 1419211461')]) -> dict: 
    '''Get a event details and history odds. history:[time, value, max bet]. `Period_results - status`: 1 = Event period is settled, 2 = Event period is re-settled, 3 = Event period is cancelled, 4 = Event period is re-settled as cancelled, 5 = Event is deleted'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/details'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_sports() -> dict: 
    '''Get a list of sports'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/sports'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_special_markets(sport_id: Annotated[Union[int, float], Field(description='Sport id Default: 1 Minimum: 1 Maximum: 29')],
                            event_type: Annotated[Literal['prematch', 'live', None], Field(description='Status: prematch, live Please note that prematch and live events are different')] = None,
                            event_ids: Annotated[Union[str, None], Field(description='Event ids. ex: 3,67,90')] = None,
                            since: Annotated[Union[int, float, None], Field(description='Since UTC time. Calls return changes since the provided since value.')] = None,
                            league_ids: Annotated[Union[str, None], Field(description='League ids. ex: 3,67,90')] = None,
                            is_have_odds: Annotated[Union[bool, None], Field(description='1 or 0. You can only get matches for which there are already open odds, or matches that will be given odds in the future')] = None) -> dict: 
    '''Get a list of special markets. Always first issue a snapshot call and continue with the delta calls. Calls return changes since the provided `since` value. You must always use the since parameter, after the first call. Please note that prematch and live events are different'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
        'event_type': event_type,
        'event_ids': event_ids,
        'since': since,
        'league_ids': league_ids,
        'is_have_odds': is_have_odds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_archive_events(sport_id: Annotated[Union[int, float], Field(description='Sport id Default: 1 Minimum: 1 Maximum: 29')],
                           page_num: Annotated[Union[int, float], Field(description='Page num Default: 1 Minimum: 1 Maximum: 1000')],
                           league_ids: Annotated[Union[str, None], Field(description='League ids. ex: 3,67,90')] = None,
                           start_before: Annotated[Union[str, None], Field(description='Start before')] = None,
                           start_after: Annotated[Union[str, None], Field(description='Start after')] = None) -> dict: 
    '''Get a list of archive events. Use pagination'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/archive'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
        'page_num': page_num,
        'league_ids': league_ids,
        'start_before': start_before,
        'start_after': start_after,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_leagues(sport_id: Annotated[Union[int, float], Field(description='Sport id Default: 1 Minimum: 1 Maximum: 29')]) -> dict: 
    '''Get a list of leagues'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/leagues'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_of_markets(sport_id: Annotated[Union[int, float], Field(description='Sport id Default: 5 Minimum: 1 Maximum: 29')],
                    league_ids: Annotated[Union[str, None], Field(description='League ids. ex: 3,67,90')] = None,
                    event_ids: Annotated[Union[str, None], Field(description='Event ids. ex: 3,67,90')] = None,
                    event_type: Annotated[Literal['prematch', 'live', None], Field(description='Status: prematch, live Please note that prematch and live events are different')] = None,
                    since: Annotated[Union[int, float, None], Field(description='Since UTC time. Calls return changes since the provided since value.')] = None,
                    is_have_odds: Annotated[Union[bool, None], Field(description='1 or 0. You can only get matches for which there are already open odds, or matches that will be given odds in the future')] = None) -> dict: 
    '''Get a list of markets. Always first issue a snapshot call and continue with the delta calls. Calls return changes since the provided `since` value. You must always use the `since` parameter, after starting your program cycle. You can make request without a `since` parameter no more than 25 times in 5 minutes. Please note that `prematch` and `live` events are different'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/markets'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
        'league_ids': league_ids,
        'event_ids': event_ids,
        'event_type': event_type,
        'since': since,
        'is_have_odds': is_have_odds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def betting_status() -> dict: 
    '''Get a betting status. Checking the Pinnacle server'''
    url = 'https://pinnacle-odds.p.rapidapi.com/kit/v1/betting-status'
    headers = {'x-rapidapi-host': 'pinnacle-odds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
