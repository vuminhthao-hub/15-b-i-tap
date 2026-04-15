import tkinter as tk
import random

# ===== HÀM XỬ LÝ =====
def xu_ly():
    result_box.delete(1.0, tk.END)

    try:
        n = int(entry_n.get())
        if n < 1 or n > 99:
            result_box.insert(tk.END, "❌ n phải từ 1 → 99\n")
            return
    except:
        result_box.insert(tk.END, "❌ Nhập n hợp lệ!\n")
        return

    # tạo mảng ngẫu nhiên
    arr = [random.randint(1, 9) for _ in range(n)]

    # phần tử phân biệt
    unique = sorted(set(arr))

    # hiển thị
    result_box.insert(tk.END, "👉 Mảng ban đầu:\n", "title")
    for x in arr:
        color = random.choice(colors)
        result_box.insert(tk.END, f"{x} ", color)

    result_box.insert(tk.END, "\n\n👉 Phần tử phân biệt:\n", "title")
    for x in unique:
        color = random.choice(colors)
        result_box.insert(tk.END, f"{x} ", color)


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("🌈 Array Color App")
root.geometry("520x420")

# nền
bg = tk.Frame(root, bg="#1e1e2f")
bg.pack(fill="both", expand=True)

card = tk.Frame(bg, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=360)

# tiêu đề
tk.Label(card,
         text="🎨 XỬ LÝ MẢNG",
         font=("Segoe UI", 16, "bold"),
         bg="white", fg="#6a11cb").pack(pady=10)

# nhập n
frame_input = tk.Frame(card, bg="white")
frame_input.pack()

tk.Label(frame_input, text="Nhập n:", bg="white").pack(side="left")

entry_n = tk.Entry(frame_input, width=10)
entry_n.pack(side="left", padx=5)

# nút
tk.Button(card,
          text="🚀 TẠO MẢNG",
          command=xu_ly,
          bg="#ff7a18",
          fg="white",
          font=("Segoe UI", 11, "bold"),
          relief="flat").pack(pady=10)

# text box
result_box = tk.Text(card,
                     height=12,
                     width=45,
                     font=("Consolas", 11),
                     bg="#f5f5f5")
result_box.pack()

# ===== MÀU NGẪU NHIÊN =====
colors = ["red", "blue", "green", "purple", "orange", "pink", "brown"]

for c in colors:
    result_box.tag_config(c, foreground=c)

result_box.tag_config("title", foreground="#6a11cb", font=("Segoe UI", 11, "bold"))

# footer
tk.Label(card,
         text="✨ Random Color Version",
         bg="white", fg="gray").pack(side="bottom", pady=5)

root.mainloop()