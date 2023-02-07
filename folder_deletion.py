import os, time, sys, datetime, time, shutil

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

main_dir = application_path.split("\\")[-1]
target_destination = r"\\192.168.50.26\it33"

now = time.time()
previous_day_timestamp = now - 86400
two_days = now - 86400 * 2
two_one_days = now - 86400 * 21
previous_day = datetime.datetime.fromtimestamp(previous_day_timestamp).strftime('%d%m%y')
print(f"Folder timestamp to delete for DAILY: {datetime.datetime.fromtimestamp(two_days).strftime('%Y-%m-%d')}")
print(f"Folder timestamp to delete for MONTHLY: {datetime.datetime.fromtimestamp(two_one_days).strftime('%Y-%m-%d')}")

for dirpath, dirnames, filenames in os.walk(application_path):
    if "MAYBANK" not in dirpath and "DAILY" not in dirpath and "MONTHLY" not in dirpath:
        continue
    sub_dir = dirpath.split("\\")[-1]
    if sub_dir == "MAYBANK" or sub_dir == "DAILY" or sub_dir == "MONTHLY":
        continue
    if "DAILY" in dirpath:
        timestamp_to_delete = two_days
    elif "MONTHLY" in dirpath:
        timestamp_to_delete = two_one_days
    main_dir = dirpath.split("\\")[2] #.33 is [2]
    frequency_dir = dirpath.split("\\")[3] #.33 is [3]
    target_destination_main_dir = os.path.join(target_destination,main_dir)
    target_destination_frequency = os.path.join(target_destination_main_dir,frequency_dir)
    target_destination_sub_dir = os.path.join(target_destination_frequency,sub_dir)
    sub_dir_creation_time = os.path.getctime(dirpath)
    if sub_dir_creation_time < timestamp_to_delete:
        print(f"Moving {dirpath} to {target_destination_sub_dir}")
        try:
            shutil.move(dirpath, target_destination_sub_dir)
        except:
            shutil.copytree(dirpath,target_destination_sub_dir, dirs_exist_ok=True)
            shutil.rmtree(dirpath)