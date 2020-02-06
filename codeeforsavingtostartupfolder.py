import os.path

save_path = 'C:/Users/username/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

name_of_file = code.py

completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

toFile = raw_input("Write what you want into the field")

file1.write(toFile)

file1.close()
