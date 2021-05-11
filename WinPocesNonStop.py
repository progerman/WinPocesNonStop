import os
import time
from datetime import datetime


process_name = 'Telegram.exe'
number_of_call_attempts=1
path_to_dir_executable_file="C:\Program Files\Telegram Desktop\Roaming\Telegram Desktop"



def  show_all_process():
    output = os.popen('wmic process get description, processid').read()
    return output

def check_specific_proccess_run(process_name = str):
    status_process_flag = False
    for i in show_all_process().split('\n'):
        if process_name in i:
            print(datetime.now(), f'Process {i.replace("      ", " ")} is run')
            status_process_flag = True
    if status_process_flag == False:
        print(datetime.now(), f'Process {process_name}  not found')
    return status_process_flag


def autorestart_process(*,number_of_call_attempts=int, process_name = str):
    while True:
        
        time.sleep(10)
        for i in range(number_of_call_attempts):
            if  check_specific_proccess_run(process_name) == False:
                output = os.popen(f'wmic process call create "{path_to_dir_executable_file}\{process_name}"').read()
                print((f'Starting process  "{path_to_dir_executable_file}\{process_name}"'))
                print( datetime.now(), 'Proces successfully created')
            
        


if __name__ == "__main__":
    autorestart_process(number_of_call_attempts=number_of_call_attempts , process_name=process_name)

