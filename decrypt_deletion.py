import os, time, sys, datetime, time, shutil

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

now = time.time()
two_days = now - 86400 * 2
print(f"Folder timestamp to delete: {datetime.datetime.fromtimestamp(two_days).strftime('%Y-%m-%d')}")

def deletion(path_destination):
    creation_time = os.path.getctime(rf"{path_destination}")
    if creation_time < two_days:
        print(f"REMOVING: {path_destination}")
        try:
            shutil.rmtree(path_destination)
        except NotADirectoryError as e:
            os.remove(path_destination)

for dirpath, dirnames, filenames in os.walk(application_path):
    if "DECRYPT" not in dirpath:
        continue
    if dirnames:
        for sub_dir in dirnames:
            sub_dir_path = os.path.join(dirpath,sub_dir)
            deletion(sub_dir_path)
    for files in filenames:
        file_path = os.path.join(dirpath,files)
        deletion(file_path)