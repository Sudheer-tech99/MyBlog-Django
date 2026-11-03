import os
from pathlib import Path
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Import blog data from blogdata.json"

    def handle(self, *args, **kwargs):
        file_path = Path(__file__).resolve().parents[3] / "blogdata.json"

        if not file_path.exists():
            self.stdout.write(
                self.style.ERROR("blogdata.json file not found!")
            )
            return

        call_command("loaddata", str(file_path))

        self.stdout.write(
            self.style.SUCCESS("Blog data imported successfully!")
        )