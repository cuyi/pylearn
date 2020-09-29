#! python
# -*- coding: UTF-8 -*-

import datetime
import sys
import getopt
import os
import shutil

def usage():
    print("Usage: copyTxtToDir -i inputDir -o outputDir")

def analysisInput():
    shortArgs = '-h-i:-o:-v'
    longArgs = ["help", "intput=", "output=", "version"]
    opts, args = getopt.getopt(sys.argv[1:], shortArgs, longArgs)

    if len(args) > 0 :
        usage()
        sys.exit(0)

    inDir = ''
    outDir = ''
    for optName, optValue in opts:
        if optName in ('-h', '--help') :
            usage()
            sys.exit(0)
        elif optName in ('-i', '--input') :
            inDir = optValue
        elif optName in ('-o', '--output') :
            outDir = optValue

    return inDir, outDir        

def copyTxtToDir(srcDir, dstDir):
    shutil.rmtree(dstDir)
    os.system("pause")
    os.mkdir(dstDir)

    for root, dirs, files in os.walk(srcDir, topdown=False):
        for file in files:
            # 过滤掉不感兴趣的文件
            if file.rfind(".txt") < 0:
                continue
            if file.find("common.txt") >= 0:
                continue
            # copy到固定目录
            srcFile = os.path.join(root, file)
            shutil.copy(srcFile, dstDir)

def main():
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("main start time is:", now_time)

    inputDir, outputDir = analysisInput()
    copyTxtToDir(inputDir, outputDir)
    
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("main start time is:", now_time)



if __name__ == "__main__":
    main()

