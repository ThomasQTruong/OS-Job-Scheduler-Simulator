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


TIME_SLICE = 5
COLUMNS = ["Job", "Start", "End", "Completed"]


def main(file_name):
  # Obtain the jobs from the file and apply RR-2 algorithm.
  df = pd.DataFrame(data=RR(job_reader.read_file(file_name), TIME_SLICE),
                    columns=COLUMNS)
  print(df)


def RR(jobs, time_slice):
  time = 0
  data = []
  jobs_length = len(jobs)
  i = 0

  # While there are still jobs left to process.
  while jobs_length > 0:
    # Run the job.
    time_taken = jobs[i].run(time_slice)

    # Didn't run; no duration left: remove from list.
    if time_taken == 0:
      jobs.pop(i)
      jobs_length -= 1
      continue

    # Add run data.
    data.append([jobs[i].name, time, time + time_taken,
                  jobs[i].duration == 0])

    # Ran for less than expected or no more duration.
    if time_taken < time_slice or jobs[i].duration == 0:
      # Remove from list since no duration left.
      jobs.pop(i)
      jobs_length -= 1
      # Reduce i by 1 so we don't skip the next job after deleting.
      i -= 1

    # Update i and time.
    if jobs_length > 0:
      i = (i + 1) % jobs_length
    time += time_taken

  return data


if __name__ == "__main__":
  main(sys.argv[1])
