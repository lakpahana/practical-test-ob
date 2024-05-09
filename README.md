**ASSESSMENT: Django Project for Data Visualization**

### Prerequisites:
- Python and Django installed on your system.
- Docker installed and running.

### Instructions:
To start the project, follow the instructions below:


1. **Clone Repository:**
   ```bash
   git clone https://github.com/lakpahana/practical-test-ob
   ```

2. **Navigate to Project Directory:**
   ```bash
   cd practical-test-ob
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Unzip Dataset:**
   Unzip the "Interview_dataset.zip" file and place the CSV files in the appropriate directory.

   ```bash
   copy to api/dataset folder
   ```

5. **Build Docker Image:**
   ```bash
   docker build -t practicaltest .
   ```

6. **Run Docker Container:**
   ```bash
   docker run -d -p 8000:8000 practicaltest
   ```

7. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

8. **Data Visualization:**
   Explore the visualized table structure and data points for the specified tables.
