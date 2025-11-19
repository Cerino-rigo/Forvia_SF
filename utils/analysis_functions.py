import streamlit as st 

def filter_percentage(df, regiones, grupo):
    df_filtered = df.copy()
    if regiones:
        df_filtered = df_filtered[df_filtered['Region'].isin(regiones)]
    if grupo and grupo != 'Todos':
        df_filtered = df_filtered[df_filtered['Group'] == grupo]

    return df_filtered

def filter_projects(df, estados, areas, avance_min):
    df_filtered = df.copy()
    if estados:
        df_filtered = df_filtered[df_filtered['State'].isin(estados)]
    if areas and areas != "Todas":
        df_filtered = df_filtered[df_filtered['Geographical scope'].isin([areas])]
    df_filtered = df_filtered[df_filtered['Percent complete'] >= avance_min]
    avg_progress = df_filtered['Percent complete'].mean() if len(df_filtered) > 0 else 0
    return df_filtered, avg_progress

def assign_coords_to_projects(df, region_col='Geographical scope'):
    region_coords = {
        'EMEA': {'lat': 50.1109, 'lon': 8.6820},
        'ASIA': {'lat': 35.6895, 'lon': 139.6917},
        'NAO': {'lat': 42.3314, 'lon': -83.0458},
        'BRAZIL': {'lat': -23.5505, 'lon': -46.6333}
    }

    df = df.copy()
    df['lat'] = df[region_col].map(lambda x: region_coords.get(x, {}).get('lat', None))
    df['lon'] = df[region_col].map(lambda x: region_coords.get(x, {}).get('lon', None))
    return df.dropna(subset=['lat','lon'])
