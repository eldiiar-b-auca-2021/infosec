if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file_name> <word>"
  exit 1
fi

file_name="$1"
word="$2"

if [ ! -f "$file_name" ]; then
  echo "File not found!"
  exit 1
fi

word_count=$(grep -o -w "$word" "$file_name" | wc -l)

echo "The word '$word' appears $word_count times in $file_name."
