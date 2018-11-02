#! /bin/bash

perl /nethome/mct30/gitclones/mirdeep2/bin/make_html.pl \
-f /nethome/mct30/bmds/miRDeep2/mirdeep_runs/plant*/output.mrd \
-k /nethome/mct30/bmds/Myzus-miRDeep2/mpe3.fa \
-s /nethome/mct30/bmds/miRDeep2/mirdeep_runs/plant*/survey.csv \
-c -y plant_Myzus