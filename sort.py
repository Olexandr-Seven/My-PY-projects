from pathlib import Path
import shutil 
import pathlib
import os
print('Input Path to your directory')
pa = input('Your Path: ')
new_dir = pathlib.Path('D:\VideoS')
if not new_dir.exists() :
    new_dir.mkdir()

new_dir = pathlib.Path('D:\ImageS')
if not new_dir.exists() :
    new_dir.mkdir()

new_dir = pathlib.Path('D:\AudioS')
if not new_dir.exists() :
    new_dir.mkdir()

new_dir = pathlib.Path('D:\DocumentS')
if not new_dir.exists() :
    new_dir.mkdir()

new_dir = pathlib.Path('D:\ArchiveS')
if not new_dir.exists() :
    new_dir.mkdir()

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION) :
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name):
    new_name = name.translate(TRANS)
    return new_name

def parse_folder(path):

    sum_files = 0
    sum_folders = 0
    for part in path.iterdir() :
        #print(part)
        if part.is_file():
            sum_files+=1
            if part.suffix in ['.rtf','.DOC', '.doc', '.DOCX', '.docx', '.TXT','.txt', '.PDF','.pdf', '.XLSX', '.xlsx', '.PPTX', '.pptx'] :
                l = str(path) + 'DocumentS\\' + normalize(part.name)
                print(l)
                shutil.move(part, l )

            elif part.suffix in ['.JPEG', '.jpeg', '.PNG','.png', '.JPG','.jpg', '.SVG', '.svg' ] :
                l = str(path) + 'ImageS\\' + normalize(part.name)
                print(l)
                shutil.move(part, l )

            elif part.suffix in ['.AVI', '.avi', '.MP4', '.mp4', '.MOV', '.mov', '.MKV', '.mkv' ] :
                l = str(path) + 'VideoS\\' + normalize(part.name)
                print(l)
                shutil.move(part, l )

            elif part.suffix in ['.MP3', '.mp3', '.OGG', '.ogg', '.WAV', '.wav', '.AMR', '.amr' ] :
                l = str(path) + 'AudioS\\' + normalize(part.name)
                print(l)
                shutil.move(part, l )

            elif part.suffix in ['.ZIP', '.zip', '.GZ', '.gz', 'TAR', 'tar'] :
                l1 = str(path) + 'ArchiveS\\'
                print(l1)
                shutil.unpack_archive(part, l1)
                os.remove(part)

        elif part.is_dir():
            sum_folders +=1
            #folders.append(part.name)
    print('Summa files = ', sum_files)
    print('Summa dirs = ', sum_folders)
            
    #return files, folders
#p = Path()
p = Path(pa)
print(p)

parse_folder(p)
print(pa)