import tkinter as tk
import random

# ===== HÀM XỬ LÝ =====
def xu_ly():
    result_box.delete(1.0, tk.END)

    try:
        n = int(entry_n.get())
        m = int(entry_m.get())
        if n <= 0 or m <= 0:
            result_box.insert(tk.END, "❌ n, m phải > 0\n")
            return
    except:
        result_box.insert(tk.END, "❌ Nhập n, m hợp lệ!\n")
        return

    # tạo ma trận random [-100,100]
    A = [[random.randint(-100, 100) for _ in range(m)] for _ in range(n)]

    # in ma trận A
    result_box.insert(tk.END, "👉 Ma trận A:\n", "title")
    for i in range(n):
        for j in range(m):
            color = random.choice(colors)
            result_box.insert(tk.END, f"{A[i][j]:4}", color)
        result_box.insert(tk.END, "\n")

    # tạo ma trận B
    B = [[0]*m for _ in range(n)]

    # kiểm tra cực tiểu
    for i in range(n):
        for j in range(m):
            is_min = True

            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < n and 0 <= y < m:
                        if (x != i or y != j) and A[x][y] <= A[i][j]:
                            is_min = False

            if is_min:
                B[i][j] = 1

    # in ma trận B
    result_box.insert(tk.END, "\n👉 Ma trận cực tiểu:\n", "title")
    for i in range(n):
        for j in range(m):
            if B[i][j] == 1:
                result_box.insert(tk.END, f"{B[i][j]:4}", "min")
            else:
                result_box.insert(tk.END, f"{B[i][j]:4}", "zero")
        result_box.insert(tk.END, "\n")


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("🌈 Matrix Min Finder")
root.geometry("560x460")

bg = tk.Frame(root, bg="#141e30")
bg.pack(fill="both", expand=True)

card = tk.Frame(bg, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

# tiêu đề
tk.Label(card,
         text="🎨 MA TRẬN CỰC TIỂU",
         font=("Segoe UI", 16, "bold"),
         bg="white", fg="#6a11cb").pack(pady=10)

# nhập n m
frame_input = tk.Frame(card, bg="white")
frame_input.pack()

tk.Label(frame_input, text="n:", bg="white").pack(side="left")
entry_n = tk.Entry(frame_input, width=5)
entry_n.pack(side="left", padx=5)

tk.Label(frame_input, text="m:", bg="white").pack(side="left")
entry_m = tk.Entry(frame_input, width=5)
entry_m.pack(side="left", padx=5)

# nút
tk.Button(card,
          text="🚀 TẠO MA TRẬN",
          command=xu_ly,
          bg="#ff7a18",
          fg="white",
          font=("Segoe UI", 11, "bold"),
          relief="flat").pack(pady=10)

# text box
result_box = tk.Text(card,
                     height=15,
                     width=55,
                     font=("Consolas", 11),
                     bg="#f4f4f4")
result_box.pack()

# ===== MÀU =====
colors = ["red", "blue", "green", "purple", "orange"]

for c in colors:
    result_box.tag_config(c, foreground=c)

result_box.tag_config("title", foreground="#6a11cb", font=("Segoe UI", 11, "bold"))
result_box.tag_config("min", foreground="#ff4081", font=("Consolas", 11, "bold"))
result_box.tag_config("zero", foreground="#999")

# footer
tk.Label(card,
         text="✨ Color Matrix Version",
         bg="white", fg="gray").pack(side="bottom", pady=5)

root.mainloop()