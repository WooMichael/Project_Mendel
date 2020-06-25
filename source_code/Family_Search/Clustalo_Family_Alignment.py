import os
from Bio import SeqIO

# stream is the variable that allows me to use the command line in python
stream = os.popen('ls /root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Family/ ')
# the output is saved
output = stream.readlines()
# `print(output)
# this is where the alignment begins
for fam in output:
    family = str(fam).strip()
    # this is the path from the Data Reference lib
    path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Family/" + str(family)
    # you want to use this when there are more than 1 sequence in a fasta file
    clustalo_command_line = "clustalo -i " + path + " " + "-o /root/Github/Project_Mendel/Data/Aligned_Reference_Sequences_From_LTP_Family/" + family
    # you want to use this when there are ONLY 1 sequence in a fasta file
    copy_file_command_line = "cp " + path + " " + "/root/Github/Project_Mendel/Data/Aligned_Reference_Sequences_From_LTP_Family/" + family
    # print(clustalo_command_line)
    # counter counts the amount of sequences in the fasta file...
    counter = 0
    for seq_record in SeqIO.parse(path, "fasta"):
        # counts how many record (sequences) there are in the family record
        counter += 1
        # print(counter)
    # after counting the records we then choose which command we want to run below
    if (counter == 1):
        print("only 1 seq")
        os.popen(copy_file_command_line)
    if (counter > 1):
        print("more than 1 seq")
        os.popen(clustalo_command_line)
#  print(path)
