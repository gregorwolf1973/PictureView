# PictureView – Full Documentation

## Overview

PictureView is a Home Assistant add-on that lets you browse images recorded by a security camera directly inside the Home Assistant interface. Images are displayed in chronological order with a day-based timeline sidebar. Subfolders created automatically by cameras and NVR systems are scanned recursively.

---

## Installation

### Via Add-on Repository (recommended)

1. Open **Settings → Add-ons → Add-on Store** in Home Assistant
2. Click **⋮ (three dots)** in the top right → **Repositories**
3. Paste `https://github.com/gregorwolf1973/PictureView` and click **Add**
4. Find **PictureView** in the store and click **Install**
5. After installation: click **Start**, then enable **Show in sidebar**

### As a local add-on

Copy the `picture_view/` directory to `/addons/` on your HA host, then reload local add-ons via the store menu.

---

## Configuration Options

### `image_folder` *(string)*

The path to the folder where your camera saves images. This path is resolved inside the add-on container.

**Common values:**
| HA path | Container path |
|---|---|
| `/share/camera` | `/share/camera` ✓ |
| `/media/camera` | `/media/camera` ✓ |

The add-on has `share:rw` and `media:rw` mapped. Other paths (e.g. inside `/config`) may not be accessible.

**Subfolder support:** The add-on recursively scans all subfolders. If your camera creates daily folders like `20260515/`, all images inside are found automatically.

---

### `auto_delete_enabled` *(boolean, default: `false`)*

> ⚠ **WARNING: Enabling this option will permanently delete image files from your disk. Deleted images cannot be recovered.**

When set to `true`, the add-on runs a cleanup job every hour and removes all image files whose modification time is older than `delete_after_days` days.

- **Default is `false`** – no images are ever deleted unless you explicitly enable this
- When active, the web interface header shows a **red warning bar** with the current retention period
- The add-on configuration description also contains a visible warning

---

### `delete_after_days` *(integer, 1–365, default: `30`)*

Number of days to keep images. Images older than this value are deleted when `auto_delete_enabled` is `true`.

Examples:
- `1` – keep only today's images
- `7` – one week
- `30` – one month (default)
- `365` – one full year

---

### `web_port` *(port, default: `8200`)*

Internal port used by the Flask web server. You normally do not need to change this. Home Assistant Ingress proxies requests through this port transparently.

---

## Web Interface

### Image Viewer

The main area shows the currently selected image at full size. The image is displayed with `object-fit: contain`, meaning it fills the available area while preserving the original aspect ratio (letterboxed with black bars if needed).

**Toolbar (top of image):**
- File name and full path relative to `image_folder`
- Creation date and time
- Image counter (e.g. `42 / 317`)
- ⚙ Aspect ratio correction button

### Navigation Controls

| Button | Keyboard | Action |
|---|---|---|
| Erstes / First | `Home` | Jump to first image (oldest) |
| Zurück / Back | `←` | Previous image |
| Weiter / Next | `→` | Next image |
| Letztes / Last | `End` | Jump to last image (newest) |

### Timeline Sidebar

The right panel groups all available images by calendar day (newest day at the top). Each day entry shows:
- Abbreviated weekday + date
- Number of images that day

Click a day header to expand it and see individual entries with timestamps. Click any entry to jump directly to that image. The timeline automatically scrolls to and highlights the currently displayed image.

### Aspect Ratio Correction

Click the **⚙ gear icon** next to the image counter to open the correction panel:

| Setting | Description |
|---|---|
| **Width ×** | Horizontal stretch factor (0.50–2.00) |
| **Height ×** | Vertical stretch factor (0.50–2.00) |

**Example:** If your camera records 4:3 images that should be displayed as 16:9, set Width × to approximately `1.33`.

Values are stored in `localStorage` and survive page reloads. Click **Reset** to return to `1.00 / 1.00`.

### Dark / Light Theme

Click the sun/moon icon in the header to toggle themes. The choice is remembered in `localStorage`. On first visit the theme follows the system preference (`prefers-color-scheme`).

### Auto-Refresh

The image list refreshes automatically every 60 seconds. If new images have been added to the folder, the timeline updates and the counter is corrected. The currently displayed image remains selected.

---

## Folder Structure (inside the add-on)

```
/app/
├── app.py            – Flask backend (API + cleanup thread)
└── templates/
    └── index.html    – Single-page frontend
```

---

## API Endpoints

These are internal endpoints used by the frontend. They can also be used for integration or debugging.

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serves the main HTML page |
| `/api/images` | GET | Returns JSON list of all images (sorted by mtime) |
| `/api/image/<path>` | GET | Serves an image file by relative path |
| `/api/stats` | GET | Returns total count, days, folder, delete settings |

### `/api/images` response example

```json
[
  {
    "name": "20260515/snap_090752.jpg",
    "basename": "snap_090752.jpg",
    "date": "2026-05-15",
    "datetime": "2026-05-15 09:07:52",
    "timestamp": 1747296472.0
  }
]
```

### `/api/stats` response example

```json
{
  "total": 317,
  "days": 12,
  "auto_delete_enabled": false,
  "delete_after_days": 30,
  "folder": "/share/camera"
}
```

---

## Security Notes

- The `/api/image/<path>` endpoint validates that the resolved file path stays within `image_folder` to prevent path traversal attacks
- The add-on runs without login protection – access is controlled by Home Assistant's own authentication
- No data is sent to external servers

---

## Troubleshooting

### No images are shown

1. Verify `image_folder` is set correctly (e.g. `/share/camera`)
2. Check that the folder exists and is not empty
3. Check the add-on log (**Settings → Add-ons → PictureView → Log**)
4. Supported formats: `.jpg` `.jpeg` `.png` `.gif` `.webp` `.bmp`

### Images appear distorted

Open the ⚙ correction panel in the image toolbar and adjust **Width ×** or **Height ×** until the image looks correct.

### Auto-delete is not removing old images

- Confirm `auto_delete_enabled` is `true` in the configuration
- The cleanup runs every hour – wait up to 60 minutes after enabling
- Check that the add-on has write access to the image folder (`share:rw` or `media:rw`)

### New camera images are not appearing

The list refreshes every 60 seconds. For an immediate update, reload the browser page.

### The add-on won't start

Check the log for Python errors. Common causes:
- `image_folder` path does not exist (the add-on will start anyway and show "No images found")
- Port `8200` is already in use – change `web_port` in the configuration
