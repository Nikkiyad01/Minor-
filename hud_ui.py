import customtkinter as ctk
import math

# Global variables
app = None
canvas = None
angle = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def animate():
    global angle, canvas, app
    if app is None or canvas is None:
        return

    canvas.delete("all")

    cx, cy = 190, 190
    radii = [150, 110, 70]

    for r in radii:
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r,
                           outline="#00E5FF", width=3)

    x = cx + 150 * math.cos(math.radians(angle))
    y = cy + 150 * math.sin(math.radians(angle))

    canvas.create_line(cx, cy, x, y, fill="#00E5FF", width=3)

    angle += 3
    angle %= 360

    app.after(30, animate)


def start_hud():
    global app, canvas

    # WINDOW SETUP
    app = ctk.CTk()
    app.title("Iron Man HUD")
    app.geometry("420x620")

    # TITLE
    title = ctk.CTkLabel(
        app,
        text="J.A.R.V.I.S SYSTEM ONLINE",
        font=("Orbitron", 26, "bold"),
        text_color="#00E5FF"
    )
    title.pack(pady=10)

    # CANVAS
    canvas = ctk.CTkCanvas(
        app,
        width=380,
        height=380,
        bg="black",
        highlightthickness=0
    )
    canvas.pack(pady=10)

    # Start Animation
    animate()

    # STATUS TEXT
    status = ctk.CTkLabel(
        app,
        text="Scanning...",
        font=("Consolas", 20),
        text_color="#00E5FF"
    )
    status.pack(pady=5)

    # FOOTER
    footer = ctk.CTkLabel(
        app,
        text="Iron Man HUD   v1.0",
        font=("Consolas", 14),
        text_color="#0099FF"
    )
    footer.pack(pady=10)

    app.mainloop()
