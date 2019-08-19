# """
# preprocessing.py
# Functions for preprocessing files
# """


# # DEFINITIONS

# #AminoAcids = "ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR ACE NH2".split()
# #peptide_chain = list(AminoAcids)

# # GETTING AN ARRAY FROM GRO FILE

# def load(f_name):
#     """
#     Function that reads in trajectory. Should take a .gro file as input, read
#     in all the lines and return relevant quantities

#     Parameters
#     ----------
#     f_name : str, 
#         Name of file to load

#     Returns
#     -------
#     xyz : np.array,
#         Array with shape (n_atoms, 3) of x,y,z positions of all the atoms
#         # there are 38487 atoms (96 mols, including waters)
#     """
#     # FUNCTION THAT READS IN TRAJECTORY

#     line_list = list()
#     with open(f_name) as f:
#         for line in f:
#             line_list.append(line.split())
#     return line_list
# #------- trying to write an if statement to differentiate between molecules 
# #        for line in f:
# #            If two elements in last line are 15PAS and SC1, then this line is the first line of a new molecule
# #------- below is something that could be used to do the same thing as above
#    # with open(f_name) as f:
#    #     array = []
#    #     for line in f:
#    #         array.append(line)
# #------- (1) trying to print only certain lines
# #    line_list = list()
# #    with open(f_name) as f:
# #        for line in f:
# #            line_list.append(line.split())
# #            if "BB" in line  # isn't this how you find a phrase?
# #                FoundPhrase = line
# #                break
# #            print(line)
# #    return line_list
# #------- (2) trying to print only certain lines
# #    line_list = list()
# #    with open(f_name) as f:
# #        for i, line in enumerate(f):
# #            if i == 3:
# #                # 3rd line
# #                break
# #    return line_list
# #------- (1) TRYING TO MAKE DICTIONARY FOR FIRST 10 RESIDUES
# #    line_list = list()
# #    with open(f_name) as f:
# #        for line in f:
# #            line_list.append(line.split()
# #            dicts = {
# #            keys = range(10)
# #            values = ["1PAS", "1PAS", "2PHE", "2PHE", "2PHE", "2PHE", "3ALA", "4GLY", "5COA", "6COP"]
# #            for i in keys:
# #                dicts[i] = values[i]
# #            }
# #            print(dicts)
# #    return line_list
# #------- (2) TESTING DICTIONARY FOR FIRST 10 RESIDUES
# #        line_list = list()
# #        with open(f_name) as f:
# #            for line in f:
# #                line_list.append(line.split()
# #                residues = {" ": }
# #                print(residues)
# #        return line_list

# #----- how the dictionary should look
# # 1PAS = {10.202, 1.658, 12.957}
# # 1PAS = {9.903, 1.694, 12.943}
# # 2PHE = {10.312, 1.914, 13.108}
# # ...

# #----- dictionary
# #    dict ={}
# #    For line in f:
# #        arr = []
# #        resname = row[0]    # does this mean the resname for each line is set as the first element in that list? (if each line is a list)
# #        # v1 (x position coordinate), v2 (y position coordinate), v3 (z position coordinate)
    
# #        arr = [v1,v2,v3]
# #        dict.update(resname:arr)

# #----- dictionary
# #    dict = {}
# #    dict[''] = ''
# #    dict[''] = ''

# #----- dictionary
# # lst1 = ["val1", "val2", "val3"]
# # lst2 = ["vala", "valb", "valc"]
# # str_to_array: [String: [String]] = [:]
# # str_to_array["key1"] = lst1
# # print(lst1)

# #------- THING1 this is the function that is specific to DFAG
# def thing1(file_name):   # defining a new function - thing - takes the .gro file as argument
#     rows = load(file_name) # print(rows) after this to make sure it works
#     #print(rows)
#     allmols = []   # these three are empty to start
#     mol = []
#     bead = []
#     count = 2   # tells you where you're starting
#     for _ in range (96):     # for one of the molecules
#         for _ in range (29):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             bead = rows[count]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(bead)     # adding the new res to mol
#             count += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#         #print(allmols[0])   # this prints the first molecule (so 29 rows)
#         #print(allmols[0][0])    # this prints the first row in the  first molecule 
#         #print(allmols[0][0][0]) # this prints the first item in the first row of the first molecule -- 1PAS
#     print(allmols[0])      # this is the desired output - list of all the molecules made up of smaller lists each with lists of the items in each row in that molecule
#     return allmols  

# # ^^ this needs to be made generalizable to all .gro files for these molecules (not just 96 moles and not specifically 29 rows per molecule)
# # see thing3 for the generalizable version

# #-------






# #------- THING2 (a test of thing1) --> NOT USING THIS
# def thing2(file_name):
#     rows = load(file_name)
#     allmols = []
#     mol = []
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues
#     # print(rows[2])             # [2] prints the first residue line and every number after 2 prints the residue line at that number
#     molcount = 2
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # sadding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             # do i need a continue statement here?
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             #mol = []                # start a new mol list 
#             print(oneresline[firstitem])
#             print(rows[startcount][firstitem])
#             print(oneresline[seconditem])
#             print(rows[startcount][seconditem])
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             allmols.append(mol)
#             return allmols
#         else:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             #allmols.append(mol) # adding this molecule to the list of all molecules
#         #mol = []        # this line is necessary to reinitialize - mol should be empty before each new molecule
# #        residue = []
#     #return allmols
# #        print(len(allmols))
# #        print(allmols[0])
# #    c = len(mol[0])     # c is supposed to be the length of the first molecule (number of rows)
# #    print(c)        # this prints 96 9's
# #    for i in range(0, 2783):
# #        d = len(allmols[i][0])     # d should = 9 --> this will be the length of any row in the .gro
# #        print(allmols[i][0])    # putting the [0] makes it a single list
# #####################
# #       #   ***CODE TO GET RID OF NUMBER BEFORE RESIDUES***
# #        if allmols[i][0][0][1] == allmols[i + 1][0][0][1] and allmols[i][0][0][2] == allmols[i + 1][0][0][2] and allmols[i][0][0][3] == allmols[i + 1][0][0][3]:
# #        # trying to get around disregarding numbers - if the second element in the first item of the row matches the second element in the first item of the next row...
# #            totalresiduelistpermolecule.append(allmols[i][0])    # add the entire line to residuelist
# #        elif allmols[i][0][0][1] == allmols[i + 1][0][0][2] and allmols[i][0][0][2] == allmols[i + 1][0][0][3] and allmols[i][0][0][3] == allmols[i + 1][0][0][4]:
# #            totalresiduelistpermolecule.append(allmols[i][0])    # add the entire line to residuelsit
# #        else:
# #            totalresiduelistpermolecule = []
# #            totalresiduelistpermolecule.append(allmols[0][0])
# #        totalresiduelistpermolecule = []
# #    print(d)       # printing d prints each row of the .gro file as its own list (not all together in a single big list)
# #    numcolumnsperrow = len(allmols[0][0])
# #    print(numcolumnsperrow)     # this prints 9
# #    f = allmols[0][0][0]
# #    print(f)        # this prints 1PAS
# #    print(allmols[0])          
# #    print(allmols[0][0])       
# #    print(allmols[0][0][0])    
# #    return allmols      # ** this DOES NOT return the same thing as thing function

# #-----------




# #------------- THING3 (a test of thing2) --> this is good this is the generalizable function
# def thing3(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     #print(totalfilereslines)        # this prints 2783 with (counttotal - 4) and 2784 with (counttotal - 3) --> lower section won't work unless this prints 2783
#     #print(rows[2])             # [2] prints the first residue line and every number after 2 prints the residue line at that number
#     #print(rows[2][seconditem])
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     #print(mol)          # THIS WORKS THIS PRINTS ONE MOLECULE
#     lengthofonemolecule = len(mol)
#     #print(lengthofonemolecule)
#     allmols.append(mol) # adding this molecule to the list of all molecules
#     #print(allmols)      # all mols only has the one molecule now
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     #print(numofmoleculesinfile)
#     #print(startcount)
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#         #print(allmols[0])   # this prints the first molecule (so 29 rows)
#         #print(allmols[0][0])    # this prints the first row in the  first molecule 
#         #print(allmols[0][0][0]) # this prints the first item in the first row of the first molecule -- 1PAS
#     #    print(allmols[0][0][0])
#     print(allmols[0])       # this prints the list for the first molecule (contains 29 lists of beads)
#     return allmols



# #-------- THING 4 -- TEST COPY of THING 3----------#
# def thing4(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     groupresiduetype = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     allmols.append(mol) # adding this molecule to the list of all molecules
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []                # start with empty list
#     allmols = []            # start with empty list
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for i in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             # THE RANGE ABOVE STARTS AT 0 -- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
#             oneresline = rows[startcount]       # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             if len(mol) == 0 and allmols[0][i][0][-3:] == allmols[0][i + 1][0][-3:]:        # this may be the case for the first bead (residue line) of the molecule       
#                 groupresiduetype.append(oneresline)
#                 mol.append(oneresline)     # adding the new res to mol
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(mol)>1 and allmols[0][i][0][-3:] == allmols[0][i - 1][0][-3:] or allmols[0][i][0][-3:] == allmols[0][lengthofonemolecule - (i + 1)][0][-3:]:
#                 groupresiduetype.append(oneresline)
#                 mol.append(oneresline)     # adding the new res to mol
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(mol)>1 and allmols[0][i][0][-3:] != allmols[0][i - 1][0][-3:]: 
#                 break   ## not break but you have to find a way to start the next residue group
#             elif len(mol)>1 and allmols[0][i][0][-3:] == allmols[0][i - 1][0][-3:]:
#                 groupresiduetype.append(oneresline)
#                 mol.append(oneresline)     # adding the new res to mol
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(mol) == lengthofonemolecule:
#                 break
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#         #print(allmols[0][17][0][-3:])       # this prints only the last 3 characters of the first item in the string for each row (the residue name)
#         print(groupresiduetype)
#     return allmols




# #------------- THING5 ---- TEST COPY of THING3
# def thing5(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     #print(lengthofonemolecule)      # this prints 29
#     allmols.append(mol) # adding this molecule to the list of all molecules
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
# #    print(allmols[0][0][0][0])       # this prints the list for the first molecule (contains 29 lists of beads)
# #    print(len(allmols[0]))      # this prints 29
#     #print(lengthofonemolecule)
# ##############
#     startcount = 2
#     groupresiduetype = []
#     backcount = 1
# #    #print(rows[2])      # this prints the list for the first residue's bead
#     #print(lengthofonemolecule)         # prints 29
#     for _ in allmols:       # for a molecule in allmols
#         #print(allmols[0][0])       # this prints the list of the first bead in the first molecule
#         #print(allmols[0][0][0])
#         for i in range(lengthofonemolecule):        # for a bead in one molecule -- lengthofonemolecule = 29
#             #print(len(allmols[0]))
#             oneresline = rows[startcount]
#             #print(allmols[0][0][0][-3:])        # this prints PAS
#             # print(allmols[0][i][0][-3:])      # prints all the residue names for one molecule (no numbers in front)
#             if i == 0 and allmols[0][i][0][-3:] == allmols[0][i + 1][0][-3:]:  # this is helpful for the first line of the molecule
#                 groupresiduetype.append(oneresline)
#             #    mol.append(oneresline)     # adding the new res to mol
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif i > 0 and allmols[0][i][0][-3:] == allmols[0][i - backcount][0][-3:] and allmols[0][i][1] != allmols[0][i - backcount][1]:
#                 groupresiduetype.append(oneresline)
#             #    mol.append(oneresline)     # adding the new res to mol
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 backcount += 1
#                 continue
#             elif i > 0 and allmols[0][i][0][-3:] != allmols[0][i - backcount][0][-3:]:
#             #    groupresiduetype.append(oneresline)
#                 startcount += 1 
#                 backcount += 1
#                 continue 
#             elif i > 0 and allmols[0][i][0][-3:] == allmols[0][i - backcount][0][-3:] and allmols[0][i][0] != allmols[0][i - backcount][0]:
#                 groupresiduetype.append(oneresline)
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 backcount += 1
#                 continue
#             elif i > 0 and allmols[0][i][0] == allmols[0][i - backcount][0] and allmols[0][i][1] == allmols[0][i - backcount][1]:      # this would run when you've reached the first line of the next molecule
#                 break
#         backcount = []
#         groupresiduetype = []       # right now this should only give you an array with 4 PAS beads for each molecule
#         #allmols.append(mol) # adding this molecule to the list of all molecules
#         #mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     print(groupresiduetype)     # this should now print the 4 PAS beads for each molecule
#     # still need to get it to go back and start collecting the next residue for the same molecule
#     return allmols

# #-----


# #            elif len(mol)>1 and allmols[0][i][0][-3:] != allmols[0][i - 1][0][-3:] and #that residue is not already present in the beads up until that residue line: 
# #                break   ## not break but you have to find a way to start the next residue group
# #            elif allmols[0][i][0][-3:] == allmols[0][lengthofonemolecule - (i + 1)][0][-3:]:
# #                groupresiduetype.append(oneresline)
# #            #    mol.append(oneresline)     # adding the new res to mol
# #                startcount += 1      # increasing the count by one as you go to the next row
# #                continue
# #            elif len(mol)>1 and allmols[0][i][0][-3:] != allmols[0][i - 1][0][-3:]: 
# #                break   ## not break but you have to find a way to start the next residue group


# #_____________ THING 6 --- TEST COPY of THING 3 __________________#
# def thing6(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     #print(lengthofonemolecule)      # this prints 29
#     allmols.append(mol) # adding this molecule to the list of all molecules
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
# #    print(allmols[0][0][0][0])       # this prints the list for the first molecule (contains 29 lists of beads)
# #    print(len(allmols[0]))      # this prints 29
#     #print(lengthofonemolecule)
# ##############
#     startcount = 2
#     groupresiduetype = []
#     backcount = 1
#     oneresline = []
#     #print(rows[2])      # this prints the list for the first residue's bead
#     #print(lengthofonemolecule)         # prints 29
#     for _ in allmols:       # for a molecule in allmols
#         #print(allmols[0][0])       # this prints the list of the first bead in the first molecule
#         #print(allmols[0][0][0])
#         for i in range(lengthofonemolecule):        # for a bead in one molecule -- lengthofonemolecule = 29
#             oneresline = rows[startcount]
#             #print(allmols[0][0][0][-3:])        # this prints PAS
#             # print(allmols[0][i][0][-3:])      # prints all the residue names for one molecule (no numbers in front)
#             if len(groupresiduetype) == 0:  # this is helpful for the first line of the molecule -- **this would only work for the first residue group
#                 groupresiduetype.append(oneresline[0][-3:])     # add the residue name (without the number)
#                 groupresiduetype.append(oneresline[1])     # add the bead name
#                 groupresiduetype.append(oneresline[3])     # add the x position
#                 groupresiduetype.append(oneresline[4])     # add the y position
#                 groupresiduetype.append(oneresline[5])     # add the z position
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(groupresiduetype) > 0 and allmols[0][i][0][-3:] == allmols[0][i - backcount][0][-3:] and allmols[0][i][1] != allmols[0][i - backcount][1]:
#                 groupresiduetype.append(oneresline[1])     # add the bead name
#                 groupresiduetype.append(oneresline[3])     # add the x position
#                 groupresiduetype.append(oneresline[4])     # add the y position
#                 groupresiduetype.append(oneresline[5])     # add the z position
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 backcount += 1
#                 continue
#             elif len(groupresiduetype) > 0 and allmols[0][i][0][-3:] != allmols[0][i - backcount][0][-3:]:
#             #    groupresiduetype.append(oneresline)
#                 startcount += 1 
#                 backcount += 1
#                 continue 
#             elif len(groupresiduetype) > 0 and allmols[0][i][0][-3:] == allmols[0][i - backcount][0][-3:] and allmols[0][i][0] != allmols[0][i - backcount][0]:
#                 groupresiduetype.append(oneresline[1])     # add the bead name
#                 groupresiduetype.append(oneresline[3])     # add the x position
#                 groupresiduetype.append(oneresline[4])     # add the y position
#                 groupresiduetype.append(oneresline[5])     # add the z position
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 backcount += 1
#                 continue
#             elif len(groupresiduetype) > 0 and allmols[0][i][0] == allmols[0][i - backcount][0] and allmols[0][i][1] == allmols[0][i - backcount][1]:      # this would run when you've reached the first line of the next molecule
#                 break
#         #startcount += 1
#         #backcount = len(groupresiduetype) + 1
#         #groupresiduetype = []       # right now this should only give you an array with 4 PAS beads for each molecule
#         #allmols.append(mol) # adding this molecule to the list of all molecules
#         #mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     print(groupresiduetype)     # this should now print the 4 PAS beads for each molecule
#     residue = {}
#     # still need to get it to go back and start collecting the next residue for the same molecule
#     return allmols


# #-------------- THING 7 --- test of THING 3 -----------#
# def thing7(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     allmols.append(mol) # adding this molecule to the list of all molecules
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     #print(allmols)
# ##############
#     startcount = 2
#     groupresiduetype = []
#     backcount = 1
#     oneresline = []
#     residue = {}
#     for _ in allmols:       # for a molecule in allmols
#         for bead in range(lengthofonemolecule):        # for a bead in one molecule -- lengthofonemolecule = 29
#             oneresline = rows[startcount]
#             if len(groupresiduetype) == 0:  # this is helpful for the first line of the molecule -- **this would only work for the first residue group
#                 groupresiduetype.append(oneresline[0][-3:])     # add the residue name (without the number)
#                 groupresiduetype.append(oneresline[1])     # add the bead name
#                 groupresiduetype.append(oneresline[3])     # add the x position
#                 groupresiduetype.append(oneresline[4])     # add the y position
#                 groupresiduetype.append(oneresline[5])     # add the z position
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(groupresiduetype) > 0 and allmols[0][bead][0][-3:] == allmols[0][bead - 1][0][-3:]:
#                 groupresiduetype.append(oneresline[1])     # add the bead name
#                 groupresiduetype.append(oneresline[3])     # add the x position
#                 groupresiduetype.append(oneresline[4])     # add the y position
#                 groupresiduetype.append(oneresline[5])     # add the z position
#                 startcount += 1      # increasing the count by one as you go to the next row
#                 continue
#             elif len(groupresiduetype) > 0 and allmols[0][bead][0][-3:] != allmols[0][bead - 1][0][-3:]:
#                 break
#         #startcount += 1
#         #backcount = len(groupresiduetype) + 1
#         #groupresiduetype = []       # right now this should only give you an array with 4 PAS beads for each molecule
#         #allmols.append(mol) # adding this molecule to the list of all molecules
#         #mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     print(groupresiduetype)     # this should now print the 4 PAS beads for each molecule
#     # still need to get it to go back and start collecting the next residue for the same molecule
#     return allmols




# #______________ THING 8 ---- TEST of THING 3 ___________#
# def thing8(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     allmols.append(mol) # adding this molecule to the list of all molecules
# ###### the section above is for figuring out how many beads there are in the entire system AND how many beads (residue lines) there are per molecule    ######
# ###### the section below is adding the part from thing1 that creates a list with x lists within it (x stands for the # of molecules) and within each x, there are y lists (y stands for the # of residue lines (beads) per molecule), and each y has 9 items (residue name, bead type, atom #, x position, y position, z position, x velocity, y velocity, z velocity) ######
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     #print(allmols)
# ##############
#     startcount = 2
#     residue = []    # residue means all the bead lines for a single residue
#     oneresline = []
#     residuedict = {}
#     for _ in allmols:       # the space indicates 1 molecule --> for 1 molecule in allmols
#         for bead in range(lengthofonemolecule):
#             oneresline = rows[startcount]
#             if len(residue) == 0:
#                 residue.append(oneresline[bead])   # add the residue name to the residue list
#                 residuedict[allmols[0][bead][1]] = [allmols[0][bead][3], allmols[0][bead][4], allmols[0][bead][5]]
#                 residuename = allmols[0][bead][0]
#                 print(str(residuename))
#                 #print(residue)
#                 print(residuedict)
#             #    print(allmols[0][bead][0])
#                 startcount += 1
#                 continue
#             elif len(residue)>0 and allmols[0][bead][0][-3:] == allmols[0][bead - 1][0][-3:] and allmols[0][bead][0] == allmols[0][bead - 1][0]:
#                 residue.append(oneresline[bead])
#                 residuedict[allmols[0][bead][1]] = [allmols[0][bead][3], allmols[0][bead][4], allmols[0][bead][5]]
#                 residuename = allmols[0][bead][0]
#                 print(str(residuename))
#                 #print(residue)
#                 print(residuedict)
#             #    print(allmols[0][bead][0])
#                 startcount += 1
#                 continue
#             elif len(residue)>0 and allmols[0][bead][0][-3:] != allmols[0][bead - 1][0][-3:] and allmols[0][bead][0][-3:] == allmols[0][bead + 1][0][-3:]:
#                 print(residuedict)
#                 residue = []
#                 residue.append(oneresline[bead])
#                 residuedict[allmols[0][bead][1]] = [allmols[0][bead][3], allmols[0][bead][4], allmols[0][bead][5]]
#                 residuename = allmols[0][bead][0]
#                 print(str(residuename))
#                 #print(residue)
#                 print(residuedict)                 # possibly get rid of 
#             #    print(allmols[0][bead - 1][0])     # possibly get rid of
#                 startcount += 1
#                 continue
#             elif len(residue)>0 and allmols[0][bead][0][-3:] == allmols[0][bead - 1][0][-3:] and allmols[0][bead][0] != allmols[0][bead - 1][0]:
#                 print(residuedict)
#                 residue = []
#                 residue.append(oneresline[bead])
#                 residuedict[allmols[0][bead][1]] = [allmols[0][bead][3], allmols[0][bead][4], allmols[0][bead][5]]
#                 residuename = allmols[0][bead][0]
#                 print(str(residuename))
#                 #print(residue)
#                 print(residuedict)
#             #    print(allmols[0][bead - 1][0])
#                 startcount += 1
#                 continue
#             elif len(residue)>0 and allmols[0][bead][0][-3:] != allmols[0][bead - 1][0][-3:] and allmols[0][bead][0][-3:] != allmols[0][bead + 1][0][-3:]:
#                 print(residuedict)
#                 residue = []
#                 residue.append(oneresline[bead])
#                 residuedict[allmols[0][bead][1]] = [allmols[0][bead][3], allmols[0][bead][4], allmols[0][bead][5]]
#                 residuename = allmols[0][bead][0]
#                 print(str(residuename))
#                 #print(residue)
#                 print(residuedict)
#             #    print(allmols[0][bead - 1][0])
#                 startcount += 1
#                 continue
#         #print(residue)
#         #print(allmols[0][bead - 1][0])
#         #print(residuedict)
#     return allmols



#     ##################################### change stuff under here
# #            for bead in range(0, lengthofonemolecule - len(residue)): ### change all the bead variable names here
# #                oneresline = rows[startcount]
# #                if len(residue) == 0:
# #                    residuedict["allmols[0][bead][1]"] = ["allmols[0][bead][3]", "allmols[0][bead][4]", "allmols[0][bead][5]"]
# #                    allmols[0][bead][0] = residuedict["allmols[0][bead][1]"]    # I want this to be renaming the dictionary the name of the residue
# #                    startcount += 1
# #                    # create dictionary with the name of the string located at allmols[0][i][0]
# #                    # make a key for that dictionary with the name being the string located at allmols[0][i][1] and the 
# #                    # value for that key a list of the three strings located at allmols[0][i][3] , allmols[0][i][4] , and allmols[0][i][5]
# #                    continue 
# #                elif len(residue) != 0 and allmols[0][bead][0][-3:] == allmols[0][bead - 1][0][-3:]:
# #                    residuedict["allmols[0][bead][1]"] = ["allmols[0][bead][3]", "allmols[0][bead][4]", "allmols[0][bead][5]"]
# #                    allmols[0][bead][0] = residuedict["allmols[0][bead][1]"]    # I want this to be renaming the dictionary the name of the residue
# #                    startcount += 1
# #                    # make a key for the same dictionary just created with the name being the string located at allmols[0][i][1] and the 
# #                    # value for that key a list of the three strings located at allmols[0][i][3] , allmols[0][i][4] , and allmols[0][i][5]
# #                    continue 
# #                elif len(residue) != 0 and allmols[0][bead][0][-3:] != allmols[0][bead - 1][0][-3:] and allmols[0][bead][0][-3:] == allmols[0][bead + 1][0][-3:]:
# #                    # create a new dictionary with the name of the string located at allmols[0][i][0]
# #                    # make a key for that dictionary with the name being the string located at allmols[0][i][1] and the 
# #                    # value for that key a list of the three strings located at allmols[0][i][3] , allmols[0][i][4] , and allmols[0][i][5]
# #                    startcount += 1
# #                    break 
# #                elif len(residue) != 0 and allmols[0][bead][0][-3:] != allmols[0][bead - 1][0][-3:] and allmols[0][bead][0][-3:] != allmols[0][bead + 1][0][-3:]:
# #                    # create a new dictionary with the name of the string located at allmols[0][i][0]
# #                    # make a key for that dictionary with the name being the string located at allmols[0][i][1] and the 
# #                    # value for that key a list of the three strings located at allmols[0][i][3] , allmols[0][i][4] , and allmols[0][i][5]
# #                    # THIS IS THE ONE FOR RESIDUES WITH ONLY ONE BEAD
# #                    startcount += 1
# #                    break
# #            # the dictionary you have right before it empties has all the beads for that residue
# #            print(residuedict)
# #            residue.append(len(_______))
# #            residue = []
# #            residuedict = {}            # dictionary empties 
# #    return allmols



# ###############
# #    for _ in allmols:       # for a molecule in allmols
# #        for i in range(lengthofonemolecule):        # for a bead in one molecule -- lengthofonemolecule = 29
# #            oneresline = rows[startcount]
# #            if len(groupresiduetype) == 0:  # this is helpful for the first line of the molecule -- **this would only work for the first residue group
# #                groupresiduetype.append(oneresline[0][-3:])     # add the residue name (without the number)
# #                groupresiduetype.append(oneresline[1])     # add the bead name
# #                groupresiduetype.append(oneresline[3])     # add the x position
# #                groupresiduetype.append(oneresline[4])     # add the y position
# #                groupresiduetype.append(oneresline[5])     # add the z position
# #                startcount += 1      # increasing the count by one as you go to the next row
# #                continue
# #            elif len(groupresiduetype) > 0 and allmols[0][i][0][-3:] == allmols[0][i - 1][0][-3:]:
# #                groupresiduetype.append(oneresline[1])     # add the bead name
# #                groupresiduetype.append(oneresline[4])     # add the y position
# #                groupresiduetype.append(oneresline[5])     # add the z position
# #                startcount += 1      # increasing the count by one as you go to the next row
# #                continue
# #            elif len(groupresiduetype) > 0 and allmols[0][i][0][-3:] != allmols[0][i - 1][0][-3:]:
# #                break
#         #startcount += 1
#         #backcount = len(groupresiduetype) + 1
#         #groupresiduetype = []       # right now this should only give you an array with 4 PAS beads for each molecule
#         #allmols.append(mol) # adding this molecule to the list of all molecules
#         #mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
# #    print(groupresiduetype)     # this should now print the 4 PAS beads for each molecule
#     # still need to get it to go back and start collecting the next residue for the same molecule
# #    return allmols




# #_______________________ THING 9 ---- THIS IS IT ------ _________________________#
# def thing9(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     totalresiduelistpermolecule = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     allmols.append(mol) # adding this molecule to the list of all molecules
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []
#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule
#     #print(allmols)
# ########### code below makes nested dictionaries for each residue for each molecule, but each dictionary only keeps the last bead key (not all of them) ############

# ########## Kirill's below
#     # #count = 0
#     # system = list()
#     # for molecule in allmols:           # for a list of all the bead lists in one of the molecules
#     #     molecule_dict = dict()      # creates new molecule dictionaries (molecule_dict_1, molecule_dict_2, etc.)
#     #     #count = 0
#     #     for bead_iter,line in enumerate(molecule):
#     #         res_name = line[0][-3:] + "_" + line[0][:-3]
#     #         bead_name  = line[1]
#     #         x,y,z = float(line[3]),float(line[4]),float(line[5])
#     #         if res_name in molecule_dict.keys():
#     #             molecule_dict[res_name][bead_name+"_"+str(bead_iter)] = [x,y,z]
#     #         elif res_name not in molecule_dict.keys():
#     #             molecule_dict[res_name] = dict()
#     #             molecule_dict[res_name][bead_name+"_"+str(bead_iter)] = [x,y,z]
#     #     system.append(molecule_dict)
#     # return system
# ################## mine below #############
#         for molecule in allmols:
#             molecule_dict = dict()
#             total_beads_in_residue_list = []
#             for residue_line in molecule:
#                 #print(residue_line[0])              # this prints the residue name
#                 #count = 0
#                 if len(total_beads_in_residue_list) == 0:
#                     molecule_dict[residue_line[0]] = dict()             # make the residue name a key in the dictionary
#                     molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]       # make the bead name a key in the dictionary with the value [x position, y position, z position]
#                     total_beads_in_residue_list.append(residue_line[0])     # here you know you're appending the residue name not the bead name so you can reference it later
#                     #print(total_beads_in_residue_list[0])
#                     #print(total_beads_in_residue_list)
#                     #print(molecule_dict)
#                 elif len(total_beads_in_residue_list) != 0 and residue_line[0] == total_beads_in_residue_list[0]:
#                     molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]
#                     total_beads_in_residue_list.append(residue_line[0])
#                     #count += 1
#                     #print(molecule_dict)
#                 elif len(total_beads_in_residue_list) != 0 and residue_line[0] != total_beads_in_residue_list[0]:
#                     total_beads_in_residue_list = []
#                     molecule_dict[residue_line[0]] = dict()             # make the bead name a key in the dictionary
#                     molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]
#                     total_beads_in_residue_list.append(residue_line[0])
#                     #count = 0
#         print(molecule_dict)
#     return molecule


# # #________________ THING 10 -- final preprocessing script -- Kirill code at end _____________#
# def load(f_name):
#     line_list = list()
#     with open(f_name) as f:
#         for line in f:
#             line_list.append(line.split())
#     return line_list

# def thing10(file_name):
#     rows = load(file_name)
#     allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
#     mol = []            # list containing residue lines for an individual molecule
#     oneresline = []
#     startcount = 2  # first row with a residue in .gro file
#     firstitem = 0       # first item in a row
#     seconditem = 1       # second item in a row
#     counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
#     totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
   
#     for _ in range(totalfilereslines):       
#         oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#         if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#             continue
#         elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
#             continue
#         elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
#             break
#     lengthofonemolecule = len(mol)
#     allmols.append(mol) # adding this molecule to the list of all molecules
#     numofmoleculesinfile = totalfilereslines/lengthofonemolecule
#     startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
#     mol = []
#     allmols = []

#     for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
#         for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
#             oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
#             mol.append(oneresline)     # adding the new res to mol
#             startcount += 1      # increasing the count by one as you go to the next row
#         allmols.append(mol) # adding this molecule to the list of all molecules
#         mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule

#     system = list()
#     for molecule in allmols:           # for a list of all the bead lists in one of the molecules
#         molecule_dict = dict()      # creates new molecule dictionaries (molecule_dict_1, molecule_dict_2, etc.)
#         for bead_iter,line in enumerate(molecule):
#             res_name = line[0][-3:] + "_" + line[0][:-3]
#             bead_name  = line[1]
#             x,y,z = float(line[3]),float(line[4]),float(line[5])
#             if res_name in molecule_dict.keys():
#                 molecule_dict[res_name][bead_name+"_"+str(bead_iter)] = [x,y,z]
#             elif res_name not in molecule_dict.keys():
#                 molecule_dict[res_name] = dict()
#                 molecule_dict[res_name][bead_name+"_"+str(bead_iter)] = [x,y,z]
#         system.append(molecule_dict)
#         print(molecule_dict)
#     return system


#________________ THING 11 -- final preprocessing script -- Olivia code at end _____________#

# this function loads the .gro file for the system
def load(f_name):
    line_list = list()
    with open(f_name) as f:
        for line in f:
            line_list.append(line.split())
    return line_list

def thing11(file_name):
    rows = load(file_name)
    allmols = []        # this is going to be a list containing lists of all the molecules (with their residue lines)
    mol = []            # list containing residue lines for an individual molecule
    oneresline = []
    startcount = 2  # first row with a residue in .gro file
    firstitem = 0       # first item in a row
    seconditem = 1       # second item in a row
    counttotal = len(open(file_name).readlines())       # counttotal is equal to the total number of lines in the .gro file
    totalfilereslines = counttotal - 3                  # totalfilereslines is equal to the total number of lines in the .gro file with residues (2787 for DFAG)
   
    for _ in range(totalfilereslines):       
        oneresline = rows[startcount]            # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
        if oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:    # if the first two terms are not the same as those in row 2....
            mol.append(oneresline)     # adding the new res to mol
            startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
            continue
        elif oneresline[firstitem] == rows[2][firstitem] and oneresline[seconditem] != rows[2][seconditem]:
            mol.append(oneresline)     # adding the new res to mol
            startcount += 1      # increasing the count by one as you go to the next row
            continue
        elif len(mol) == 0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
            mol.append(oneresline)     # adding the new res to mol
            startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
            continue
        elif oneresline[firstitem] != rows[2][firstitem] and oneresline[seconditem] == rows[2][seconditem]:
            mol.append(oneresline)     # adding the new res to mol
            startcount += 1      # increasing the count by one as you go to the next row (count starts at 2)
            continue
        elif len(mol)>0 and oneresline[firstitem] == rows[startcount][firstitem] and oneresline[seconditem] == rows[startcount][seconditem]:
            break
    lengthofonemolecule = len(mol)
    allmols.append(mol) # adding this molecule to the list of all molecules
    numofmoleculesinfile = totalfilereslines/lengthofonemolecule
    startcount = 2                  # you need this to make startcount 2 again bc the last for loop increased the #
    mol = []
    allmols = []

    for _ in range (int(numofmoleculesinfile)):     # for one of the molecules
        for _ in range (lengthofonemolecule):    # for each residue within a molecule (b/c each molecule is 29 lines)
            oneresline = rows[startcount]   # the residue equals the value of rows at the number count represents --> rows[2] is the third line of .gro
            mol.append(oneresline)     # adding the new res to mol
            startcount += 1      # increasing the count by one as you go to the next row
        allmols.append(mol) # adding this molecule to the list of all molecules
        mol = []    # this line is necessary to reinitialize - mol should be empty before each new molecule

    for molecule in allmols:
        molecule_dict = dict()
        total_beads_in_residue_list = []
        res_count = 0 
        for residue_line in molecule:
            res_name = residue_line[0][-3:] + "_" + residue_line[0][:-3]
            bead_name = residue_line[1]
            x,y,z = float(residue_line[3]),float(residue_line[4]),float(residue_line[5])
            if len(total_beads_in_residue_list) == 0:
                molecule_dict[res_name] = dict()             # make the residue name a key in the dictionary
                molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]       # make the bead name a key in the dictionary with the value [x position, y position, z position]
                total_beads_in_residue_list.append(residue_line[0])     # here you know you're appending the residue name not the bead name so you can reference it later
                res_count += 1
                #print(total_beads_in_residue_list[0])
                #print(total_beads_in_residue_list)
                #print(molecule_dict)
            elif len(total_beads_in_residue_list) != 0 and residue_line[0] == total_beads_in_residue_list[0]:
                molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]
                total_beads_in_residue_list.append(residue_line[0])
                res_count += 1
                #count += 1
                #print(molecule_dict)
            elif len(total_beads_in_residue_list) != 0 and residue_line[0] != total_beads_in_residue_list[0]:
                total_beads_in_residue_list = []
                molecule_dict[res_name] = dict()             # make the bead name a key in the dictionary
                molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]
                total_beads_in_residue_list.append(residue_line[0])
                res_count += 1
                #count = 0
        print(molecule_dict)
    return molecule

#### alternate final block of olivias code -- no added numbering system for residues and beads
    # for molecule in allmols:
    #     molecule_dict = dict()
    #     total_beads_in_residue_list = []
    #     for residue_line in molecule:
    #         #print(residue_line[0])              # this prints the residue name
    #         #count = 0
    #         if len(total_beads_in_residue_list) == 0:
    #             molecule_dict[residue_line[0]] = dict()             # make the residue name a key in the dictionary
    #             molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]       # make the bead name a key in the dictionary with the value [x position, y position, z position]
    #             total_beads_in_residue_list.append(residue_line[0])     # here you know you're appending the residue name not the bead name so you can reference it later
    #             #print(total_beads_in_residue_list[0])
    #             #print(total_beads_in_residue_list)
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] == total_beads_in_residue_list[0]:
    #             molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             #count += 1
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] != total_beads_in_residue_list[0]:
    #             total_beads_in_residue_list = []
    #             molecule_dict[residue_line[0]] = dict()             # make the bead name a key in the dictionary
    #             molecule_dict[residue_line[0]][residue_line[1]] = [float(residue_line[3]), float(residue_line[4]), float(residue_line[5])]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             #count = 0
    #     print(molecule_dict)
    # return molecule

############## - alternate final block of Olivia's code above -- numbering system for residues AND res_count numbering for beads --> numbers beads in a molecule 0-28 -- this block is in the final code for olivia
    # for molecule in allmols:
    #     molecule_dict = dict()
    #     total_beads_in_residue_list = []
    #     res_count = 0 
    #     for residue_line in molecule:
    #         res_name = residue_line[0][-3:] + "_" + residue_line[0][:-3]
    #         bead_name = residue_line[1]
    #         x,y,z = float(residue_line[3]),float(residue_line[4]),float(residue_line[5])
    #         bead_number = residue_line[2]
    #         if len(total_beads_in_residue_list) == 0:
    #             molecule_dict[res_name] = dict()             # make the residue name a key in the dictionary
    #             molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]       # make the bead name a key in the dictionary with the value [x position, y position, z position]
    #             total_beads_in_residue_list.append(residue_line[0])     # here you know you're appending the residue name not the bead name so you can reference it later
    #             res_count += 1
    #             #print(total_beads_in_residue_list[0])
    #             #print(total_beads_in_residue_list)
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] == total_beads_in_residue_list[0]:
    #             molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             res_count += 1
    #             #count += 1
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] != total_beads_in_residue_list[0]:
    #             total_beads_in_residue_list = []
    #             molecule_dict[res_name] = dict()             # make the bead name a key in the dictionary
    #             molecule_dict[res_name][bead_name+"_"+str(res_count)] = [x,y,z]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             res_count += 1
    #             #count = 0
    #     print(molecule_dict)
    # return molecule

####### - alternate final block of olivias code - numbering system for residues AND bead_number system used to name beads 0-2784 for all beads in the entire system (not the best system) -- better system is the block above
    # for molecule in allmols:
    #     molecule_dict = dict()
    #     total_beads_in_residue_list = [] 
    #     for residue_line in molecule:
    #         res_name = residue_line[0][-3:] + "_" + residue_line[0][:-3]
    #         bead_name = residue_line[1]
    #         x,y,z = float(residue_line[3]),float(residue_line[4]),float(residue_line[5])
    #         bead_number = residue_line[2]
    #         if len(total_beads_in_residue_list) == 0:
    #             molecule_dict[res_name] = dict()             # make the residue name a key in the dictionary
    #             molecule_dict[res_name][bead_name+"_"+str(bead_name)] = [x,y,z]       # make the bead name a key in the dictionary with the value [x position, y position, z position]
    #             total_beads_in_residue_list.append(residue_line[0])     # here you know you're appending the residue name not the bead name so you can reference it later
    #             #print(total_beads_in_residue_list[0])
    #             #print(total_beads_in_residue_list)
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] == total_beads_in_residue_list[0]:
    #             molecule_dict[res_name][bead_name+"_"+str(bead_name)] = [x,y,z]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             #count += 1
    #             #print(molecule_dict)
    #         elif len(total_beads_in_residue_list) != 0 and residue_line[0] != total_beads_in_residue_list[0]:
    #             total_beads_in_residue_list = []
    #             molecule_dict[res_name] = dict()             # make the bead name a key in the dictionary
    #             molecule_dict[res_name][bead_name+"_"+str(bead_name)] = [x,y,z]
    #             total_beads_in_residue_list.append(residue_line[0])
    #             #count = 0
    #     print(molecule_dict)
    # return molecule
