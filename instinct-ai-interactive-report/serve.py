#!/usr/bin/env python3
"""Run the Instinct interactive report on localhost with Python's standard library."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = None
    for port in range(8000, 8010):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), handler)
            break
        except OSError:
            continue
    if server is None:
        raise SystemExit("Ports 8000–8009 are unavailable. Free a port and try again.")
    url = f"http://127.0.0.1:{server.server_port}/"
    print(f"Instinct report running at {url}")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping local server.")
    finally:
        server.server_close()
