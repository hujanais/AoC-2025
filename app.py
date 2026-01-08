import polars as pl

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
