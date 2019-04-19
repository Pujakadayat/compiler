FILE=assignments
CFILE=samples/$(FILE).c
SFILE=assembly/$(FILE).s

main:
	python3 -m src.main -tr -a $(CFILE)

force:
	python3 -m src.main -sptrf $(CFILE)

asm:
	gcc $(SFILE) -o assembly/$(FILE)

make run:
	./assembly/$(FILE)

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
