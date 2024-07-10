# CarbMonitor

Final project for CS50's web development with python and javascript.

# Common issues

If you encounter issues accessing the scripts folder when building your Docker container (especially on Windows), it may be due to your code editor using Windows-style line endings (CRLF) for shell scripts.

Fixing the Issue in VS Code:

1 - Open your script file (e.g., commands.sh or init_volumes.sh) in Visual Studio Code.

2 - Look at the bottom right corner of the VS Code status bar to check the current line ending format (CRLF or LF).

3 - Click on CRLF and select LF from the dialog that appears.

After making these changes, rebuild your Docker image to ensure the updates take effect.