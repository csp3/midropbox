import os
import dropbox

os.system('cls' if os.name == 'nt' else 'clear')

access_token = "sl.BBe-KSk-yAeMTaM18-mPA9Az8pKL7E1FEf4i-Kera2Yv_P8K4Xnlt_IqjeN8zSlzRNIidJwoGjQ2qTECVu4H2ufYB5q69ODEC-csN2ZEz2MDBQ5NKrW7wPgigxyFHyukaPDhNv6Gaazq"

sw = False 

try:
    dbx = dropbox.Dropbox(access_token)
    dbx.users_get_current_account()
    # print(dbx.users_get_current_account())
    dropbox_user_name = dbx.users_get_current_account().name.display_name
    dropbox_email = dbx.users_get_current_account().email
    print("---------------------------------------")
    print('Autenticación Dropbox: \nPropiedad de: {} <{}>'.format(dropbox_user_name, dropbox_email))
    print("---------------------------------------")
except dropbox.auth.AuthError as err:
    print(err)

# upload_file
def dropbox_upload_file(local_path, local_file, dropbox_file_path):
    try:
        file_local = local_path + '/' + local_file
        file_dbox  = dropbox_file_path + '/' + local_file 
        dbx.files_upload(open(file_local, 'rb').read(), file_dbox, mode=dropbox.files.WriteMode("overwrite"))
        global sw 
        sw = True   
    except Exception as e:
        print('\nError uploading file to Dropbox: ' + str(e))

# listar_file
def dropbox_list_files(path):
    try:
        files = dbx.files_list_folder(path).entries 
        print('\ncarpeta ' + path + ':')
        for file in files:
            print(file.name)
    except Exception as e:
        print('\n' + str(e))

# 
dropbox_upload_file('.','imagen.png', '/favoritos')
if (sw):
    dropbox_list_files('/favoritos')
else:
    print('\nNo se pudo Listar los archivos\n')

print('\n') 
