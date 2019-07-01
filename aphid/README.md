# Aphid Gut/Bacteriocyte sRNA Analysis Project

Download genomes for Myzus persicae, Buchnera Aphidicola, and Brassica oleracea var. capitata Wisconsin Golden Acre from AphidBase and NCBI. 
Use fetchGenomes to collect other bacteria and virus genomes

    Pulls genomes from literature review into downloaded FASTA files
bowtie2-indexing

    Indexes each of the individual genomes and then the big three together
G006-alignments

    Aligns all three together and each individual alignment with full reads files

elimMatched

    Eliminates the reads that matched perfectly or with one mismatch to Myzus, Buchnera, or plant and generates new FASTA files with only the unmatched reads
    Used later for other bacteria and virus alignments
elimUnmatched

    Eliminates the reads that didn't match perfectly or with one mismatch to Myzus, Buchnera, or plant and generates new FASTA files with only the matched reads
    Used later for miRNA analysis
perSAM-BSUB-pegasus.sh >

    Calculates percentage of reads used in alignment that mapped to the specificed group of genomes
# miRNA Analysis

miRDeep2

    Runs miRDeep2 on the Myzus only gut dataset from elimUnmatched
bowtie1-miRDeep-P

    Runs miRDeep-p on the plant only gut dataset
miranda

    Runs miranda on the miRDeep2/-P outputs

# Figure Production

two_pannel_stacked_bar_figure_1.1

    Generates Figure 1
figure_2_miRNA_venn

    Generates Figure 2
