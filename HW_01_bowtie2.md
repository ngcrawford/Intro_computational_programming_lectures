1. Install bowtie2

		brew tap homebrew/science
		brew install bowtie2

2. Make the bowtie2 index. This will take a little while.

		wget http://www.butterflygenome.org/sites/default/files/Hmel1-1_Release_20120601.tgz

	- If you don't have wget installed use brew to install it.

		bowtie2-build Hmel1-1_primaryScaffolds.fa Hmel1-1_primaryScaffolds

	- This set makes the index that bowtie2 uses to align the reads to the genome.

3. Align test reads.

		bowtie2  -x Hmel1-1_primaryScaffolds -1 heli.R1s.fq.gz -2 heli.R2s.fq.gz 

	- Play around with bowtie2 and read the documentation. 
	
	- Can you use `grep` and `wc` to see how changing the settings affects the number of reads that align?	

4. Install samtools.

	brew install samtools

5. Can you figure out how to pipe the output of bowtie2 into samtools so that the final file is a BAM? You'll need to consult the internet to figure this out.


