FILE=samples/assignment.c

main:
	python3 -m src.main -p $(FILE)

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
