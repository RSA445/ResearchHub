import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ResearchHub")
root.geometry("900x650")
root.configure(bg="#0a0f2c")
root.resizable(False, False)

# ========== أدوات مساعدة ==========
def hide_all_frames():
    for frame in all_frames:
        frame.pack_forget()

def show_frame(frame):
    hide_all_frames()
    frame.pack(fill='both', expand=True)

def create_labeled_entry(parent, label, show=None):
    frame = tk.Frame(parent, bg=parent['bg'])
    tk.Label(frame, text=label, bg=parent['bg'], fg="white", anchor='w', font=("Helvetica", 10, "bold")).pack(fill='x')
    entry = tk.Entry(frame, show=show, font=("Helvetica", 11), relief="flat", bd=2)
    entry.pack(fill='x', pady=5, ipady=5)
    frame.pack(pady=5, fill='x')
    return entry

def create_back_button(parent):
    return tk.Button(parent, text="← رجوع للرئيسية", command=lambda: show_frame(home_frame), bg="#444", fg="white", font=("Helvetica", 10, "bold"), width=20)

# ========== دوال النظام ==========
def login():
    email = login_email.get().strip()
    password = login_password.get().strip()
    if email == "taif" and password == "1234":
        messagebox.showinfo("Login", "مرحبًا بك Roz!")
        show_frame(home_frame)
    else:
        messagebox.showerror("خطأ", "البريد أو كلمة المرور غير صحيحة")

def signup():
    name = signup_name.get().strip()
    email = signup_email.get().strip()
    password = signup_password.get().strip()
    dob = signup_dob.get().strip()
    if all([name, email, password, dob]):
        messagebox.showinfo("تم", f"تم إنشاء حساب لـ {name}")
        show_frame(login_frame)
    else:
        messagebox.showerror("خطأ", "يرجى ملء جميع الحقول")

def reset_password():
    email = forgot_email.get().strip()
    if email:
        messagebox.showinfo("تم", f"تم إرسال رابط إعادة التعيين إلى {email}")
        show_frame(login_frame)
    else:
        messagebox.showerror("خطأ", "يرجى إدخال البريد الإلكتروني")

def logout():
    messagebox.showinfo("تسجيل الخروج", "تم تسجيل الخروج بنجاح.")
    show_frame(login_frame)

def show_search_results(query):
    results_win = tk.Toplevel(root)
    results_win.title("نتائج البحث")
    results_win.geometry("600x400")
    tk.Label(results_win, text=f"نتائج البحث لـ: {query}", font=("Helvetica", 14, "bold"), fg="#0a0f2c").pack(pady=10)
    for i in range(3):
        tk.Label(results_win, text=f"بحث {i+1}: الذكاء الاصطناعي في التعليم", font=("Helvetica", 11)).pack(anchor='w', padx=20, pady=3)

# ========== الإطارات ==========
login_frame = tk.Frame(root, bg="#0a0f2c")
signup_frame = tk.Frame(root, bg="#0a0f2c")
forgot_frame = tk.Frame(root, bg="#0a0f2c")
home_frame = tk.Frame(root, bg="#0a0f2c")
references_frame = tk.Frame(root, bg="#0a0f2c")
upload_frame = tk.Frame(root, bg="#0a0f2c")
profile_frame = tk.Frame(root, bg="#0a0f2c")
search_frame = tk.Frame(root, bg="#0a0f2c")
all_frames = [login_frame, signup_frame, forgot_frame, home_frame, references_frame, upload_frame, profile_frame, search_frame]

# ========== تسجيل الدخول ==========
login_box = tk.Frame(login_frame, bg="#162447", padx=30, pady=30)
login_box.pack(expand=True)
tk.Label(login_box, text="ResearchHub", font=("Helvetica", 26, "bold"), fg="white", bg="#162447").pack(pady=(0, 30))
login_email = create_labeled_entry(login_box, "البريد الإلكتروني")
login_password = create_labeled_entry(login_box, "كلمة المرور", show="*")
tk.Button(login_box, text="تسجيل الدخول", command=login, bg="#1e90ff", fg="white", width=30, height=2).pack(pady=10)
tk.Button(login_box, text="نسيت كلمة المرور؟", command=lambda: show_frame(forgot_frame), bg="#444", fg="white", width=30, height=2).pack(pady=5)
tk.Button(login_box, text="إنشاء حساب جديد", command=lambda: show_frame(signup_frame), bg="#444", fg="white", width=30, height=2).pack(pady=5)

# ========== إنشاء الحساب ==========
signup_box = tk.Frame(signup_frame, bg="#162447", padx=30, pady=30)
signup_box.pack(expand=True)
tk.Label(signup_box, text="إنشاء حساب جديد", font=("Helvetica", 22, "bold"), fg="white", bg="#162447").pack(pady=(0, 20))
signup_name = create_labeled_entry(signup_box, "الاسم")
signup_email = create_labeled_entry(signup_box, "البريد الإلكتروني")
signup_password = create_labeled_entry(signup_box, "كلمة المرور", show="*")
signup_dob = create_labeled_entry(signup_box, "تاريخ الميلاد")
tk.Button(signup_box, text="تسجيل الحساب", command=signup, bg="#28a745", fg="white", width=30, height=2).pack(pady=10)
create_back_button(signup_box).pack(pady=5)

# ========== نسيت كلمة المرور ==========
forgot_box = tk.Frame(forgot_frame, bg="#162447", padx=30, pady=30)
forgot_box.pack(expand=True)
tk.Label(forgot_box, text="نسيت كلمة المرور؟", font=("Helvetica", 22, "bold"), fg="white", bg="#162447").pack(pady=(0, 20))
forgot_email = create_labeled_entry(forgot_box, "أدخل بريدك الإلكتروني")
tk.Button(forgot_box, text="إرسال كلمة مرور جديدة", command=reset_password, bg="#f39c12", fg="white", width=30, height=2).pack(pady=10)
create_back_button(forgot_box).pack(pady=5)

# ========== الصفحة الرئيسية ==========
home_header = tk.Frame(home_frame, bg="#1b1f3b")
tk.Button(home_header, text="👤", command=lambda: show_frame(profile_frame), bg="#0f132b", fg="white", font=("Helvetica", 14), relief='flat').pack(side="right", padx=20)

menu_items = [
    ("🏠 الرئيسية", home_frame),
    ("📚 المراجع", references_frame),
    ("📥 رفع بحث", upload_frame),
    ("🔍 البحث", search_frame),
]
for text, frame in menu_items:
    tk.Button(home_header, text=text, command=lambda f=frame: show_frame(f), bg="#1b1f3b", fg="white", relief='flat', font=("Helvetica", 10, "bold"), padx=15).pack(side='left')

home_header.pack(fill='x', pady=(0,10))

features_frame = tk.Frame(home_frame, bg="#0a0f2c")
tk.Label(features_frame, text="مرحبًا Roz! 👋", font=("Helvetica", 18, "bold"), bg="#0a0f2c", fg="white").pack(pady=10)
tk.Label(features_frame, text="استكشف ميزات المنصة:", font=("Helvetica", 12), bg="#0a0f2c", fg="white").pack(pady=5)

cards = [
    ("🔍 البحث الذكي", "ابحث عن الأبحاث بسهولة وبسرعة"),
    ("📥 رفع الأبحاث", "قم برفع أبحاثك ومشاركتها"),
    ("📚 تنظيم المراجع", "إدارة مراجعك في مكان واحد"),
    ("📊 إحصائيات", "تابع تقدم أبحاثك وتحليلها")
]
for title, desc in cards:
    card = tk.Frame(features_frame, bg="#162447", padx=10, pady=10)
    tk.Label(card, text=title, font=("Helvetica", 12, "bold"), bg="#162447", fg="white").pack(anchor='w')
    tk.Label(card, text=desc, font=("Helvetica", 10), bg="#162447", fg="white").pack(anchor='w')
    card.pack(fill='x', padx=20, pady=5)

features_frame.pack(fill='both', expand=True)

# ========== إدارة المراجع ==========
tk.Label(references_frame, text="إدارة المراجع التقنية", font=("Helvetica", 18, "bold"), bg="#0a0f2c", fg="white").pack(pady=20)
refs = ["مقال: مستقبل البرمجة بلغة بايثون", "ورقة: تعلم الآلة في الصحة", "دراسة: تحليل البيانات الضخمة"]
for ref in refs:
    row = tk.Frame(references_frame, bg="#0a0f2c")
    tk.Label(row, text=ref, bg="#0a0f2c", fg="white", font=("Helvetica", 10)).pack(side='left', padx=10)
    tk.Button(row, text="تعديل", bg="#1e90ff", fg="white", width=10).pack(side='left', padx=5)
    tk.Button(row, text="حذف", bg="#dc3545", fg="white", width=10).pack(side='left', padx=5)
    row.pack(pady=5)
create_back_button(references_frame).pack(pady=20)

# ========== رفع الأبحاث ==========
tk.Label(upload_frame, text="رفع بحث تقني جديد", font=("Helvetica", 18, "bold"), bg="#0a0f2c", fg="white").pack(pady=20)
create_labeled_entry(upload_frame, "عنوان البحث")
create_labeled_entry(upload_frame, "المجال التقني")
create_labeled_entry(upload_frame, "الوصف")
tk.Button(upload_frame, text="اختيار ملف PDF", bg="#1e90ff", fg="white", width=30).pack(pady=10)
tk.Button(upload_frame, text="رفع البحث", bg="#28a745", fg="white", width=30, height=2).pack(pady=5)
create_back_button(upload_frame).pack(pady=20)

# ========== الملف الشخصي ==========
tk.Label(profile_frame, text="الملف الشخصي للمستخدم", font=("Helvetica", 18, "bold"), bg="#0a0f2c", fg="white").pack(pady=20)
profile_data = {
    "الاسم": "Roz",
    "البريد الإلكتروني": "roz@nu.edu.sa",
    "الجامعة": "جامعة نجران",
    "الاهتمامات": "الذكاء الاصطناعي - تطوير الويب"
}
for label, value in profile_data.items():
    tk.Label(profile_frame, text=f"{label}: {value}", font=("Helvetica", 12), bg="#0a0f2c", fg="white").pack(anchor='w', padx=20, pady=5)
tk.Button(profile_frame, text="تعديل البيانات", bg="#1e90ff", fg="white", width=20).pack(pady=10)
create_back_button(profile_frame).pack(pady=20)

# ========== البحث ==========
search_box = tk.Frame(search_frame, bg="#0a0f2c")
search_box.pack(pady=20)
tk.Label(search_box, text="البحث", font=("Helvetica", 18, "bold"), bg="#0a0f2c", fg="white").pack(pady=10)
search_entry = tk.Entry(search_box, font=("Helvetica", 12), width=50)
search_entry.pack(pady=10, ipady=5)
tk.Button(search_box, text="بحث", command=lambda: show_search_results(search_entry.get()), bg="#1e90ff", fg="white", width=30).pack(pady=10)

# بدء التطبيق
show_frame(login_frame)
root.mainloop()