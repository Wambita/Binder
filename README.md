# Merge: A Study in Executable Encapsulation

## 1. Introduction

 Merge, a  **binary binder** is an educational cybersecurity tool designed to explore the mechanics of file structures, process spawning, and binary manipulation on Linux systems. It demonstrates how multiple independent programs can be bundled into a single executable "wrapper" and extracted during runtime.

### Why This Project?

Understanding binders is critical for both software distribution (creating self-extracting installers) and malware analysis (identifying dropper patterns). This project provides hands-on experience with:

* **Binary File I/O:** Handling raw bytes to prevent data corruption.
* **Runtime Extraction:** Managing temporary filesystems for execution.
* **Process Orchestration:** Using sub-processes to manage execution flow.

---

## 2. Features

* **Native Sequential Execution:** Guarantees that binary A finishes before binary B begins.
* **Zero-Trace Execution:** Utilizes system memory and temporary directories to ensure the host system remains clean post-execution.
* **Automatic Permission Handling:** Dynamically assigns executable bits (`+x`) to internal payloads during the extraction phase.
* **Format Agnostic:** Capable of binding any file type (scripts, compiled binaries, or assets) provided the stub is configured for the environment.

---

## 3. Technical Architecture

The tool uses a **Stub-and-Payload** architecture. The final output is a single file containing a Python-based execution engine followed by raw binary data segments.

### The Breakdown:

1. **The Stub:** The "brains" of the operation. It reads its own source code, identifies the location of the payloads using a **Magic Delimiter**, and handles the extraction logic.
2. **Magic Delimiter:** A unique 18-byte sequence (`b"--MAGIC_DELIMITER--"`) used as a boundary marker to prevent data overlap.
3. **Payloads:** The original binaries are appended as raw bytes, preserving their integrity regardless of the original encoding.

---

## 4. Getting Started

### Prerequisites

* **Environment:** Linux (Ubuntu/Debian recommended).
* **Language:** Python 3.8+.
* **Isolation:** It is highly recommended to run this in a **Virtual Machine (VM)** or **Docker Container** to isolate execution from your primary host.

### Installation & Usage

```bash
# Clone the repository
git clone https://github.com/Wambita/Binder.git
cd merge

# Set permissions
chmod +x merge.py

# Bind two files
./merge.py bin1.py bin2.py -o bundled_app #you can use any 2 binary python files you have  with code, I provided a sample for demonstration purposes.

# Run the result
./bundled_app

```

---

## 5. Security & Ethical Considerations

### Role Play: Binary Analyst Perspective

In a professional setting, binary modification must be handled with strict adherence to legal and ethical frameworks.

* **Ethical Use:** This tool should only be used on systems where the user has explicit authorization.
* **Malware Analysis:** Recognizing these patterns is essential for developing EDR (Endpoint Detection and Response) signatures that flag suspicious file extractions in `/tmp` directories.
* **Integrity:** Always verify binaries using SHA-256 hashes to ensure they haven't been tampered with by unauthorized binders.

---

## 6. Implementation Challenges

* **Text vs. Binary Mode:** One of the primary hurdles was ensuring files were read in `rb` mode. Reading compiled ELF files in text mode causes character decoding failures.
* **Cross-Platform Paths:** Using the `os` and `tempfile` modules was essential to ensure the stub works across different Linux distributions without hardcoding paths.

---

## 7. Future Enhancements (Bonuses)

* **[ ] GUI Wrapper:** A Tkinter or PyQt interface for drag-and-drop binding.
* **[ ] Multi-Format Support:** Adding logic to detect if a payload is an ELF or a Script and adjusting the `subprocess` call accordingly.
* **[ ] Encryption:** Encrypting the payloads at rest and decrypting them in memory during runtime.

---

## 8. Author & License

**Lead Developer:** Sheila Fana
**Project Date:** March 2026

### License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this tool for educational purposes.

---

### Disclaimer

**For Educational Purposes Only.** Unauthorized use of these techniques on systems without permission is illegal and unethical. The author assumes no liability for misuse.
