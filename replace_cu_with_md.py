import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".cu"):
            pre, ext = os.path.splitext(file)
            new_file_name = pre + ".md"
            with open(os.path.join(r, file), "r") as f_data:
                data = f_data.readlines()   
    
                header = "# {0}\n```C++\n".format(file)
                footer = "\n```"
                with open(os.path.join(r, new_file_name), "w+") as fOut:
                    fOut.write(header)
                    for line in data:
                        fOut.write(line)
                        
                    fOut.write(footer)