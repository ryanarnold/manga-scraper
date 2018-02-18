# This script renames all the manga images scraped from manga-fox.com
# This is needed because image filenames are in sha1 format.

import json
import os

manga_details = json.load(open('./temp/manga_details.json'))

for manga in manga_details:
    manga_title = manga['manga_title']
    chapter_number = str(manga['chapter_number']).zfill(3)
    images = manga['images']

    print('Processing manga: %s' % manga_title)
    print('  Processing chapter %s' % chapter_number)

    for image in manga['images']:
        page_number = image['url'].split('-')[-1].split('.')[0].zfill(2)
        path = image['path']
        new_filename = '{0} Chapter {1} Pg {2}.jpg'.format(manga_title, chapter_number, page_number)

        print('    Renaming {0} to {1}'.format(path, new_filename))

        os.rename('./temp/' + path, './temp/full/' + new_filename)
