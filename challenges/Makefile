CC = gcc

TARGETS = fmt uaf vuln_basic

all: $(TARGETS)

fmt: 
	$(CC) format-string/fmt.c -o format-string/fmt -no-pie -w

uaf:
	$(CC) use-after-free/uaf.c -o use-after-free/uaf -no-pie -w

vuln_basic: 
	$(CC) stack-overflow/vuln_basic.c -o stack-overflow/vuln_basic -fno-stack-protector -no-pie -w

clean:
	rm -f format-string/fmt
	rm -f use-after-free/uaf
	rm -f stack-overflow/vuln_basic
	
run-fmt: fmt
	./format-string/fmt

run-uaf: uaf
	./use-after-free/uaf

run-vuln: vuln_basic
	./stack-overflow/vuln_basic