import asyncio
import glob
import os
import csv

FOLDER_PATH = <base_file_path>"

async def chain(folder_name):
    backup_folder_path = f"{FOLDER_PATH}/{folder_name}"

    with open("wkc_files.csv", "a+") as csvfile:
        fieldnames = ["scanned_date", "book_name", "download_url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for book_name in os.listdir(backup_folder_path):
            for page in os.listdir(f"{backup_folder_path}/{book_name}"):
                download_url = f"https://<some_url>/{folder_name}/{book_name.replace(' ', '+')}/{page}"
                writer.writerow({fieldnames[0]: folder_name, fieldnames[1]: book_name, fieldnames[2]: download_url})

async def main(*folders):
    await asyncio.gather(*(chain(folder_name) for folder_name in folders))


if __name__ == '__main__':

    with open("wkc_files.csv", "w") as csvfile:
        fieldnames = ["scanned_date", "book_name", "download_url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    import time
    start = time.perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*os.listdir(FOLDER_PATH)))
    end = time.perf_counter() - start
    print(f"Completed at {end:0.2f} Sconds")
