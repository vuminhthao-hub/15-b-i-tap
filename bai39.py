import tkinter as tk

# ===== HÀM XỬ LÝ =====
def tim_bo():
    result_box.delete(1.0, tk.END)

    for a in range(1, 100):
        for b in range(a+1, 100):
            for c in range(b+1, 100):
                if a*a + b*b == c*c:

                    if b == a+1 and c == b+1:
                        result_box.insert(tk.END, f"({a}, {b}, {c}) - Liên tiếp\n")

                    elif a%2==0 and b%2==0 and c%2==0 and b==a+2 and c==b+2:
                        result_box.insert(tk.END, f"({a}, {b}, {c}) - Chẵn liên tiếp\n")


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("Tìm bộ số")

btn = tk.Button(root, text="Tìm", command=tim_bo)
btn.pack()

# 👉 TẠO result_box Ở ĐÂY
result_box = tk.Text(root, height=15, width=50)
result_box.pack()

root.mainloop()
