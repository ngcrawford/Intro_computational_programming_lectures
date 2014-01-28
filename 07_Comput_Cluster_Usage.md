# RUNNING JOBS ON A CLUSTER

---

# CURRENT OPTIONS

Boston University Shared Computing Cluster - [SCC][1]
	
* 1408 shared processors
* 232 GPUs
* 23 terabytes memory
* ~ 1 pentabyte 
* You can get an account [here][7].

Extreme Science and Engineering Discovery Environment - [XSEDE][3]
	
* [Mason][2]: large memory computer cluster (8 TB memory)
* [Gordon][4]: similar to SCC
* BU XSEDE access can be obtained [here][5].


---

# SYSTEM SOFTWARE

Most clusters are running some form of linux.

* Typically you [ssh][6] into the system from terminal on your laptop.

		ssh -X your_user_name@scc1.bu.edu

* You'll end up in a home directory (~)

---

# THINGS TO DO

Modify your `.bashrc` the way you like it.

* Setup pip:

		mkdir python_packages
		easy_install --prefix=$HOME/python_packages/ pip
		pip install --install-option="--prefix=$HOME/python_packages" package_of_interest

* Then add the following line to your `.bashrc`

	export PYTHONPATH="$HOME/python_packages/lib/python2.7/site-packages:$PYTHONPATH

---

# THINGS TO DO

Setup your home directory:

	.
	├── code
	├── data -> /path/to/data/store
	├── python_packages
	├── R
	└── source

* I like to have a `code` directory that contains the scripts that I've written as well as a `source` directory that contains other peoples code.

* It helps to be consistent with upper/lowercase of directory names.

---

# INSTALLING OTHER PEOPLES CODE

1. First check that it doesn't already exist on the system.
		
		# lists all modules
		module avail 

		# load a module - in this case `parallel`
		module load parallel/20131222

		# you can add module loads to your bashrc file...

---

# INSTALLING OTHER PEOPLES CODE

Install it yourself.

* [RTFM][8]: Read The Fucking Manual!!!
* Download the code and follow the instructions.

		cd ~/source
		wget http://path/to/web/gzip/or/tar/awesome_software.tar.gz
		tar -xzf awesome_software.tar.gz
		cd awesome_software
		cat README.txt

* Then follow the instructions in the README.

---

# INSTALLING OTHER PEOPLES CODE

If you get errors google them and/or ask for help on stackoverflow.

* Or, ask me for help! ;)
* You will often need to do a `--prefix` install where you define the system path to install the binaries. I like to set this to the current folder so the source and the binaries are stored together.
* Once you get it compiled you'll typically need to update your `.bashrc` with the path to the binaries.

* If you think it's something lots of people will want to use ask SCC of XSEDE to install it as a system module.

---

# RUNNING CODE

SCC and XSEDE use Sun Grid Engine ([SGE][9]) to manage the nodes and the batch-queue.

* The SGE commands all start with 'q': `qsub`, `qstat`, `qdel`, etc.

* Basic Template:

		qsub \
		-V \
		-N name_of_run \
		-pe omp 8 \
		-l h_rt=20:00:00 \
		-b y \
		'command to run'

* `-V` imports your system environment variables (e.g., .bashrc) into the node where command is executed.
* `-pe omp 8` is how you define then number of processor cores to use
* `-l h_rt=20:00:00` tells the system how long to run the analysis 
* `-b y` lets you submit the command from the command line.

---

# RUNNING CODE 

To check the status of commands you're running...

	qstat -u your_user_name

What if you made a mistake?!

	qdel 12314214 # the number is the run ID

---

# EZ-PARELLELIZATION

Many bioinformatics packages will allow you to use multiple processor cores.

* But, if the code is single threaded and you want to run the same command in parallel on lots of files you can use [parallel][10]

* For example: you want convert gzipped files to bgzipped files.

		find *.gz > filenames.txt
		cat filenames.txt # make sure everything looks ok.

		parallel \
		--dry-run \
		-j 8 \
		'cd current/directory;
		gunzip -c {} | bgzip > {.}.bgzipped.gz' \
		< filenames.txt

		# running this command will print all the 'sub-commands' without executing them (--dry-run)

---

# RUNNING CODE 

Then submit the cmd to the cluster.

	qsub \
	-V \
	-N gzip_2_bgzip \
	-pe omp 8 \
	-l h_rt=1:00:00 \
	-b y \
	"parallel \
	-j 8 \
	'cd current/directory; \
	gunzip -c {} | bgzip > {.}.bgzipped.gz' \
	< filenames.txt"


[1]: http://www.bu.edu/tech/about/research/computation/scc/
[2]: https://www.xsede.org/web/guest/iu-mason
[3]: https://www.xsede.org/
[4]: https://www.xsede.org/web/guest/sdsc-gordon
[5]: http://www.bu.edu/tech/about/research/computation/xsede/
[6]: http://en.wikipedia.org/wiki/Secure_Shell
[7]: http://www.bu.edu/tech/accounts/special/research/
[8]: http://en.wikipedia.org/wiki/RTFM
[9]: http://en.wikipedia.org/wiki/Oracle_Grid_Engine
[10]: http://www.gnu.org/software/parallel/



