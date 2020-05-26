import os

def addStartContent(index,contents,newFilename):
    contents.insert(index, "lr_start_transaction(\"Txn1\")\n")

    f = open(newFilename, "w")
    contents = "".join(contents)
    f.write(contents)

    index=index+2
    return index

def addEndContent(index2,contents,newFilename):
    contents.insert(index2+1, "lr_end_transaction(\"Txn1\",LR_PASS)\n")

    f = open(newFilename, "w")
    contents = "".join(contents)
    f.write(contents)

    index2=index2+2
    return index2


def openFileforStartTxn(index,fileName,newFilename):
    f = open(fileName, "r")
    contents = f.readlines()


    for items in contents:
        if ((len(contents)-1 >= index) and (contents[index].__contains__("web_"))):
            index=addStartContent(index,contents,newFilename)
            #print(index)
            continue
        elif index==len(contents)-1:
            break
        else:
            index=index+1
    f.close()

def openFileforEndTxn(index2,fileName,newFilename):
    f = open(fileName, "r")
    f.seek(0)
    contents = f.readlines()


    for items in contents:
        if ((len(contents)-1 >= index2) and (contents[index2].__contains__("LAST"))):
            index2=addEndContent(index2,contents,newFilename)
            #print(index2, len(contents))
            continue
        elif index2==len(contents)+1:
            break
        else:
            index2=index2+1
    f.close()

def mainF(oldfilePath,newfilePath):
    fileName = oldfilePath
    newFilename = newfilePath

    if(os.path.exists(fileName) and fileName.endswith(".c")):
        openFileforStartTxn(0,fileName,newFilename)
        openFileforEndTxn(0,fileName,newFilename)
        return "New File created"
    else:
        return "File path doesn't exists"
