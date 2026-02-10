import requests
from rich import print

print("[bold green]Python Termux siap 🚀[/bold green]")
r = requests.get("https://api.github.com")
print("Status:", r.status_code)
