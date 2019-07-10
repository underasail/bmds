# The green peach aphid gut contains host plant microRNAs identified by comprehensive annotation of Brassica oleracea small RNA data
###### Max C. Thompson, Honglin Feng, Stefan Wuchty, and Alexandra C. C. Wilson

- Code included here was used to format, analyze, and display the data and results present in the above paper.
- Scripts are often paired wherein a BASH script is used to call the primary Python script either in the terminal interface or within the University of Miami's Pegasus Supercomputer using the LSF job scheduler. Please note that scheduling systems and requriements may be very different for your local cluster.

## Workflow

1. Genomes for [Myzus persicae](https://bipaa.genouest.org/sp/myzus_persicae/download/genome/CloneG006_v2/), [Buchnera aphidicola](https://www.ncbi.nlm.nih.gov/assembly/?term=(%22Buchnera+aphidicola+(Myzus+persicae)%22)+AND+(G006%5BInfraspecific+Name%5D+OR+G002%5BInfraspecific+Name%5D+OR+USDA%5BInfraspecific+Name%5D)), and [Brassica oleracea var. oleracea](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/695/525/GCF_000695525.1_BOL/) were manually downloaded from AphidBase and NCBI. 

2. Use fetchGenomes to collect genomes for bacterial and viral libraries
   - Pulls genomes from literature review into downloaded FASTA files.
3. Index the genomes using bowtie2
4. Filter small-RNA-seq data to your specifications
5. Align small-RNA-seq data to the respective genomic libraries using bowtie2
6. Analyze the alignments with respect to your genomes of interest using percentage_calculations_other_bacteria
   - Parses bowtie2 output SAM files and assigns each read alignment to a genome set.
   - Genome sets are compared for overlap and percentages are assigned to each section based on the total reads in the fasta file used in making these alignments.
7. 
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
