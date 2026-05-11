import sys

SUSPICIOUS_KEYWORDS = ["error", "fail", "denied", "invalid", "warning"]

def filter_log(log_path):
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                lower_line = line.lower()
                if any(keyword in lower_line for keyword in SUSPICIOUS_KEYWORDS):
                    print(line.strip())
    except FileNotFoundError:
        print(f"[!] Log file not found: {log_path}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_filter.py <log_file_path>")
        sys.exit(1)

    log_file = sys.argv[1]
    filter_log(log_file)
