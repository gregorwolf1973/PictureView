# PictureView – Home Assistant Add-on Repository

A lightweight security camera image viewer for Home Assistant OS.

[![Add to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgregorwolf1973%2FPictureView)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/gregorwolf1973)

---

## Add-ons in this repository

### PictureView

Browse all security camera snapshots directly inside Home Assistant – sorted by time, grouped by day in a timeline sidebar.

| | |
|---|---|
| **Version** | 0.05 |
| **Architectures** | aarch64 · amd64 · armv7 |
| **Ingress** | Yes (opens in HA sidebar, no extra login) |

**Features at a glance:**
- Chronological image viewer with Previous / Next / First / Last navigation
- Keyboard shortcuts (← → Home End)
- Timeline sidebar grouped by day – click any thumbnail to jump directly
- Recursive subfolder scan – works with cameras that create dated subfolders automatically
- Aspect ratio correction for cameras with non-square pixels
- Optional auto-delete after 1–365 days (disabled by default, with warning)
- Dark / Light theme
- Auto-refresh every 60 seconds

→ See [picture_view/README.md](picture_view/README.md) for full documentation.

---

## Installation

1. Click the **Add to Home Assistant** button above, or go to:
   **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
   and add: `https://github.com/gregorwolf1973/PictureView`
2. Install **PictureView** from the store
3. Set `image_folder` to your camera's image path (e.g. `/share/camera`)
4. Start the add-on and enable **Show in sidebar**

---

## Support

If this add-on is useful to you, consider buying me a coffee ☕

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/gregorwolf1973)

---

## License

MIT License – © gregorwolf1973
