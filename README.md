# Blender 3D Background Autosaver

## Description

This is a Python script for Blender 3D that automatically saves your work at regular intervals. The auto-save happens in the background so it won't interrupt your workflow. It creates a new .blend file each time it saves, providing version control and allowing you to revert to a previous version if necessary. The name of the saved file includes the timestamp of when it was saved.

## Purpose

The purpose of this script is to minimize the risk of losing work due to unforeseen circumstances such as software crashes or accidental oversights in manual saving. Regular auto-saving can be a lifesaver in many situations.

## Installation

To install this script, follow these steps:

1. Download the Python script from the repository.
2. Open your Blender project.
3. Navigate to the Scripting tab and click on "New" to create a new script.
4. Copy and paste the contents of the downloaded Python script into the scripting area.
5. Press the "Run Script" button to start the auto-save functionality.
6. Save your Blender file in your desired location. This is a crucial step as the autosave script will save new versions in the same directory as the original file. If you do not save your file, the autosave versions will be stored in a temporary directory.


Once installed, the script will automatically start saving your work every 30 minutes.

## Configuration

The auto-save interval can be adjusted to meet your requirements. Here's how to do it:

1. In the `execute()` function, find the line `self._timer = wm.event_timer_add(30.0, window=context.window)`.
2. Change `30.0` to the number of seconds you want between each time check. For example, to check every minute, change it to `60.0`.
3. In the `modal()` function, find the line `if self._cycles > 60:`.
4. Change `60` to the number of checks you want to wait before saving. This should be equal to your desired auto-save interval (in minutes) multiplied by two. For example, to save every 15 minutes (assuming you set the timer to check every minute as in step 2), change it to `30`.

Please note that decreasing the time interval between checks will increase the script's usage of system resources. Adjust according to your system's capabilities.
