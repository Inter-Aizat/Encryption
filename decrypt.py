import sys, os, shutil
import zipfile
import pyzipper

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

main_dir = application_path.split("\\")[-1]

def unzip_file(file_path, decrypt_path):
    try:
        with pyzipper.AESZipFile(file_path) as f:
            zip_filename = file_path.split("\\")[-1]
            zip_password = zip_filename.replace('.zip','')
            zip_password = zip_password.encode('utf-8')
            f.extractall(path=decrypt_path, pwd=b'Mbb@'+zip_password)
    except:
        for dirpath, dirnames, filenames in os.walk(application_path):
            if "venv" in dirnames:
                dirnames.remove("venv")
            sub_dir = dirpath.split("\\")[-1]
            if main_dir in sub_dir or "CYCLE" in sub_dir or "DAILY" in sub_dir or "MONTHLY" in sub_dir or "CHARGE CARD" in sub_dir or "PURCHASING" in sub_dir:
                continue
            if "CYCLE" not in dirpath and "DAILY" not in dirpath and "MONTHLY" not in dirpath:
                continue
            folder_date = dirpath.split("\\")[-1]
            folder_date = folder_date.encode('utf-8')
            try:
                with pyzipper.AESZipFile(file_path) as f:
                    f.extractall(path=decrypt_path, pwd=b'Mbb@'+folder_date)
            except Exception as e:
                # print(e)
                continue
    finally:
        os.remove(file_path)

for dirpath, dirnames, filenames in os.walk(application_path,):
    if "venv" in dirnames:
        dirnames.remove("venv")
    if "DECRYPT" not in dirpath:
        continue
    for filename in filenames:
        if ".zip" not in filename:
            continue
        unzip_file(fr"{dirpath}\{filename}", dirpath)