from datetime import datetime
import fiona
from fiona.crs import CRS

def create_geopackage(filepath: str):
    """
    Initializes a production-grade GeoPackage container and seeds it 
    with standard vector layers using Fiona.
    """
    
    # 1. Define the Coordinate Reference System (WGS 84 Lat/Long)
    # This automatically writes to the underlying gpkg_spatial_ref_sys table.
    crs = CRS.from_epsg(4326)

    # 2. Define the schema layout for properties and the geometry type
    schema = {
        'geometry': 'Point',
        'properties': {
            'name': 'str:80',
            'amenity': 'str:50',
            'updated_at': 'str:24'
        }
    }

    # 3. Open the file context using the standard GPKG driver
    # Creating a layer inside a GeoPackage uses the 'layer' attribute
    with fiona.open(
        filepath,
        mode='w',
        driver='GPKG',
        crs=crs,
        schema=schema,
        layer='points_of_interest'
    ) as layer:

        # Sample vector feature records to insert
        records = [
            {
                'geometry': {'type': 'Point', 'coordinates': (32.5825, 0.3476)}, # Longitude, Latitude
                'properties': {
                    'name': 'Makerere University Campus',
                    'amenity': 'university',
                    'updated_at': datetime.utcnow().isoformat()
                }
            },
            {
                'geometry': {'type': 'Point', 'coordinates': (30.6568, -0.6072)},
                'properties': {
                    'name': 'MUST Main Campus',
                    'amenity': 'university',
                    'updated_at': datetime.utcnow().isoformat()
                }
            }
        ]

        # Batch write elements into the GeoPackage layer
        layer.writerecords(records)

    print(f"✅ Production GeoPackage successfully created at: {filepath}")

if __name__ == "__main__":
    create_geopackage("data/spatial_store.gpkg")