# Robotics TurtleBot3 – Kelompok 1

## Requirements
* Docker >= 24
* Docker Compose >= 2.20
* Ubuntu 22.04 LTS

## Quick Start
```bash
export ROS_DOMAIN_ID=31
cd docker
docker compose build
docker compose up -d
docker compose exec dev bash
```

## Struktur Repositori
* `docker/` — Dockerfile, Compose file, dan runtime entrypoint script
* `src/` — ROS 2 packages (my_first_robot_package)
* `config/` — Konfigurasi Nav2, SLAM, dan QoS profile
* `launch/` — File launch ROS 2
* `maps/` — Peta hasil SLAM
* `data/` — Log misi, bags, dan data eksperimen
* `docs/` — Laporan dan panduan deployment
* `tests/` — File pengujian

## Menjalankan Misi
```bash
ros2 run my_first_robot_package hello_robot
```

## Konfigurasi
|
Parameter | Lokasi | Default |
| :--- | :--- | :--- |
| `ROS_DOMAIN_ID` | `docker/compose.yaml` | `31` |


## Versi
v1.0.0 — commit 1c6c43f
