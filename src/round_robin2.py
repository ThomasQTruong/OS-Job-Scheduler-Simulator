"""
 * round_robin2.py
 * Simulates the RR algorithm of the job scheduler for OS.
 *   Time-slice = 5.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import sys
import job_reader
import pandas as pd


COLUMNS = ["Job", "Start", "End", "Completed"]


def main(file_name):
  # Obtain the jobs from the file and apply RR5 algorithm.
  df = pd.DataFrame(data=RR5(job_reader.read_file(file_name)), columns=COLUMNS)
  print(df)


def RR5(jobs):
  pass


if __name__ == "__main__":
  main(sys.argv[1])
