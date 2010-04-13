#Copyright (c) 2010 Erik Tollerud (etolleru@uci.edu) 

major = 0
minor = 1
dev = True
release = not dev

version = str(major)+'.'+str(minor)+('.dev' if dev else '')


def get_repo_revision():
    """
    Returns the bzr revision number.
    
    :returns: The revision number
    :rtype: int
    
    :except ValueError: If this is a release version
    :except IOError: If the .bzr directory or info files cannot be found 
    """
    import os
    from os import path

    if release:
        raise ValueError('revsion number not valid for release')
    bzrdir = path.join(path.split(__file__)[0],'..','.bzr')
    if not path.exists(bzrdir):
        raise IOError('.bzr directory does not exist, cannot get revision')
    
    lrevfn = path.join(bzrdir,'branch','last-revision')
    if not path.exists(lrevfn):
        raise IOError('last-revision file does not exist, cannot get revision')
        
    with open(lrevfn) as f:
        s = f.read()
        
    return int(s.split()[0])
    
