#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[32];
	void (*fn)();
} User;

void hello(char *name);

void win(char* name) {
	if (strcmp(name, "Bob") == 0) { 
		char flag[] = "pwnlab{use_after_free}\n";
		printf("Hello %s! You win!\nFLAG: %s\n", name, flag);
	} else {
		hello(name);
	}
}

void hello(char* name) {
    printf("Hello %s", name);
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);

    User *u = malloc(sizeof(User));
	u->fn = hello;
    strcpy(u->name, "Alice");

    u->fn(u->name);

    free(u);  
	
	User *p = malloc(sizeof(User));
	
	printf("\nWhat is your name?\n");
	fgets(p->name, sizeof(User), stdin);

    u->fn(u->name);

    return 0;
}