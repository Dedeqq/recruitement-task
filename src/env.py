from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1]
DATA_DIR = PROJECT_DIR / "data"
MODELS_DIR = PROJECT_DIR / "models"
DATASET_PATH = DATA_DIR / "dataset.parquet"
MODEL_PATH = MODELS_DIR / "fake_news_model.pkl"
