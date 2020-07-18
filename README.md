# Hack It Ship It

## Contribution

### Requirements
Developers need Python 3 installed on their local machine.

### Setup
1. Clone this repository
1. Create a virtual environment in project directory.
    ```
    python -m venv venv
    ```
1. Activate the virtual environment.
    ```bash
    # Windows
    venv/Scripts/activate

    # MacOS / Linux
    source venv/bin/activate
    ```
1. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```

### How to Run
To start the game, use the following command.
```bash
python src/main.py
```
Make sure you have up-to-date dependencies.

### Project Structure
- `README.md` : This document.
- `requirements.txt` : List of dependencies of this project.
- `src` : Source code directory.
    - `main.py` : Entrypoint of the game.
    - `Scene.py` : Scene is a class responsible for event handling
        & rendering.
    - `StartScene.py` : Start menu scene.
    - `MainScene.py` : Gameplay scene.
    - `assets` : Directory for binary asset files.
        - `fonts`
        - `images`