# -*- coding: utf-8 -*-
import os
import subprocess
import time
import sys

conf = 'C:\\Users\\imijic\\OneDrive - fer.hr\\opensmile-2.3.0\\config\\gemaps\\gemaps.conf'
wav_dir = "C:\\Users\\imijic\\OneDrive - fer.hr\\OST wavs"
csv_dir = "C:\\Users\\imijic\\OneDrive - fer.hr\\OST csvs"

wav_names = os.listdir(wav_dir)

wav_files = []
out_files = []
commands = []

for wav in wav_names:
    wav_files.append(os.path.join(wav_dir, wav))   

for wav in wav_names:
    temp = str.split(wav, '_')[0]
    temp = temp + '.csv'
    out_files.append(os.path.join(csv_dir, temp))

for wave_file, feat_file in zip(wav_files, out_files):
    
    command = 'SMILExtract_Release -I "{input_file}" -C "{conf_file}" --lldcsvoutput "{output_file}"'.format(
                        input_file = wave_file,
                        conf_file = conf,
                        output_file = feat_file
                        )
    commands.append(command)

def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()

    output = process.communicate()[0]
    exitCode = process.returncode

    if (exitCode == 0):
        return output
    else:
        raise subprocess.ProcessException(command, exitCode, output)    
    
    
for command in commands:
    t0 = time.time()
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
#==============================================================================
#     execute(command)
#==============================================================================
    t1 = time.time()
    total = t1-t0
    print(total)