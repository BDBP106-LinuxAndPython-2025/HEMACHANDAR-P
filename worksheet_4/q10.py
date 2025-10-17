#!/usr/bin/python3
#
# 10. Short note on seeking within files:
# Seeking changes the file pointer’s position.
# It allows you to jump to a specific part of a file for reading or writing.
# Use file.seek(offset, whence) where whence is:
# 0: Beginning of file (default)
# 1: Current position
# 2: End of file