# API Demo Template (Homelab + Proxmox VM)

This project is a minimal FastAPI app behind Nginx, packaged with Docker Compose.

It exposes:
- `GET /` for a welcome message
- `GET /add?a=<int>&b=<int>` for query-string addition
- `POST /add` for JSON addition

## 1. Run on the Proxmox VM

From the VM:

```bash
docker compose up -d --build
```

Check containers:

```bash
docker compose ps
```

The Nginx container publishes port `80` (`docker-compose.yml` maps `80:80`).

## 2. Find the VM IP address

On the VM:

```bash
ip a
```

Look for the LAN interface IP, for example `192.168.1.50`.

Use that IP from any other machine on the same network.

## 3. Call the API from a web browser

On another machine, open:

- `http://<VM_IP>/`
- `http://<VM_IP>/add?a=2&b=3`

Example:

- `http://192.168.1.50/`
- `http://192.168.1.50/add?a=2&b=3`

## 4. Call the API with curl from another machine

Set the VM IP:

```bash
VM_IP=192.168.1.50
```

Root endpoint:

```bash
curl "http://$VM_IP/"
```

GET add endpoint:

```bash
curl "http://$VM_IP/add?a=7&b=9"
```

POST add endpoint:

```bash
curl -X POST "http://$VM_IP/add" \
  -H "Content-Type: application/json" \
  -d '{"a":7,"b":9}'
```

## 5. Expected responses

- `GET /` returns:

```json
{"message":"This is a simple API."}
```

- `GET /add?a=7&b=9` returns:

```json
{"result":16}
```

- `POST /add` with `{"a":7,"b":9}` returns:

```json
{"result":16}
```

## 6. Troubleshooting

- If calls fail from another machine, confirm the VM firewall and network allow inbound TCP `80`.
- Confirm containers are running: `docker compose ps`
- Check logs:

```bash
docker compose logs -f
```
