"""
 * shortest_job_first.py
 * Simulates the SJF algorithm of the job scheduler for OS.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import sys
import job_reader
import pandas as pd


COLUMNS = ["Job", "Start", "End", "Completed"]


def main(file_name):
  # Obtain the jobs from the file.
  jobs = job_reader.read_file(file_name)
  # Sort the job by duration from least to greatest.
  jobs.sort()

  # Apply SJF algorithm.
  df = pd.DataFrame(data=SJF(jobs), columns=COLUMNS)
  print(df)


def SJF(jobs):
  """
    Applies the Shortest Job First algorithm.
    Runs based on which job has the least duration.

    @param jobs - the list of jobs to run.
    @return list - the list of data: [name, start, end, completed?].
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
