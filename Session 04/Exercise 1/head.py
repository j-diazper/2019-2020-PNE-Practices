from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
lines= file_contents.split("\n",)
print(lines[0])