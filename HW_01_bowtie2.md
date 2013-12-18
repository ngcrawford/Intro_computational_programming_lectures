# Homework \# 1

The main purpose of this assignment is to get you setup with `brew` and `bowtie2` and `samtools`. So that you have some data to work with I've added two test files of R1 and R2 *Heliconius* reads to the `test_data` folder. To get these files you'll need to update your git repo the newest version on github. To do that you should just run the following command from within the git repo you made yesterday.

		git pull origin master

If you run into issues you can always make a new repo.

		git clone git@github.com:ngcrawford/comp_bio_lectures.git

Once everything is up to date you can start with the assignment.

1. Install `bowtie2`.

		brew tap homebrew/science
		brew install bowtie2

2. Make the `bowtie2` index.

		wget http://www.butterflygenome.org/sites/default/files/Hmel1-1_Release_20120601.tgz

	- If you don't have `wget` installed use brew to install it.

	- The file you downloaded it tarred and gziped. The internet will tell you how to decompress it.

			
	<pre><code>bowtie2-build Hmel1-1_primaryScaffolds.fa Hmel1-1_primaryScaffolds</pre></code>

	- This command makes the index that `bowtie2` uses to align the reads to the genome. This will take a little while.

3. Align the test reads. You should run this from the directory that contains the `bowtie2` indices. 

		bowtie2  -x Hmel1-1_primaryScaffolds -1 test_data/heli.R1s.fq.gz -2 test_data/heli.R2s.fq.gz 

	- Play around with `bowtie2` and read the [documentation][]. 
	
	- Can you use `grep` and `wc` to see how changing the alignment stringency settings affects the number of reads that align?	

4. Install `samtools`.

		brew install samtools

5. Can you figure out how to pipe the output of `bowtie2` into `samtools` so that the final file is a BAM? Hint, you'll need to consult the internet to figure this out.

[documentation]: http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml
