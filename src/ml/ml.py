from .ml_trainer import train_link_prediction_model
from .ml_features import extract_features
from utils import find_node_index


def run_ml_task(graph):
    print("\n" + "=" * 50)
    print("🤖 BONUS TASK: Link Prediction System")
    print("=" * 50)

    # call trainer
    clf, acc, real_edges = train_link_prediction_model(graph)

    print(f"\n✅ Model Trained Successfully!")
    print(f"🎯 Accuracy: {acc * 100:.2f}%")
    print("-" * 30)

    # interface
    while True:
        try:
            print("\n🔍 Interactive Mode: Predict connection between two airports.")
            u = find_node_index(graph, "🛫 Source Airport: ")
            v = find_node_index(graph, "🛬 Target Airport: ")

            if u == v:
                print("❌ Source and Target cannot be the same.")
                continue

            # extract data
            features = extract_features(graph, u, v)

            # predict
            probs = clf.predict_proba([features])[0]
            prob_percent = probs[1] * 100

            print(f"\n📊 Feature Analysis:")
            print(f"   • Sum of Degrees: {features[0]}")
            print(f"   • Common Neighbors: {features[1]}")
            print(f"   • Jaccard Coeff: {features[2]:.4f}")

            print(f"\n🧠 AI Perdict:")
            if prob_percent > 50:
                print(f"   ✅ CONNECTED (Probability: {prob_percent:.1f}%)")
            else:
                print(f"   ❌ NOT CONNECTED (Probability: {prob_percent:.1f}%)")

            reality = "YES (Flight Exists)" if (u, v) in real_edges else "NO (No Flight)"
            print(f"   📚 Actual Data: {reality}")

            if input("\nTest another pair? (y/n): ").lower() != 'y':
                break

        except Exception as e:
            print(f"Error: {e}")
            break
