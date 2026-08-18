#!/usr/bin/env python3
"""How Cybersecurity Works - Development Server Launcher"""
import subprocess
import sys
import os

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.environ['PYTHONPATH'] = os.getcwd()

    print("=" * 60)
    print("  How Cybersecurity Works - Daily Reading Platform")
    print("=" * 60)
    print()
    print("  Starting server at http://127.0.0.1:8000")
    print("  Press Ctrl+C to stop")
    print()

    try:
        subprocess.run(
            [sys.executable, '-m', 'uvicorn', 'backend.main:app',
             '--host', '127.0.0.1', '--port', '8000'],
            cwd=os.getcwd(),
        )
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    main()
