# Simple Learning Management System in Python

class Class:
    def __init__(self, class_id, name, description):
        self.id = class_id
        self.name = name
        self.description = description
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def __str__(self):
        return f"Class ID: {self.id}, Name: {self.name}, Description: {self.description}, Lessons: {len(self.lessons)}"


class Lesson:
    def __init__(self, lesson_id, title, content):
        self.id = lesson_id
        self.title = title
        self.content = content

    def __str__(self):
        return f"Lesson ID: {self.id}, Title: {self.title}, Content: {self.content[:30]}..."


class LearningManagementSystem:
    def __init__(self):
        self.classes = []
        self.class_id_counter = 1
        self.lesson_id_counter = 1

    def add_class(self, name, description):
        new_class = Class(self.class_id_counter, name, description)
        self.classes.append(new_class)
        self.class_id_counter += 1
        print(f"Class added: {new_class}")

    def add_lesson(self, class_id, title, content):
        class_ = next((c for c in self.classes if c.id == class_id), None)
        if class_:
            new_lesson = Lesson(self.lesson_id_counter, title, content)
            class_.add_lesson(new_lesson)
            self.lesson_id_counter += 1
            print(f"Lesson added to class {class_id}: {new_lesson}")
        else:
            print(f"Class ID {class_id} not found")

    def show_classes(self):
        for class_ in self.classes:
            print(class_)
            for lesson in class_.lessons:
                print(f"  - {lesson}")

if __name__ == '__main__':
    lms = LearningManagementSystem()

    # Adding classes
    lms.add_class("Math 101", "Introduction to Algebra")
    lms.add_class("History 101", "World History Overview")

    # Adding lessons to classes
    lms.add_lesson(1, "Lesson 1: Basic Algebra", "This lesson covers the basics of algebra.")
    lms.add_lesson(1, "Lesson 2: Advanced Algebra", "This lesson covers advanced topics in algebra.")
    lms.add_lesson(2, "Lesson 1: Ancient Civilizations", "This lesson covers ancient civilizations.")

    # Displaying classes and their lessons
    lms.show_classes()
