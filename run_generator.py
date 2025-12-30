# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generator.core import LoremGenerator

def main():
    parser = argparse.ArgumentParser(description="Lorem Ipsum Generator")
    parser.add_argument("--paragraphs", "-p", type=int, default=1, help="Number of paragraphs")
    parser.add_argument("--words", "-w", type=int, help="Number of words (overrides paragraphs)")
    parser.add_argument("--output", "-o", help="Output file")
    
    args = parser.parse_args()

    if args.words:
        # Just words
        words = LoremGenerator.generate_words(args.words)
        result = " ".join(words)
    else:
        # Paragraphs
        result = LoremGenerator.generate_paragraphs(args.paragraphs)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result + "\n")
            print(f"Generated text saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        print(result)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
