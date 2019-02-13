main:
	python3 src/main.py -s -p --verbose --grammar grammars/grammar2.txt samples/plain.c

character_count:
	python3 character_count.py words.txt

lint:
	black ./

clean:
	rm -f *.o logs/*
