from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
from pathlib import Path
import time

def get_folder_files(dirid):
    results = drive_service.files().list(q=f"'{dirid}' in parents", fields='files(id, name)').execute()
    return results.get('files', [])



starttime = time.time()

print(starttime)

pathtodownload = Path('D:/Devil/cryptomaraphone')

if not pathtodownload.exists():
    pathtodownload.mkdir()


#настройки
path_to_key = 'D:/GIT/python/downloader/' #папка с сектретным файлом
secret_key = '****************' #Секретный файл
folder_id = '*****************'  # ID папки на Google Диске, которую вы хотите скачать


# Укажите путь к файлу JSON вашего служебного аккаунта и область доступа
SERVICE_ACCOUNT_FILE = path_to_key + secret_key
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Создайте объект учетных данных с использованием файла служебного аккаунта и области доступа
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Создайте объект Google Drive API
drive_service = build('drive', 'v3', credentials=credentials)


folder_to_move = None
dict_of_folder  = {}
error_files  = {}

# Запросите список файлов в указанной папке
result = get_folder_files(folder_id)

#перебираем список папок на удаленном диске и смотрим в нутри
for file in result:
    remoute_files = get_folder_files(file.get('id'))


    for i in remoute_files:
        if  pathtodownload.joinpath(file.get('name')).joinpath(i.get('name')).exists():
            print(f"File {i.get('name')} in dir {file.get('name')} is exist")
        else: 
           error_files [i.get('name')] = i.get('id')


    if pathtodownload.joinpath(file.get('name')).exists():
        for i in pathtodownload.joinpath(file.get('name')).iterdir():
            print(i)
    else:
        print(f"No file {file.get('name')}")
    dict_of_folder [file.get('name')] = file.get('id')

 


#качаем файлы
for k,v in dict_of_folder.items():
    print('Start to download')
    #создаем папку если такая не существует
    newfolderpath_name = Path(pathtodownload.joinpath(k))
    if not newfolderpath_name.exists():
        newfolderpath_name.mkdir()
    #получаем список файлов папке
    filenames = get_folder_files(v)
    for file in filenames:

        file_id = file['id']
        file_name = file['name']
        #удаляем из названия все лишнее иначе вин не создаст файл
        new_file_name = "".join(c if c.isalnum() or c in (' ', '.', '-') else '_' for c in file_name)

        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(newfolderpath_name / new_file_name, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        print(f'Successfully downloaded: {file_name} Time to comlete {(time.time() - starttime) / 60} min')

print(f"Finish. Time to comlete {(time.time() - starttime) / 60} min")


 

