import sys
import argparse

parser = argparse.ArgumentParser(
                description='Text file conversion.'
                )

# args = parser.parse_args()

for x in sys.argv[1:]:
     print (x)