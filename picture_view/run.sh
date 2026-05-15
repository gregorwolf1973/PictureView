#!/usr/bin/with-contenv bashio

IMAGE_FOLDER=$(bashio::config 'image_folder')
DELETE_AFTER_DAYS=$(bashio::config 'delete_after_days')
WEB_PORT=$(bashio::config 'web_port')

export IMAGE_FOLDER
export DELETE_AFTER_DAYS
export WEB_PORT

bashio::log.info "Starting PictureView..."
bashio::log.info "Image folder: ${IMAGE_FOLDER}"
bashio::log.info "Delete after: ${DELETE_AFTER_DAYS} days"

exec python3 /app/app.py
