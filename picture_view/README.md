# PictureView – Home Assistant Add-on

A lightweight security camera image viewer for Home Assistant OS. Browse all your camera snapshots in order, organized by day in a timeline – directly inside Home Assistant.

![Architectures](https://img.shields.io/badge/arch-aarch64%20|%20amd64%20|%20armv7-blue)
![Version](https://img.shields.io/badge/version-0.05-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/gregorwolf1973)

---

## Features

- **Image viewer** – browse camera snapshots sorted by creation time (oldest → newest)
- **Subfolder support** – automatically scans all subfolders created by your camera
- **Timeline sidebar** – all images grouped by day; click any day or thumbnail to jump directly
- **Navigation** – Previous / Next / First / Last buttons + keyboard shortcuts (← → Home End)
- **Aspect ratio correction** – correct camera distortion with independent width/height stretch factors (0.5×–2.0×), stored per browser
- **Auto-delete** – optionally delete images older than 1–365 days (disabled by default, with clear warning)
- **Dark / Light theme** – follows system preference, switchable in the header
- **Auto-refresh** – picks up new images every 60 seconds without page reload
- **Home Assistant Ingress** – no extra port, no extra login; opens directly in the HA sidebar

## Screenshots

| Viewer with timeline | Settings |
|---|---|
| Dark mode, timeline on the right | HA add-on configuration panel |

## Installation

### Method 1: Add Repository (recommended)

[![Add to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgregorwolf1973%2FPictureView)

Click the button above → the repository is added automatically → continue from step 4.

**Or manually:**

1. In Home Assistant: **Settings → Add-ons → Add-on Store**
2. Top right **⋮ → Repositories**
3. Enter: `https://github.com/gregorwolf1973/PictureView`
4. **PictureView** appears in the store → **Install**
5. **Start** → enable **Show in sidebar** → **Open**

### Method 2: Local add-on

1. Copy the `picture_view/` folder to `/addons/` on your Home Assistant host (via SSH or Samba):
   ```
   /addons/picture_view/
   ├── config.yaml
   ├── build.yaml
   ├── Dockerfile
   ├── run.sh
   └── app/
       ├── app.py
       └── templates/
           └── index.html
   ```
2. **Settings → Add-ons → Add-on Store → ⋮ → Reload local add-ons**
3. **PictureView** under "Local add-ons" → **Install** → **Start**

## Configuration

| Option | Description | Default |
|---|---|---|
| `image_folder` | Path to the folder (and subfolders) containing your camera images | `/share/camera` |
| `auto_delete_enabled` | **Enable auto-delete. WARNING: deleted images are gone forever!** | `false` |
| `delete_after_days` | Delete images older than N days (1–365). Only active when auto-delete is enabled | `30` |
| `web_port` | Internal port for the web interface | `8200` |

### Supported image formats

`JPG` · `JPEG` · `PNG` · `GIF` · `WEBP` · `BMP`

### Camera subfolder layout

Many IP cameras and NVRs create dated subfolders automatically, e.g.:

```
/share/camera/
├── 20260515/
│   ├── snap_090752.jpg
│   └── snap_091830.jpg
└── 20260516/
    └── snap_080100.jpg
```

PictureView scans all subfolders recursively and shows all images sorted by creation time.

## Usage

### Navigation

| Control | Action |
|---|---|
| **Weiter / Next** button | Next image |
| **Zurück / Back** button | Previous image |
| **Erstes / First** button | Jump to first image |
| **Letztes / Last** button | Jump to last image |
| `→` | Next image |
| `←` | Previous image |
| `Home` | First image |
| `End` | Last image |

### Timeline

The timeline panel on the right shows every day that has at least one image. Click a day to expand it and see individual thumbnails with timestamps. Click any thumbnail to jump directly to that image. The currently displayed image is always highlighted in the timeline.

### Aspect ratio correction

Some cameras record with non-standard pixel aspect ratios (e.g. 1:1 pixels on a widescreen sensor). Click the **⚙ gear button** in the image toolbar to open the correction panel:

- **Width ×** – stretch the image horizontally (e.g. `1.12` to widen by 12 %)
- **Height ×** – stretch the image vertically
- Values are saved in the browser and restored on next visit

### Auto-delete

> ⚠ **Warning:** Auto-delete permanently removes image files from disk. This cannot be undone.

To enable:
1. Open the add-on configuration in Home Assistant
2. Set **Enable auto-delete** to `true`
3. Set **Delete after days** to the desired retention period
4. Restart the add-on

When active, the header bar shows a **red warning** with the current retention period.

## Architecture

- **Backend:** Python 3 / Flask – serves images, scans folders recursively, runs cleanup in a background thread
- **Frontend:** Single-page HTML/JS – no external dependencies, HA-style dark/light CSS variables
- **Base image:** Official Home Assistant Alpine Linux base image
- **Supported architectures:** `aarch64` (Raspberry Pi 4/5), `amd64`, `armv7`

## Troubleshooting

**No images shown**
- Check that `image_folder` points to the correct path (e.g. `/share/camera` maps to `/homeassistant/share/camera` on the host)
- Make sure the folder exists and contains supported image files (jpg, png, …)
- Check the add-on log for errors

**Images look squashed / stretched**
- Use the ⚙ gear button in the toolbar to adjust the Width × and Height × correction factors

**Auto-delete is not working**
- Make sure `auto_delete_enabled` is set to `true` in the add-on configuration
- Cleanup runs once per hour; it may take up to 60 minutes after enabling

**New images are not appearing**
- The viewer auto-refreshes every 60 seconds
- Force a refresh by reloading the page

## License

MIT License – © gregorwolf1973
