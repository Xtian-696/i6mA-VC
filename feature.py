import sys

sys.path.extend(["../../", "../", "./"])
import numpy as np

from binary import binary
from kmer import Kmer

import argparse


def read_fasta(file):
    f = open(file)
    documents = f.readlines()
    string = ""
    flag = 0
    fea=[]
    for document in documents:
        if document.startswith(">") and flag == 0:
            flag = 1
            continue
        elif document.startswith(">") and flag == 1:
            string=string.upper()
            fea.append(string)
            string = ""
        else:
            string += document
            string = string.strip()
            string=string.replace(" ", "")

    fea.append(string)
    f.close()
    return fea


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fasta', required=True, help="fasta file name")
    args = parser.parse_args()
    print(args)


    fasta = read_fasta(args.fasta)

    print(np.shape(fasta))

    feature_name=["binary","Kmer"]

    feature={"binary":"binary(fasta)","Kmer":"Kmer(fasta)"}

    for i in feature_name:
        eval(feature[i])


if __name__ == '__main__':
    main()