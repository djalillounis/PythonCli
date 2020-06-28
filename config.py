import os
import re
import subprocess
import time
import datetime

"""
This file contains all the cmun function and Params for the Cardano cli
Having this parms in a sinlge file will make maintaaining the code very easy.

"""
# function that will retun the Shelly CLI parms in a list
def configParms():
   network="--testnet-magic 42 "
   Shelly_CLI = "cardano-cli shelley "
   reslist = []
   reslist.append(Shelly_CLI)
   reslist.append(network)
   return reslist


#function to send simple CMD to the bash
def snedCmdtoSell_testing(cmc):
    os.system(cmd)

#function to will send cmd to Shelly CLI
def sendCmdtoShell(cmd):

    result = subprocess.run([cmd], stdout=subprocess.PIPE,shell=True)
    res = result.stdout
    res = res.decode('utf-8')

    return res

#Function to get the network parms
#I need to add a cleanup before each call
def protocolParms(Network):
    snedCmdtoSell_testing("ls -al")
    snedCmdtoSell_testing("mkdir ./tmp")
    path = "./tmp/"
    parms = configParms()
    datetime.datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
    suf = datetime.datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
    suf = str(suf)
    suf =suf.replace(" ","")
    suf =suf.replace(":","-")
    suf = suf+".json"
    fileName ="params"+suf
    outFile = "--out-file " + path+fileName
    cmd= parms[0]+"query protocol-parameters "+parms[0]+" "+outFile
    sendCmdtoShell(cmd)
    print ("Parm  File Created : " + fileName)

#funcotion will create a directory if it does not exisit
def Mkdir(_name):
    cmd  = "mkdir " + _name
    cmd1 = sendCmdtoShell("ls -l | grep '^d' | awk '{print $9}'")
    cmd1 = cmd1.split("\n")
    exist = True
    Created = False

    for item in cmd1:

        if item == _name:
            exist = True
            print("Walletal ready exisit")
            break
        else:
            exist = False



    if exist==False:
        print("Direcotry created")
        res = sendCmdtoShell(cmd)
        Created = True
    return Created
