# Portfolio Project

This is a personal portfolio website built using Django and SQLite3. The project showcases work, experience, and other relevant details.

## Features
- Responsive design
- Dynamic content management
- Review and testimonial submission
- Secure authentication
- Image upload support

## Installation

### Requirements
- Python 3.11+
- Django 5.1.6
- SQLite3 (default database)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/portfolio.git
cd portfolio

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

## Usage
- Open `http://127.0.0.1:8000/` in a browser to view the portfolio.
- Admin panel: `http://127.0.0.1:8000/admin/` (requires superuser credentials).

## License
This project is protected under the following terms:

**Custom License**

- You may not use, copy, modify, or distribute this project or its contents without explicit written permission from the author.
- Unauthorized use of this software in any form is strictly prohibited.
- For permissions, please contact the author.

See [LICENSE](LICENSE) for more details.

## Author
Created by Boluwatife Akingbade. Reach out for permissions or contributions.
