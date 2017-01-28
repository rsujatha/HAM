# HAM
Halo Abundance Matching-
http://www.ncra.tifr.res.in:8081/~tirth/Teaching/Cosmology/Cosmology-Project-6-HAM.pdf



To get the shortened data just run following commands sequentially

"python saving_important_columns.py"
"python extracting_required_data.py"

NOTE: above commands assume that yang* file and out* file is already present in the current directory


To generate the output file for Part 3.1 run following command

"python abundance_matching.py"

This generates a text file with columns "Mass Luminosity X Y Z" in respective units 
(This is different order as compared to the temp files generated in previous python codes)


Running the 2_pt_corr_test*.py files:
-------------------------------------


1) 2_pt_corr_test1.py is a skeleteon code which was originally thought as 
the way yo compute the distance between the points

2) 2_pt_corr_test2.py is a brute force method applied on all the points 
and corrects for the edge effects in a robust manner. Sadly, the code is highly 
unoptimised and causes memory error as the number of pairs are simply too huge

3) 2_pt_corr_test3.py is a better code as in reduces the points considered 
for distance computation based on 'r'. For a given r and dr the code runs 
in about 2-3 hrs. 

3.5) "Code by Sujatha (Not added to git)": It is a revised version of the 2_pt_corr_test2.py 
in which instead of all points, the points which lie <75 Mpc are only considered.
This code computes a histogram from 0 to 75 Mpc, with required binning. 
Takes about 3-4 hrs on her laptop
