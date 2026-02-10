from rich.console import Console
from rich.table import Table
from rich import print
import json
import os
from datetime import datetime
import shutil

FILE_NAME = "notes.json"
BACKUP_FILE = "notes_backup.json"

console = Console()


class NotesManager:

    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()

    # ================= LOAD =================
    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                return json.load(f)
        return []

    # ================= SAVE + AUTO BACKUP =================
    def save_notes(self):
        # backup dulu
        if os.path.exists(self.file_name):
            shutil.copy(self.file_name, BACKUP_FILE)

        with open(self.file_name, "w") as f:
            json.dump(self.notes, f, indent=2)

    # ================= ADD =================
    def add_note(self, text):
        note = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": text
        }
        self.notes.append(note)
        self.save_notes()
        print("Catatan ditambahkan ✔️")

    # ================= LIST =================
    def list_notes(self):
        if not self.notes:
            console.print("[yellow]Belum ada catatan 📭[/yellow]")
            return

        table = Table(title="📒 Daftar Catatan", show_lines=True)
        table.add_column("No", style="cyan", justify="center")
        table.add_column("Waktu", style="green")
        table.add_column("Catatan", style="white")

        for i, note in enumerate(self.notes, start=1):
            table.add_row(str(i), note["time"], note["text"])

        console.print(table)

    # ================= DELETE =================
    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            self.save_notes()
            print(f"Catatan dihapus: {removed['text']} 🗑️")
        else:
            print("Index tidak valid")

    # ================= EDIT =================
    def edit_note(self, index, new_text):
        if 0 <= index < len(self.notes):
            self.notes[index]["text"] = new_text
            self.notes[index]["time"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            self.save_notes()
            print("Catatan diperbarui ✏️")
        else:
            print("Index tidak valid")

    # ================= SEARCH =================
    def search_notes(self, keyword):
        found = False
        for i, note in enumerate(self.notes, 1):
            if keyword.lower() in note["text"].lower():
                print(f"{i}. {note['time']} | {note['text']}")
                found = True

        if not found:
            print("Tidak ada catatan yang cocok.")


# ================= MAIN =================
def main():
    manager = NotesManager(FILE_NAME)

    while True:
        console.print("\n[bold cyan]=== Notes CLI ===[/bold cyan]")
        print("1. Tambah catatan")
        print("2. Lihat catatan")
        print("3. Hapus catatan")
        print("4. Edit catatan")
        print("5. Keluar")
        print("6. Cari catatan 🔎")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            teks = input("Isi catatan: ")
            manager.add_note(teks)

        elif pilihan == "2":
            manager.list_notes()

        elif pilihan == "3":
            manager.list_notes()
            try:
                idx = int(input("Nomor yang dihapus: ")) - 1
                manager.delete_note(idx)
            except ValueError:
                print("Input harus angka")

        elif pilihan == "4":
            manager.list_notes()
            try:
                idx = int(input("Nomor yang diedit: ")) - 1
                teks_baru = input("Isi baru: ")
                manager.edit_note(idx, teks_baru)
            except ValueError:
                print("Input harus angka")

        elif pilihan == "5":
            print("Sampai jumpa 👋")
            break

        elif pilihan == "6":
            key = input("Kata kunci: ")
            manager.search_notes(key)

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
