# Python_Scripts
Collection of scripts for different purposes

## corr_tables.py
takes in two files on the command line. first will have a the genes of interest, the second will have all genes and the information of interest. the output file will contain genes of interest and the information of interest only

## GO_conversion.py
Takes in files that contain hofstenia transcript IDs in the first column, then convert them into files that contain uniprot format gene ids that can then be fed into GO analysis through DAVID

## isolate_fasta_headsr.py
Takes in fasta files and will spit out all gene names

## one_sig_value.py
Takes in files with pvalues, and will pull out all genes with at least one significant p value

## quant_file_extract.py
Takes in the quant.sf files that are generated after salmon, and spit out files containing two columns: gene_names and num_reads

## combining_countfiles.py
Takes in any number of the output of quant_file_extract.py script and will spit out two outputs. the first will have all of the numreads combined into a table. the second will have all of the numreads combined into a table but have all gnees with zero expresison values filtered out. 
