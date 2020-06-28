import os
import re
import subprocess
import time
import datetime
from config import sendCmdtoShell,snedCmdtoSell_testing

#cardano-cli shelley address key-gen \
#--verification-key-file payment.vkey \
#--signing-key-file payment.skey

def createAdres(_name,type,network):
    name =_name+".key"
    signing_key_file = name+".skey"
    verification_key_file=name+".vkey"
    cmd ="cardano-cli shelley address key-gen "+" --verification-key-file "+verification_key_file +" --signing-key-file "+ signing_key_file
    sendCmdtoShell(cmd)
    name=""
 #cardano-cli shelley stake-address key-gen \
 #--verification-key-file stake.vkey \
 #--signing-key-file stake.skey
    name =_name+".stake"
    Stackig_signing_key_file = name+".skey"
    Stackig_verification_key_file=name+".vkey"
    cmd ="cardano-cli shelley stake-address key-gen "+" --verification-key-file "+Stackig_verification_key_file +" --signing-key-file "+ Stackig_signing_key_file
    sendCmdtoShell(cmd)
    name=""
 #cardano-cli shelley address build \
 #--payment-verification-key-file payment.vkey \
 #--stake-verification-key-file stake.vkey \
 #--out-file payment.addr \
 #--testnet-magic 42
    addrFile =_name+".pyment.addr"
    print(verification_key_file)
    print(Stackig_verification_key_file)
    cmd = "cardano-cli shelley address build --payment-verification-key-file "+verification_key_file+ " --stake-verification-key-file "+Stackig_verification_key_file+" --out-file " + addrFile +" " +  network
    sendCmdtoShell(cmd)
    print("--------------------------------------------")
    print("Address created " +addrFile)
    Hexa = sendCmdtoShell("cat "+ addrFile)
    addr = Hexa.decode('utf-8')
    print(addr)

    print("--------------------------------------------")
