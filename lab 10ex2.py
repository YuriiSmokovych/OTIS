import os

dir_program = os.listdir(path="C:\program files")
print(dir_program)

dir_windows = os.listdir(path="C:\windows")

write_win = open('w.txt','wt')
for index in dir_windows:
    write_win.write(index + '\n')
write_win.close()