# AI Enhanced Traffic Management Network

## Overview
The rapid growth of infrastructure in the 21st century has created an urgent need for smarter traffic management systems. Traditional methods often fall short due to static signal timings, limited real-time data processing, and poor system integration. These inefficiencies lead to traffic congestion, increased fuel consumption, and higher emissions.

This project introduces an intelligent traffic management system that models traffic junctions as nodes in a graph-like structure. Each node communicates with neighboring junctions to share traffic density data, allowing for better coordination and dynamic adaptation to traffic patterns in real time. By leveraging AI, the system can optimize signal timings to reduce congestion and create a sustainable traffic ecosystem.

The project uses YOLO object detection for real-time vehicle detection and a fuzzy logic algorithm to dynamically adjust traffic signals based on traffic density.

## Features
- **Real-time Vehicle Detection:** Utilizes YOLOv11 and OpenCV to detect and classify vehicles (e.g., cars, motorcycles, buses, trucks, and bicycles).
- **Dynamic Signal Control:** A fuzzy logic algorithm optimizes traffic light timing based on real-time traffic density.
- **Communication Between Nodes:** Traffic junctions share traffic density data with neighboring junctions for better overall coordination.
- **Cloud-Enabled:** Deployment-ready with Google Cloud and Docker for scalability and reliability.

## Technology Used

### Machine Learning & Computer Vision
- **YOLOv11:** Real-time object detection for vehicle identification.
- **PyTorch & TensorFlow:** Frameworks for building and fine-tuning the detection models.
- **OpenCV:** Image and video processing for handling input from traffic cameras.

### Programming & Scripting
- **Python:** Core language for AI algorithms, detection models, and backend development.
- **NumPy & Pandas:** Data manipulation and analysis.

### Communication Protocols
- **HTTPS:** Secure communication.
- **MQTT & Socket.IO:** Real-time data transfer between nodes and system components.

### Web Development
- **HTML & CSS:** Frontend interface for traffic management system monitoring.

### Backend Development
- **Flask:** Lightweight web framework for the backend API.

### Database Management
- **SQL:** Storing and managing traffic data.

### Cloud & Deployment
- **Google Cloud:** Hosting and scaling the system.
- **Docker:** Containerized environment for easy deployment and scalability.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arungjose/trafficnetwork.git
   cd trafficnetwork
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

5. **Open the folder code and run the script:**
    ```bash
    cd code
    python main.py
    ```

## Usage
1. Upload video streams or connect live camera feeds for real-time traffic monitoring.
2. Adjust system parameters for different junctions if needed.
3. View vehicle counts and traffic density data in the web interface.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push the changes to your branch.
5. Create a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
Thank you for checking out the AI Enhanced Traffic Management Network! We hope it helps pave the way for smarter, more efficient traffic management systems.

