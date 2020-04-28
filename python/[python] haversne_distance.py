df['coor_dist'] = 6371 * np.arccos(
    np.sin(np.radians(df['start_lat'])) * np.sin(np.radians(df['destination_lat'])) +
    np.cos(np.radians(df['start_lat'])) * np.cos(np.radians(df['destination_lat'])) * np.cos(np.radians(df['destination_lng']) - np.radians(df['start_lng']))
)
