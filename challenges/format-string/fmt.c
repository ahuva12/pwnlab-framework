#include <stdio.h>

void win() {
	char flag[] = "pwnlab{format_string_bag}\n";
	printf("You win!\nFLAG: %s\n", flag);
}

void safe() {
    printf("Nothing happens...\n");
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);

    char input[100];
	void (*func_ptr)() = safe;	
    void *addr_func_ptr = &func_ptr;

    printf("What is your name?\n");
	
    fgets(input, sizeof(input), stdin);

    printf(input); 	

    func_ptr();	

    return 0;
}



