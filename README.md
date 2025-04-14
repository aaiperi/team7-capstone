# Team 7 Capstone Project: Region Selection for Efficient Video Transmission

## Project Overview

With the increasing number and quality of CCTV cameras, efficiently transmitting video data has become crucial. This project aims to develop an AI-based region selection algorithm that distinguishes between important (e.g., moving objects) and unimportant (e.g., background buildings, sky) areas in video. The system allows selective transmission, optimizing bandwidth and storage.

The project is conducted in collaboration with **Saloris Inc.** as part of the SW-centered university program at Kyungpook National University.

## Participating Company
- **Company**: Saloris Inc.
- **CEO / Advisor**: Hyun-Woo Kim (maker@saloris.world)

## Team Structure

Team 7 is divided into two subteams, each working on a different yet complementary approach:

### 🔹 Team A – Scene-Centric Tracking for CCTV Analysis
- Focus: Detect vehicle movement patterns using background subtraction and clustering
- Model: SegFormer + MOG2 motion detection
- Output: Direction tracking and anomaly detection (wrong-way driving, overspeeding)
Members: Dong-Jae Jang, Min-Jun Choi, Rakshitha Nagaraj

### 🔹 Team B – Frame Difference-Based Segmentation
- Focus: Improve segmentation performance using difference images (computed between consecutive frames)
- Model: SegFormer (Pre-trained on Cityscapes)
- Output: Enhanced active region detection for efficient metadata-based video transmission
Members: Seung-Hoon Lee, Min-Jun Choi, Aiperi Aibekova, Andrej Matos

---

## Repository Structure
- `data/` – Raw and preprocessed video frames
- `notebooks/` – Experiment and testing notebooks
- `src/` – Source code for region detection and processing
- `results/` – Output videos, evaluation metrics
- `docs/` – Any reports, presentations, or diagrams

## Tech Stack
- Python, PyTorch
- SegFormer
- YOLOv8 + ByteTrack
- OpenCV, MOG2, HSV filters
- Cityscapes & Custom Datasets – Training and evaluation
- Label Studio
- IoU, F1, Accuracy, FPS – Evaluation metrics

## 🚀 How to Run

To set up and run the project locally:

```bash
# 1. Clone the repo
git clone https://github.com/aaiperi/team7-capstone.git

# 2. Move into the project directory
cd team7-capstone

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run preprocessing or training scripts
python src/main.py

## Acknowledgment

This research was supported by the Ministry of Science and ICT and the Institute for Information & Communications Technology Planning & Evaluation (IITP) as part of the SW-centered university project.  
**Project Code: 2021-0-01082**

This project is for academic and research purposes only.
