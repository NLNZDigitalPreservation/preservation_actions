import csv 
import os
import sys
import win32com.client
import time

dst = r"E:\work\MCW_quick\converts"
report = r"E:\work\MCW_quick\mcw_2022.csv"

with open(report) as data:
    reader = csv.reader(data.read())

good_puids =  ["fmt/346", "x-fmt/1", "x-fmt/64", "x-fmt/65"] 


def process_file(my_path):
    relative_path = my_path.replace(r"E:\work\MCW_quick\originals", "")[1:]
 
    ie, __ = relative_path.split(os.sep, 1)
    __, fname = relative_path.rsplit(os.sep, 1)
    try:
        fname_stripped, ext = fname.rsplit(".", 1)
    except:
        fname_stripped = fname



    new_fname = fname_stripped+".pdf"
    wdFormatPDF = 17
    word = win32com.client.Dispatch('Word.Application')


    out_file = os.path.join(dst, ie, new_fname) 
    out_path = os.path.join(dst, ie)
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # doc = word.Documents.Open(my_path)
    # doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    # doc.Close()
    # word.Quit()

    try:
        if not os.path.exists(my_path):
            print (f"Missing in-file: {my_path}")

        elif not os.path.exists(out_file):    
            doc = word.Documents.Open(my_path)
            doc.SaveAs(out_file, FileFormat=wdFormatPDF)
            doc.Close()
            word.Quit()
            print (f"Success: {my_path}")
            time.sleep(4)
        else:
            print (f"Exists: {out_file}")
     
    except:
        print (f"Failed: {my_path}")


rows = []
with open(report, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


for r in rows:
    puid = r[14]
    my_path = r[3]

    if puid not in good_puids:
        pass

    else:
        process_file(my_path)

    # quit()