import tkinter as tk

# ===== HÀM TÍNH =====
def kiem_tra():
    try:
        n = int(entry_n.get())

        # vế trái
        ve_trai = sum(i**3 for i in range(3, n+1))

        # vế phải
        ve_phai = (n**2 * (n+1)**2) // 4

        # hiển thị
        result_left.config(text=f"Vế trái = {ve_trai}")
        result_right.config(text=f"Vế phải = {ve_phai}")

        if ve_trai == ve_phai:
            result_status.config(text="✅ ĐÚNG!", fg="#2ecc71")
        else:
            result_status.config(text="❌ SAI!", fg="#e74c3c")

    except:
        result_status.config(text="❌ Lỗi nhập!", fg="red")


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("📊 Kiểm tra công thức")
root.geometry("500x380")
root.configure(bg="#e8f5e9")  # xanh nhạt

# ===== HEADER =====
header = tk.Label(root,
                  text="📘 KIỂM TRA CÔNG THỨC",
                  font=("Arial", 16, "bold"),
                  bg="#2e7d32",
                  fg="white",
                  pady=10)
header.pack(fill="x")

# ===== KHUNG NHẬP =====
input_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
input_frame.pack(pady=15, padx=20, fill="x")

tk.Label(input_frame, text="Nhập n:", bg="white", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10)

entry_n = tk.Entry(input_frame, font=("Arial", 11))
entry_n.grid(row=0, column=1, padx=10)

btn = tk.Button(input_frame,
                text="▶ Kiểm tra",
                command=kiem_tra,
                bg="#43a047",
                fg="white",
                font=("Arial", 10, "bold"),
                relief="flat",
                padx=10)
btn.grid(row=0, column=2, padx=10)

# ===== KHUNG KẾT QUẢ =====
result_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_left = tk.Label(result_frame, text="Vế trái = ?", font=("Consolas", 12), bg="white")
result_left.pack(pady=10)

result_right = tk.Label(result_frame, text="Vế phải = ?", font=("Consolas", 12), bg="white")
result_right.pack(pady=10)

result_status = tk.Label(result_frame, text="", font=("Arial", 14, "bold"), bg="white")
result_status.pack(pady=15)

# ===== FOOTER =====
footer = tk.Label(root,
                  text="🌿 Green UI Version",
                  bg="#e8f5e9",
                  fg="#555")
footer.pack(pady=5)

root.mainloop()