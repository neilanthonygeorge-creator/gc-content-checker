# GC Content Checker

A Python-based bioinformatics tool for calculating GC content and performing basic quality control (QC) on DNA sequences from FASTA files.

## Features
- Calculates GC percentage of DNA sequences
- Removes ambiguous bases (`N`) before analysis
- Performs sequence quality control checks
- Labels sequences as PASS or FAIL based on:
  - Minimum sequence length
  - GC content range
- Reads FASTA files using Biopython

## Requirements
Install Biopython before running the script:

pip install biopython

## Files Included
- `gc-content-checker.py` → Main Python script
- `sequence.fasta` → Example FASTA file
- `README.md` → Project documentation

# How to Run

Run the script using:

python gc-content-checker.py


## Example Output
---Processing the files:{filename}---
ID:NZ_JBJYSV010000031.1 | GC: 38.9275274670% |  Result: PASS

## Technologies Used
- Python
- Biopython

## Applications
This project can be used for:
- Basic bioinformatics sequence analysis
- FASTA file quality control
- Learning biological data processing using Python

## Author
Neil George
