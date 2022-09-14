import os

def getFolder():
  return os.getcwd()

def getFiles():
  folder = getFolder()
  files = os.listdir(folder)
  files.remove('main.py')
  files = removeFoldersFromList(files)
  return files

def removeFoldersFromList(list):
  return [element for element in list if "." in element]

def createFolder(path, folderName):
  if not folderExists(path):
    os.mkdir(path)
    print(f'Pasta {folderName} criada com sucesso!')

def folderExists(path):
  return os.path.exists(path)

def removeExtension(file):
  return file.rsplit(".")[0]

def moveFile(source, destination, file):
  os.replace(source, destination)
  print(f'Arquivo {file} movido com sucesso!')

if __name__ == "__main__":
  files = getFiles()
  for file in files:
    folderName = removeExtension(file)
    path = getFolder() + "\\" + folderName
    createFolder(path, folderName)
    source = getFolder() + "\\" + file
    destination = getFolder() + "\\" + folderName + "\\" + file
    moveFile(source, destination, file)
