"""
 * job.py
 * The job with its basic information: name and duration.
 *
 * Copyright (c) 2024, Thomas Truong
"""

class Job:
  """
    The job with its basic information: name and duration.
  """
  name = ""      # Name of the job.
  duration = -1  # Duration left for the job to run.


  def __init__(self, name, duration):
    self.name = name
    self.duration = duration


  def run(self, duration):
    """
     * Runs the job.
     *
     * @param duration - the duration to run for.
     * @return int - the duration successfully ran.
    """

    # Cannot run any further: no duration left.
    if self.duration <= 0:
      return 0

    # Can run job, run job here.

    # Finished job, update the job's duration based on how long it ran for.
    elif self.duration < duration:
      # Cannot run full duration (not enough duration left for the job).
      time_spent = self.duration
      self.duration = 0
      return time_spent
    # Ran full duration.
    self.duration -= duration
    return duration
