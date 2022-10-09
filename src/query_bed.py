"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work

    # FIXME: put your code here

    # print(args)
    # print(args.bed)
    # print(args.query)
    # print(args.outfile)

    table = Table()

    for line in args.bed:
        #print(line)
        bedline = parse_line(line)
        #print(bedline)
        table.add_line(bedline)
        
    for line in args.query:
        #print(line)

        query_lst = line.split("\t")
        #print(query_lst)

        query_chrom = query_lst[0]
        query_start = int(query_lst[1])
        query_end = int(query_lst[2])

        chrom_list = table.get_chrom(query_chrom)

        for bedline in chrom_list:
            bed_chrom = bedline[0]
            bed_start = int(bedline[1])
            bed_end = int(bedline[2])
            
            if query_start <= bed_start and query_end >= bed_end:
                print_line(bedline, args.outfile)


if __name__ == '__main__':
    main()



