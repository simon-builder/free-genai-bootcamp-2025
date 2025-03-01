# CLAUDE.md for ASL Fingerspelling Practice App

## Commands
- **Run app**: `streamlit run app.py`
- **Install dependencies**: `pip install -r requirements.txt`
- **Lint**: `flake8 app.py`
- **Format code**: `black app.py`

## Code Style Guidelines
- **Imports**: Group in order: standard lib, third-party, local
- **Formatting**: 4-space indentation, 88 character line limit
- **Types**: Use type hints for function parameters and returns
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Error handling**: Use try/except blocks with specific exceptions
- **Comments**: Docstrings for functions/classes, inline for complex logic

## Project Architecture
- Streamlit for UI
- OpenCV for webcam access
- MediaPipe for hand detection/tracking
- Focus on clean, readable code over optimization
- Keep UI simple and functional