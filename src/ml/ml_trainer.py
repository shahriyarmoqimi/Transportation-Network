# src/ml_trainer.py
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from .ml_features import extract_features


def train_link_prediction_model(graph):

    print("⏳ [Trainer] Generating Dataset (Positive & Negative samples)...")

    data = []
    labels = []
    real_edges = set()
    limit = 5000

    # nodes with connection
    count = 0
    for u in range(graph.n):
        for item in graph.adj[u]:
            v = item[0] if isinstance(item, tuple) else item
            real_edges.add((u, v))

            if count < limit:
                feat = extract_features(graph, u, v)
                data.append(feat)
                labels.append(1)
                count += 1

    # nodes without connection
    count = 0
    while count < limit:
        u = random.randint(0, graph.n - 1)
        v = random.randint(0, graph.n - 1)

        if u != v and (u, v) not in real_edges:
            feat = extract_features(graph, u, v)
            data.append(feat)
            labels.append(0)
            count += 1

    print(f"⏳ [Trainer] Training Model on {len(data)} samples...")

    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return clf, accuracy, real_edges