#картинки
import cv2
import os
import glob
import sys
sys.path
img_dir = r'C:\Users\Ilia\Documents\git\printScans\imgs'# Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []

for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
    
########принтер
import tempfile
import win32api
import win32print

def printprint (x):
    filename = tempfile.mktemp(".txt")
    open (filename, 'w').write (x)
    win32api.ShellExecute(0,"printto",filename,'"%s"' % win32print.GetDefaultPrinter(), ".",0)
    
printprint("Тестовая страница")

