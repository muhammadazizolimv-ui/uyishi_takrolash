students = {}


def add_student():
    """Yangi talaba qo'shadi."""
    name = input("Ism: ").strip()
    while True:
        age_input = input("Yosh: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Yosh raqam bo'lishi kerak.")

    students[name] = age
    print(f"{name} talaba sifatida qo'shildi.")


def view_students():
    """Barcha talabalarni ko'rsatadi."""
    if not students:
        print("Talabalar mavjud emas.")
        return

    print("Talabalar:")
    for name, age in students.items():
        print(f"- {name}: {age} yosh")


def average_age():
    """Talabalar o'rtacha yoshini hisoblaydi."""
    if not students:
        print("Talabalar mavjud emas.")
        return

    avg_age = sum(students.values()) / len(students)
    print(f"O'rtacha yosh: {avg_age}")


while True:
    print("1. Talaba qo'shish")
    print("2. Talabalarni ko'rish")
    print("3. O'rtacha yoshni hisoblash")
    print("4. Chiqish")

    choice = input("Tanlov: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_age()
    elif choice == "4":
        print("Dastur yakunlandi.")
        break
    else:
        print("Noto'g'ri tanlov! Iltimos 1 dan 4 gacha raqam kiriting.")
