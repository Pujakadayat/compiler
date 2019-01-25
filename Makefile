# all:
# 	main

# main:
# 	python3 compiler.py ....

character_count:
	python3 character_count.py words.txt

lint:
	black ./

clean:
	rm *.o
