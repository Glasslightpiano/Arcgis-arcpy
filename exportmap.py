# coding=utf-8
import os
import arcpy

# 設定資料夾路徑(路徑上不要有中文)
path = "C:/Fast Deal/exportmap_test/"

mxdpath = path + "MXD/"
outputPDF = path + "PDF/"
outputPNG = path + "PNG/"

# 讀取MXD資料夾內的全部.mxd檔案，並分為輸出PDF和PNG兩類
file = os.listdir(mxdpath)
for mxdFile in file:
    PDF = "112.mxd"
    PNG = "(PNG).mxd"

    # PDF出圖
    if mxdFile.endswith(PDF):
        pdfMxd = arcpy.mapping.MapDocument(mxdpath + mxdFile)
        arcpy.mapping.ExportToPDF(pdfMxd, outputPDF + mxdFile[:-3] + "pdf", resolution=300)
        print (mxdFile[:-3] + "pdf export successful.")
        del pdfMxd

    # PNG出圖
    elif mxdFile.endswith(PNG):
        pngMxd = arcpy.mapping.MapDocument(mxdpath + mxdFile)
        arcpy.mapping.ExportToPNG(pngMxd, outputPNG + mxdFile[:-9] + ".png", resolution=300)
        print (mxdFile[:-9] + ".png export successful.")
        del pngMxd

    else:
        print ("File name error, please check.")

print ("All Finish!")
