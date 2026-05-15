# Changelog

## 0.05
- Added `auto_delete_enabled` option (boolean, default: `false`) – auto-delete is now **off by default**
- Warning text in HA add-on configuration (EN + DE) when auto-delete is enabled
- Red warning indicator in the web interface header when auto-delete is active
- Stats API now returns `auto_delete_enabled` status

## 0.04
- Added `icon.png` (256×256) and `logo.png` (250×100) in HA blue/cyan style

## 0.03
- Image now fills the full viewer frame (fixed black bars with absolute positioning)
- Added aspect ratio correction panel (⚙ gear button in toolbar)
  - Independent Width × and Height × stretch factors (0.50–2.00)
  - Values stored in `localStorage`, restored on next visit

## 0.02
- Recursive subfolder scanning – camera-created subfolders are scanned automatically
- Image API uses relative paths to support files with identical names in different subfolders

## 0.01
- Initial release
- Image viewer sorted by creation time
- Day-based timeline sidebar
- Previous / Next / First / Last navigation
- Keyboard shortcuts: ← → Home End
- Dark / Light theme (follows system preference)
- Auto-refresh every 60 seconds
- Configurable auto-delete (1–365 days)
