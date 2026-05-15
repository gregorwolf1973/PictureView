# PictureView

Security camera image viewer for Home Assistant.

## Configuration

| Option | Description | Default |
|---|---|---|
| `image_folder` | Path to the folder with camera images | `/share/camera` |
| `delete_after_days` | Auto-delete images older than N days (1-365) | `30` |
| `web_port` | Web interface port | `8200` |

## Supported image formats

JPG, JPEG, PNG, GIF, WEBP, BMP

## Usage

Images are sorted by creation time (oldest first). Use the navigation buttons or keyboard shortcuts to browse:

- `→` / Next button: Next image
- `←` / Back button: Previous image
- `Home`: First image
- `End`: Last image

The timeline on the right shows all available days. Click a day to expand it and jump to a specific image.

## Auto-delete

Images older than `delete_after_days` are deleted automatically every hour. Set to 365 to keep images for a full year.
