
from datetime import datetime

class Stopwatch:
    def __init__(self):
        self.start_time = None      # datetime when currently running
        self.elapsed = 0.0          # accumulated seconds while paused/stopped
        self.running = False
        self.ispaused = False

    def start(self):
        """Start fresh from 0."""
        if not self.running and not self.ispaused:
            self.start_time = datetime.now()
            self.elapsed = 0.0
            self.running = True

    def pause(self):
        """Pause and accumulate elapsed time."""
        if self.running and self.start_time is not None:
            delta = (datetime.now() - self.start_time).total_seconds()
            self.elapsed += delta
            self.start_time = None
            self.running = False
            self.ispaused = True

    def resume(self):
        """Resume from the accumulated elapsed time."""
        if not self.running:
            self.start_time = datetime.now()
            self.running = True

    def stop(self):
        """Stop (like pause) but keep elapsed time (final value)."""
        if self.running and self.start_time is not None:
            delta = (datetime.now() - self.start_time).total_seconds()
            self.elapsed += delta
        self.start_time = None
        self.running = False

    def reset(self):
        """Reset to zero."""
        self.start_time = None
        self.elapsed = 0.0
        self.running = False

    def get_total_seconds(self):
        total = self.elapsed
        if self.running and self.start_time is not None:
            total += (datetime.now() - self.start_time).total_seconds()
        return total

    def get_elapsed_time(self):

        total_seconds = int(self.get_total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"
