import os
import time
#1 Source
source = ['/home/aalam/bin']

#2 Backup Directory
target_dir = '/tmp/backup'

#3 files are stored as Zip file
#4 name of file as current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Check if target directory exist otherwise create it
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#5 Use Zip command to create Zip Archive

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

#Run the Backup

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successfully back to', target)
else:
    print('Backup failed')
