"""
 * first_come_first_serve.py
 * Simulates the FCFS algorithm of the job scheduler for OS.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import sys
import job_reader
import pandas as pd


COLUMNS = ["Job", "Start", "End", "Completed"]


def main(file_name):
  # Obtain the jobs from the file and apply FCFS algorithm.
  df = pd.DataFrame(data=FCFS(job_reader.read_file(file_name)), columns=COLUMNS)
  print(df)


def FCFS(jobs):
  """
   * The First-Come-First-Serve algorithm.
   * Runs the jobs based on which came first.
   *
   * @param jobs - the list of jobs.
   * @return list - the list of data: [name, start, end, completed?].
  """
  time = 0
  data = []

  for job in jobs:
    duration = job.duration
    # Run the job.
    job.run(job.duration)
    # Save data.
    data.append([job.name, time, time + duration, job.duration == 0])
    time += duration

  return data


if __name__ == "__main__":
  main(sys.argv[1])
