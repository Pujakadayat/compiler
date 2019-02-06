all:
	main

main:
	python3 src/main.py -s -p samples/plain.c

character_count:
	python3 character_count.py words.txt

lint:
	black ./

clean:
	rm *.o
