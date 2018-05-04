Proton
======
The RSS and Atom aggregator built with Python, Flask, and SQLite3.

Install
-------
Installation directions. Tested using Linux Mint 18.3.
::

    # Clone the repository
    git clone https://github.com/tmajest/Proton.git

    # Create virtual environment
    cd Proton && python3 -m venv venv
    . venv/bin/activate

    # Update pip and install packages
    pip install --upgrade pip
    pip install -e .

Run
---
To run, set up required flask environment variables, initialize the database, and run the flask app.
::

    # Set up environment variables
    export FLASK_APP=proton
    export FLASK_DEBUG=1
    export FLASK_ENV=development

    # Initialize the database
    flask init-db

    # Run the program
    flask run

Test
----
To test Proton, install test dependencies and then run pytest.
::

    # Install pytest
    pip install -e .[test]

    # Run tests
    pytest



