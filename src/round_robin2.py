"""
 * round_robin2.py
 * Simulates the RR algorithm of the job scheduler for OS.
 *   Time-slice = 5.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import sys
import job_reader


def main(file_name):
  # Obtain the jobs from the file.
  jobs = job_reader.read_file(file_name)

  for job in jobs:
    print(job.name, job.duration)


if __name__ == "__main__":
  main(sys.argv[1])
