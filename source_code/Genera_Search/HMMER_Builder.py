import os
from Bio import SeqIO

stream = os.popen(
    'ls home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/')
output = stream.readlines()
ref_path = "home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/"
hmm_path = "home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Genera/"

for fam in output:
    family = str(fam).strip()
    path = ref_path + family
    gen_stream = os.popen("ls " + path)
    gen_output = gen_stream.readlines()
    dir_gen_path = hmm_path + fam + "/"
    if not os.path.exists(dir_gen_path):
        os.mkdir(dir_gen_path)
    for gen in gen_output:
        hmm_gen = gen.replace('.fa', '.hmm')
        gen_path = path + "/" + gen
        command_line_msa = "hmmbuild " + dir_gen_path + hmm_gen + " " + gen_path
        print(command_line_msa)
        os.popen(str(command_line_msa))
