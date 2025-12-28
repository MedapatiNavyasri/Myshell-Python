 **MyShell🖥️**
A custom Command Line Interpreter (CLI) built from scratch using Python. This project demonstrates core Operating System concepts, including process management, environment state handling, and the REPL architecture.
## 🚀 Overview
MyShell is a functional terminal interface that bridges the gap between the user and the Operating System. It can execute standard system commands (like ls, dir, mkdir) while providing custom "built-in" utilities for enhanced diagnostics.
## ✨ Key Features
### REPL Architecture: Implements the standard Read-Evaluate-Print-Loop cycle.
### Process Management: Spawns and manages child processes for external binaries using the subprocess module.
### Stateful Navigation: Correctly handles directory changes (cd) by modifying the parent process environment.
### Custom Built-ins:history: Tracks and displays all commands used in the current session.
### sysinfo: Displays real-time OS version, hardware architecture, and network node information.
### Signal Handling: Gracefully manages Ctrl+C (Interrupts) and Ctrl+D (EOF) to prevent crashes.
## 🛠️ Technical Concepts ExploredTokenization: Parsing raw string input into executable argument arrays.
### Process Isolation: Understanding why the shell remains stable even if a child process fails.
### Environment Variables: Interfacing with the os and platform modules to retrieve system data.
### Cross-Platform Compatibility: Logic designed to run on both Windows (CMD/PowerShell) and Unix-based systems.
## 💻 Installation & Usage
1. Run from SourceIf you have Python installed:Bashpython myshell.py
2. Run Standalone BinaryCheck the Releases section to download the standalone .exe (Windows) or binary (Linux/Mac) which runs without needing a Python installation.
