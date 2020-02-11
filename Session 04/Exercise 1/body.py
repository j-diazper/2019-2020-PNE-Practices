from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
lines= file_contents.split("\n")
body=lines[1:]

bodystr= " "

bodystr= bodystr.join(body)

print(bodystr)
