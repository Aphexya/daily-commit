import yaml
from datetime import datetime
from git import Repo
from time import sleep
from random import randint

FILE_TO_COMMIT_NAME = 'update_me.yaml'


def update_file_to_commit():
    """Update the YAML file with the number of times it has been committed and the last update timestamp."""
    try:
        with open(FILE_TO_COMMIT_NAME, 'r') as file:
            current_data = yaml.safe_load(file)
            update_times = int(current_data['UPDATE_TIMES']) + 1
            last_update = datetime.now().strftime("%A %B %d %Y at %X%p")
    except (FileNotFoundError, KeyError, TypeError, ValueError) as e:
        print(f"Error reading the YAML file: {e}")
        return None
    updated_data = {
        'UPDATE_TIMES': update_times,
        'LAST_UPDATE': last_update
    }
    with open(FILE_TO_COMMIT_NAME, 'w') as file:
        yaml.dump(updated_data, file, default_flow_style=False, sort_keys=True)
    return updated_data


def commit_repository(yaml_data):
    """Commit the updated YAML file to the Git repository."""
    if not yaml_data:
        print("No data to commit.")
        return
    repo = Repo('.')
    repo.index.add([FILE_TO_COMMIT_NAME])
    commit_message = f'Updated {yaml_data["UPDATE_TIMES"]} times. Last update was on {yaml_data["LAST_UPDATE"]}.'
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()

if __name__ == '__main__':
    with open("log.txt", "a") as f:
        f.write(f"Jalan pada {datetime.now()}\n")

    # ⏱ Commit LANGSUNG SEKARANG saat program dijalankan
    for i in range(randint(1, 10)):
        updated_yaml_data = update_file_to_commit()
        commit_repository(updated_yaml_data)

    # 🔁 Lalu lanjut loop harian
    while True:
        sleep(86400)  # Tunggu 24 jam
        for i in range(randint(1, 10)):
            updated_yaml_data = update_file_to_commit()
            commit_repository(updated_yaml_data)

