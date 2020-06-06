import os
from Bio import SeqIO
stream = os.popen('ls /root/Github/Project_Mendel/Data/Aligned_Reference_Sequences_From_LTP')
output = stream.readlines()
ref_path = "/root/Github/Project_Mendel/Data/Aligned_Reference_Sequences_From_LTP/" 
hmm_path = "/root/Github/Project_Mendel/Data/HMM_Builds_From_Aligned_Reference_Sequences_LTP/"
for fam in output:
    family = str(fam).strip()
    path = ref_path + family
    hmm_family = family.replace('.fa','.hmm')
    command_line_msa = "hmmbuild " + hmm_path + hmm_family  + " " + ref_path + family    
    command_line_single = "hmmbuild " + hmm_path + hmm_family  + " " + ref_path + family 
   # command_line_cp = "cp " + ref_path + family  + " " + hmm_path + hmm_family 
    counter = 0
    for seq_record in SeqIO.parse(path,"fasta"):
        counter += 1
        #print(counter)
        #print("only 1 seq")
    if(counter == 1):
        print("only 1 seq")
        os.popen(str(command_line_single))
   #     os.popen(str(command_line_cp))

    if(counter > 1):
   # print(command_line)
        os.popen(str(command_line_msa))
