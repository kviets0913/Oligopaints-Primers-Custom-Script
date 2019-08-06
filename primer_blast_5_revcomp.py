#!/usr/bin/env python

bc21mer= open('bc19mer.240k.fasta')
oligo_file = open(input (str("Please enter the name of the olgio file you want to search (include the extension and put name in quotation marks):" )))
#job_title = input (str("Please enter the gene you are entering, indicate if DNA or RNA library, also in quotation:"))
good_primer = open("good_primers.fasta","w")
bad_primer = open("bad_primers.fasta","w")

name = []
primer =[]
oligo=[]
matches = 0
section1 = 0
section2 = 0
section3 = 0
section4 = 0
section5 = 0
section6 = 0
section7 = 0

dct = {}

number_oligo = 0
for line in oligo_file:
    number_oligo = number_oligo + 1

oligo_file.seek(0)   
count = 0

for i in bc21mer:
    fields = i.rstrip("\r\n").split("\t")
    if i.startswith(">"):
        name= [fields[0]]
        real_name= fields[0]
    else:    
        primer = list(i) 
        new_primer = list(i)
        comp = []
        for bp in new_primer:
            if bp == "A":
                comp.append("T")
            if bp == "T":
                comp.append("A")
            if bp == "C":
                comp.append("G")
            if bp == "G":
                comp.append("C")  
        primer_revcomp = comp[::-1]
        
        dct[real_name] = primer
        oligo_file.seek(0)
        for line in oligo_file:
            count = count + 1
            fields = line.rstrip("\r\n").split("\t")
            oligo = list(fields[3]) 
            #Section 1
            section1 = 0
            section2 = 0
            section3 = 0
            section4 = 0
            section5 = 0
            section6 = 0
            section7 = 0
            if primer [0:15] == oligo [0:15] or primer_revcomp [0:15] == oligo [0:15]:
                section1 = section1 + 1
            if primer [0:15] == oligo [1:16] or primer_revcomp [0:15] == oligo [1:16]:
                section1 = section1 + 1
            if primer [0:15] == oligo [2:17] or primer_revcomp [0:15] == oligo [2:17]: 
                section1 = section1 + 1   
            if primer [0:15] == oligo [3:18] or primer_revcomp [0:15] == oligo [3:18]:
                section1 = section1 + 1     
            if primer [0:15] == oligo [4:19] or primer_revcomp [0:15] == oligo [4:19]:
                section1 = section1 + 1    
            if primer [0:15] == oligo [5:20] or primer_revcomp [0:15] == oligo [5:20]:
                section1 = section1 + 1
            if primer [0:15] == oligo [6:21] or primer_revcomp [0:15] == oligo [6:21]:
                section1 = section1 + 1   
            if primer [0:15] == oligo [7:22] or primer_revcomp [0:15] == oligo [7:22]:
                section1 = section1 + 1 
            if primer [0:15] == oligo [8:23] or primer_revcomp [0:15] == oligo [8:23]:
                section1 = section1 + 1
            if primer [0:15] == oligo [9:24] or primer_revcomp [0:15] == oligo [9:24]:
                section1 = section1 + 1
            if primer [0:15] == oligo [10:25] or primer_revcomp [0:15] == oligo [10:25]:
                section1 = section1 + 1
            if primer [0:15] == oligo [11:26] or primer_revcomp [0:15] == oligo [11:26]:
                section1 = section1 + 1
            if primer [0:15] == oligo [12:27] or primer_revcomp [0:15] == oligo [12:27]:
                section1 = section1 + 1
            if primer [0:15] == oligo [13:28] or primer_revcomp [0:15] == oligo [13:28]:
                section1 = section1 + 1
            if primer [0:15] == oligo [14:29] or primer_revcomp [0:15] == oligo [14:29]:
                section1 = section1 + 1           
            if primer [0:15] == oligo [15:30] or primer_revcomp [0:15] == oligo [15:30]:
                section1 = section1 + 1 
            if primer [0:15] == oligo [16:31] or primer_revcomp [0:15] == oligo [16:31]:
                section1 = section1 + 1
            if primer [0:15] == oligo [17:32] or primer_revcomp [0:15] == oligo [17:32]:
                section1 = section1 + 1
            if primer [0:15] == oligo [18:33] or primer_revcomp [0:15] == oligo [18:33]:
                section1 = section1 + 1
            if primer [0:15] == oligo [19:34] or primer_revcomp [0:15] == oligo [19:34]:
                section1 = section1 + 1 
            if primer [0:15] == oligo [20:35] or primer_revcomp [0:15] == oligo [20:35]:
                section1 = section1 + 1
            if primer [0:15] == oligo [21:36] or primer_revcomp [0:15] == oligo [21:36]:
                section1 = section1 + 1
            if primer [0:15] == oligo [22:37] or primer_revcomp [0:15] == oligo [22:37]:
                section1 = section1 + 1
            if primer [0:15] == oligo [23:38] or primer_revcomp [0:15] == oligo [23:38]:
                section1 = section1 + 1      
            if primer [0:15] == oligo [24:39] or primer_revcomp [0:15] == oligo [24:39]:
                section1 = section1 + 1
            if primer [0:15] == oligo [25:40] or primer_revcomp [0:15] == oligo [25:40]:
                section1 = section1 + 1          
            if primer [0:15] == oligo [26:41] or primer_revcomp [0:15] == oligo [26:41]:
                section1 = section1 + 1
            if primer [0:15] == oligo [27:42] or primer_revcomp [0:15] == oligo [27:42]:
                section1 = section1 + 1            
            if primer [0:15] == oligo [28:43] or primer_revcomp [0:15] == oligo [28:43]:
                section1 = section1 + 1
            if primer [0:15] == oligo [29:44] or primer_revcomp [0:15] == oligo [29:44]:
                section1 = section1 + 1
            if primer [0:15] == oligo [30:45] or primer_revcomp [0:15] == oligo [30:45]:
                section1 = section1 + 1
            if primer [0:15] == oligo [31:46] or primer_revcomp [0:15] == oligo [31:46]: 
                section1 = section1 + 1
            if primer [0:15] == oligo [32:47] or primer_revcomp [0:15] == oligo [32:47]:
                section1 = section1 + 1
            if primer [0:15] == oligo [33:48] or primer_revcomp [0:15] == oligo [33:48]:
                section1 = section1 + 1
            if primer [0:15] == oligo [34:49] or primer_revcomp [0:15] == oligo [34:49]:
                section1 = section1 + 1
            if primer [0:15] == oligo [35:50] or primer_revcomp [0:15] == oligo [35:50]:
                section1 = section1 + 1
            if primer [0:15] == oligo [36:51] or primer_revcomp [0:15] == oligo [36:51]:
                section1 = section1 + 1
            if section1 !=0:
                print "erg section 1"
                bad_primer.write(str(name))
                bad_primer.write("\n")
                bad_primer.write(i)
                bad_primer.write("\n")
                break
            if section1 == 0:
                #print "hello"    
                #Section 2
                #Comapring Primer 1-15    
                if primer [1:16] == oligo [0:15] or primer_revcomp [1:16] == oligo [0:15]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [1:16] or primer_revcomp [1:16] == oligo [1:16]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [2:17] or primer_revcomp [1:16] == oligo [2:17]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [3:18] or primer_revcomp [1:16] == oligo [3:18]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [4:19] or primer_revcomp [1:16] == oligo [4:19]:
                    section2 = section2 + 1 
                if primer [1:16] == oligo [5:20] or primer_revcomp [1:16] == oligo [5:20]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [6:21] or primer_revcomp [1:16] == oligo [6:21]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [7:22] or primer_revcomp [1:16] == oligo [7:22]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [8:23] or primer_revcomp [1:16] == oligo [8:23]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [9:24] or primer_revcomp  [1:16] == oligo [9:24]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [10:25] or primer_revcomp  [1:16] == oligo [10:25]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [11:26] or primer_revcomp  [1:16] == oligo [11:26]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [12:27] or primer_revcomp  [1:16] == oligo [12:27]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [13:28] or primer_revcomp  [1:16] == oligo [13:28]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [14:29] or primer_revcomp  [1:16] == oligo [14:29]:
                    section2 = section2 + 1         
                if primer [1:16] == oligo [15:30] or primer_revcomp  [1:16] == oligo [15:30]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [16:31] or primer_revcomp  [1:16] == oligo [16:31]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [17:32] or primer_revcomp  [1:16] == oligo [17:32]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [18:33] or primer_revcomp  [1:16] == oligo [18:33]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [19:34] or primer_revcomp  [1:16] == oligo [19:34]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [20:35] or primer_revcomp  [1:16] == oligo [20:35]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [21:36] or primer_revcomp  [1:16] == oligo [21:36]:
                    section2 = section2 + 1 
                if primer [1:16] == oligo [22:37] or primer_revcomp  [1:16] == oligo [22:37]:
                    section2 = section2 + 1 
                if primer [1:16] == oligo [23:38] or primer_revcomp  [1:16] == oligo [23:38]:
                    section2 = section2 + 1        
                if primer [1:16] == oligo [24:39] or primer_revcomp  [1:16] == oligo [24:39]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [25:40] or primer_revcomp  [1:16] == oligo [25:40]:
                    section2 = section2 + 1      
                if primer [1:16] == oligo [26:41] or primer_revcomp  [1:16] == oligo [26:41]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [27:42] or primer_revcomp  [1:16] == oligo [27:42]:
                    section2 = section2 + 1              
                if primer [1:16] == oligo [28:43] or primer_revcomp  [1:16] == oligo [28:43]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [29:44] or primer_revcomp  [1:16] == oligo [29:44]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [30:45] or primer_revcomp  [1:16] == oligo [30:45]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [31:46] or primer_revcomp  [1:16] == oligo [31:46]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [32:47] or primer_revcomp  [1:16] == oligo [32:47]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [33:48] or primer_revcomp  [1:16] == oligo [33:48]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [34:49] or primer_revcomp  [1:16] == oligo [34:49]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [35:50] or primer_revcomp  [1:16] == oligo [35:50]:
                    section2 = section2 + 1
                if primer [1:16] == oligo [36:51]or primer_revcomp [1:16] == oligo [36:51]:
                    section2 = section2 + 1
                if section2 !=0:
                    print "erg"
                    bad_primer.write(str(name))
                    bad_primer.write("\n")
                    bad_primer.write(i)
                    bad_primer.write("\n")
                    break     
                if section2 ==0:                       
                    #Section 3
                    #Comapring Primer 2-17  
                    if primer [2:17] == oligo [0:15] or primer_revcomp  [2:17] == oligo [0:15]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [1:16] or primer_revcomp  [2:17] == oligo [1:16]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [2:17] or primer_revcomp  [2:17] == oligo [2:17]:
                        section3 = section3 + 1 
                    if primer [2:17] == oligo [3:18] or primer_revcomp  [2:17] == oligo [3:18]:
                        section3 = section3 + 1 
                    if primer [2:17] == oligo [4:19] or primer_revcomp  [2:17] == oligo [4:19]:
                        section3 = section3 + 1  
                    if primer [2:17] == oligo [5:20] or primer_revcomp  [2:17] == oligo [5:20]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [6:21] or primer_revcomp  [2:17] == oligo [6:21]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [7:22] or primer_revcomp  [2:17] == oligo [7:22]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [8:23] or primer_revcomp  [2:17] == oligo [8:23]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [9:24] or primer_revcomp  [2:17] == oligo [9:24]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [10:25] or primer_revcomp  [2:17] == oligo [10:25]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [11:26] or primer_revcomp  [2:17] == oligo [11:26]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [12:27] or primer_revcomp  [2:17] == oligo [12:27]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [13:28] or primer_revcomp  [2:17] == oligo [13:28]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [14:29] or primer_revcomp  [2:17] == oligo [14:29]:
                        section3 = section3 + 1        
                    if primer [2:17] == oligo [15:30] or primer_revcomp  [2:17] == oligo [15:30]:
                        section3 = section3 + 1 
                    if primer [2:17] == oligo [16:31] or primer_revcomp  [2:17] == oligo [16:31]:
                        section3 = section3 + 1 
                    if primer [2:17] == oligo [17:32] or primer_revcomp  [2:17] == oligo [17:32]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [18:33] or primer_revcomp  [2:17] == oligo [18:33]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [19:34] or primer_revcomp  [2:17] == oligo [19:34]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [20:35] or primer_revcomp  [2:17] == oligo [20:35]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [21:36] or primer_revcomp  [2:17] == oligo [21:36]:
                        section3 = section3 + 1     
                    if primer [2:17] == oligo [22:37] or primer_revcomp  [2:17] == oligo [22:37]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [23:38] or primer_revcomp  [2:17] == oligo [23:38]:
                        section3 = section3 + 1   
                    if primer [2:17] == oligo [24:39] or primer_revcomp  [2:17] == oligo [24:39]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [25:40] or primer_revcomp  [2:17] == oligo [25:40]:
                        section3 = section3 + 1            
                    if primer [2:17] == oligo [26:41] or primer_revcomp  [2:17] == oligo [26:41]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [27:42] or primer_revcomp  [2:17] == oligo [27:42]:
                        section3 = section3 + 1             
                    if primer [2:17] == oligo [28:43] or primer_revcomp  [2:17] == oligo [28:43]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [29:44] or primer_revcomp  [2:17] == oligo [29:44]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [30:45] or primer_revcomp  [2:17] == oligo [30:45]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [31:46] or primer_revcomp  [2:17] == oligo [31:46]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [32:47] or primer_revcomp  [2:17] == oligo [32:47]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [33:48] or primer_revcomp [2:17] == oligo [33:48]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [34:49] or primer_revcomp [2:17] == oligo [34:49]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [35:50] or primer_revcomp [2:17] == oligo [35:50]:
                        section3 = section3 + 1
                    if primer [2:17] == oligo [36:51] or primer_revcomp  [2:17] == oligo [36:51]:
                        section3 = section3 + 1
                    if section3 !=0:
                        print "erg"
                        bad_primer.write(str(name))
                        bad_primer.write("\n")
                        bad_primer.write(i)
                        bad_primer.write("\n")
                        break                          
                    if section3 ==0:       
                        #Section 4
                        #Comapring Primer 2-17  
                        if primer [3:18] == oligo [0:15] or primer_revcomp [3:18] == oligo [0:15]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [1:16] or primer_revcomp [3:18] == oligo [1:16]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [2:17] or primer_revcomp [3:18] == oligo [2:17]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [3:18] or primer_revcomp [3:18] == oligo [3:18]:
                            section4 = section4 + 1  
                        if primer [3:18] == oligo [4:19] or primer_revcomp [3:18] == oligo [4:19]:
                            section4 = section4 + 1   
                        if primer [3:18] == oligo [5:20] or primer_revcomp [3:18] == oligo [5:20]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [6:21] or primer_revcomp [3:18] == oligo [6:21]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [7:22] or primer_revcomp [3:18] == oligo [7:22]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [8:23] or primer_revcomp [3:18] == oligo [8:23]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [9:24] or primer_revcomp [3:18] == oligo [9:24]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [10:25] or primer_revcomp [3:18] == oligo [10:25]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [11:26] or primer_revcomp [3:18] == oligo [11:26]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [12:27] or primer_revcomp [3:18] == oligo [12:27]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [13:28] or primer_revcomp [3:18] == oligo [13:28]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [14:29] or primer_revcomp [3:18] == oligo [14:29]:
                            section4 = section4 + 1        
                        if primer [3:18] == oligo [15:30] or primer_revcomp [3:18] == oligo [15:30]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [16:31] or primer_revcomp [3:18] == oligo [16:31]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [17:32] or primer_revcomp [3:18] == oligo [17:32]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [18:33] or primer_revcomp [3:18] == oligo [18:33]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [19:34] or primer_revcomp [3:18] == oligo [19:34]:
                            section4 = section4 + 1   
                        if primer [3:18] == oligo [20:35] or primer_revcomp [3:18] == oligo [20:35]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [21:36] or primer_revcomp [3:18] == oligo [21:36]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [22:37] or primer_revcomp [3:18] == oligo [22:37]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [23:38] or primer_revcomp [3:18] == oligo [23:38]:
                            section4 = section4 + 1   
                        if primer [3:18] == oligo [24:39] or primer_revcomp [3:18] == oligo [24:39]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [25:40] or primer_revcomp [3:18] == oligo [25:40]:
                            section4 = section4 + 1      
                        if primer [3:18] == oligo [26:41] or primer_revcomp [3:18] == oligo [26:41]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [27:42] or primer_revcomp [3:18] == oligo [27:42]:
                            section4 = section4 + 1          
                        if primer [3:18] == oligo [28:43] or primer_revcomp [3:18] == oligo [28:43]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [29:44] or primer_revcomp [3:18] == oligo [29:44]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [30:45] or primer_revcomp [3:18] == oligo [30:45]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [31:46] or primer_revcomp [3:18] == oligo [31:46]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [32:47] or primer_revcomp [3:18] == oligo [32:47]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [33:48] or primer_revcomp [3:18] == oligo [33:48]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [34:49] or primer_revcomp [3:18] == oligo [34:49]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [35:50] or primer_revcomp [3:18] == oligo [35:50]:
                            section4 = section4 + 1
                        if primer [3:18] == oligo [36:51] or primer_revcomp [3:18] == oligo [36:51]:
                            section4 = section4 + 1
                        if section4 !=0:
                            print "erg"
                            bad_primer.write(str(name))
                            bad_primer.write("\n")
                            bad_primer.write(i)
                            bad_primer.write("\n")
                            break
                        if section4 ==0:                    
                            #Section 5
                            #Comapring Primer 4-19 
                            if primer [4:19] == oligo [0:15] or primer_revcomp [4:19] == oligo [0:15]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [1:16] or primer_revcomp [4:19] == oligo [1:16]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [2:17] or primer_revcomp [4:19] == oligo [2:17]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [3:18] or primer_revcomp [4:19] == oligo [3:18]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [4:19] or primer_revcomp [4:19] == oligo [4:19]:
                                section5 = section5 + 1   
                            if primer [4:19] == oligo [5:20] or primer_revcomp [4:19] == oligo [5:20]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [6:21] or primer_revcomp [4:19] == oligo [6:21]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [7:22] or primer_revcomp [4:19] == oligo [7:22]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [8:23] or primer_revcomp [4:19] == oligo [8:23]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [9:24] or primer_revcomp [4:19] == oligo [9:24]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [10:25] or primer_revcomp [4:19] == oligo [10:25]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [11:26] or primer_revcomp [4:19] == oligo [11:26]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [12:27] or primer_revcomp [4:19] == oligo [12:27]:
                                section5 = section5 + 1 
                            if primer [4:19] == oligo [13:28] or primer_revcomp [4:19] == oligo [13:28]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [14:29] or primer_revcomp [4:19] == oligo [14:29]:
                                section5 = section5 + 1        
                            if primer [4:19] == oligo [15:30] or primer_revcomp [4:19] == oligo [15:30]:
                                section5 = section5 + 1   
                            if primer [4:19] == oligo [16:31] or primer_revcomp [4:19] == oligo [16:31]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [17:32] or primer_revcomp [4:19] == oligo [17:32]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [18:33] or primer_revcomp [4:19] == oligo [18:33]: 
                                section5 = section5 + 1
                            if primer [4:19] == oligo [19:34] or primer_revcomp [4:19] == oligo [19:34]:
                                section5 = section5 + 1    
                            if primer [4:19] == oligo [20:35] or primer_revcomp [4:19] == oligo [20:35]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [21:36] or primer_revcomp [4:19] == oligo [21:36]:
                                section5 = section5 + 1   
                            if primer [4:19] == oligo [22:37] or primer_revcomp [4:19] == oligo [22:37]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [23:38] or primer_revcomp [4:19] == oligo [23:38]:
                                section5 = section5 + 1       
                            if primer [4:19] == oligo [24:39] or primer_revcomp [4:19] == oligo [24:39]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [25:40] or primer_revcomp [4:19] == oligo [25:40]:
                                section5 = section5 + 1           
                            if primer [4:19] == oligo [26:41] or primer_revcomp [4:19] == oligo [26:41]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [27:42] or primer_revcomp [4:19] == oligo [27:42]:
                                section5 = section5 + 1           
                            if primer [4:19] == oligo [28:43] or primer_revcomp [4:19] == oligo [28:43]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [29:44] or primer_revcomp [4:19] == oligo [29:44]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [30:45] or primer_revcomp [4:19] == oligo [30:45]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [31:46] or primer_revcomp [4:19] == oligo [31:46]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [32:47] or primer_revcomp [4:19] == oligo [32:47]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [33:48] or primer_revcomp [4:19] == oligo [33:48]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [34:49] or primer_revcomp [4:19] == oligo [34:49]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [35:50] or primer_revcomp [4:19] == oligo [35:50]:
                                section5 = section5 + 1
                            if primer [4:19] == oligo [36:51] or primer_revcomp [4:19] == oligo [36:51]:
                                section5 = section5 + 1
                            if section5 !=0:
                                print "erg"
                                bad_primer.write(str(name))
                                bad_primer.write("\n")
                                bad_primer.write(i)
                                bad_primer.write("\n")
                                break
                            if section5 == 0:           
                                #Section 6
                                #Comapring Primer 5-20        
                                if primer [5:20] == oligo [0:15] or primer_revcomp [5:20] == oligo [0:15]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [1:16] or primer_revcomp [5:20] == oligo [1:16]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [2:17] or primer_revcomp [5:20] == oligo [2:17]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [3:18] or primer_revcomp [5:20] == oligo [3:18]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [4:19] or primer_revcomp [5:20] == oligo [4:19]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [5:20] or primer_revcomp [5:20] == oligo [5:20]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [6:21] or primer_revcomp [5:20] == oligo [6:21]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [7:22] or primer_revcomp [5:20] == oligo [7:22]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [8:23] or primer_revcomp [5:20] == oligo [8:23]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [9:24] or primer_revcomp [5:20] == oligo [9:24]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [10:25] or primer_revcomp [5:20] == oligo [10:25]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [11:26] or primer_revcomp [5:20] == oligo [11:26]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [12:27] or primer_revcomp [5:20] == oligo [12:27]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [13:28] or primer_revcomp [5:20] == oligo [13:28]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [14:29] or primer_revcomp [5:20] == oligo [14:29]:
                                    section6 = section6 + 1     
                                if primer [5:20] == oligo [15:30] or primer_revcomp [5:20] == oligo [15:30]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [16:31] or primer_revcomp [5:20] == oligo [16:31]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [17:32] or primer_revcomp [5:20] == oligo [17:32]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [18:33] or primer_revcomp [5:20] == oligo [18:33]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [19:34] or primer_revcomp [5:20] == oligo [19:34]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [20:35] or primer_revcomp [5:20] == oligo [20:35]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [21:36] or primer_revcomp [5:20] == oligo [21:36]:
                                    section6 = section6 + 1   
                                if primer [5:20] == oligo [22:37] or primer_revcomp [5:20] == oligo [22:37]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [23:38] or primer_revcomp [5:20] == oligo [23:38]:
                                    section6 = section6 + 1  
                                if primer [5:20] == oligo [24:39] or primer_revcomp [5:20] == oligo [24:39]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [25:40] or primer_revcomp [5:20] == oligo [25:40]:
                                    section6 = section6 + 1       
                                if primer [5:20] == oligo [26:41] or primer_revcomp [5:20] == oligo [26:41]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [27:42] or primer_revcomp [5:20] == oligo [27:42]:
                                    section6 = section6 + 1           
                                if primer [5:20] == oligo [28:43] or primer_revcomp [5:20] == oligo [28:43]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [29:44] or primer_revcomp [5:20] == oligo [29:44]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [30:45] or primer_revcomp [5:20] == oligo [30:45]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [31:46] or primer_revcomp [5:20] == oligo [31:46]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [32:47] or primer_revcomp [5:20] == oligo [32:47]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [33:48] or primer_revcomp [5:20] == oligo [33:48]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [34:49] or primer_revcomp [5:20] == oligo [34:49]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [35:50] or primer_revcomp [5:20] == oligo [35:50]:
                                    section6 = section6 + 1
                                if primer [5:20] == oligo [36:51] or primer_revcomp [5:20] == oligo [36:51]:
                                    section6 = section6 + 1
                                if section6 !=0:
                                    print "erg"
                                    bad_primer.write(str(name))
                                    bad_primer.write("\n")
                                    bad_primer.write(i)
                                    bad_primer.write("\n")
                                    break
                                if section6 == 0:
                                    #Section 7
                                    #Comapring Primer 6-21        
                                    if primer [6:21] == oligo [0:15] or primer_revcomp [6:21] == oligo [0:15]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [1:16] or primer_revcomp [6:21] == oligo [1:16]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [2:17] or primer_revcomp [6:21] == oligo [2:17]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [3:18] or primer_revcomp [6:21] == oligo [3:18]:
                                        section7 = section7 + 1   
                                    if primer [5:20] == oligo [4:19] or primer_revcomp [6:21] == oligo [4:19]:
                                        section7 = section7 + 1  
                                    if primer [5:20] == oligo [5:20] or primer_revcomp [6:21] == oligo [5:20]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [6:21] or primer_revcomp [6:21] == oligo [6:21]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [7:22] or primer_revcomp [6:21] == oligo [7:22]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [8:23] or primer_revcomp [6:21] == oligo [8:23]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [9:24] or primer_revcomp [6:21] == oligo [9:24]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [10:25] or primer_revcomp [6:21] == oligo [10:25]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [11:26] or primer_revcomp [6:21] == oligo [11:26]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [12:27] or primer_revcomp [6:21] == oligo [12:27]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [13:28] or primer_revcomp [6:21] == oligo [13:28]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [14:29] or primer_revcomp [6:21] == oligo [14:29]:
                                        section7 = section7 + 1     
                                    if primer [5:20] == oligo [15:30] or primer_revcomp [6:21] == oligo [15:30]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [16:31] or primer_revcomp [6:21] == oligo [16:31]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [17:32] or primer_revcomp [6:21] == oligo [17:32]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [18:33] or primer_revcomp [6:21] == oligo [18:33]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [19:34] or primer_revcomp [6:21] == oligo [19:34]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [20:35] or primer_revcomp [6:21] == oligo [20:35]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [21:36] or primer_revcomp [6:21] == oligo [21:36]:
                                        section7 = section7 + 1 
                                    if primer [5:20] == oligo [22:37] or primer_revcomp [6:21] == oligo [22:37]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [23:38] or primer_revcomp [6:21] == oligo [23:38]:
                                        section7 = section7 + 1      
                                    if primer [5:20] == oligo [24:39] or primer_revcomp [6:21] == oligo [24:39]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [25:40] or primer_revcomp [6:21] == oligo [25:40]:
                                        section7 = section7 + 1           
                                    if primer [5:20] == oligo [26:41] or primer_revcomp [6:21] == oligo [26:41]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [27:42] or primer_revcomp [6:21] == oligo [27:42]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [28:43] or primer_revcomp [6:21] == oligo [28:43]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [29:44] or primer_revcomp [6:21] == oligo [29:44]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [30:45] or primer_revcomp [6:21] == oligo [30:45]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [31:46] or primer_revcomp [6:21] == oligo [31:46]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [32:47] or primer_revcomp [6:21] == oligo [32:47]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [33:48] or primer_revcomp [6:21] == oligo [33:48]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [34:49] or primer_revcomp [6:21] == oligo [34:49]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [35:50] or primer_revcomp [6:21] == oligo [35:50]:
                                        section7 = section7 + 1
                                    if primer [5:20] == oligo [36:51] or primer_revcomp [6:21] == oligo [36:51]:
                                        section7 = section7 + 1
                                    if count == number_oligo:
                                        if section7 !=0:
                                            print "erg"
                                            bad_primer.write(str(name))
                                            bad_primer.write("\n")
                                            bad_primer.write(i)
                                            #bad_primer.write("\n")
                                            break
                                        if section7 ==0:
                                             print name 
                                             count = 0
                                             section1 = 0
                                             section2 = 0                        
                                             section3 = 0
                                             section4 = 0
                                             section5 = 0
                                             section6 = 0
                                             section7 = 0
                                             good_primer.write(str(name))
                                             good_primer.write("\n")
                                             good_primer.write(i)
                                             #good_primer.write("\n")
                                        else:
                                            count = 0
                                            section1 = 0
                                            section2 = 0                        
                                            section3 = 0
                                            section4 = 0
                                            section5 = 0
                                            section6 = 0
                                            section7 = 0
                                            print "BAD PRIMER =%s" % name


# only use primer that remove frist 4 primer 
# output calculate tm
# select for C or G forward              

            