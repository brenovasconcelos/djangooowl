import csv
from django.core.management.base import BaseCommand
from core.models import User
import requests

API_KEY = "AIzaSyAg0-xK94fHVyV-Gn6Bad44YgQbSQ-3O_I"
GOOGLE_MAPS_URL = "https://maps.googleapis.com/maps/api/geocode/json?address={search_str}&key={api_key}"


class Command(BaseCommand):
    """
    Command that handle with the user CSV
    """

    help = "script to insert users from a csv file"

    def handle(self, *args, **kwargs):
        """
        This is a simple script that insert users
        on a local database from a csv file
        """
        users = open("utils/customers.csv")
        user_by_line = list(csv.reader(users))
        db_fields = user_by_line[0]
        user_by_line.remove(db_fields)
        user_bulk_insert = []

        for user in user_by_line:

            preloaded_user = zip(db_fields, user)
            user_dict = dict(preloaded_user)
            print("Inserting ", user_dict["first_name"])
            latitude, longitude = get_coordinates(user_dict["city"])
            user_bulk_insert.append(
                User(
                    first_name=user_dict["first_name"],
                    last_name=user_dict["last_name"],
                    city=user_dict["city"],
                    company=user_dict["company"],
                    email=user_dict["email"],
                    gender=user_dict["gender"],
                    title=user_dict["title"],
                    latitude=latitude,
                    longitude=longitude,
                )
            )

        User.objects.bulk_create(user_bulk_insert)

        return "users inserted on database"


def get_coordinates(city_name):
    """
    This function gets the coordinates based on 'city' field

    returns LATITUDE and LONGITUDE
    """

    formatted_cn = city_name.replace(" ", "%20")
    url = GOOGLE_MAPS_URL.format(search_str=formatted_cn, api_key=API_KEY)
    ret = requests.get(url).json()

    lat = ret["results"][0]["geometry"]["location"]["lat"]
    lng = ret["results"][0]["geometry"]["location"]["lng"]

    return lat, lng