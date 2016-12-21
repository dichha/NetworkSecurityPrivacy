from zipfile import ZipFile
import re
import json

zip_f = ZipFile('..\\hillaryclinton_1478304000.zip')
for info in zip_f.infolist():
    print(info.filename)
    print(zip_f.getinfo(info.filename))
