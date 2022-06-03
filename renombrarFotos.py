import os
import pathlib
from datetime import datetime
import shutil

input = 'Ruta input'
ouput = 'Ruta ouput'

def unix2datetime(unix):
    print(unix)
    return datetime.utcfromtimestamp(unix).strftime('%d-%m-%Y_%H-%M-%S')


def copy_rename(old_file_name, new_file_name):

        src_file = os.path.join(input, old_file_name)


        shutil.copy(src_file, ouput)

        

        dst_file = os.path.join(ouput, old_file_name)


        new_dst_file_name = os.path.join(ouput, new_file_name)

        os.rename(dst_file, new_dst_file_name)
        

for path in pathlib.Path(input).iterdir():
    info = path.stat()


    # Data de creación
    ctime = info.st_ctime
    
    # Data de modificación
    mtime = info.st_mtime

    

    if mtime <= ctime:
        date_create = unix2datetime(mtime)
    else:
        date_create = unix2datetime(ctime)



    file_name, fild_extension = os.path.splitext(path)





    if fild_extension != '.jpeg' and fild_extension != '.JPG' and fild_extension != '.JPEG' and fild_extension != '.jpg':

        
        continue # Se va a la siguiente iteración

    new_filename = date_create + fild_extension


    


    if file_name.find != -1:

        # print(file_name[file_name.find(input)+len(input)+1:])
        file_name = file_name[file_name.find(input)+len(input)+1:]+fild_extension
        copy_rename(file_name, new_filename)



    print(file_name,' -> ', new_filename)

    break