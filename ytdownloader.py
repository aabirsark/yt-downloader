from pytube import YouTube

# starting the programe
print("Welcome to Roar Download :-)")


def formatSizeUnits(bytes):
  if(bytes >= 1073741824) :
     bytes = str((bytes / 1073741824)) + " GB"; 
  elif (bytes >= 1048576):
    bytes = str((bytes / 1048576)) + " MB"; 
  elif (bytes >= 1024):
    bytes = str((bytes / 1024)) + " KB"; 
  elif (bytes > 1):
    bytes = str(bytes) + " bytes"; 
  elif(bytes == 1):
    bytes = str(bytes) + " byte"; 
  else: 
    bytes = "0 bytes"; 
    
  return bytes;


def download():
    inputUrl = str(input("url --->> "))
    
    if (inputUrl== "e"):
        return
    yt = YouTube(inputUrl )
    print("Inputed url title -> " +  yt.title)
    con = str(input("sure to download (y/n) --->> "))
    if con== "y" or con == "yes":
        stream = yt.streams.get_by_itag(135)
        print("file size -> " + formatSizeUnits(stream.filesize)  )
        print("Downloading...")
        stream.download()
        
    else :
        print("permission denied returning back <<----//")
        return
        




while True:
    print("\npress d to download video\npress e for exit")
    print("\n")
    a = str(input("=> "))
    if(a == "d"):
        download()
    elif a == "e":
        break
        
