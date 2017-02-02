# HAM
Halo Abundance Matching-
http://www.ncra.tifr.res.in:8081/~tirth/Teaching/Cosmology/Cosmology-Project-6-HAM.pdf

For running all programs one after another, run following:

"source project_bash.sh"


Project description
----------------------------
To get the shortened data just run following commands sequentially

"python saving_important_columns.py"
"python extracting_required_data.py"

NOTE: above commands assume that yang* file and out* file is already present in the current directory

The SDSS is a magnitude limited survey. Hence the number density of the 
yang data must be the observed density which is likely to be less than 
the true density. Since we assume monotic relation between Galaxy Luminosity
and Halo mass, the largest halo would match with highest luminosity and the smallest mass 
would not have observationally visible luminosities to match with. 
 
 Solution: We chop off lower halo masses to match the density of observational data.
 
 
To match simulation and observation density run	the following command

"python density_range_sorting.py"

To generate the output file for Part 3.1 run following command

"python abundance_matching.py"

This generates a text file with columns "Mass Luminosity X Y Z" in respective units 
(This is different order as compared to the temp files generated in previous python codes)

-------------------------------------
Description of the 2_pt_corr_test*.py files:
-------------------------------------


1) 2_pt_corr_test1.py is a skeleteon code which was originally thought as 
the way yo compute the distance between the points

2) 2_pt_corr_test2.py is a brute force method applied on all the points 
and corrects for the edge effects in a robust manner. Sadly, the code is highly 
unoptimised and causes memory error as the number of pairs are simply too huge

3) 2_pt_corr_test3.py is a modification of test2 by directly obtaining
histogram after every iteration. It also accounts for periodic boundary condition.

4) 2_pt_corr_test4.py another version to try out various optimisation.  


---------------------------
Execution of 2 point correlation
--------------------------------
To check the code indeed gives 2 pt correlation we compute Xi(r) for randomly distributed points.
To do this test run the following command.
"python Xi_test.py"


For generating different subsets of the mock catalog run the following command

"python Generating_Subsets_Of_Mock_Galaxy_Catalog.py"

At this point we can run the 2 pt correlation on each of the Subsets of Mock Catalog
This can be currently done by running 

 "python 2_point_correlation_final.py" or "python 2_pt_corr_test4.py"     ####Needs refinement of bin size

In 2_point_correlation_final.py, the terminal output can be limited by changing the variable 'chatter' to False

To plot the estimator Vs distance in log scale run the following command

"python final.py"


