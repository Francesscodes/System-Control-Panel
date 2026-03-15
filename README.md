System Control Panel 

A simple, lightweight GUI application built with Python and Tkinter that provides quick access to Windows system power commands. This tool replaces the need for navigating through multiple OS menus by placing Shutdown, Restart, and Logout functions into a single, stylized window.

Key Features

One-Click Power Actions: Execute system commands directly from the interface.

Clean GUI: A compact 300x200 window with a light blue background and high-contrast, color-coded buttons.

System Integration: Uses the Python os module to communicate directly with Windows shell commands.

Responsive Layout: Buttons are centered and styled for a modern feel using Tkinter's grid system.

 Command Breakdown
The application utilizes the following system-level commands:
Feature              	Action	                                       Technical Command
Shutdown	    Powers off the PC after a 1-second delay	                 shutdown /s /t 1
Restart      	Reboots the PC after a 1-second delay                       	shutdown /r /t 1
Logout	      Signs the current user out of the session	                      shutdown /l

Technical Stack
Language: Python 3.

Library: tkinter (Standard GUI library).

OS Module: Handles terminal command execution.

 Requirements & Setup
Operating System: This application is specifically designed for Windows (as it uses Windows-specific /s, /r, and /l flags).

Installation: No external libraries are required as Tkinter is included with standard Python installations.

Run the App:

Bash
python main.py
Warning: Ensure all work is saved before clicking the buttons, as the shutdown and restart commands are set to trigger almost immediately (1-second delay).

 Future Improvements
Timer Customization: Allow users to set a custom countdown for shutdown.

Confirmation Dialogs: Add a "Are you sure?" pop-up to prevent accidental clicks.

Cross-Platform Support: Implement commands for Linux (systemctl poweroff) and macOS.
