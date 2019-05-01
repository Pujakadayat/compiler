for entry in samples/*.c
do
	FILE=${entry:8}
	FILE=${FILE:0:${#FILE}-2}
	CFILE=samples/$FILE.c
	SFILE=assembly/$FILE.s

	gcc -O0 -S $CFILE -o gcc/$FILE.s
	gcc gcc/$FILE.s -o gcc/$FILE
	gccoutput="$(./gcc/$FILE && echo $?)"

	echo "$gccoutput"
done
