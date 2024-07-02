# Sign Language to Speech Translator

This project aims to bridge the communication gap for hearing-impaired individuals by using object detection and natural language processing. By utilizing a YOLO model trained on sign language or another custom model, the system detects objects from the camera feed. The detected classes are written to a `words.txt` file, which are then sent to ChatGPT to create meaningful sentences. These sentences are then written to a `meaningful.txt` file and translated into audio.

- **Real-time Object Detection**: Uses YOLO model trained on sign language for instant object detection from the camera feed.
- **Natural Language Processing**: Sends detected words to ChatGPT to form meaningful sentences.
- **Text to Speech**: Converts the meaningful sentences into audio.
- **Inclusivity**: Designed to facilitate communication for hearing-impaired individuals.

  ## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/kadiryavuzakinci/SignLanguage
    cd SignLanguage
    ```

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
3. **Set up the ChatGPT API Key:**
    - Edit a `config.yaml` file in the root directory.
    - Add your ChatGPT API key to the `config.yaml` file in the following format: 
    ```yaml
    api_key: "sk-"
    ```

    ## Usage

1. **Train your model**
   
3. **Run the main script:**
    ```sh
    python main.py
    ```

3. **Object Detection:**
    - The system will start the camera feed and begin detecting objects.
    - Detected classes will be written to the `words.txt` file.

4. **Generate Meaningful Sentences:**
    - The words in the `words.txt` file are sent to ChatGPT every 10 seconds.
    - ChatGPT processes the words and creates meaningful sentences.
    - These sentences are written to the `meaningful.txt` file.

5. **Text to Speech:**
    - The sentences in `meaningful.txt` are converted to audio.
    - The audio output is played, allowing for verbal communication.


# Contact
For any inquiries, open an issue on GitHub.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
