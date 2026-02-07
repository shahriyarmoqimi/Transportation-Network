# ✈️ Transportation Network Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Course](https://img.shields.io/badge/Course-Graph%20Theory-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## 📖 Overview

This project is a comprehensive analysis of global transportation networks (specifically airport flight routes) using **Graph Theory** algorithms and **Machine Learning**.

The system models airports as nodes and flight routes as directed edges to solve complex routing problems, analyze network capacity, and predict potential future connections between airports.

This project was developed as part of the **Graph Theory Course (Fall 2025)**.

---

## 🚀 Key Features

### 1. Graph Construction & Data Parsing
- Efficiently parses real-world datasets (`airports.dat`, `routes.dat`).
- Constructs a directed graph where:
  - **Nodes**: Airports (with metadata like City, Country, IATA code).
  - **Edges**: Flight routes between airports.
  - **Weights**: Geographic distance calculated using the **Haversine Formula**.

### 2. Shortest Path Algorithms (Task 1)
- **Dijkstra's Algorithm**: Implementation of the classic algorithm to find the shortest path between two airports based on distance.
- **Label Correcting Algorithm**: A queue-based iterative approach (similar to SPFA/Bellman-Ford) to handle dynamic updates and potential negative edges (theoretical).
- **Performance Analysis**: Compares the execution time and path validity of both algorithms.

### 3. Maximum Flow Analysis (Task 2)
- Calculates the maximum capacity of flights between a source and a destination.
- Uses the **Edmonds-Karp** algorithm (BFS for finding augmenting paths).
- **Assumption**: The capacity of an edge is defined by the number of parallel flights (frequency) between two airports.

### 4. Link Prediction with Machine Learning (Bonus Task)
- Uses a **Random Forest Classifier** to predict the existence or likelihood of a flight route between two unconnected airports.
- **Feature Engineering**: Extracts topological features from the graph structure:
  - **Sum of Degrees**: Represents the combined "hub strength" of two airports.
  - **Common Neighbors**: The number of shared connections (intermediate airports).
  - **Jaccard Coefficient**: Measures the similarity between the neighborhoods of two nodes.

---

## 📂 Project Structure

The project follows a modular structure for better maintainability and scalability:

```text
Transportation-Network/
├── data/                  # Dataset files
│   ├── airports.dat       # Airport metadata
│   └── routes.dat         # Flight route information
├── src/                   # Source code
│   ├── ml/                # Machine Learning Module
│   │   ├── __init__.py
│   │   ├── ml.py          # ML interface
│   │   ├── ml_features.py # Feature extraction logic
│   │   └── ml_trainer.py  # Model training and dataset creation
│   ├── data_loader.py     # Parses .dat files and builds the graph
│   ├── dijkstra_algo.py   # Implementation of Dijkstra
│   ├── graph.py           # Adjacency list graph class
│   ├── lc_algo.py         # Label Correcting algorithm
│   ├── main.py            # Main entry point (CLI)
│   ├── max_flow_algo.py   # Max Flow implementation
│   └── utils.py           # Helper functions (e.g., Haversine, Node search)
└── report.pdf             # Project report and analysis
```

---

## 🛠️ Installation & Requirements

To run this project, ensure you have Python 3.10 or higher installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Transportation-Network.git](https://github.com/YOUR_USERNAME/Transportation-Network.git)
    cd Transportation-Network
    ```

2.  **Install Dependencies:**
    The core algorithms (Dijkstra,Label Correcting, Max Flow) use standard Python libraries.
    For the **Bonus Machine Learning Task**, you must install `scikit-learn`:
    
    ```bash
    pip install scikit-learn
    ```

---

## 💻 Usage

To start the application, run the main script from the root directory:

```bash
python src/main.py
```
---

### Interactive CLI Flow
The program runs in an interactive command-line interface:

1.  **Data Loading**: The system automatically reads `airports.dat` and `routes.dat` to build the graph.
2.  **Main Menu**:
    - **Task 1 (Shortest Path)**: 
      - Enter a **Source** and **Destination** airport (e.g., "Tehran", "Frankfurt").
      - The system calculates the shortest path using both **Dijkstra** and **Label Correcting** algorithms.
      - It displays the path sequence, total distance (km), and execution time for comparison.
    - **Task 2 (Max Flow)**: 
      - Enter two airports to find the maximum flow bottleneck.
      - **Assumption**: Edge capacity = Number of daily flights.
3.  **Bonus Task (ML Prediction)**:
    - At the end, you can choose to run the Link Prediction module.
    - The model trains on the current graph topology.
    - You can test specific pairs of airports to see the probability of a connection based on their features.

---

## 🧠 Algorithmic Details

### 1. Shortest Path Analysis
- **Dijkstra's Algorithm**: Implemented with an array-based priority selection. Efficient for this dataset size and guarantees the shortest path for non-negative weights.
- **Label Correcting (LC)**: A dynamic programming approach using a queue. While typically used for graphs with negative edges, here it serves as a performance benchmark against Dijkstra.

### 2. Maximum Flow (Edmonds-Karp)
- We transformed the graph into a flow network where the capacity of an edge is defined by the frequency of flights.
- BFS is used to find augmenting paths until no more flow can be pushed from Source to Sink.

### 3. Machine Learning (Link Prediction)
This module predicts missing or potential routes using a **Random Forest Classifier**. It extracts the following features from the graph structure:
- **Sum of Degrees**: Indicates if the nodes are major hubs.
- **Common Neighbors**: The number of shared connections.
- **Jaccard Coefficient**: A normalized measure of neighborhood similarity.
- **Distance (Optional)**: Geographic distance between nodes.

---

## 🎓 Course Information

- **Course**: Graph Theory
- **Semester**: Fall 2025
- **University**: SBU

---

## 📄 License

This project is open-source and available for educational purposes.
