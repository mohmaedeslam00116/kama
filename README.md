# Kama Language

A custom programming language for AI and data analysis.

## Description

Kama is a custom programming language built on top of Python, designed to simplify AI and data analysis tasks. It provides a user-friendly syntax and a set of built-in commands for common operations like data loading, model training, and text processing.

## Installation

To install Kama, use pip:

```bash
pip install kama-lang


Usage
Here's a simple example of how to use Kama:

from kama.core.kama import Kama

kama = Kama()

code = """
(x_train, y_train), (x_test, y_test) = load_data('mnist')
model = train_dnn((x_train, y_train), model_type='simple_dnn', hyperparams={'epochs': 2})
save_model(model, 'my_trained_model.pkl')
"""

kama.execute(code)
print("Code executed successfully!")

Project Structure
The project is structured as follows:

kama/
├── __init__.py
├── app.py        # Main app (Streamlit interface)
├── core/
│   ├── __init__.py
│   └── kama.py   # Kama class
├── commands/
│   ├── __init__.py
│   ├── data.py       # Data processing commands
│   ├── models.py     # Model training commands
│   ├── cloud.py      # Cloud upload commands
│   ├── text.py       # Text processing commands
│   └── image.py     # Image processing commands
├── utils/
│   ├── __init__.py
│   └── helpers.py  # Helper functions
├── ui/
│    ├── __init__.py
│    ├── resource.py       # Resource management UI
│    ├── big_data.py      # Big data processing UI
│    ├── cloud.py         # Cloud upload UI
│    ├── models.py        # Model management UI
│    ├── prediction.py   # Prediction UI
│    ├── data_ops.py    # Data operations UI
│    └── text_ops.py    # Text operations UI
│    └── image_ops.py  # Image operations UI
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_utils.py
│   └── test_commands/
│       ├── __init__.py
│       ├── test_data.py       # Test data commands
│       ├── test_models.py     # Test model commands
│       ├── test_cloud.py      # Test cloud commands
│       ├── test_text.py       # Test text commands
│       └── test_image.py     # Test image commands
└── setup.py
└── requirements.txt

Adding New Commands
To add a new command to Kama:

Create a new Python file inside the kama/commands/ directory (e.g., kama/commands/my_command.py).

Define your command function in that file.

Import the function in kama/commands/__init__.py.

Add the command to the command_list dictionary in kama/__init__.py.

You can also add the new command to the context using the kama.context in the app.py.

Adding New UI Elements
To add a new UI Element you should follow the below instructions:

Create a new python file inside the kama/ui/ directory (e.g., kama/ui/my_ui.py).

Define your UI function inside that file using the streamlit framework.

Import the function in kama/ui/__init__.py.

Add the ui function in the app.py.

Running Tests
To run the tests, navigate to the kama directory and execute:

python -m unittest discover tests

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues on the GitHub repository.

License
This project is licensed under the MIT License.
