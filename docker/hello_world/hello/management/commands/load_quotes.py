from django.core.management.base import BaseCommand

from hello.parse_quotes import parse_quotes
from hello.models import Quotes

class Command(BaseCommand):

    help = "Loads quote from txt file to database"

    def add_arguments(self, parser):
        parser.add_argument("--file_name",
            dest="file_name",
            required=True,
            help="Path to the file containing quotes")

    def handle(self, *args, **options):
        quotes = parse_quotes(options['file_name'])
        for author, quote in quotes:
            new_quote = Quotes(author=author, text=quote)
            new_quote.save()