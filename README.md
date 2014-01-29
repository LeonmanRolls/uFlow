uFlow
=====

Micro data-flow interpreter for python

Short command line scripts can often follow the data-flow programming
paradigm. This script takes in a list of variables and 
command line arguments and executes functions as soon as the function's 
dependencies are met. By simply stating required data and functions
without any regard to the actual flow of the program, this might allow 
short scripts to be written faster and be more readable. The functions 
can also be executed in parallel data permitting but at this scale 
speed improvements are unlikely to be noticeable, so the aim is to 
benefit the coder.
