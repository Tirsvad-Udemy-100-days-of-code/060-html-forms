"""!
@file smtp_sink.py
@brief A tiny local SMTP server that keeps what it receives, for screenshots.

It speaks just enough SMTP (EHLO, MAIL, RCPT, DATA, QUIT) for smtplib, and shows
the received messages as plain text on a small web page, so a screenshot can
prove that the contact form really delivered an email. It listens on local
addresses only and never relays anything.

Usage: python smtp_sink.py [smtp_port] [http_port]
"""

import socketserver
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

LOCAL_HOST = "127.0.0.1"
DEFAULT_SMTP_PORT = 1025
DEFAULT_HTTP_PORT = 8025

INBOX: list[str] = []
INBOX_LOCK = threading.Lock()


class SmtpHandler(socketserver.StreamRequestHandler):
    """!@brief Handle one SMTP conversation."""

    def reply(self, text: str) -> None:
        """!
        @brief Send one reply line.
        @param text Reply including the status code.
        """
        self.wfile.write(f"{text}\r\n".encode())

    def handle(self) -> None:
        """!@brief Answer SMTP commands until the client quits."""
        self.reply("220 smtp-sink ready")
        while True:
            line = self.rfile.readline().decode("utf-8", "replace").strip()
            command = line.upper()
            if not line or command.startswith("QUIT"):
                self.reply("221 bye")
                return
            if command.startswith("EHLO") or command.startswith("HELO"):
                self.reply("250 smtp-sink")
            elif command.startswith("DATA"):
                self.reply("354 end with a line holding a single dot")
                self.store(self.read_data())
                self.reply("250 stored")
            else:
                self.reply("250 ok")

    def read_data(self) -> str:
        """!
        @brief Read the message body up to the single-dot line.
        @return The message text.
        """
        lines: list[str] = []
        while True:
            line = self.rfile.readline().decode("utf-8", "replace").rstrip("\r\n")
            if line == "." or not line and self.rfile.closed:
                break
            lines.append(line[1:] if line.startswith("..") else line)
        return "\n".join(lines)

    def store(self, text: str) -> None:
        """!
        @brief Keep a received message.
        @param text The message text.
        """
        with INBOX_LOCK:
            INBOX.append(text)
        print("received a message of", len(text), "characters", flush=True)


class InboxPage(BaseHTTPRequestHandler):
    """!@brief Show the received messages as plain text."""

    def do_GET(self) -> None:  # noqa: N802 - name fixed by http.server
        """!@brief Answer every GET with the inbox."""
        with INBOX_LOCK:
            body = "\n\n----\n\n".join(INBOX) or "(no mail received yet)"
        data = f"Inbox of the local mail sink\n\n{body}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        """!
        @brief Keep the console quiet.
        @param format Unused.
        @param args Unused.
        """


def main() -> int:
    """!
    @brief Start the SMTP and web servers.
    @return Never returns normally.
    """
    smtp_port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SMTP_PORT
    http_port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_HTTP_PORT
    web = HTTPServer((LOCAL_HOST, http_port), InboxPage)
    threading.Thread(target=web.serve_forever, daemon=True).start()
    with socketserver.ThreadingTCPServer((LOCAL_HOST, smtp_port), SmtpHandler) as smtp:
        smtp.daemon_threads = True
        smtp.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
