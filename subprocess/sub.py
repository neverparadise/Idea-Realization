import subprocess

cmd = 'nvidia-smi'
#for i in range(10):
#    subprocess.run(cmd, shell=True)

import logging

logging.basicConfig(filename="./mylog.txt", level=logging.INFO)

def hap(a, b):
    ret = a + b
    logging.info(f"input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4)