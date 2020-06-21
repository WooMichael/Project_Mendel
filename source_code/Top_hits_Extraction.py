import os
stream = os.popen('ls /root/Github/Project_Mendel/Data/MSA_Scans_From_nhmmerscan/')
output = stream.readlines()
msa_path = "/root/Github/Project_Mendel/Data/MSA_Scans_From_nhmmerscan/"
top_hit_output = "/root/Github/Project_Mendel/Data/Top_Hits_Scans/"
for fam in output:
    path = msa_path + fam.strip()
    with open(path,'r') as handler:
        top_hit = handler.readlines()[2:3]
        top_hit_line = str(top_hit).split()
        if(len(top_hit_line) > 1):
            target_name_family = top_hit_line.__getitem__(0)
            query_name = top_hit_line.__getitem__(2)
            e_value = top_hit_line.__getitem__(12)
            bit_score = top_hit_line.__getitem__(13)
            print(top_hit_line)
        #print(len(top_hit_line))
        if(len(top_hit_line) == 1):
            print("Scan did not show no hits")
    
