import customtkinter as ctk
from databaseManager import *

root = ctk.CTk()
root.geometry("1280x720")
root.title("MarkManager")
boldFont = ctk.CTkFont(family="Arial", size=40, weight="bold")
buttonBoldFont = ctk.CTkFont(family="Arial", weight="bold")
coursesBoldFont = ctk.CTkFont(family="Arial", size=20, weight="bold")
courseFrameWidth = 1280*0.675-50

global courseListFrame

def render():
    #Frames
    courseListFrame = ctk.CTkFrame(master=root, corner_radius=20)
    profileFrame = ctk.CTkFrame(master=root, corner_radius=20)

    #Frame Labels
    coursesLabel = ctk.CTkLabel(master=courseListFrame, text="Courses", font=boldFont)
    optionsLabel = ctk.CTkLabel(master=profileFrame, text="Options", font=boldFont)

    #Option Buttons
    addCourseButton = ctk.CTkButton(master=profileFrame, text="Add Course", font=buttonBoldFont)

    semesterSelection = ctk.CTkOptionMenu(master=courseListFrame)

    #Packing/Placing
    courseListFrame.place(relx=0.30, rely=0.01, relwidth=0.69, relheight=0.98)
    profileFrame.place(relx=0.01, rely=0.01, relwidth=0.275, relheight=0.98)
    coursesLabel.pack(pady=20)
    optionsLabel.pack(pady=20)
    addCourseButton.pack(pady=35)
    courseRender(courseListFrame)

def courseRender(frame):
    courses = [('CEN100', 'Intro to Engineering', 89.2, 1), ('MTH141', 'Linear Algebra', 67.6, 1), ('PCS211', 'Physics: Mechanics', 56.0, 1), ('CHY102', 'General Chemistry', 62.0, 1), ('MTH140', 'Calculus I', 0, 1)]
    #SOLVE NULL AVERAGE MARK ISSUE
    for course in courses:
        code, title, average, semester = course
        courseFrame = ctk.CTkFrame(master=frame, width=courseFrameWidth, height=100, corner_radius=20)

        #Labels
        courseLabel = ctk.CTkLabel(master=courseFrame, text=(f"{code} - {title}"), font=coursesBoldFont, anchor="nw")
        markLabel = ctk.CTkLabel(master=courseFrame, text=(f"{average}%"), font=coursesBoldFont)

        #Grade Color Selection
        if (100 >= average >= 90):
            markLabel.configure(text_color="#3d7dcc")
        elif (90 >= average >= 80):
            markLabel.configure(text_color="#92c91c")
        elif (80 >= average >= 70):
            markLabel.configure(text_color="#4d9e3a")
        elif (70 >= average >= 60):
            markLabel.configure(text_color="#c98a1c")
        elif (60 >= average >= 50):
            markLabel.configure(text_color="#c91c1c")
        elif (49 <= average):
            markLabel.configure(text_color="gray")

        #Buttons
        editCoursesButton = ctk.CTkSwitch(master=courseFrame, text="Edit Courses", font=buttonBoldFont)
        openCourseButton = ctk.CTkButton(master=courseFrame, text="Open Course", font=buttonBoldFont)

        #Packing/Placing
        courseFrame.pack(pady=10)
        courseFrame.pack_propagate(False)
        markLabel.pack(side="right", padx=15)
        courseLabel.pack(pady=15, padx=15, anchor="nw")
        openCourseButton.pack(padx=15, anchor="sw")

render()
root.mainloop()