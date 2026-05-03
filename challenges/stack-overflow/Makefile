CC = gcc
CFLAGS = -fno-stack-protector -no-pie -w

TARGET = vuln_basic
SRC = vuln_basic.c

all:
	$(CC) $(SRC) -o $(TARGET) $(CFLAGS)

clean:
	rm -f $(TARGET)

run: all
	./$(TARGET)
	
