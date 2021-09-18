import zipfile,os

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    print(f'Creating {zipfilename}....')
    backupZip = zipfile.ZipFile(zipfilename,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Adding the current folder to the ZIP file.')
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()

    print('Done')

backupToZip(r'C:\delicious')
