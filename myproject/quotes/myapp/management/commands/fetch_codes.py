import requests
from django.core.management.base import BaseCommand
from myapp.models import Quote

class Command(BaseCommand):
    help = 'Fetch and store quotes from the API'

    def handle(self, *args, **kwargs):
        response = requests.get("https://api.quotable.io/quotes?limit=150")  # Adjust limit as needed
        data = response.json()

        for item in data['results']:
            text = item["content"]
            author = item["author"]

            if not Quote.objects.filter(text=text, author=author).exists():
                Quote.objects.create(text=text, author=author)

        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored quotes'))
