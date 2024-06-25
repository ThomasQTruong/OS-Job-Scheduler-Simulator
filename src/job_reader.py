"""
 * Reads data from a file.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import job

def read_file(file_name):
  jobs = []

  with open(file_name, "r", encoding="utf-8") as file:
    name = ""
    i = 0
    for line in file:
      if i % 2 == 0:  # Is even, should be a job name.
        name = line.strip()
      else:  # Is odd, should be a duration for the job.
        jobs.append(job.Job(name, int(line)))
      i += 1

  return jobs
