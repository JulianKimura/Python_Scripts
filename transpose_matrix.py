#!/usr/bin/env python3

import pandas as pd

counts = pd.read_table('/Users/JulianKimura/Documents/Lab/Single_Cell_Seq/URD/subsampled_cleaned_embryo_juv/45000_subsample_counts.txt')
counts_tp = counts.transpose()
counts_tp.to_csv('/Users/JulianKimura/Documents/Lab/Single_Cell_Seq/URD/subsampled_cleaned_embryo_juv/45000_subsample_counts_transposed.txt', sep = '\t')




