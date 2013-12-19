# ADVANCED LINUX

---

# OVERVIEW

- cut
- compression (gzip and gunzip) and tar
- top and htop
- curl and wget
- awk, sed, (etc)

---

# CUT

- `cut` allows you to select specific columns from a csv/tsv file

- similar to sort

	`sort -k1,1` = sort by the first column 
	`cut -f1` = select the first column

- the default delimiter is tab. To set to comma use `-d','`.

- I don't use `cut` very often, but it's invaluable when you need to make a standard bed-file.

---

# COMPRESSING FILES

- `gzip` is the standard tool for compressing files. The 'g' comes from GNU project.

		gzip filename.txt

- `gunzip` decompress a gzipped file

		gunzip filename.txt.gz

- `gunzip -c gunzip filename.txt.gz` will send the unzipped data to standard out. This allows you to incorporate gzipped data into pipelines.

---

# COMPRESSING FILES CONTINUED

- If you need to compress a directory use `tar`. 

		tar -czf directory.tar.gz directory/

	- this produces a gzipped 'tarball' of the directory.

	- Note that the order of the result and the input is reversed from 'standard' linux commands. 
		- `-c` = compress directory
		- `-z` = gzip output
		- `-f` = skip errors

- If you need to decompress a `tar.gz` file replace the `-c` flag with `-x` (= e**X**tract)

		tar -xzf directory.tar.gz

---

# WORKING WITH RUNNING PROCESSES

- The `top` command will show you what's currently running on your system.

- You can use `brew install htop` to install a fancier version.

- To kill a process you can use the `kill` command and a process id you obtained from `top`/`htop`.

		kill [process ID]

---

# DOWNLOADING FILES FROM THE WEB

- I usually use `wget` since it's the *standard* linux approach, but you can also use `curl` which comes with OS X by default.

		wget http://www.centos.org
		curl http://www.centos.org > centos-org.html


---

# LINUX PROGRAMMING LANGUAGES

- **AWK**: "an interpreted programming language designed for text processing and typically used as a data extraction and reporting tool." *--wikipedia*

- **SED**: "a Unix utility that parses and transforms text, using a simple, compact programming language." *--wikipedia*

- Selecting columns with **AWK**.

		awk '{print $1,$2,$3,$6,$4}' test_data/example_bed.bed | head

	- Similar to `cut`, but easier to reorder columns.

- Replacing words with **SED**.

		sed 's/HE/SCF/g' test_data/example_bed.bed | head

---

# REGULAR EXPRESSIONS

- **Regular expressions (REGEX)**: "a sequence of characters that forms a search pattern, mainly for use in pattern matching with strings, or string matching." *--wikipedia*

- Regular expressions are a powerful tool for searching and filtering. However, they are *difficult* to debug and often contain unexpected edge cases.

- You can play around with regex expressions on the web: [regex testing site](http://gskinner.com/RegExr/)


---

# PUTTING IT ALL TOGETHER

- **Curly braces ( {, and } )**: group commands so that both read the same stdin.

- **Back-slashes**: escape characters so they're ignored. Here they escape the invisible new-line ("\n") characters.

- **Example**:

		cat test_data/example_bed.bed \
		| { head -n 1; tail -n +2 \
		| sort -k1,1 -k2,2g; } \
		> file.wheader.sorted.bed

---


<img src="images/command_line_fu.png" alt="XKCD" style="width: 500px;"/>





