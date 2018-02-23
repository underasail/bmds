#! /bin/bash

#BSUB -J ACYPI8971_membrane_abinitio
#BSUB -e /nethome/mct30/err/ACYPI8971_membrane_abinitio.err
#BSUB -o /nethome/mct30/out/ACYPI8971_membrane_abinitio.out
#BSUB -n 8
#BSUB -q general
#BSUB -W 165:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle/\
main/source/bin/membrane_abinitio2.static.linuxgccrelease \
-in:file:fasta /nethome/mct30/aphid/acypi8971.fa \
-in:file:spanfile /nethome/mct30/aphid/acypi8971_octopus.span \
-in:file:lipofile /nethome/mct30/aphid/acypi8971.lips4
-in:file:frag3 /nethome/mct30/aphid/robetta/aat000_03_05.200_v1_3 \
-in:file:frag9 /nethome/mct30/aphid/robetta/aat000_09_05.200_v1_3
-in:path:database \
/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle/main/database \
-abinitio:membrane \
-score:find_neighbors_3dgrid \
-membrane:no_interpolate_Mpair \
-membrane:Menv_penalties \
-membrane:normal_cycles 40 \
-membrane:normal_mag 15 \
-membrane:center_mag 2 \
-out:file:silent /nethome/mct30/aphid/ACYPI008971_silent.out
-nstruct 30000

# Protein sequence in fasta format, Octopus transmembrane prediction, 
# Lipophilicity prediction, 3-residue fragments, 9-residue fragments, 
# Path to rosetta database, Membrane ab initio application, 
# Use a 3D lookup table for residue neighbors calculations, 
# Switch off the interpolation between the two layers for the Mpair term, 
# Switch on the following penalties:
#     * no non-helical secondary structure fragments in predicted 
#       transmembrane helical regions in the hydrophobic layer of the membrane.
#     * no N- and C- termini residues of predicted transmembrane helical 
#       regions in the hydrophobic layer of the membrane.
#     * no transmembrane helices with orientation >45 degrees relative to the 
#       membrane normal vector.
# Speed settings for Monte Carlo based membrane normal and center search
# Number of output structures
# Silent output file