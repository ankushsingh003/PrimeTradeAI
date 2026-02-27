import os

# Define the absolute path
file_path = r'd:\primetradeai\data.csv'

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned_lines = []
# Header
header = "timestamp,open,high,low,close,volume_btc,volume_usd\n"
cleaned_lines.append(header)

for line in lines:
    line = line.strip()
    if not line:
        continue
    # Skip the original header if it exists in any form
    if 'timestamp' in line.lower():
        continue
    # Remove leading and trailing double quotes
    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]
    cleaned_lines.append(line + '\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

print(f"Successfully cleaned {len(cleaned_lines)} lines.")
