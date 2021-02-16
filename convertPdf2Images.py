import os
import time
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path

import json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
fname = {}
startTime = time.time()
print("Started at ", time.ctime(startTime))
for root, d_names, f_names in os.walk(APP_ROOT+'/static/pdfs'):
    for f in f_names:
        if f.endswith('.pdf'):
            fWoExtension = os.path.splitext(f)[0]
            if not fWoExtension in fname:
                print(fWoExtension)
                seconds = time.time()
                fname[fWoExtension] = {}
                pages = convert_from_path(os.path.join(root, f), dpi=200, grayscale=True, size=(600, 846))
                fname[fWoExtension]['path'] = '/static/pdfs/'+fWoExtension
                fname[fWoExtension]['pages'] = dict([(x,0) for x in range(1,len(pages)+1)])
                os.mkdir(APP_ROOT+'/static/pdfs/'+fWoExtension)
                for idx, page in enumerate(pages):
                    page.save(APP_ROOT+'/static/pdfs/'+fWoExtension+'/'+fWoExtension+'_'+str(idx+1)+'.png', 'PNG')
                print(' pages ', len(pages), ' time ', time.time() - seconds, ' secs' )
with open(APP_ROOT+'/static/pdfs/pdfs.json', "w") as fp:
    json.dump(fname , fp) 
endTime = time.time()
print("Ended at ", time.ctime(startTime), ' - ',  endTime - startTime, 'secs')