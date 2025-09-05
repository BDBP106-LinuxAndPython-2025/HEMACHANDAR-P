ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ ls
feed1based  feed2based  feed3based  feed4based  file1.txt  file2a.txt  heightbased  pig_weights.txt  question1-IA1.sh  question2-IA1.sh  question3-IA1.sh  SOCR-HeightWeight.csv  weighttbased
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ rm feed2based feed3based feed4based heightbased question2-IA1.sh question3-IA1.sh weighttbased 
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ ls
feed1based  file1.txt  file2a.txt  pig_weights.txt  question1-IA1.sh  SOCR-HeightWeight.csv
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ cat pig_weights.txt 
��Feed 1	Feed 2	Feed 3	Feed 4
60.8	68.3	102.6	87.9
57.1	67.7	102.2	84.7
65	74	100.5	83.2
58.7	66.3	97.5	85.8
61.8	69.9	98.9	90.3
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ vi pigweightedited.txt
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ sort -k 2n pigweightedited.txt  > feed2based
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ cat feed2based


#!/bin/bash
Feed 1	Feed 2	Feed 3	Feed 4
58.7	66.3	97.5	85.8
57.1	67.7	102.2	84.7
60.8	68.3	102.6	87.9
61.8	69.9	98.9	90.3
65	74	100.5	83.2
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ sort -k 3n pigweightedited.txt  > feed3based
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ sort -k 4n pigweightedited.txt  > feed4based
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ cat feed3based


#!/bin/bash
Feed 1	Feed 2	Feed 3	Feed 4
58.7	66.3	97.5	85.8
61.8	69.9	98.9	90.3
65	74	100.5	83.2
57.1	67.7	102.2	84.7
60.8	68.3	102.6	87.9
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ cat feed4based


#!/bin/bash
Feed 1	Feed 2	Feed 3	Feed 4
65	74	100.5	83.2
57.1	67.7	102.2	84.7
58.7	66.3	97.5	85.8
60.8	68.3	102.6	87.9
61.8	69.9	98.9	90.3
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ ls
feed1based  feed2based  feed3based  feed4based  file1.txt  file2a.txt  pigweightedited.txt  pig_weights.txt  question1-IA1.sh  SOCR-HeightWeight.csv
ibab@IBAB-MSc-BDB-Comp07:~/IA-1_Practicals_MOCk$ vi question2-IA1.sh

