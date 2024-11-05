# Personal Therapist Chatbot

## Project Overview
The Personal Therapist Chatbot is a human-trained chatbot designed to provide psychological support to users by engaging them in conversations. The web interface is built using HTML, CSS, and Bootstrap, offering a clean and user-friendly chat environment. The chatbot simulates real-time dialogue and helps users feel comforted and supported.

## Key Features
- Human-trained chatbot designed for psychological support.
- Web-based interface built with HTML and Bootstrap.
- Users can view chat history with distinct bot and user messages.
- Responsive design for easy usage across devices.
- Integrates with the OpenAI API for enhanced language processing.

## Files
- `home.html`: Contains the chat interface with message input, history, and bot interaction.
- `layout.html`: Template for the website's layout, including Bootstrap integration.
- `navbar.html`: Navigation bar with project branding.
- `main.py`: Backend logic for handling chatbot responses.

## Technologies Used
- **HTML, CSS, Bootstrap** for the frontend.
- **Python** for the backend.
- **JavaScript** for handling chat form submission and scroll history.
- **OpenAI API key** for language model integration.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/parthdave333/personal-therapist-chatbot.git

2. Install Python dependencies listed in requirements.txt:
   ```bash
      pip install -r requirements.txt

3. Generate and integrate the OpenAI API key:
Visit [OpenAI's API key page](https://platform.openai.com/api-keys).
Log in or create an OpenAI account.
Generate a new API key and copy it.
Update the project with your API key by adding it to main.py or an environment variable as instructed in your code.


## Example in main.py:
    import openai
    openai.api_key = "your_openai_api_key_here"

## Run the backend server to start the chatbot:
    python main.py
   Open home.html in your browser to start chatting with the bot.

## Contribution
Feel free to open a pull request to improve the chatbot's responses or web interface. Contributions are welcome!
