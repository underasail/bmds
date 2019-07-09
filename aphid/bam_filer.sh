#! /bin/bash

for file in ~/bmds/SAM_out/*_Gut_*not_m_s.map; do
    samtools view -bS $file | samtools sort - -o ${file%.map}.sorted.bam
    samtools index ${file%.map}.sorted.bam
done


for bam_file in ~/bmds/SAM_out/*_Gut_*not_m_s.sorted.bam; do 
    echo $bam_file
    echo "Reads aligning before filtering:"
    grep -v -c "^@" ${bam_file%.sorted.bam}.map;
    echo "Reads aligning w/ 0mm and 0gap filtering:"
    # samtools view -bS $bam_file | bamtools filter -tag XO:0 | samtools view -h | wc -l;
    # samtools view -bS $bam_file | bamtools filter -tag XM:0 | samtools view -h | wc -l; 
    bamtools filter -tag XO:0 -in $bam_file | \
    bamtools filter -tag XM:0 -out ${bam_file%.sorted.bam}_mm0_gap0.sorted.bam
    samtools index ${bam_file%.sorted.bam}_mm0_gap0.sorted.bam
    samtools view -h ${bam_file%.sorted.bam}_mm0_gap0.sorted.bam | grep -v -c "^@"
    echo
done

for file in ~/bmds/SAM_out/*_Gut_*not_m_s_mm0_gap0.sorted.bam; do
    samtools view -h $file > ${file%.sorted.bam}.map
done
