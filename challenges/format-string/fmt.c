#include <stdio.h>

void win() {
	char flag[] = "pwnlab{format_string_bag}\n";
	printf("You win!\nFLAG: %s\n", flag);
}

int main() {
    char input[100];

    printf("What is your name?\n");
    fgets(input, sizeof(input), stdin);

    printf(input);  

    return 0;
}