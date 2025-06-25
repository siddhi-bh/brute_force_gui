import tkinter as tk
from tkinter import messagebox
import time
import threading

# Simulated password list (like a small dictionary attack)
password_list = [
    "123456", "admin123", "letmein", "password", "secure123"
]

# Fake brute force logic
def brute_force(username, correct_password, log_output):
    for pwd in password_list:
        log_output.insert(tk.END, f"Trying: {pwd}\n")
        log_output.see(tk.END)
        time.sleep(0.5)
        if pwd == correct_password:
            log_output.insert(tk.END, f"\n✅ Password found: {pwd}\n")
            messagebox.showinfo("Success", f"Password found: {pwd}")
            return
    log_output.insert(tk.END, "\n❌ Failed to find the password.\n")
    messagebox.showerror("Failure", "Password not found.")

# Start button logic
def start_attack():
    username = username_entry.get()
    correct_password = password_entry.get()
    log_output.delete(1.0, tk.END)

    if not username or not correct_password:
        messagebox.showwarning("Input Error", "Please enter both fields.")
        return

    # Use a thread so the UI doesn't freeze
    threading.Thread(
        target=brute_force,
        args=(username, correct_password, log_output),
        daemon=True
    ).start()

# GUI Setup
root = tk.Tk()
root.title("Brute Force Login Simulation (Educational)")
root.geometry("450x400")

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Real Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Start Brute Force", command=start_attack, bg="orange").pack(pady=10)

log_output = tk.Text(root, height=12, width=50)
log_output.pack(pady=5)

root.mainloop()
