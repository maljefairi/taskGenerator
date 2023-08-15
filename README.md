# taskGenerator

An employee engagement & recognition system generator which leverages OpenAI's GPT-4 model to create dynamic activities aimed at enhancing organizational growth and values.

![Repository Owner](https://github.com/maljefairi.png)

## Overview

This system fosters employee engagement by rewarding activities in alignment with an organization's core values and growth objectives. It dynamically suggests activities based on predefined dimensions such as Cognitive Abilities, Values, Educational Achievements, and more. 

## Features

- **Dynamic Activity Suggestion**: Proposes activities based on different dimensions and sub-dimensions.
- **Web Interface**: Integrated Flask-based web interface found under the `templates` folder.
- **Persistent Data Storage**: Activities are stored and managed in `generated_activities.json` and its copy `generated_activities copy.json`.
- **Customizable Dimension Mapping**: Adjust and configure the predefined dimensions in the `DIMENSIONS` variable.

## Prerequisites

Before you begin, ensure you have:

- Python 3.6 or above
- `openai` Python library
- An active OpenAI API key
- Flask (for the web interface)

## Setup & Execution

1. Clone the repository.
```bash
git clone https://github.com/maljefairi/taskGenerator.git
```
2. Install the required Python libraries.
```bash
pip install openai Flask
```
3. Set up your OpenAI API key.
```bash
export OPENAI_API_KEY='YOUR_API_KEY'
```
4. To run the generator directly:
```bash
python generator.py
```
For the web interface:
```bash
python app.py
```
By default, the generator script creates 5 activities. Modify the number as needed.

## Contribution

Contributions, issues, and feature requests are welcome! Check the [Issues](https://github.com/maljefairi/taskGenerator/issues) page for open tasks.

## License

[MIT](https://opensource.org/licenses/MIT)

## About the Owner

This project is maintained by [Mohammed Al-Jefairi](https://github.com/maljefairi). Feel free to reach out for more details or any queries.

---

Remember to replace `'YOUR_API_KEY'` with your actual OpenAI API key when running the generator.