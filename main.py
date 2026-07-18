"""
SehatSaathi — Main Entry Point
Launches the Flask web server for local hosting.
Open http://127.0.0.1:5000 in your browser after running.
"""
import sys
# Block the broken TensorFlow installation from being imported by mediapipe.
# Must be set BEFORE importing app.py (which imports mediapipe via detection/).
sys.modules['tensorflow'] = None

import os
import webbrowser
import threading
import time


def main():
    """Start the Flask web server and open the browser."""
    # Ensure we're in the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    host = "127.0.0.1"
    port = 5000

    print("=" * 58)
    print("  SehatSaathi — AI-Powered Disease Screening")
    print("=" * 58)
    print()
    print(f"  Starting local web server...")
    print(f"  URL: http://{host}:{port}")
    print()
    print("  Press Ctrl+C to stop the server.")
    print("=" * 58)
    print()

    # Open the browser after a short delay (give Flask time to start)
    def open_browser():
        time.sleep(2)
        webbrowser.open(f"http://{host}:{port}")

    threading.Thread(target=open_browser, daemon=True).start()

    # Import and run the Flask app
    from app import app
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=False)


if __name__ == "__main__":
    main()
