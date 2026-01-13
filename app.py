import polars as pl


def inspect_parquet():
    df = pl.DataFrame(
        {
            "filename": ["nitf_file_1", "nitf_file_2", "nitf_file_3"],
            "point_id": ["pointid_1", "pointid_2", "pointid_3"],
            "longitude": [42.3797, 42.3812, 42.3785],
            "latitude": [-71.1034, -71.1045, -71.1028],
            "elevation": [12.3, 15.7, 10.2],
            "pixel_x": [1024.5, 2048.3, 1536.7],
            "pixel_y": [768.2, 1024.6, 892.1],
            "grid_x": [10.25, 20.48, 15.37],
            "grid_y": [7.68, 10.25, 8.92],
            "pixels_between_grid_cols": [100, 100, 100],
            "pixles_between_grid_rows": [100, 100, 100],
            "image_id": ["IMG_001", "IMG_002", "IMG_003"],
            "sensor_x": [4521234.5, 4521245.8, 4521228.3],
            "sensor_y": [-4238156.2, -4238167.5, -4238148.9],
            "sensor_z": [4152987.3, 4152998.6, 4152980.1],
            "nrows": [8192, 8192, 8192],
            "ncols": [8192, 8192, 8192],
            "lat_left": [-71.1050, -71.1061, -71.1044],
            "lon_left": [42.3790, 42.3805, 42.3778],
            "lat_above": [-71.1018, -71.1029, -71.1012],
            "lon_above": [42.3804, 42.3819, 42.3792],
            "n_grid_row_shift": [0, 1, -1],
            "n_grid_col_shift": [0, -1, 1],
            "gsd_x": [0.5, 0.5, 0.5],
            "gsd_y": [0.5, 0.5, 0.5],
            "incidence_angle": [15.3, 18.7, 12.9],
        }
    )

    # df.write_parquet("nitf.parquet")
    df = pl.read_parquet("nitf.parquet")
    print(df.columns)


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
    unique_images = (
        metadata.unique("image_id")
        .select("image_id", "coordinates")
        .sort(by="image_id")
        .to_dict()
    )

    print(unique_images)

    # Create Geographic Bounding Boxes
    geographic_boxes = {}
    for image, coordinates in zip(
        unique_images["image_id"], unique_images["coordinates"], strict=False
    ):
        geographic_boxes[image] = get_surrounding_box(coordinates)
