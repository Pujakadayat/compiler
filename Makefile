FILE=samples/if.c

main:
	python3 -m src.main -r   $(FILE)

force:
	python3 -m src.main -ptrf $(FILE)

test:
	python3 -m tests.testing -v

install:
	pip3 install -r requirements.txt

character_count:
	python3 character_count.py words.txt

format:
	black ./

lint:
	pylint src/ tests/

clean:
	rm -f *.o logs/* tables/*
