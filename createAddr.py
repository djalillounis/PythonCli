import os
import re
import subprocess
import time
import datetime
from config import sendCmdtoShell,snedCmdtoSell_testing,configParms,Mkdir



def createPayAddr (_name):
    wltDirbool = Mkdir(_name)
    if wltDir:
        wltDir=_name
        parms =configParms()
        if len(parms) >= 1 :
            name =_name+".key"

            signing_key_file = name+".skey"
            verification_key_file=name+".vkey"
            cmd ="cardano-cli shelley address key-gen "+" --verification-key-file "+verification_key_file +" --signing-key-file "+ signing_key_file
            sendCmdtoShell(cmd)
            cmd =""
            cmd ="mkdir ./name"
            sendCmdtoShell(cmd)
            name=""


            addrFile =_name+".pyment.addr"
            print(verification_key_file)

            cmd = parms[0] + " address build --payment-verification-key-file "+verification_key_file+" --out-file " + addrFile +" " +  parms[1]
            sendCmdtoShell(cmd)
            print("--------------------------------------------")
            print("Address created " +addrFile)
            Hexa = sendCmdtoShell("cat "+ addrFile)
            addr = Hexa.decode('utf-8')
            print(addr)

            print("--------------------------------------------")

        else:
            print("Impossible to get network parms check config.py")
    else:
        print("A walet with the same name is already created.")
#Converting the Payment Address to Stacking Address
def covert_to_Stacking (_name):
    print("Convert Payment Add to Stacking Add")


createPayAddr("Djalil_test")
