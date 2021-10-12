# Jwalk (Python 3)

A tool to calculate the **S**olvent **A**ccessible **S**urface **D**istances (**SASD**) between crosslinked residues  
  
This version of Jwalk is simply a modernization of the original invented by the [Topf Lab](https://github.com/Topf-Lab/Jwalk)  
All functionality is original and compatibility has been upgraded for Python 3  
Jwalk works on Linux / MacOS / Windows

## Dependencies
The following can be installed with ```pip```

|          | Package           |
| -------- | ----------------- |
| Required | ```BioPython```   |
| Required | ```numpy```       |
| Required | ```freesasa```    |

## Installation

```
  # Move to cloned directory
  cd Jwalk

  # Run install script
  python setup.py install
```

## Running Jwalk
``` $ jwalk -f 1FGA.pdb```
**Given no optional arguments, Jwalk will find all SASD between all Lys-to-Lys crosslinks in the provided PDB**

## Running Options
```
    -h, --help            show this help message and exit
    -f F                  Input path to .pdb file
    -o O                  Output path for Jwalk results (default: Out to "./Jwalk_results" in the current working
                            directory)
    -xl_list XL_LIST      OPTIONAL: Input path to crosslink list (default: Finds all Lys-to-Lys crosslinks)
    -xl_dist_cutoff XL_DIST_CUTOFF
                            OPTIONAL: Specify maximum crosslink distance cutoff in Angstroms (default: Keeps all
                            distances)
    -aa1 AA1              OPTIONAL: Specify inital crosslink amino acid three letter code (default: LYS)
    -aa2 AA2              OPTIONAL: Specify ending crosslink amino acid three letter code (default: LYS)
    -vox VOX              OPTIONAL: Specify voxel resolution to use in Angstrom (default: 1 Angstrom)
    -ncpus NCPUS          OPTIONAL: Specify number of cpus to use (default: cpu_count())
```

## Input \& Output
Crosslink lists in the ```-xl_list``` input should be pipe delmited:  
```res_num_1|chain_1|res_num_2|chain_2|```

Example of 5 crosslinks between 2 chains:
```
54|A|21|B|
13|A|54|A|
2|B|13|B|
17|B|12|A|
```

If your PDB file does not contain chain identifiers, use \"x\" as the chain"
```
14|x|63|x|
```

Jwalk will create a results directory and place the outputs as follows:
```
./Jwalk_results
 ⎿ inputfile_crosslink_list.txt
 ⎿ inputfile_crosslinks.pdb
```

## Visualization
To visualize the crosslinks PDB ...  
In PYMOL, open the crosslinks.pdb file and ```set valence, 0``` along with ```show sticks, all``` and ```hide spheres, all```  
In Chimera, uncomment all the MODEL lines in the PDB then open the crosslinks.pdb file and select ```Actions > Atoms/Bonds > show```  

## Citation

[DOI](https://doi.org/10.1074/mcp.M116.058560)
> 
    J.Bullock, J. Schwab, K. Thalassinos, M. Topf (2016)
        The importance of non-accessible crosslinks and solvent accessible surface distance
        in modelling proteins with restraints from crosslinking mass spectrometry. 
        Molecular and Cellular Proteomics (15) pp.2491–2500

## Funding

* BBSRC London Interdisciplinary Doctoral Programme (Joshua Bullock)
* MRC MR/M019292/1 (Maya Topf)

## License

[GPL-V3](https://choosealicense.com/licenses/gpl-3.0/)
> 
    Copyright 2016 - Josh Bullock & Birkbeck College University of London
