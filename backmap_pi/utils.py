import numpy as np
import re

def get_molecule_inds(Gro, Itps):
    molecules = list()
    for Itp in Itps:
        molecule_inds = list()
        for ind in range(Gro.n_atoms - Itp.n_atoms + 1):
            if (Gro.top[ind:ind + Itp.n_atoms]==Itp.top).all():
                molecule_inds.append([ind, ind+Itp.n_atoms])
        molecules.append(molecule_inds)
    return np.asarray(molecules)

def load_file(f_name):
    line_list = list()
    with open(f_name) as f:
        for line in f:
            line_list.append(line.split())
    return line_list

def parse_itp(f_name):
    itp = list()
    lines = load_file(f_name)
    atoms_flag = 0
    for line in lines:
        if atoms_flag and ("[" in line) and ("]" in line):
            break
        if atoms_flag and len(line)>0 and line[0]!=";":
            itp.append(line[1:5])
        if line==["[","atoms","]"]:
            atoms_flag = 1 
    return np.array(itp)

def parse_gro(f_name):
    lines = load_file(f_name)
    gro = list()
    for line in lines[2:-1]:
        res_id,res_name = re.findall(r'[A-Za-z]+|\d+', line[0])
        bead_name  = line[1]
        x, y, z = line[3], line[4], line[5]
        gro.append([res_id, res_name, bead_name, x, y, z])
    return np.asarray(gro)