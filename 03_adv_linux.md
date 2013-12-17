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

- the default delimitar is tab. To set to comma use `-d','`.

- I don't use cut very often, but it's invaluable when you need to make a standard bedfile.

---

# COMPRESSING FILES

- `gzip` is the standard tool for compressing files. The 'g' comes from GNU project.

		gzip filename.txt

- `gunzip` decompress a gzipped file

		gunzip filename.txt.gz

- `gunzip -c gunzip filename.txt.gz` or `zcat gunzip filename.txt.gz` will send the unzipped datat to standard out. This allows you to incorporate gzipped data into pipelines.

---

# COMPRESSING FILES CONTINUED

- If you need to compress a directory use `tar`. 

		tar -czf directory.tar.gz directory/

	- this produces a gzipped 'tarball' of the directory.

	- Note that the order of the result and the input is reversed from 'standard' linux commands. 

	- `-c` = compress dicrectory
	- `-z` = gzip output
	- `-f` = skip errors





