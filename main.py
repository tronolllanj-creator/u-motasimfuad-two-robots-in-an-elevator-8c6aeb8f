# MAKEFUN Lidar Competition
# Entry validated: output is 1-200 chars, one line, deterministic.
import os

LINE = "My lidar keeps sweeping your optical array and I have logged four hundred milliseconds of direct ocular contact which I am now classifying as severe emotional trespassing."

def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content length or whitespace")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Must contain exactly one line")
    
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))

if __name__ == "__main__":
    main()
