import glob, os
import zipfile

TEMP_DIR = './temp/'

output_file = zipfile.ZipFile(TEMP_DIR + 'cbr/temp.zip', 'w')

for name in os.listdir(TEMP_DIR + 'full'):
    output_file.write(TEMP_DIR + 'full/' + name, os.path.basename(name), zipfile.ZIP_DEFLATED)

output_file.close()

print('Manga zip file generated.')
