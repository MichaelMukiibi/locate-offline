# Contributing Guidelines

Thank you for helping build offline GIS tooling. Please follow these explicit guidelines when submitting updates.

## Technical Rules
- **No Heavy Frameworks**: Do not add dependencies like GeoPandas or Fiona. All interactions must pass through python's native `sqlite3` or low-level bindings to preserve lightweight architecture.
- **Strict Typing**: All source implementations require explicit Python type hints.

## Pull Request Process
1. Fork the repository and build your feature path from `main`.
2. Ensure local test validations pass completely: `pytest tests/`
3. Structure your commit messages using conventional syntax:
   - `feat(db): implement manual WKB geometric parsing`
   - `fix(cli): resolve bounding box boundary exception`