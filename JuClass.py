# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:29:25 2018

@author: cqju
"""

from scipy import io as spio
import numpy as np
class Transform():
    def __init__(self):
        pass
        #from scipy import io as spio
        #self.mpc = mpc
        #self.spio = spio
    
    
    def read_mpc_case(fname):
        if type(fname) != str:
            raise RuntimeError('Input type is wrong in \'read_mpc_case\'')
    
        op = spio.loadmat(fname)
        op = op["mpc"]
        allnames = op.dtype.names
        
        mpc = dict()
        if "version" in allnames:
            mpc["version"] = str(int(op["version"][0,0]))
        if "baseMVA" in allnames:
            mpc["baseMVA"] = op["baseMVA"][0,0][0,0]
        if "branch" in allnames:
            mpc["branch"] = op["branch"][0,0]
        if "bus" in allnames:
            mpc["bus"] = op["bus"][0,0].astype(float)
        if "gen" in allnames:
            mpc["gen"] = op["gen"][0,0].astype(float)
        if "gencost" in allnames:
            mpc["gencost"] = op["gencost"][0,0].astype(float)
        if "areas" in allnames:
            mpc["areas"] = op["areas"][0,0].astype(int)
        
        
        
        return mpc
    
    ### dump inactive branches: 
    def dump_inactive_branch(mpc):
        mpc["branch"] = mpc["branch"][np.where(mpc["branch"][:,10] == 1)[0],:]
        if np.shape(mpc["bus"])[0] != np.shape(mpc["branch"])[0] + 1: 
            raise RuntimeError('Input type is wrong in \'read_mpc_case\' \n \
                               Error! The case is not a distribution case. \n Dist-Flow model not applicable.')
        return mpc



#mpc = Transform.read_mpc_case("case33bw.mat")
#mpc= Transform.dump_inactive_branch(mpc)