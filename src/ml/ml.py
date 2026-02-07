from .ml_trainer import train_link_prediction_model


def run_ml_task(graph):
    print("\n" + "=" * 50)
    print("🤖 BONUS TASK: Link Prediction System")
    print("=" * 50)

    clf, acc, real_edges = train_link_prediction_model(graph)

    print(f"\n✅ Model Trained Successfully!")
    print(f"🎯 Accuracy: {acc * 100:.2f}%")
    print("-" * 30)
