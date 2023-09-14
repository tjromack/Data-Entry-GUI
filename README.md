# Flask App: Disc Golf Player Data Entry


# Description


This customizable Flask app offers a straightforward GUI for users to input specific data fields into a database. In its current configuration, it serves as a tool for inputting disc golf player data, including their first name, last name, and a unique PDGA number.


The primary inspiration behind this project was to create a solution that streamlines the manual data entry process, especially for real-time inputs. While the present use-case revolves around capturing the performance of disc golf players in PDGA pro tour events, the foundational concept can be adapted for any scenario that requires efficient, real-time manual data input.



# Features

Simple GUI: Powered by HTML/CSS, this app provides a concise interface to view existing player data and add new records.

Data Integrity: The app ensures that no duplicate PDGA numbers are entered. In case of a duplicate entry attempt, the user is promptly notified.

Real-time Data Viewing: As you feed the database, you can simultaneously view the data in real-time.

Extensibility: The core functionality can be leveraged for various other applications that involve real-time manual data input.

# Setup and Usage

Ensure you have Python and Flask installed.

Clone the repository.

Navigate to the project directory and run app.py.

Open your browser and go to http://localhost:5000/ to access the GUI.

Enter disc golf player data and monitor the list for real-time updates.

# Future Scope

The next iterations will focus on capturing more granular performance metrics of the players, primarily their placements in PDGA pro tour events.
