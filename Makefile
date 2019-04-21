FILE=negativeTest
CFILE=samples/$(FILE).c
SFILE=assembly/$(FILE).s

main:
	python3 -m src.main -rtap $(CFILE)

force:
	python3 -m src.main -sptrf $(CFILE)

asm:
	gcc $(SFILE) -o assembly/$(FILE)
	./assembly/$(FILE); echo $$?

gcc:
	gcc -O0 -S $(CFILE)

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
