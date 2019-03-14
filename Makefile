FILE=samples/multiple_functions.c

main:
	python3 -m src.main $(FILE)

force:
	python3 -m src.main -p -f $(FILE)

test:
	python3 -m tests.testing -v

character_count:
	python3 character_count.py words.txt

format:
	black ./

lint:
	pylint src/

clean:
	rm -f *.o logs/* tables/*
