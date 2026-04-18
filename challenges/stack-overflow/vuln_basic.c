#include <stdio.h>
#include <stdlib.h>

void win() {
	char flag[] = "pwnlab{stack_overflow}\n";
	printf("You win!\nFLAG: %s\n", flag);
}

void vuln() {

    char buffer[32];

    printf("What is your name?\n");

	// intentionally vulnerable (classic stack overflow for educational purposes)
    gets(buffer);

    printf("Hello %s\n", buffer);
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);

    printf("Welcome!\n");
    vuln();
    printf("Goodbye!\n");
	
    return 0;
}