class RegistrationSystem:

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student):
        self.students[student.student_id] = student
        print(f"Student '{student.name}' added.")

    def update_student_id(self, old_id, new_id):

        if old_id not in self.students:
            print("Student not found.")
            return

        if new_id in self.students:
            print("New ID already exists.")
            return

        student = self.students.pop(old_id)
        student.student_id = new_id
        self.students[new_id] = student

        print("Student ID updated successfully.")

    def notify_student(self, student, message):
        print(f"Notification for {student.name}: {message}")

    def register_student(self, student_id, course_id):

        student = self.students.get(student_id)
        course = self.courses.get(course_id)

        if not student:
            print("Student not found.")
            return

        if not course:
            print("Course not found.")
            return

        # Check duplicate registration
        if student in course.registered_students:
            self.notify_student(
                student,
                f"You are already registered for '{course.title}'."
            )
            return

        # Check seat availability
        if len(course.registered_students) >= course.max_seats:
            self.notify_student(
                student,
                f"Registration failed. '{course.title}' is full."
            )
            return

        # Register
        course.registered_students.append(student)

        self.notify_student(
            student,
            f"Successfully registered for '{course.title}'."
        )


    def view_courses(self):

        if not self.courses:
            print("No courses available.")
            return

        for course in self.courses.values():
            print(course)
            print("-" * 40)


    def view_registered_students(self, course_id):

        course = self.courses.get(course_id)

        if not course:
            print("Course not found.")
            return

        print(f"\nStudents enrolled in {course.title}:")

        for student in course.registered_students:
            print(student)