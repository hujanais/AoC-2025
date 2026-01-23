import polars as pl
import numpy as np


def main():
    print("Welcome to AoC 2025.  Just run the code directly in the solutions folder")


def inspect_parquet():
    # Set a seed for reproducibility
    np.random.seed(42)

    # Create mock data
    num_entries = 50

    filenames = [f"nitf_file_{i + 1}" for i in range(num_entries)]
    point_ids = [f"pointid_{i + 1}" for i in range(num_entries)]
    longitudes = np.random.uniform(42.375, 42.385, num_entries).tolist()
    latitudes = np.random.uniform(-71.105, -71.100, num_entries).tolist()
    elevations = np.random.uniform(10, 20, num_entries).tolist()
    pixel_x = np.random.uniform(1000, 3000, num_entries).tolist()
    pixel_y = np.random.uniform(700, 1100, num_entries).tolist()
    grid_x = np.random.uniform(5, 25, num_entries).tolist()
    grid_y = np.random.uniform(5, 15, num_entries).tolist()
    pixels_between_grid_cols = [100] * num_entries
    pixels_between_grid_rows = [100] * num_entries
    image_ids = [f"IMG_{str(i + 1).zfill(3)}" for i in range(num_entries)]
    sensor_x = np.random.uniform(4521200, 4521300, num_entries).tolist()
    sensor_y = np.random.uniform(-4238300, -4238100, num_entries).tolist()
    sensor_z = np.random.uniform(4152900, 4153100, num_entries).tolist()
    nrows = [8192] * num_entries
    ncols = [8192] * num_entries
    lat_left = np.random.uniform(-71.110, -71.100, num_entries).tolist()
    lon_left = np.random.uniform(42.378, 42.380, num_entries).tolist()
    lat_above = np.random.uniform(-71.105, -71.095, num_entries).tolist()
    lon_above = np.random.uniform(42.380, 42.382, num_entries).tolist()
    n_grid_row_shift = np.random.randint(-1, 2, num_entries).tolist()
    n_grid_col_shift = np.random.randint(-1, 2, num_entries).tolist()
    gsd_x = [0.5] * num_entries
    gsd_y = [0.5] * num_entries
    incidence_angle = np.random.uniform(10, 20, num_entries).tolist()

    # Create the DataFrame
    df = pl.DataFrame(
        {
            "filename": filenames,
            "point_id": point_ids,
            "longitude": longitudes,
            "latitude": latitudes,
            "elevation": elevations,
            "pixel_x": pixel_x,
            "pixel_y": pixel_y,
            "grid_x": grid_x,
            "grid_y": grid_y,
            "pixels_between_grid_cols": pixels_between_grid_cols,
            "pixels_between_grid_rows": pixels_between_grid_rows,
            "image_id": image_ids,
            "sensor_x": sensor_x,
            "sensor_y": sensor_y,
            "sensor_z": sensor_z,
            "nrows": nrows,
            "ncols": ncols,
            "lat_left": lat_left,
            "lon_left": lon_left,
            "lat_above": lat_above,
            "lon_above": lon_above,
            "n_grid_row_shift": n_grid_row_shift,
            "n_grid_col_shift": n_grid_col_shift,
            "gsd_x": gsd_x,
            "gsd_y": gsd_y,
            "incidence_angle": incidence_angle,
        }
    )

    df.write_parquet("nitf.parquet")
    # df = pl.read_parquet("nitf.parquet")
    # print(df.columns)


def get_surrounding_box(coordinates: list[list[float]]):
    """Get the bounding box."""
    longitudes = [c[0] for c in coordinates]
    latitudes = [c[1] for c in coordinates]

    min_lon = min(longitudes)
    min_lat = min(latitudes)
    max_lon = max(longitudes)
    max_lat = max(latitudes)

    print(f"({min_lon},{min_lat}) - ({max_lon},{max_lat})")


if __name__ == "__main__":
    # Create sample data
    metadata = pl.DataFrame(
        {
            "image_id": [101, 101, 102, 103, 103, 103, 104, 105, 105],
            "coordinates": [
                # New York area - 4 corner points forming a bounding box
                [
                    [40.7128, -74.0060],
                    [40.7150, -74.0060],
                    [40.7150, -74.0030],
                    [40.7128, -74.0030],
                ],
                [
                    [40.7128, -74.0060],
                    [40.7150, -74.0060],
                    [40.7150, -74.0030],
                    [40.7128, -74.0030],
                ],
                # London area
                [
                    [51.5074, -0.1278],
                    [51.5100, -0.1278],
                    [51.5100, -0.1250],
                    [51.5074, -0.1250],
                ],
                # Tokyo area
                [
                    [35.6762, 139.6503],
                    [35.6800, 139.6503],
                    [35.6800, 139.6550],
                    [35.6762, 139.6550],
                ],
                [
                    [35.6762, 139.6503],
                    [35.6800, 139.6503],
                    [35.6800, 139.6550],
                    [35.6762, 139.6550],
                ],
                [
                    [35.6762, 139.6503],
                    [35.6800, 139.6503],
                    [35.6800, 139.6550],
                    [35.6762, 139.6550],
                ],
                # Sydney area
                [
                    [-33.8688, 151.2093],
                    [-33.8650, 151.2093],
                    [-33.8650, 151.2140],
                    [-33.8688, 151.2140],
                ],
                # Paris area
                [
                    [48.8566, 2.3522],
                    [48.8600, 2.3522],
                    [48.8600, 2.3570],
                    [48.8566, 2.3570],
                ],
                [
                    [48.8566, 2.3522],
                    [48.8600, 2.3522],
                    [48.8600, 2.3570],
                    [48.8566, 2.3570],
                ],
            ],
        }
    )

    # Get Unique Images + Coordinates
    unique_images = metadata.unique("image_id").select("image_id", "coordinates").sort(by="image_id").to_dict()

    print(unique_images)

    # Create Geographic Bounding Boxes
    geographic_boxes = {}
    for image, coordinates in zip(unique_images["image_id"], unique_images["coordinates"], strict=False):
        geographic_boxes[image] = get_surrounding_box(coordinates)
