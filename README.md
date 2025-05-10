## Task 1

httpServer_crash.go represents HTTP server that simultes an unreliable banking service.

Algorithm uses a probabilistic model to simulate failure scenrios based on random number generation:

1. **Core Dump (0.5% chance)**
Crashes the server, request restart.
2. **Internal Server error (19.5% chance)**
HTTP 500 Error
3. **Database Connection (30% chance)**
Send `error.html` file, simulate database unavailability
4. **Latency Issues (20% chance)**
Make server progressively slower
5. **Successful Responce (30% chance)**
Nomal response `index.html`
