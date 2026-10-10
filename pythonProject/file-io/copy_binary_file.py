import shutil

source = "C:/Users/udayd/OneDrive/Desktop/IO/hello.jpj.webp";
target = "C:/Users/udayd/OneDrive/Desktop/Op/hello.jpj.webp";

shutil.copyfile(source, target)
print(source + " is copied to " + target)
