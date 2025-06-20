import asyncio
from desktop_notifier import DesktopNotifier
import time

notifier = DesktopNotifier()

async def main():
    for i in range(5):
        time.sleep(10)
        await notifier.send(title="Reminder", message="Drink Water !!!")

asyncio.run(main())