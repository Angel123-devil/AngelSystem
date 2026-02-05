import tkinter as tk
from tkinter import messagebox
import time
import random

# ================== LOGIN SCREEN ==================
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("AngelSystem Login")

root.protocol("WM_DELETE_WINDOW", lambda: None)
root.bind("<Alt-F4>", lambda e: "break")
root.bind("<Escape>", lambda e: "break")

login_frame = tk.Frame(root, bg="black")
login_frame.pack(expand=True)

tk.Label(
    login_frame,
    text="➤ ANGEL SYSTEM",
    fg="white",
    bg="black",
    font=("Ubuntu", 42, "bold")
).pack(pady=20)

tk.Label(
    login_frame,
    text="User: angel",
    fg="gray",
    bg="black",
    font=("Ubuntu", 14)
).pack(pady=5)

pwd = tk.Entry(login_frame, show="*", font=("Ubuntu", 16))
pwd.pack(pady=10)

def login():
    if pwd.get() == "angel":
        login_frame.destroy()
        start_desktop()
    else:
        messagebox.showerror("Login Failed", "Wrong password")

tk.Button(
    login_frame,
    text="Login",
    font=("Ubuntu", 14),
    command=login
).pack(pady=10)

# ================== DESKTOP ==================
def start_desktop():
    dark_mode = True
    internet_connected = True

    bg_dark = "#2c001e"
    bg_light = "#f2f2f2"

    root.configure(bg=bg_dark)

    # ===== TOP BAR =====
    top = tk.Frame(root, bg="#1e1e1e", height=32)
    top.pack(fill="x", side="top")

    title = tk.Label(
        top, text="➤ AngelSystem 3.1",
        fg="white", bg="#1e1e1e", font=("Ubuntu", 10)
    )
    title.pack(side="left", padx=10)

    status = tk.Label(
        top, text="🌐 Connected  |  🛡 Protected",
        fg="lightgreen", bg="#1e1e1e", font=("Ubuntu", 10)
    )
    status.pack(side="left", padx=20)

    clock = tk.Label(top, fg="white", bg="#1e1e1e")
    clock.pack(side="right", padx=10)

    def tick():
        clock.config(text=time.strftime("%H:%M:%S"))
        root.after(1000, tick)
    tick()

    # ===== THEME TOGGLE =====
    def toggle_theme():
        nonlocal dark_mode
        dark_mode = not dark_mode
        desktop.configure(bg=bg_dark if dark_mode else bg_light)

    tk.Button(
        top, text="🌙 / ☀",
        bg="#1e1e1e", fg="white",
        bd=0, command=toggle_theme
    ).pack(side="right", padx=10)

    # ===== DESKTOP =====
    desktop = tk.Canvas(root, bg=bg_dark, highlightthickness=0)
    desktop.pack(fill="both", expand=True)

    # ===== WALLPAPER =====
    desktop.create_text(
        root.winfo_screenwidth()//2,
        root.winfo_screenheight()//2 - 80,
        text="➤",
        fill="#ff5500",
        font=("Ubuntu", 260, "bold")
    )

    desktop.create_text(
        root.winfo_screenwidth()//2,
        root.winfo_screenheight()//2 + 120,
        text="ANGEL SYSTEM",
        fill="white",
        font=("Ubuntu", 48, "bold")
    )

    # ================= SYSTEM MONITOR =================
    def system_monitor():
        m = tk.Toplevel(root)
        m.title("System Monitor")
        m.geometry("420x300")

        cpu = tk.Label(m, font=("Ubuntu", 12))
        ram = tk.Label(m, font=("Ubuntu", 12))
        disk = tk.Label(m, font=("Ubuntu", 12))

        cpu.pack(pady=10)
        ram.pack(pady=10)
        disk.pack(pady=10)

        def update():
            cpu.config(text=f"CPU Usage: {random.randint(5,90)}%")
            ram.config(text=f"RAM Usage: {random.randint(20,85)}%")
            disk.config(text=f"Disk Activity: {random.randint(1,70)}%")
            m.after(1000, update)

        update()

    # ================= SECURITY =================
    def security():
        s = tk.Toplevel(root)
        s.title("Security By Angel.exe")
        s.geometry("520x360")
        s.configure(bg="black")

        tk.Label(
            s,
            text="SECURITY BY ANGEL",
            fg="red",
            bg="black",
            font=("Consolas", 22, "bold")
        ).pack(pady=15)

        info = tk.Label(
            s,
            text="Firewall: ACTIVE\nSystem Protection: ENABLED\nThreats Blocked: 1024",
            fg="white",
            bg="black",
            font=("Consolas", 12)
        )
        info.pack(pady=10)

        def scan():
            messagebox.showinfo(
                "Scan Complete",
                "No threats found.\nAngelSystem is fully protected."
            )

        tk.Button(
            s,
            text="Run Deep Scan",
            bg="red",
            fg="white",
            font=("Arial", 12),
            command=scan
        ).pack(pady=20)

    # ================= AI ASSISTANT =================
    def ai_angel():
        a = tk.Toplevel(root)
        a.title("Angel AI Assistant")
        a.geometry("500x350")

        chat = tk.Text(a, state="disabled", wrap="word")
        chat.pack(expand=True, fill="both")

        entry = tk.Entry(a)
        entry.pack(fill="x")

        def respond():
            msg = entry.get().lower()
            entry.delete(0, "end")

            if "hello" in msg:
                reply = "Hello. AngelSystem is running perfectly."
            elif "system" in msg:
                reply = "All systems are secured and stable."
            elif "internet" in msg:
                reply = "Internet status: Connected (offline simulation)."
            elif "security" in msg:
                reply = "Security By Angel is active. No threats detected."
            else:
                reply = "Command not recognized. Type 'help'."

            chat.config(state="normal")
            chat.insert("end", f"You: {msg}\nAngel: {reply}\n\n")
            chat.config(state="disabled")

        entry.bind("<Return>", lambda e: respond())

    # ================= DOCK =================
    dock = tk.Frame(desktop, bg="#1e1e1e")
    dock.place(relx=0.5, rely=0.93, anchor="center")

    apps = [
        ("📊", system_monitor),
        ("🛡", security),
        ("🧠", ai_angel),
    ]

    for icon, cmd in apps:
        tk.Button(
            dock,
            text=icon,
            font=("Arial", 20),
            bg="#1e1e1e",
            fg="white",
            bd=0,
            width=3,
            command=cmd
        ).pack(side="left", padx=10, pady=6)

root.mainloop()
