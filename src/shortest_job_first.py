"""
 * shortest_job_first.py
 * Simulates the SJF algorithm of the job scheduler for OS.
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
