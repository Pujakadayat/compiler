main:
	python3 src/main.py -s -p --verbose --grammar grammars/grammar2.txt samples/basic_math.c

character_count:
	python3 character_count.py words.txt

lint:
	black ./
	pylint **/*.py


clean:
	rm -f *.o logs/*
