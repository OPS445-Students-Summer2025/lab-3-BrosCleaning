#!/usr/bin/env python3
# Author ID: sbashyal@myseneca.ca

import subprocess

def free_space():
    # Run the command: df -h | grep '/$' | awk '{print $4}'
    result = subprocess.run(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # Decode output as utf-8 string
    )
    return result.stdout.strip()


if __name__ == "__main__":
    print(free_space())
