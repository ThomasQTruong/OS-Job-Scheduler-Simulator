"""
 * trial_simulator.py
 * Simulates n amounts of trial for each algorithm.
 *
 * Copyright (c) 2024, Thomas Truong
"""

import job
import copy
from first_come_first_serve import FCFS
from shortest_job_first import SJF
from round_robin1 import RR
from random import randrange
import pandas as pd

RANDOM_CAP = 20  # The maximum number the random can be.
N = 20           # Number of trials.
COLUMNS = ["Job", "Start", "End", "Completed"]


def main():
  # Averages: FCFS, SJF, RR2, RR5
  averages = [[0, 0, 0, 0],  # 5 jobs.
              [0, 0, 0, 0],  # 10 jobs.
              [0, 0, 0, 0]]  # 15 jobs.
  i = 0
  for job_amount in range(5, 20, 5):
    for _ in range(N):
      jobs = generate_jobs(job_amount, RANDOM_CAP)
      jobs_copy = copy.deepcopy(jobs)
      averages[i][0] += calculate_average(pd.DataFrame(data=FCFS(jobs_copy),
                                             columns=COLUMNS), job_amount) / N
      jobs_copy = copy.deepcopy(jobs)
      jobs_copy.sort()
      averages[i][1] += calculate_average(pd.DataFrame(data=SJF(jobs_copy),
                                              columns=COLUMNS), job_amount) / N
      jobs_copy = copy.deepcopy(jobs)
      averages[i][2] += calculate_average(pd.DataFrame(data=RR(jobs_copy, 2),
                                              columns=COLUMNS), job_amount) / N
      jobs_copy = copy.deepcopy(jobs)
      averages[i][3] += calculate_average(pd.DataFrame(data=RR(jobs_copy, 5),
                                              columns=COLUMNS), job_amount) / N
    i += 1
  print_averages(averages)


def generate_jobs(n, random_cap):
  """
   * Generates n number of jobs with random duration.
   *
   * @param n - the number of jobs to generate.
   * @param random_cap - the maximum number the random can be.
   * @return list - the list of jobs generated.
  """
  jobs = []

  for i in range(n):
    jobs.append(job.Job(f"Job{i + 1}", randrange(1, random_cap + 1)))

  return jobs


def calculate_average(dataframe, jobs_length):
  """
   * Calculates the average for the dataframe.
   *
   * @param dataframe - the dataframe that contains the run history.
   * @param jobs_length - the amount of jobs.
   * @return float - the average turnaround time calculated.
  """
  return dataframe.where(dataframe[COLUMNS[3]])[COLUMNS[2]].sum() / jobs_length


def print_averages(averages):
  i = 5
  for arr in averages:
    print(f"{i} Jobs Average for {N} Trials:")
    print(f"FCFS: {round(arr[0], 2)}")
    print(f"SJF: {round(arr[1], 2)}")
    print(f"RR-2: {round(arr[2], 2)}")
    print(f"RR-5: {round(arr[3], 2)}")
    print()
    i += 5

if __name__ == "__main__":
  main()
