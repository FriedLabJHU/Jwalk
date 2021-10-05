# Jwalk

A tool to calculate the **S**olvent **A**ccessible **S**urface **D**istances (**SASD**) between crosslinked residues  
  
This version of Jwalk is simply a modernization of the original invented by the [Topf Lab](https://github.com/Topf-Lab/Jwalk)  
All functionality is original and compatibility has been upgraded for Python 3  
Jwalk works on Linux / MacOS

## Dependencies
The following can be installed with ```pip```

|          |Package            |
| -------- | ----------------- |
| Required | ```BioPython```   |
| Required | ```numpy```       |
| Required | ```collections``` |
| Optional | ```freesasa```    |

## Installation

```
  # Move to cloned directory
  cd Jwalk

  # Run install script
  python setup.py install
```

## Running Jwalk
``` $ jwalk ```
* Given no arguments, Jwalk will find all SASD between all Lysines in all PDBs in the working directory *

## Running Options
```
    -h, --help        show this help message and exit
    -lys LYS          calculate lysine crosslinks (default)
    -xl_list XL_LIST  calculate crosslinks from input list (see Examples)
    -i I              specify input pdb: -i [inputfile.pdb]   (default runs on every .pdb in directory)
    -aa1 AA1          specify starting amino-acid via three letter code eg. HIS
    -aa2 AA2          specify starting amino-acid via three letter code eg. TYR
    -surface SURFACE  use higher accuracy method to calculate solvent accessibility - slower
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
In order to visualize the crosslinks in Chimera select ```Actions > Atoms/Bonds > show```

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
    Copyright 2016 - Birkbeck College University of London
    The Jwalk inventor is: Josh Bullock