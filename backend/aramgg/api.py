import os
from typing import Dict, List

import django
import requests
from aramgg.models import Champion, User

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.local_settings"
django.setup()


API_KEY = "RGAPI-1f479b8e-1c4b-400d-a871-b98ed6029f1f"
BASE_URL = "https://na1.api.riotgames.com"
PARAMS = {"api_key": API_KEY}


class RiotApiRequests:
    def __init__(self, summoner_name: str, request_limit: int = 10):
        self.summoner_name = summoner_name
        self.request_limit = request_limit

    def get_account_info(self) -> User:
        """ Get account information based on the summoner name """

        url = f"{BASE_URL}/lol/summoner/v4/summoners/by-name/{self.summoner_name}"
        request = requests.get(url=url, params=PARAMS)
        data = request.json()
        User.objects.update_or_create(
            username=data["name"],
            defaults={
                "profile_icon": data["profileIconId"],
                "account_id": data["accountId"],
                "level": data["summonerLevel"],
            },
        )
        return User.objects.get(username=data["name"])

    @staticmethod
    def get_match_list(user: User) -> List[Dict[str, int]]:
        """ Get list of game IDs and timestamps based on the summoner's account ID """

        url = f"{BASE_URL}/lol/match/v4/matchlists/by-account/{user.account_id}"
        request = requests.get(url=url, params=PARAMS)
        match_list = request.json()
        final_list = [
            {"gameId": match["gameId"], "timestamp": match["timestamp"]}
            for match in match_list["matches"]
        ]
        final_list = sorted(final_list, key=lambda k: k["timestamp"])

        # If user already has a record of timestamp,
        # only get game records that happened after given timestamp
        if user.last_updated is not None:
            final_list = list(
                filter(
                    lambda element: element["timestamp"] > user.last_updated, final_list
                )
            )

        return final_list

    @staticmethod
    def get_match_data(user: User, match_id: int) -> Dict:
        """ Get information about specific match based on the match ID """

        url = f"{BASE_URL}/lol/match/v4/matches/{match_id}"
        request = requests.get(url=url, params=PARAMS)
        data = request.json()
        participant_identity_list = data["participantIdentities"]
        participant_id = None

        for identity in participant_identity_list:
            if identity["player"]["currentAccountId"] == user.account_id:
                participant_id = identity["participantId"]
                break

        # Get the match information about the user
        participant_info = next(
            participant
            for participant in data["participants"]
            if participant["participantId"] == participant_id
        )
        participant_stats = participant_info["stats"]

        # Get or create champion records and update relative fields
        champion, created = Champion.objects.get_or_create(
            champion_id=participant_info["championId"],
        )
        if participant_stats["win"]:
            champion.win += 1
        else:
            champion.loss += 1
        champion.total_damage_done += participant_stats["totalDamageDealtToChampions"]
        champion.total_healing_done += participant_stats["totalHeal"]
        champion.total_damage_taken += participant_stats["totalDamageTaken"]
        champion.kill += participant_stats["kills"]
        champion.death += participant_stats["deaths"]
        champion.assist += participant_stats["assists"]
        champion.save()

        user.champion.add(champion)
        user.save()
        return data

    def get_total_match_info(self) -> List:
        """ Return combined dictionary with relevant match information """

        aram_list = list()
        user = self.get_account_info()
        match_list = self.get_match_list(user=user)

        for index, match in zip(range(self.request_limit), match_list):
            match_data = self.get_match_data(user=user, match_id=match["gameId"])
            if match_data["gameMode"] == "ARAM":
                aram_list.append(match_data)
            timestamp = match_data["gameCreation"]
            user.last_updated = (
                timestamp
                if (user.last_updated is None or timestamp > user.last_updated)
                else user.last_updated
            )
            user.save()

        return aram_list


if __name__ == "__main__":
    riot_api = RiotApiRequests(summoner_name="juis", request_limit=10)
    total_match_info = riot_api.get_total_match_info()
