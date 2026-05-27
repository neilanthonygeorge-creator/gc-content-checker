"""
GC Content and FASTA QC Checker

This script:
1. Calculates GC percentage
2. Performs sequence quality control
3. Reads FASTA files using Biopython
4. Labels sequences as PASS or FAIL
"""
#Code for finding out the GC content
def gc_count(sequence):
    sequence=sequence.upper().replace("N","")  #To convert into upper case and replace N
    if len(sequence)==0:
        return None
    #Calculate percentage
    return(sequence.count("G")+sequence.count("C"))/len(sequence)*100

def passes_qc(sequence,min_length,min_gc,max_gc):
    #Check length
    if len(sequence)<min_length:
        return False

    #Calculate GC content and store in variable gc
    gc= gc_count(sequence)

    #Check if sequence was empty or invalid
    if gc is None:
        return False

    #Check whether GC is within range
    return min_gc<=gc<=max_gc

#To retrieve information from FASTA files
def process_fasta(filename):
    print("---Processing the files:{filename}---")
    from Bio import SeqIO 
    try:
        for record in SeqIO.parse(filename, "fasta"):
            sequence=record.seq
            seq_id=record.id

            #Apply QC settings
            if passes_qc(sequence,8,30,80):
                status="PASS"
            else:
                status="FAIL"

            gc_val=gc_count(sequence)
            gc_display= f"{gc_val:.10f}%" if gc_val is not None else "0%"

            print(f"ID:{seq_id} | GC: {gc_display} |  Result: {status}")


    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error sequence: {e}")

if __name__=="__main__":
    #Pass the actual filename  as a string in quotes here
    process_fasta("sequence.fasta")
    process_fasta("Mus musculus FGFR3 gene.fasta")    #This can be any FASTA file according to name
