"""
Minimal Tkinter GUI front-end for Zehef.

This script launches the existing `zehef.py` in a subprocess using the
current Python interpreter and streams stdout/stderr into a scrolling
text widget. It keeps the GUI responsive by reading output in a background
thread and allows cancelling the running process.

Usage:
  python zehef_gui.py

Notes:
 - The GUI uses `sys.executable` to run `zehef.py` so it uses the same
   Python interpreter that started the GUI.
 - For a packaged app, you may want to run the bundled exe instead.
"""

import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import subprocess
import threading
import sys
import os


class ZehefGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zehef - GUI")
        self.geometry("800x480")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.proc = None

        self._build_widgets()

    def _build_widgets(self):
        frm = ttk.Frame(self)
        frm.pack(fill=tk.X, padx=8, pady=8)

        ttk.Label(frm, text="Email:").pack(side=tk.LEFT, padx=(0, 6))
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(frm, textvariable=self.email_var, width=50)
        self.email_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.run_btn = ttk.Button(frm, text="Run", command=self.start)
        self.run_btn.pack(side=tk.LEFT, padx=6)

        self.stop_btn = ttk.Button(frm, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT)

        # Output area
        self.output = ScrolledText(self, wrap=tk.WORD, state=tk.DISABLED)
        self.output.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))

        # Bind Enter in entry to start
        self.email_entry.bind('<Return>', lambda e: self.start())

    def _append(self, text):
        self.output.configure(state=tk.NORMAL)
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.output.configure(state=tk.DISABLED)

    def start(self):
        if self.proc and self.proc.poll() is None:
            self._append("A process is already running.\n")
            return

        email = self.email_var.get().strip()
        if not email:
            self._append("Please enter an email address.\n")
            return

        # Command: use the same interpreter that runs this GUI
        zehef_py = os.path.join(self.script_dir, 'zehef.py')
        if not os.path.exists(zehef_py):
            self._append(f"zehef.py not found in {self.script_dir}\n")
            return

        cmd = [sys.executable, zehef_py, email]
        self._append(f"Starting: {cmd}\n\n")

        try:
            # Request text mode with UTF-8 decoding and replace errors so
            # undecodable bytes won't raise a UnicodeDecodeError when the
            # child process emits bytes outside the console code page.
            # Python's Popen supports `encoding` and `errors` (3.6+).
            self.proc = subprocess.Popen(
                cmd,
                cwd=self.script_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,
            )
        except Exception as e:
            self._append(f"Failed to start process: {e}\n")
            return

        self.run_btn.configure(state=tk.DISABLED)
        self.stop_btn.configure(state=tk.NORMAL)

        t = threading.Thread(target=self._reader_thread, daemon=True)
        t.start()

    def _reader_thread(self):
        try:
            for line in self.proc.stdout:
                # marshal back to the main thread via after
                self.after(0, self._append, line)
        except Exception as e:
            self.after(0, self._append, f"Error reading output: {e}\n")

        rc = self.proc.wait()
        self.after(0, self._append, f"\nProcess exited with code {rc}\n")
        self.after(0, self._on_finish)

    def _on_finish(self):
        self.run_btn.configure(state=tk.NORMAL)
        self.stop_btn.configure(state=tk.DISABLED)
        self.proc = None

    def stop(self):
        if not self.proc:
            return
        if self.proc.poll() is None:
            try:
                self.proc.terminate()
                self._append("\nTermination requested.\n")
            except Exception as e:
                self._append(f"Failed to terminate process: {e}\n")


if __name__ == '__main__':
    app = ZehefGUI()
    app.mainloop()
