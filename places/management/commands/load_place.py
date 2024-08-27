import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enjoymap.settings")
import django

django.setup()
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

    image_instance, created = Image.objects.get_or_create(
        location_id=location_id,
        position=image_number
    )

    file_format = image_url.rsplit('.', 1)[-1].lower()
    filename = f'{location_json["title"]}_{image_number}.{file_format}'
    image_instance.file.save(filename, ContentFile(response.content), save=True)


class Command(BaseCommand):
    help = 'Запустите команду с аргументом в виде сссылки на json локации'

    def add_arguments(self, parser):
        parser.add_argument('json_urls', nargs='+', type=str, help='URL(s) to the JSON file(s) with location data')

    def handle(self, *args, **options):
        for url in options['json_urls']:
            try:
                location_json = get_location_json(url)
                location_id = post_location(location_json)
                for image_number, image_url in enumerate(location_json['imgs'], start=1):
                    fetch_and_post_image(image_url, location_id, image_number, location_json)
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {location_json["title"]}'))
            except requests.RequestException as e:
                self.stderr.write(self.style.ERROR(f'Failed to fetch JSON from {url}: {e}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))
