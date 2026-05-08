import joblib
from src.env import MODEL_PATH


class FakeNewsCLI:
    def __init__(self):
        self._model = joblib.load(MODEL_PATH)

    def predict(self, text: str | list[str]) -> list[int]:
        if isinstance(text, str):
            text = [text]
        print(text)
        return self._model.predict(text).tolist()

    def run(self):
        print("\n=== Fake News Detector CLI ===")
        print("Wklej tekst i naciśnij Enter.")
        print("Wpisz pustą linię, aby zakończyć.\n")

        while True:
            text = input("Input: ")
            if text.strip() == "":
                print("Exiting...")
                break

            prediction = self.predict(text)

            label = "REAL 🟢" if prediction == [1] else "FAKE 🔴"

            print(f"\nPrediction: {label}\n")


if __name__ == "__main__":
    app = FakeNewsCLI()
    app.run()
