#Rename all files in an folder
def bulkRename (directory,name,number,extention):
    import os
    
    folderpath = os.listdir(directory)
    for i in folderpath:
        os.rename(i,name+ str(number)+extention)
        number+=1
    return "Successful"
