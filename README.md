
---

<div style="margin: auto; width: 100%; text-align: center; padding: 10px;">
    <img src="./.git_media/thumb.png" alt="Mycellium Logo" />
</div>

---

> **Mycellium** is an open-source voice-to-text technology designed to revolutionize the drive-through ordering process. This tool serves as an innovative replacement for traditional drive-through order takers, aiming to improve efficiency and accuracy in fast-food restaurants at a cost-effective price.

## Core Features
- **Voice Recording Daemon**: Automated voice recording with a 5-second interval for efficient order processing.
- **Robust Error Handling**: Requests users to restate their orders for clarity and accuracy.
- **Integration with OpenAI**: Seamlessly parses OpenAI responses into usable JSON format.

## Getting Started

### Installation:
To install and contribute to Mycellium, please follow these steps:

1. **Clone the Repository**:
   
   Clone Mycellium into your current working directory:
   ```bash
   git clone https://github.com/trifledmatter/mycellium ./
   ```

2. **Install Dependencies**:

   Using PIP, install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

### How to Use Mycellium

Mycellium simplifies the ordering process with these steps:

1. **Record Order**:
   
   Start by running the record command to capture the customer's request:
   ```bash
   mycellium record
   ```

2. **Transcribe Audio**:
   
   Convert the recorded audio into text for processing:
   ```bash
   mycellium transcribe
   ```

3. **Execute Action**:
   
   Use the transcription to perform the required action based on the customer's order:
   ```bash
   mycellium action
   ```

### Contributing

We welcome contributions to Mycellium! If you're interested in helping improve this project, please read our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to submit issues, propose changes, and submit pull requests.

### License

Mycellium is open for sharing and distribution under the [CC BY-ND 4.0 License](./LICENSE). This means you're free to share, copy, and redistribute this project in any format or through any medium. Just make sure to follow the guidelines detailed in the attached [CC BY-ND 4.0 License](./LICENSE). Not adhering to these terms could lead to a revocation of the permissions granted under this license.

### Support

For support, questions, or more information, please contact us at [support@gradison.ca](mailto:support@gradison.ca).