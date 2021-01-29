"""
convert csv to unicode box drawing
from AdamantPenguin/box-drawing-utils on GitHub
License: GPLv3
"""

### setup ###

# imports
import csv
import sys

# characters to use - basically so i don't need to copy/paste as much
CHARS = {
    'top left': "╭",
    'top right': "╮",
    'bottom left': "╰",
    'bottom right': "╯",
    'horizontal': "─",
    'vertical': "│",
    'left T': "├",
    'right T': "┤",
    'up T': "┬",
    'down T': "┴",
    'cross': "┼"
}

# get filename from command line
try:
    input_file = sys.argv[1]
except:
    print(f"Usage: {sys.argv[0]} input_filename", file=sys.stderr)
    sys.exit(1)

# read input file into an array
input_array = []
with open(input_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        input_array.append(row)


### render table ###

# calculate each column's width
column_widths = []
for col_id in range(len(input_array[0])): # for each column
    max_width = 0
    for row in input_array: # for each row
        if len(row[col_id]) > max_width: # if col_idth cell is the longest seen
            max_width = len(row[col_id])
    column_widths.append(max_width)

# calculate total row width (including formatting)
row_width = 0
for width in column_widths:
    row_width += 2 + width + 1
row_width += 2

## construct output string ##
output = ""

# first line - top border
output += CHARS['top left']
for width in column_widths:
    output += CHARS['horizontal'] * (width + 2) + CHARS['up T']
output = output[:-1] # remove trailing T
output += CHARS['top right'] + '\n'

# middle lines - actual content
for row in input_array:

    # first line - content
    for i in range(len(row)):
        output += CHARS['vertical'] + ' ' * (column_widths[i] - len(row[i]) + 1) + row[i] + ' '
    output += CHARS['vertical'] + '\n'

    # second line - border
    output += CHARS['left T']
    for width in column_widths:
        output += CHARS['horizontal'] * (width + 2) + CHARS['cross']
    output = output[:-1] # remove trailing cross
    output += CHARS['right T'] + '\n'
    
output = output[:-row_width] # remove trailing line

# final line - bottom border
output += CHARS['bottom left']
for width in column_widths:
    output += CHARS['horizontal'] * (width + 2) + CHARS['down T']
output = output[:-1] # remove trailing T
output += CHARS['bottom right']

## print the output ##
print(output)
