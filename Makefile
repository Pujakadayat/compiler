main:
	python3 -m src.main -p -f samples/basic_math.c

test:
	python3 -m tests.testing -v

character_count:
	python3 character_count.py words.txt

lint:
	black ./
	pylint src/

clean:
	rm -f *.o logs/* tables/*
