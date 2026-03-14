@echo off
setlocal

where python >nul 2>nul && set "MPREMOTE=python -m mpremote"

if not defined MPREMOTE (
	echo Could not find python/mpremote. Install it with: python -m pip install mpremote
	exit /b 1
)

%MPREMOTE% --help >nul 2>nul
if errorlevel 1 (
	echo python was found, but mpremote is not available.
	echo Install it with: python -m pip install mpremote
	exit /b 1
)

%MPREMOTE% cp demonstration_mode.py :main.py
%MPREMOTE% cp motors.py :motors.py
%MPREMOTE% cp playing_with_leds\larson_scanner.py :larson_scanner.py
%MPREMOTE% cp object_avoiding\wall_avoid_proportional.py :wall_avoid_proportional.py
%MPREMOTE% cp line_following\p_line_follower.py :p_line_follower.py
%MPREMOTE% cp 3rd_party\hcsr04.py :hcsr04.py

echo Demo file copied to the robot. Its ready to test!