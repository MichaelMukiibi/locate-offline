# System Architecture & Storage Engine Specification

## Data Layer Layout
GeoPackage functions as a standard SQLite 3 database containing a mandatory structure defined by the OGC encoding specification. 

### Core Meta Tables
- `gpkg_contents`: The primary directory of the container. Maps user spatial data tables to coordinate reference systems.
- `gpkg_spatial_ref_sys`: Stores spatial coordinate identifiers (e.g., EPSG:4326 for WGS84).
- `gpkg_geometry_columns`: Defines which columns in user tables store the spatial geometry binaries.

### Geometry Blobs
Vector features are encoded into standard SQLite `BLOB` fields using the explicit GeoPackage binary format header:
- Magic bytes: `GP` (0x4750)
- Version: `0`
- Flags: Byte order layout, envelope dimensions configuration
- SRS ID: 32-bit Integer

## Performance Target
- Spatial querying utilizes the SQLite `R-Tree` virtual table extension. 
- Bounding-box filtering executes in $O(\log N)$ time rather than full-table scans $O(N)$.