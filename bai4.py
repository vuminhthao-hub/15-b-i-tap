import tkinter as tk
import math

# ===== HÀM XỬ LÝ =====
def xu_ly():
    result_label.config(text="", fg="black")

    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
    except:
        result_label.config(text="❌ Nhập số hợp lệ!", fg="red")
        return

    # ===== KIỂM TRA TAM GIÁC =====
    if a + b <= c or a + c <= b or b + c <= a:
        result_label.config(text="❌ Không phải tam giác!", fg="red")
        return

    # ===== XÁC ĐỊNH LOẠI TAM GIÁC =====
    if a == b == c:
        loai = "Tam giác đều"
    elif a == b or b == c or a == c:
        loai = "Tam giác cân"
    elif abs(a*a + b*b - c*c) < 1e-6 or \
         abs(a*a + c*c - b*b) < 1e-6 or \
         abs(b*b + c*c - a*a) < 1e-6:
        loai = "Tam giác vuông"
    else:
        loai = "Tam giác thường"

    # ===== TÍNH DIỆN TÍCH (HERON) =====
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # ===== HIỂN THỊ =====
    result_label.config(
        text=f"{loai}\nDiện tích S = {S:.2f}",
        fg="green"
    )

# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("Tam giác")
root.geometry("350x300")
root.configure(bg="#f5f5f5")

tk.Label(root,
         text="KIỂM TRA TAM GIÁC",
         font=("Arial", 14, "bold"),
         bg="#f5f5f5").pack(pady=10)

frame_input = tk.Frame(root, bg="#f5f5f5")
frame_input.pack()

# nhập a
tk.Label(frame_input, text="Cạnh a:", bg="#f5f5f5").grid(row=0, column=0)
entry_a = tk.Entry(frame_input, width=10)
entry_a.grid(row=0, column=1)

# nhập b
tk.Label(frame_input, text="Cạnh b:", bg="#f5f5f5").grid(row=1, column=0)
entry_b = tk.Entry(frame_input, width=10)
entry_b.grid(row=1, column=1)

# nhập c
tk.Label(frame_input, text="Cạnh c:", bg="#f5f5f5").grid(row=2, column=0)
entry_c = tk.Entry(frame_input, width=10)
entry_c.grid(row=2, column=1)

# nút
tk.Button(root,
          text="Kiểm tra",
          bg="#4CAF50",
          fg="white",
          font=("Arial", 10, "bold"),
          command=xu_ly).pack(pady=10)

# kết quả
result_label = tk.Label(root, text="", bg="#f5f5f5", font=("Arial", 12))
result_label.pack()

root.mainloop()
