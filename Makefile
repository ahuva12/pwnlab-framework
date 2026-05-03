CC = gcc

BUILD_SRC = challenges
BUILD_DIR = build

TARGETS = $(BUILD_DIR)/fmt $(BUILD_DIR)/uaf $(BUILD_DIR)/vuln_basic

all: $(BUILD_DIR) $(TARGETS)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/fmt: $(BUILD_SRC)/format-string/fmt.c | $(BUILD_DIR)
	$(CC) $< -o $@ -no-pie -w

$(BUILD_DIR)/uaf: $(BUILD_SRC)/use-after-free/uaf.c | $(BUILD_DIR)
	$(CC) $< -o $@ -no-pie -w

$(BUILD_DIR)/vuln_basic: $(BUILD_SRC)/stack-overflow/vuln_basic.c | $(BUILD_DIR)
	$(CC) $< -o $@ -fno-stack-protector -no-pie -w

clean:
	rm -rf $(BUILD_DIR)

run-fmt: $(BUILD_DIR)/fmt
	./$(BUILD_DIR)/fmt

run-uaf: $(BUILD_DIR)/uaf
	./$(BUILD_DIR)/uaf

run-vuln: $(BUILD_DIR)/vuln_basic
	./$(BUILD_DIR)/vuln_basic