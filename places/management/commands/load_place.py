import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Location, Image


def get_location_json(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    return response.json()


def post_location(location_json):
    location, created = Location.objects.get_or_create(
        title=location_json['title'],
        defaults={
            'short_description': location_json['description_short'],
            'long_description': location_json['description_long'],
            'lng': location_json['coordinates']['lng'],
            'lat': location_json['coordinates']['lat']
        }
    )
    return location.id


def fetch_and_post_image(image_url, location_id, image_number, location_json):
    response = requests.get(image_url)
    response.raise_for_status()

    file_format = image_url.rsplit('.', 1)[-1].lower()
    filename = f'{location_json["title"]}_{image_number}.{file_format}'
    content_file = ContentFile(response.content, name=filename)
    Image.objects.get_or_create(
                                location_id=location_id,
                                position=image_number,
                                file=content_file
                                )

class Command(BaseCommand):
    help = 'Запустите команду с аргументом в виде сссылки на json локации'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+', type=str, help='URL(s) to the JSON file(s) with location data')

    def handle(self, *args, **options):
        for url in options['json_urls']:
            try:
                serialize_location = get_location_json(url)
                location_id = post_location(serialize_location)
                for image_number, image_url in enumerate(serialize_location['imgs'], start=1):
                    fetch_and_post_image(image_url, location_id, image_number, serialize_location)
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {serialize_location["title"]}'))
            except requests.exceptions.HTTPError as HTTP_error:
                self.stderr.write(self.style.ERROR(f'HTTP error {HTTP_error}'))
            except requests.exceptions.ConnectionError as connection_error:
                self.stderr.write(self.style.ERROR(f'Connection error {connection_error}'))

