# MailProcessor

**DE** | [EN](#en)

---

## DE

MailProcessor ist ein System-Tray-Launcher für die drei Universal Mail Tools:

- **Universal Mail Cleaner** — IMAP-Postfach nach Regeln bereinigen
- **Universal Docs Grabber** — Dokumente und Anhänge aus Mails laden
- **Universal Invoice Mail** — Rechnungen automatisch aus Mails extrahieren

### Features

- System-Tray-Icon: per Rechtsklick jederzeit ein Tool starten
- Erster Start: Einrichtungsassistent mit automatischem Scan nach vorhandenen Tools
- GitHub-Installer: Tools direkt aus GitHub Releases herunterladen
- Versionsnummern im Tray-Menü (aus CHANGELOG.md jedes Tools)
- Einstellungen: Pfade anpassen, Tools entfernen, manuell hinzufügen
- Autostart mit Windows (Registry-Eintrag)
- Zweisprachig: Deutsch / Englisch

### Installation

1. Python 3.10+ installieren
2. Abhängigkeiten installieren: `pip install -r requirements.txt`
3. Starten: `start.bat` (Doppelklick) oder `python main.py`
4. Im Einrichtungsassistenten die gewünschten Tools auswählen

### Voraussetzungen

- Python 3.10+
- PySide6 6.x
- Eines oder mehrere der Universal Mail Tools

---

<a name="en"></a>

## EN

MailProcessor is a system tray launcher for the three Universal Mail Tools:

- **Universal Mail Cleaner** — Clean IMAP mailbox by rules
- **Universal Docs Grabber** — Download documents and attachments from mails
- **Universal Invoice Mail** — Extract invoices automatically from mails

### Features

- System tray icon: launch any tool via right-click at any time
- First run: setup wizard with automatic scan for installed tools
- GitHub installer: download tools directly from GitHub Releases
- Version numbers in tray menu (read from each tool's CHANGELOG.md)
- Settings: change paths, remove tools, add manually
- Windows autostart (registry entry)
- Bilingual: German / English

### Installation

1. Install Python 3.10+
2. Install dependencies: `pip install -r requirements.txt`
3. Launch: `start.bat` (double-click) or `python main.py`
4. Select desired tools in the setup wizard

### Requirements

- Python 3.10+
- PySide6 6.x
- One or more Universal Mail Tools

---

## License

MIT License — see LICENSE file for details.
