import os
import shutil
import glob
import bibtexparser
from os.path import basename, exists, join, split
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode


class bibTex:

    def __init__(self, filename, sync_dir):

        self.fname = filename
        self.fname_exact = basename(filename).split('.')[0]
        self.wdir =  join(sync_dir, self.fname_exact)

        if not exists(self.wdir):
            os.mkdir(self.wdir)
    
    @property
    def load(self):
        
        with open(self.fname, encoding='utf-8') as bibtex_file:
            parser = BibTexParser(customization=convert_to_unicode)
            bib_database = bibtexparser.load(bibtex_file, parser=parser)
        
        return bib_database.entries
    
    @property
    def get_file_path(self):

        bib_db = self.load
        file_path_db = []
        for bib_item in bib_db:
            try:
                datpath = bib_item['file'].split(':')
                datpath = datpath[1].replace('$\\backslash$', ':') + datpath[2]
                file_path_db.append(datpath)
            except KeyError:
                continue
        
        return file_path_db
    
    def moving_file(self):
        
        file_db = self.get_file_path
        for file_item in file_db:
            file_id = basename(file_item)
            if not exists(join(self.wdir, file_id)):
                try:
                    shutil.copy(file_item, self.wdir)
                    print('Added ' + file_id[0:10])
                except FileNotFoundError:
                    print('Missing ' + file_id)
                    continue


def check(sync_dir, source):

    data = glob.glob(sync_dir + '/*/*.*')
    src_data = glob.glob(source + '/*.*')

    data_dict = {}
    for k, val in map(split, data):
        if val in data_dict.keys():
            data_dict[val] += (basename(k),)
        else:
            data_dict[val] = (basename(k),)
    
    data = set(map(basename, data))
    src_data = set(map(basename, src_data))

    diff_data = data.difference(src_data)
    print('=' * 10)
    if diff_data:
        for missval in diff_data:
            if missval in data:
                print('- ' + missval, data_dict[missval])
            else:
                print('+ ' + missval)
    else:
        print('Updated All.')


if __name__ == '__main__':

    mendeleyBibTexPath = 'D:/OneDrive/Mendeley/BibTex'
    syncDir = 'D:/OneDrive/Mendeley/Data'
    sourceDir = 'D:/Mendeley/Data'

    mendeleyBibTexList = glob.glob(mendeleyBibTexPath + '/*.bib')

    for mendeleyBibTex in mendeleyBibTexList:
        mendeleyData = bibTex(mendeleyBibTex, syncDir)
        mendeleyData.moving_file()

    check(syncDir, sourceDir)