#
## This script extracts likelihood results from migrate-n runs and prints them to stdout.
## It assumes runs are in separate folders, and a single file within each folder contains the word parmfile in its filename.
## It also takes a token to search for run directories within the input directory, and a token to search for result text files.
## It will exclude pdf files.
## Usage:
## python3 extract_marginal_lhoods.py [directory path with run directories] [run directory token] [result file token]
## Example:
## python3 ~/PycharmProjects/migrate_UtilScripts/extract_marginal_lhoods.py ~/Desktop/migrate_feriarum_4Pop_TESTCONSTANTS_Jul092020/ _migrate _4Pop
#

from os import listdir, path
import sys
import re

# Store user inputs in variables.
dirpath = sys.argv[1]
token_input = sys.argv[2]
token_resultfile = sys.argv[3]

# Get list of run directories, then search run directory token among list.
dir_list = listdir(dirpath)
dir_runlist = [x for x in dir_list if re.search(token_input, x)]

# Search within each run directory, the result file using the result file token. Takes only the first match of result file token at each run directory.
for rundir in dir_runlist:
    rundir_list = listdir(path.join(dirpath + rundir))
    result_file = [x for x in rundir_list if re.search(token_resultfile, x) and not re.search("pdf", x)][0]
    result_filehandle = open(path.join(dirpath + rundir + '/' + result_file), 'r')
    lines = result_filehandle.read()
    marg_lhoods = re.findall(r'\s+All[\s\-\d\.]+', lines)[-1]
    print(result_file + marg_lhoods.strip('\n'))
