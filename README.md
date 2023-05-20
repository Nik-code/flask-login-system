# Flask Login System

This is a Flask-based web application implementing a login system. It allows users to sign up, log in, and view their user profile.

## Features

- User registration: Users can create an account by providing their username, password, fullname, email, phone, and score.
- User login: Registered users can log in using their credentials.
- User profile: Once logged in, users can view their profile page, which displays their information.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Ensure you have a MySQL database server running.
   - Update the database connection parameters in `database.py` to match your MySQL configuration.
   - Create the `users` table in your MySQL database. You can use the following SQL command as a starting point:

     ```sql
     CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255) NOT NULL,
       password VARCHAR(255) NOT NULL,
       fullname VARCHAR(255),
       email VARCHAR(255),
       phone VARCHAR(255),
       score INT
     );
     ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

- Sign Up:
  - Visit the home page and click on the "Sign Up" link.
  - Fill in the registration form with your details and submit the form.
- Log In:
  - Visit the home page and click on the "Log In" link.
  - Enter your username and password and click the "Log In" button.
- User Profile:
  - After logging in, you will be redirected to your user profile page displaying your information.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Feel free to customize the content as per your project's specifics, such as adding more sections, providing instructions for additional functionalities, or including relevant badges or screenshots.
