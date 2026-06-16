class Admin:
    def __init__(self, ad_name):
        self.admin_name = ad_name

    def add_course(self, R1, course):
        R1.courses[course.course_id] = course
        print(f"Course '{course.title}' added successfully.")

    def update_course(self, R1, course_id,
                      title=None, description=None, max_seats=None):

        course = R1.courses.get(course_id)

        if not course:
            print("Course not found.")
            return

        if title:
            course.title = title

        if description:
            course.description = description

        if max_seats:
            if max_seats < len(course.R1):
                print("Cannot reduce seats below current enrollment.")
                return
            course.max_seats = max_seats

        print("Course updated successfully.")








