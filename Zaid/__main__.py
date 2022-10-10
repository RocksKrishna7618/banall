from Zaid import Zaid, HANDLER
import glob
from pathlib import Path
from Zaid.utils import load_plugins

path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

if __name__ == "__main__":
    print("[INFO]: ADDING HANDLERS!")
    for cmd in HANDLER:
        Zaid.add_event_handler(cmd)
    print("[INFO]: SUCCESSFULLY STARTED BOT!")
    Zaid.run_until_disconnected()
