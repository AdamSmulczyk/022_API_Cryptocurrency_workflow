#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os
from time import time, sleep
from data_processor_cc import api_runner


def main():
    print('-' * 80)
    print("Preprocessing data...")

    for i in range(5):
        api_runner()
        print('API Runner completed')
        sleep(6) #sleep for 6 seconds
        exit()

    
if __name__ == "__main__":
    main()

