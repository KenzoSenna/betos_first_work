from database import create_tables
from menu import main_menu

# This is the main entry point of the application.
# only runs if this script is executed directly, not when imported as a module.
# It creates the necessary database tables and starts the main menu.
# It ensures that the database is set up before any user interaction begins.

if __name__ == "__main__":
    create_tables()
    main_menu()