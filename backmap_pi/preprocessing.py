# """
# preprocessing.py
# Functions for preprocessing files
# """

#________________ THING 11 -- final preprocessing script -- Olivia's version of code at end _____________#

# this function loads the .gro file for the system

def load(f_name):
    line_list = list()
    with open(f_name) as f:
        for line in f:
            line_list.append(line.split())
    return line_list

# this function creates a dictionary for each of the molecules in the system
#### in each molecule's dictionary, each residue is a key with the value being a dictionary with each bead in that residue as a key
#### the value of each bead key is a list of the x, y, z positions

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

# # #________________ THING 10 -- final preprocessing script -- Kirill's version of code at end _____________#
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




