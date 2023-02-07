import sys, os, shutil
import zipfile
import pyzipper

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

main_dir = application_path.split("\\")[-1]

print(application_path.split("\\"))

def zip_folder(folder_path, password):
    zip_password = password.encode('utf-8')
    parent_folder = os.path.dirname(folder_path)
    try:
        zip_file = pyzipper.AESZipFile(f'{folder_path}.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=b'Mbb@'+zip_password
        for root, folders, files in os.walk(folder_path):
            for sub_folder in folders:
                absolute_path = os.path.join(root, sub_folder)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                zip_file.write(absolute_path, relative_path)
                print(absolute_path)
            for filename in files:
                absolute_path = os.path.join(root, filename)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                zip_file.write(absolute_path, relative_path)
                print(absolute_path)
    except IOError as message:
        print (message)
    except OSError as message:
        print(message)
    except zipfile.BadZipfile as message:
        print (message)
    except Exception as message:
        print(message)
    finally:
        zip_file.close()
        shutil.rmtree(folder_path)

def zip_file(file_path, password):
    zip_password = password.encode('utf-8')
    parent_folder = os.path.dirname(file_path)
    output_path = file_path.split(".")[0]
    try:
        zip_file = pyzipper.AESZipFile(f'{output_path}.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=b'Mbb@'+zip_password
        absolute_path = os.path.join(file_path)
        relative_path = absolute_path.replace(parent_folder + '\\','')
        zip_file.write(absolute_path, relative_path)
    except IOError as message:
        print (message)
    except OSError as message:
        print(message)
    except zipfile.BadZipfile as message:
        print (message)
    except Exception as message:
        print(message)
    finally:
        try:
            zip_file.close()
            os.remove(file_path)
        except Exception as message:
            print(message)

for dirpath, dirnames, filenames in os.walk(application_path):
    if "venv" in dirnames:
        dirnames.remove("venv")
    sub_dir = dirpath.split("\\")[-1]
    if main_dir in sub_dir or "DAILY" in sub_dir or "MONTHLY" in sub_dir :
        continue
    if "DAILY" not in dirpath and "MONTHLY" not in dirpath:
        continue
    if dirpath.split("\\")[3] != "MAYBANK":
        continue
    date_dir = dirpath.split("\\")[5]
    for name in dirnames:
        path = os.path.join(dirpath,name)
        zip_folder(path,date_dir)
    for filename in [f for f in filenames if not f.endswith('.zip')]:
        path = os.path.join(dirpath,filename)
        zip_file(path,date_dir)
        print("")