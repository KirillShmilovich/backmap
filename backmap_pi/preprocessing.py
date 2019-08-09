"""
preprocessing.py
Functions for preprocessing files
"""

def load(f_name=True):
    """
    Function that reads in trajectory. Should take a .gro file as input, read
    in all the lines and return relevant quantities

    Parameters
    ----------
    f_name : str, 
        Name of file to load

    Returns
    -------
    xyz : np.array,
        Array with shape (n_atoms, 3) of x,y,z positions of all the atoms
    """