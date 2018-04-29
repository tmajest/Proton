Proton
======
The RSS and Atom aggregator built with Python, Flask, and SQLite3.

Install
-------
Installation directions. Tested using Linux Mint 18.3.

    # Clone the repository
    git clone https://github.com/tonymajestro/Proton.git

    # Create virtual environment
    python3 -m venv venv
    . venv/bin/activate

    # Install packages
    pip install -e .

Run
---

    # Set up environment variables
    export FLASK_APP=proton
    export FLASK_DEBUG=1
    export FLASK_ENV=development

    # Initialize the database
    flask init-db

    # Run the program
    flask run

    

