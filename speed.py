# Module for speed and acceleration
__all__ = ["Speed"]

def _wait_or_change(speed_obj):
  speed_obj.decel_rate if speed_obj.mode is "DECEL"  else speed_obj.accel_rate


class AccelerationModeChange(Exception):
  __name__ = "AccelerationModeChange"


class Speed:
  modes = ("ACCEL", "DECEL", "CONST")
  def __init__(speed, accel, accel_rate, terminal_velocity, decel_rate = accel_rate * 2):
