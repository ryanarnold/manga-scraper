@echo off

set CBR_FILENAME=Nisekoi Vol 02

echo Manga Scraper and Generator
echo. 
echo Before starting, review the following settings found in spiders/manga.py:
echo  - BASE_URL
echo  - START_CHAPTER
echo  - END_CHAPTER
echo.
echo Also, review the CBR_FILENAME environment variable set in this batch file.
echo.
pause

echo Scraping manga images...
..\env\Scripts\scrapy crawl manga

echo Renaming manga images...
..\env\Scripts\python .\rename_images.py

echo Creating cbr directories...
mkdir .\temp\cbr\

echo Generating zip file...
..\env\Scripts\python .\create_cbr.py

echo Converting zip file to cbr...
move .\temp\cbr\temp.zip .\output\temp.zip
ren .\output\temp.zip "%CBR_FILENAME%".cbr

echo Deleting temp directory...
rmdir .\temp /s /q

pause
