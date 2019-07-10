# The green peach aphid gut contains host plant microRNAs identified by comprehensive annotation of Brassica oleracea small RNA data
###### Max C. Thompson, Honglin Feng, Stefan Wuchty, and Alexandra C. C. Wilson

- Code included here was used to format, analyze, and display the data and results present in the above paper.
- Scripts are often paired wherein a BASH script is used to call the primary Python script either in the terminal interface or within the University of Miami's Pegasus Supercomputer using the LSF job scheduler. Please note that scheduling systems and requriements may be very different for your local cluster.


## Initial Workflow

1. Genomes for [Myzus persicae](https://bipaa.genouest.org/sp/myzus_persicae/download/genome/CloneG006_v2/), [Buchnera aphidicola](https://www.ncbi.nlm.nih.gov/assembly/?term=(%22Buchnera+aphidicola+(Myzus+persicae)%22)+AND+(G006%5BInfraspecific+Name%5D+OR+G002%5BInfraspecific+Name%5D+OR+USDA%5BInfraspecific+Name%5D)), and [Brassica oleracea var. oleracea](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/695/525/GCF_000695525.1_BOL/) were manually downloaded from AphidBase and NCBI. 
2. Index the genomes using bowtie2
3. Filter small-RNA-seq data to your specifications
4. Align small-RNA-seq data to the respective genomic libraries using bowtie2
5. Analyze the alignments with respect to your genomes of interest using [`percentage_calculations.py`](percentage_calculations.py)
   - Parses bowtie2 output SAM files and assigns each read alignment to a genome set.
   - Genome sets are compared for overlap and percentages are assigned to each section based on the total reads in the fasta file used in making these alignments.
6. Generate read subset files for futher analysis using [`elimMatched.py`](elimMatched.py)
   - elimMatched will parse a given SAM file and associate fasta file to generate a new fasta file with only the reads that have not met the criteria for a match
     - This will set up the "unknown" reads to be aligned against the bacterial and viral libraries


## Bacterial and Viral Assignment of Unknown Reads
1. Use [`fetchGenomes.py`](fetchGenomes.py) to collect genomes for bacterial and viral libraries
   - Pulls genomes from literature review into downloaded FASTA files.
2. Index the genomes using bowtie2
3. Align small-RNA-seq data to the respective genomic libraries using bowtie2
4. Analyze the alignments with respect to your genomes of interest using [`percentage_calculations.py`](percentage_calculations.py)
5. Produce panels for figures 2 and 3 using [`figure_2-3.py`](figure_2-3.py)
   - This will generate SVGs that can be manipulated in vector graphics software (ie: Illustrator).


## Plant miRNA Analysis
1. Collect SRA datasets for plant small-RNA-seq
2. Filter small-RNA-seq data to your specifications
3. Align small-RNA-seq data to the respective genomic libraries using bowtie2
4. Annotate potential miRNA precursors using [ShortStack](https://github.com/MikeAxtell/ShortStack)
5. Assess homology to existing precursors using local BLAST against [miRBase](http://mirbase.org/ftp.shtml)
6. Collect accepted miRNA precursors and assocaited information into a csv with similar formating to Supplementary Table 3.


