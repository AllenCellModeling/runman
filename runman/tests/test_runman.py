#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test runman
"""

import runman   
import pickle
import os


def test_runman():
    """Test run management"""
    counter = []
    def step(timestep):
        counter.append(timestep)
    def log():
        if len(counter)==0:
            logval = None
        else:
            logval = counter[-1]
        print(logval)
        return logval
    run = runman.Run(assets=[counter, ],
                     stepfns=[step, ],
                     logfns=[log, ],
                     loginterval=2, 
                     snapshotinterval=4, 
                     serializewhat = ['log' 'timestamp']
                    )
    run.run(10, True)
    filename = str(abs(hash(run)))+".pkl"
    with open(filename, 'rb') as file:
        reloaded = pickle.load(file) 
    os.remove(filename)


