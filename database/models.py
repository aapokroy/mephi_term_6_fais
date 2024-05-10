from sqlalchemy import (
    Column, ForeignKey, Integer, Boolean,
    String, Date, DateTime, Float,
)

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False, unique=False)
    first_name = Column(String, nullable=False, unique=False)
    last_name = Column(String, nullable=False, unique=False)
    registration_date = Column(Date, nullable=False, unique=False)


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, nullable=False)
    position = Column(Integer, nullable=False, unique=False)
    team = Column(Integer, nullable=False, unique=False)
    department = Column(Integer, nullable=False, unique=False)
    date_of_employment = Column(Date, nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=False)
    parent_id = Column(Integer, ForeignKey('category.id'), nullable=True, unique=False)


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, unique=False)
    description = Column(String, nullable=False, unique=False)
    start_time = Column(DateTime, nullable=True, unique=False)
    end_time = Column(DateTime, nullable=True, unique=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False, unique=False)


class UserStudyingCourse(Base):
    __tablename__ = "user_studying_course"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False, unique=False)


class UserTeachingCourse(Base):
    __tablename__ = "user_teaching_course"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False, unique=False)


class Section(Base):
    __tablename__ = "section"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, unique=False)
    description = Column(String, nullable=False, unique=False)
    start_time = Column(DateTime, nullable=True, unique=False)
    end_time = Column(DateTime, nullable=True, unique=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False, unique=False)


class Step(Base):
    __tablename__ = "step"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, unique=False)
    content = Column(String, nullable=False, unique=False)
    max_score = Column(Integer, nullable=False, unique=False)
    max_attempts = Column(Integer, nullable=True, unique=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False, unique=False)


class Attempt(Base):
    __tablename__ = "attempt"

    id = Column(Integer, primary_key=True, nullable=False)
    score = Column(Float, nullable=True, unique=False)
    submission_time = Column(DateTime, nullable=False, unique=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, nullable=False)
    score = Column(Float, nullable=False, unique=False)
    submission_time = Column(DateTime, nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=False)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False, unique=False)


class UserInput(Base):
    __tablename__ = "user_input"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False, unique=False)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False, unique=False)


class TextTask(Base):
    __tablename__ = "text_task"

    id = Column(Integer, primary_key=True, nullable=False)
    answer_type = Column(Integer, nullable=False, unique=False)
    criterion = Column(Integer, nullable=False, unique=False)
    correct_answer = Column(String, nullable=False, unique=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False, unique=False)


class OpenEndedTask(Base):
    __tablename__ = "open_ended_task"

    id = Column(Integer, primary_key=True, nullable=False)
    review_type = Column(Integer, nullable=False, unique=False)
    num_reviews = Column(Integer, nullable=False, unique=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False, unique=False)


class TestTask(Base):
    __tablename__ = "test_task"

    id = Column(Integer, primary_key=True, nullable=False)
    multiple_choice = Column(Boolean, nullable=False, unique=False)
    partial_score = Column(Boolean, nullable=False, unique=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False, unique=False)


class SortingTask(Base):
    __tablename__ = "sorting_task"

    id = Column(Integer, primary_key=True, nullable=False)
    partial_score = Column(Boolean, nullable=False, unique=False)
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False, unique=False)


class TestOption(Base):
    __tablename__ = "test_option"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False, unique=False)
    is_correct = Column(Boolean, nullable=False, unique=False)
    task_id = Column(Integer, ForeignKey('test_task.id'), nullable=False, unique=False)


class SortingOption(Base):
    __tablename__ = "sorting_option"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False, unique=False)
    correct_position = Column(Integer, nullable=False, unique=False)
    task_id = Column(Integer, ForeignKey('sorting_task.id'), nullable=False, unique=False)


class AttemptSortingOption(Base):
    __tablename__ = "attempt_sorting_option"

    id = Column(Integer, primary_key=True, nullable=False)
    position = Column(Integer, nullable=False, unique=False)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False, unique=False)
    option_id = Column(Integer, ForeignKey('sorting_option.id'), nullable=False, unique=False)


class AttemptTestOption(Base):
    __tablename__ = "attempt_test_option"

    id = Column(Integer, primary_key=True, nullable=False)
    attempt_id = Column(Integer, ForeignKey('attempt.id'), nullable=False, unique=False)
    option_id = Column(Integer, ForeignKey('test_option.id'), nullable=False, unique=False)
