# Happy Birthday Special Page

This is a Streamlit web application that displays a special "Happy Birthday" surprise page. The app embeds an external webpage served at `http://localhost:8000` inside an iframe.

## Features

- Displays a birthday greeting title and message.
- Embeds an external webpage for the surprise content.

## Requirements

- Python 3.x
- Streamlit

## Installation

1. Clone the repository.
2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Make sure the external webpage is running and accessible at `http://localhost:8000`.
2. Run the Streamlit app:

```
streamlit run app.py
```

3. Open the URL provided by Streamlit in your browser to view the birthday surprise page.

## Project Structure

- `app.py`: The main Streamlit application.
- `public/`: Contains static assets such as images and gifs used in the project.

## License

This project is licensed under the MIT License.
