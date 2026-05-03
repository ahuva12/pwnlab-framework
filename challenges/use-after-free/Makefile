CC = gcc
CFLAGS = -no-pie -w

TARGET = uaf
SRC = uaf.c

all:
	$(CC) $(SRC) -o $(TARGET) $(CFLAGS)

clean:
	rm -f $(TARGET)

run: all
	./$(TARGET)
	
