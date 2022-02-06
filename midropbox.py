import os
import dropbox

os.system('cls' if os.name == 'nt' else 'clear')

access_token = "sl.BBck8u-y9iPId5YRtt_fG6jnjSPhxA6pgAWZsnTe5FfrDHkysX1fPiT09dH6mCER97q0LnCi3yoAtk2e3wdnbLSiiifjPPNLhEIf9TGva7LP6QLxrI9TPDO7RDaHaQcUPFzvkpO-lZnP"

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
        print('\ncarpeta ' + path + ':' + '\n-------------------')
        for file in files:
            print(file.name)
    except Exception as e:
        print('\n' + str(e))

#listar archivos en carpeta '.' 
con = 0
arc = []  
r = 0
archivos = os.listdir('.')
for archivo in archivos:
    arc.append(archivo) 
    con+=1
    print( str(con) + ") " + archivo)

while True:
    print('Ingrese numero: ')
    r = int(input())
    if r >= 1 and r<=con:
        break 

# 
if r != 0:
    dropbox_upload_file('.', arc[r-1], '/favoritos')
    if (sw):
        dropbox_list_files('/favoritos')
    else:
        print('\nNo se pudo Listar los archivos\n')

print('\n') 
