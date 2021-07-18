CC = python3
RUNNER = wilson.py
DIRECTORIES = $(wildcard */)
ARGS = --dev
M = "Unedited message"

run:
	$(CC) $(RUNNER) $(ARGS)

clean:
	rm __pycache__ -rf
	rm $(DIRECTORIES)__pycache__ -rf

finish:
	git add *
	git commit -m $(M)
	git push

