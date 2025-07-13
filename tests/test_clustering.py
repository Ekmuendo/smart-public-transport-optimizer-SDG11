import os
import pandas as pd
from sklearn.cluster import KMeans

def test_kmeans_clusters():
    # Dynamically get the full path to the dataset
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'sample_bus_stops.csv')

    # Load and test
    bus_stops = pd.read_csv(data_path)
    coords = bus_stops[['latitude', 'longitude']]
    
    k = 3
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(coords)

    assert len(clusters) == len(bus_stops), "Cluster count should match data points"
    assert set(clusters) == set(range(k)), f"Clusters should be labeled 0 to {k-1}"

if __name__ == "__main__":
    test_kmeans_clusters()
    print("✅ All tests passed!")
