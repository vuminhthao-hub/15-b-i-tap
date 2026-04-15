import tkinter as tk

# ===== HÀM XỬ LÝ =====
def xu_ly():
    result_box.delete(1.0, tk.END)

    s = entry.get()

    if len(s) == 0:
        result_box.insert(tk.END, "❌ Nhập chuỗi đi bro!\n")
        return

    if len(s) > 255:
        result_box.insert(tk.END, "❌ Chuỗi tối đa 255 ký tự!\n")
        return

    # bỏ dấu . và ,
    clean = s.replace(",", "").replace(".", "")

    # tách từ
    words = clean.split()

    # đếm số từ
    result_box.insert(tk.END, f"👉 Số từ: {len(words)}\n", "title")

    # thống kê độ dài từ (1 → 7)
    freq = [0]*8

    for w in words:
        l = len(w)
        if 1 <= l <= 7:
            freq[l] += 1

    result_box.insert(tk.END, "\n👉 Tần suất độ dài từ:\n", "title")

    for i in range(1, 8):
        result_box.insert(tk.END, f"{i}[{freq[i]}]  ", random_color())


# ===== RANDOM MÀU =====
import random
colors = ["red", "blue", "green", "purple", "orange", "pink"]

def random_color():
    return random.choice(colors)


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("🌈 Word Analyzer")
root.geometry("560x420")

bg = tk.Frame(root, bg="#16222A")
bg.pack(fill="both", expand=True)

card = tk.Frame(bg, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)

# tiêu đề
tk.Label(card,
         text="🎨 PHÂN TÍCH CHUỖI",
         font=("Segoe UI", 16, "bold"),
         bg="white", fg="#6a11cb").pack(pady=10)

# nhập chuỗi
entry = tk.Entry(card, width=50, font=("Segoe UI", 11))
entry.pack(pady=10)

# nút
tk.Button(card,
          text="🚀 PHÂN TÍCH",
          command=xu_ly,
          bg="#ff7a18",
          fg="white",
          font=("Segoe UI", 11, "bold"),
          relief="flat").pack(pady=5)

# kết quả
result_box = tk.Text(card,
                     height=10,
                     width=55,
                     font=("Consolas", 11),
                     bg="#f5f5f5")
result_box.pack(pady=10)

# màu
for c in colors:
    result_box.tag_config(c, foreground=c)

result_box.tag_config("title", foreground="#6a11cb", font=("Segoe UI", 11, "bold"))

# footer
tk.Label(card,
         text="✨ Color String Version",
         bg="white", fg="gray").pack(side="bottom", pady=5)

root.mainloop()