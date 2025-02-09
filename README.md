# GenAI- LinkedIn and Twitter Profile Scrapper

## Overview

`GenAI- LinkedIn and Twitter Profile Scrapper
- **agents**: Contains the agents for LinkedIn and Twitter profile lookups.
- **third_parties**: Contains scripts to interact with third-party APIs for LinkedIn and Twitter.
- **tools**: Contains utility functions and classes.
- **static**: Contains static files like CSS.
- **templates**: Contains HTML templates for the web interface.
- **app.py**: The main Flask application.
- **ice_breaker.py**: Logic for generating ice breakers and interesting facts.
- **output_parsers.py**: Parsers for processing the output from the language model.

## Features

- **LinkedIn Profile Lookup**: Finds and scrapes LinkedIn profiles for the given name.
- **Twitter Profile Lookup**: Finds and scrapes Twitter profiles for the given name.
- **Ice Breaker Generation**: Generates ice breakers, interesting facts, and topics of interest based on the scraped data.
- **Web Interface**: Simple web interface to input a name and display the generated information.

## Project Structure

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simplellmapp.git
    cd simplellmapp
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a [.env](http://_vscodecontentref_/17) file in the root directory and add the necessary API keys as shown in the provided [.env](http://_vscodecontentref_/18) file.

## Usage

1. Run the Flask application:
    ```sh
    python simplellmapp/app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

3. Enter a name in the input field and click "Do Your Magic".

4. The application will display the generated ice breakers, interesting facts, and topics of interest.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://www.openai.com/)
- [Flask](https://flask.palletsprojects.com/)
- [SerpAPI](https://serpapi.com/)
- [Scrapin](https://scrapin.io/)
- [Tweepy](https://www.tweepy.org/)
` is a web application that generates ice breakers and interesting facts about a person based on their LinkedIn and Twitter profiles. It uses the LangChain library to interact with OpenAI's GPT-3.5-turbo model and various APIs to gather and process information.


