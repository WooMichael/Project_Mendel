#Author Michael Woo
#The way the naming goes is Genera Species  Family
#The goal of this program is to sperate these three rankings into their own directories...
from Bio import SeqIO
LTP_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/LTPs132_SSU_compressed.fasta"
for record in SeqIO.parse(LTP_path,"fasta"):
    #print(record.id)
    #print(record.description)
    record_description = str(record.description).split()
    #Family = record_description.__getitem__(7)
    #Species = record_description.__getitem__(6)
    #Genera = record_description.__getitem__(5)
   # print(len(record_description))
    #print(record_description.__getitem__(7))
    if(len(record_description) ==  8):
        Family = record_description.__getitem__(7)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        #print(len(record_description))
    if(len(record_description) == 9):
       # print(record_description)
        Family = record_description.__getitem__(8)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
    if(len(record_description) == 10):
       # print(record_description)
        Family = record_description.__getitem__(9)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
    if(len(record_description) == 11):
        Family = record_description.__getitem__(10)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        #do not write unless you are ready
    #SeqIO.write(record,"demo.fa","fasta")
