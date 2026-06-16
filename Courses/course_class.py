class Course:
    def __init__(self, v1, v2, v3, v4, v5):
        self.course_id = v1
        self.title = v2
        self.description = v3
        self.max_seats = v4
        self.current_enroll=v5
        self.registered_students = []

    def available_seat(self):
        return self.max_seats-len(self.registered_students)

    def __str__(self):
        return(f"\nCourse_id: {self.course_id}"
               f"\nTitle: {self.title}"
               f"\nDescription: {self.description}"
               f"\nMax_Seats: {self.max_seats}"
               f"\nCurrent_enroll: {self.current_enroll}")

