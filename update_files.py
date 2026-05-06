import os
import re

base_dir = r'C:\Users\User\OneDrive\.TOPICS\.SOFTWARE\MAIL\REL-PUB_MailProcessor'

# 1. Update build_exe.bat
bat_path = os.path.join(base_dir, 'build_exe.bat')
with open(bat_path, 'r', encoding='utf-8') as f:
    bat_code = f.read()
bat_code = bat_code.replace(
    '  --name MailProcessor ^\n  --icon "%ICON_PATH%" ^\n  --distpath "dist" ^',
    '  --name MailProcessor ^\n  --icon "%ICON_PATH%" ^\n  --add-data "resources;resources" ^\n  --distpath "dist" ^'
)
with open(bat_path, 'w', encoding='utf-8') as f:
    f.write(bat_code)

# 2. Update tray.py
tray_path = os.path.join(base_dir, 'tray.py')
with open(tray_path, 'r', encoding='utf-8') as f:
    tray_code = f.read()

tray_code = re.sub(r'def _make_tray_icon.*?return QIcon\(pixmap\)\n\n', '', tray_code, flags=re.DOTALL)

new_icon_logic = '''        import sys
        if getattr(sys, 'frozen', False):
            base_dir = Path(sys._MEIPASS)
        else:
            base_dir = Path(__file__).parent
        icon_path = base_dir / "resources" / "icon.ico"
        self.setIcon(QIcon(str(icon_path)))'''
tray_code = tray_code.replace('        self.setIcon(_make_tray_icon())', new_icon_logic)

with open(tray_path, 'w', encoding='utf-8') as f:
    f.write(tray_code)

# 3. Update settings_dialog.py
settings_path = os.path.join(base_dir, 'settings_dialog.py')
with open(settings_path, 'r', encoding='utf-8') as f:
    settings_code = f.read()

old_autostart = '''    @staticmethod
    def _apply_autostart(enable: bool):
        import winreg
        key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        app_name = "MailProcessor"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            if enable:
                import sys
                from pathlib import Path
                script = str(Path(__file__).parent / "main.py")
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, f'"{sys.executable}" "{script}"')
            else:
                try:
                    winreg.DeleteValue(key, app_name)
                except FileNotFoundError:
                    pass
            winreg.CloseKey(key)
        except Exception:
            pass'''

new_autostart = '''    @staticmethod
    def _apply_autostart(enable: bool):
        import winreg
        key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        app_name = "MailProcessor"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
            if enable:
                import sys
                from pathlib import Path
                if getattr(sys, 'frozen', False):
                    cmd = f'"{sys.executable}"'
                else:
                    script = str(Path(__file__).parent / "main.py")
                    cmd = f'"{sys.executable}" "{script}"'
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, cmd)
            else:
                try:
                    winreg.DeleteValue(key, app_name)
                except FileNotFoundError:
                    pass
            winreg.CloseKey(key)
        except Exception:
            pass'''
            
settings_code = settings_code.replace(old_autostart, new_autostart)

with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(settings_code)

# 4. Update main.py
main_path = os.path.join(base_dir, 'main.py')
with open(main_path, 'r', encoding='utf-8') as f:
    main_code = f.read()

main_code = main_code.replace('    from tray import MailProcessorTray', '''    if cfg.start_with_windows:
        from settings_dialog import SettingsDialog
        SettingsDialog._apply_autostart(True)

    from tray import MailProcessorTray''')

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_code)

print('Updated files successfully')
