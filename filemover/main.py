from zipfile import ZipFile
from pathlib import Path
from datetime import date, timedelta

#скрипт для автоматической распаковки архива выгруженного сервиса Canva

start_date = date(2023,10,29)

video_path = Path('D:/@START-UP/tenbox/')
delta = 0

# #Создаем первую папку в списке. дальше будет работать автоматически
# pathtostring = str(start_date)
# dir_to_create = video_path / pathtostring
# if not dir_to_create.is_dir():
#     dir_to_create.mkdir()
#     print(f"Path {dir_to_create} is created")

zipfile_name = None
 
# Ищем существует ли зип файл
for i in video_path.iterdir():
    if i.suffix == '.zip':
         zipfile_name = i

if zipfile_name and zipfile_name.exists():
    print('Zip file is found. Starting to extract')
    with ZipFile(zipfile_name) as zipfile:
        zipfile.extractall(video_path)
    print("Extracted")
    zipfile_name.unlink()
    print("Zip file is delete")
else:
    print('No zip file')

#Создаем директории и переносим файлы
for i in range(100):
    index = str(i+1)
    sourse_file_pre = video_path.joinpath(index +'.mp4')
    print(sourse_file_pre)

    if sourse_file_pre.exists():
        if i % 10 == 0 : #создаем папку на каждой итерации кратной 10
            delta +=1
            pathforfiles = start_date + timedelta(days=delta)
            pathtostring = str(pathforfiles)
            dir_to_create = video_path / pathtostring
            
            if not dir_to_create.is_dir():
                dir_to_create.mkdir()
                print(f"Path {pathforfiles} is created")
    
    
        sourse_file = dir_to_create.joinpath(index +'.mp4')
        print(sourse_file)
        sourse_file_pre.replace(sourse_file)
        print(f"Move from {sourse_file_pre} to {sourse_file}")
    else:
        print('No file to parce')


        
 