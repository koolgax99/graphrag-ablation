# Ablation Study Experiment Runner

This project runs ablation studies on chatbot models using configurable parameters and a set of questions. Results are saved to CSV for further analysis.

## Structure

- `core/`: Main experiment logic and API handler.
- `config/`: Experiment configuration files.
- `data/`: Input question data.
- `outputs/`: Experiment results.
- `evaluation/`: Evaluation scripts.

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Create a `.env` file in the root directory with the following keys:
     ```
     API_URL=<your_api_url>
     NEO4J_URI=<your_neo4j_uri>
     NEO4J_DATABASE=<your_neo4j_database>
     NEO4J_USERNAME=<your_neo4j_username>
     NEO4J_PASSWORD=<your_neo4j_password>
     ```

## Running Experiments

Run the main experiment script:
```
python run_experiment.py
```
Results will be saved to `outputs/results.csv`.

## Customization

- **Questions**: Edit `data/questions.csv`.
- **Parameters**: Edit `config/study_config.yaml`.

## Evaluation

Use scripts in `evaluation/` to analyze results.

## License

MIT License.
