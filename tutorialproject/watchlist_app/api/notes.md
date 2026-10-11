Here is a simple, step-by-step walkthrough of exactly what happens underneath the hood when a user tries to create a review using this code.

Think of this process as the **"Life of a Request."**

### **Step 1: The Entry Point (The URL)**

```python
path('platforms/<int:pk>/reviews-create', ReviewCreate.as_view(), ...)

```

Imagine a user wants to review a movie (let's say the movie's database ID is `5`). They send a POST request (usually containing a JSON payload with a `rating` and `description`) to the URL: `platforms/5/reviews-create`.

* Django’s router catches this URL.
* It extracts the `5` and assigns it to the variable `pk` (Primary Key).
* It then hands the request and the `pk` over to your `ReviewCreate` view.

### **Step 2: Data Validation (The Serializer)**

```python
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)

```

Before the view can save anything, the data needs to be checked. The `CreateAPIView` automatically passes the user's incoming JSON data to the `ReviewSerializer`.

* The serializer checks: "Did they provide a valid rating (between 1 and 5)? Is the description under 200 characters?"
* Notice the `exclude = ('watchlist',)` line. You are explicitly telling the serializer: **"Do not expect the user to send the movie ID in their JSON payload."** This is a great security and design choice. The user shouldn't decide which movie they are reviewing in the JSON; the URL already tells us that!

### **Step 3: The Interception (The View)**

```python
def perform_create(self, serializer):
    pk = self.kwargs.get("pk") 
    specific_movie = WatchList.objects.get(pk=pk) 
    serializer.save(watchlist=specific_movie)

```

Once the serializer says, "The data looks good," Django is ready to save it to the database. But there is a problem: the `Review` model *requires* a `watchlist` (movie), and we just told the serializer not to ask the user for one!

This is where `perform_create` swoops in to save the day. It intercepts the save process right before the database is touched:

1. **`self.kwargs.get("pk")`**: It looks at the URL parameters and grabs that `5`.
2. **`WatchList.objects.get(pk=pk)`**: It goes to the database and says, "Give me the actual movie object that has ID 5."
3. **`serializer.save(watchlist=specific_movie)`**: It finally tells the serializer, "Okay, go ahead and save this to the database, but forcefully attach it to Movie #5."

### **Step 4: Storage (The Model)**

```python
class Review(models.Model):
    # ... fields ...
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")

```

The data officially hits the database.

* A new row is created in the `Review` table.
* The `rating` and `description` are saved.
* The `created` and `updated` timestamps are automatically generated.
* The `watchlist` column is filled with the ID of the movie fetched in Step 3.

**Summary:** The URL tells the app *which* movie is being reviewed. The serializer ensures the review text/rating is *valid*. The view *glues* the URL's movie to the user's valid data. The model actually *saves* the glued data permanently.

---

## **Django Architecture & Backend Fundamentals**

---

### **1. Project Structure & Generation Commands**

#### **Project Layout:**
```
Django-rest-framework-/                <-- Workspace / Tooling Root
├── pyproject.toml                     <-- Project metadata & dependency list (PEP 517/621)
├── .python-version                    <-- Python version lock (e.g., 3.12)
├── .venv/                             <-- Isolated virtual environment
│   └── Lib/site-packages/             <-- Unpacked raw Python source code for dependencies
└── tutorialproject/                   <-- Django Project Root
    ├── manage.py                      <-- CLI entrypoint for Django commands
    ├── core/                          <-- Main Configuration Package
    │   ├── settings.py                <-- Master settings
    │   ├── urls.py                    <-- Root routing
    │   ├── wsgi.py                    <-- Synchronous production gateway
    │   └── asgi.py                    <-- Asynchronous production gateway
    ├── watchlist_app/                 <-- Feature App (movies & reviews)
    ├── todos/                         <-- Feature App
    └── db.sqlite3                     <-- SQLite database file
```

#### **Commands to Recreate from Scratch:**
```bash
# 1. Root & Virtual Environment Setup (via uv)
mkdir Django-rest-framework- && cd Django-rest-framework-
git init
uv init                                      # Creates pyproject.toml, .python-version, main.py
uv add django djangorestframework            # Creates .venv/ and installs dependencies

# 2. Django Project Setup
mkdir tutorialproject && cd tutorialproject
uv run django-admin startproject core .       # Creates core/ and manage.py (trailing '.' prevents nested folders)

# 3. Individual Apps
uv run python manage.py startapp watchlist_app
uv run python manage.py startapp todos
```

#### **Why `tutorialproject/` Subfolder vs. Utmost Root?**
* **Root directly:** Simpler for pure Django projects; avoids `cd tutorialproject`.
* **Subfolder (`tutorialproject/` or `backend/`):** Best practice for full-stack repos (e.g. `frontend/` + `backend/`) and prevents Django runtime files (`db.sqlite3`, static, media) from cluttering tooling files in the repository root.

---

### **2. Database & Password Security**

#### **SQLite (`db.sqlite3`):**
* **Self-Contained & Serverless:** Unlike PostgreSQL or MySQL, SQLite runs no background service/daemon. The file `db.sqlite3` **is** the entire database (tables, indexes, records). Python reads and writes directly to this file.
* If deleted, all data is lost until recreated with `manage.py migrate`.

#### **Password Storage in `auth_user`:**
Passwords are never saved in plain text. Django uses salted, one-way cryptographic hashing:
```
pbkdf2_sha256$1200000$uAdDc8LTDCYvqYkfcf0BZU$Ai2IGXXeWVr2MC3v6LKf22xDyO8w8tzg9cQ49yiFHhQ=
└─────┬─────┘ └───┬───┘ └──────────┬─────────┘ └──────────────────────┬──────────────────────┘
  Algorithm   Iterations         Salt                               Hash
```
* **Algorithm (`pbkdf2_sha256`):** PBKDF2 with SHA-256.
* **Iterations (`1200000`):** Hashes the password 1.2 million times, making GPU/brute-force attacks computationally impractical.
* **Salt:** Random string unique to each user. Prevents rainbow table attacks (two identical passwords produce completely different hashes).
* **Hash:** The resulting mathematical signature. Verification recalculates this hash upon login and compares strings.

---

### **3. `settings.py` Blueprint**

* **`BASE_DIR`:** Absolute path to `tutorialproject/` anchor.
* **`SECRET_KEY`:** Cryptographic key used to sign session cookies, generate CSRF tokens, and secure password-reset tokens. (The prefix `django-insecure-` flags keys auto-generated for local development; in production, keep secret via environment variables).
* **`DEBUG`:** Enables detailed traceback pages in local development (must be `False` in production).
* **`ALLOWED_HOSTS`:** Prevents HTTP Host header poisoning attacks.
* **`INSTALLED_APPS`:** Registers built-ins (`admin`, `auth`, `sessions`, `messages`, `staticfiles`), third-party libraries (`rest_framework`), and local apps (`watchlist_app`, `todos`, `api`).
* **`MIDDLEWARE`:** Ordered pipeline of hooks run on every request/response (security, sessions, CSRF, authentication).
* **`ROOT_URLCONF`:** Entrypoint for URL routing (`core.urls`).
* **`WSGI_APPLICATION`:** Entrypoint for synchronous web servers (`core.wsgi.application`).
* **`DATABASES`:** Database configuration (defaults to SQLite: `BASE_DIR / 'db.sqlite3'`).
* **`AUTH_PASSWORD_VALIDATORS`:** Rules preventing weak passwords (minimum length, common sequences, numeric-only, similarity to username).
* **`LANGUAGE_CODE` & `TIME_ZONE`:** Localization and timezone configuration (`UTC` with `USE_TZ = True`).
* **`STATIC_URL`:** URL prefix for serving CSS, JS, and images (`/static/`).

---

### **4. Web Server Architecture: Nginx, Gunicorn, & Workers**

```
[ Client / Browser ]
         │ (HTTP / HTTPS)
         ▼
[ Nginx (Reverse Proxy) ]
  • Serves static files directly from disk
  • Handles SSL/TLS certificates
  • Defends against DDoS & Slowloris attacks (buffers slow clients)
         │ (Internal HTTP)
         ▼
[ Gunicorn / Uvicorn (App Server) ]
  • Manages Python worker processes
  • Translates HTTP requests to WSGI/ASGI calls
         │ (Python callable)
         ▼
[ Django Application ]
  • Executes views, queries database, returns response
```

#### **Workers vs. Threads vs. CPU Cores:**
* **Worker (Process):** An independent `python.exe` process with its own dedicated memory space. If one crashes, other workers continue running.
* **Thread:** A thread of execution **inside** a worker process. Multiple threads share the process's memory.
* **Hardware Mapping:** On a multi-core CPU (e.g. Ryzen 5600G with 6 Cores / 12 Hardware Threads), the OS scheduler distributes these software worker threads across physical/logical CPU threads.
* **Concurrency in WSGI:** 1 worker/thread = **1 in-flight request at an exact instant** (not 1 user forever). Since typical requests take only 20–50ms, a pool of 36 threads can handle hundreds of requests per second (millions per day).

---

### **5. WSGI vs. ASGI & The Sync vs. Async Decision**

| Dimension | **WSGI** (Synchronous) | **ASGI** (Asynchronous) |
| :--- | :--- | :--- |
| **Model** | Synchronous / Blocking | Asynchronous / Non-blocking (Event Loop) |
| **Protocols** | HTTP only | HTTP, WebSockets, HTTP/2, SSE |
| **Server** | Gunicorn, uWSGI | Uvicorn, Daphne |
| **Entrypoint** | `core/wsgi.py` | `core/asgi.py` |
| **Concurrency** | 1 in-flight request per thread | Single thread handles thousands via `asyncio` |

#### **Why NOT make everything Async?**
1. **The Event Loop Trap:** An async worker runs an event loop on a single thread. If any function runs synchronous blocking code (`time.sleep()`, heavy loops, unoptimized queries), **the entire server freezes for all users on that worker**.
2. **Django ORM is Historically Synchronous:** Django models and relations are synchronous. Calling relations like `movie.platform` inside an async view raises `SynchronousOnlyOperation` unless manually wrapped in `sync_to_async`.
3. **No Speedup for CPU/Fast DB Queries:** Async does not execute code faster; it only allows concurrent waiting. For 5ms database lookups, synchronous WSGI has lower overhead and is much simpler to debug.

#### **When to use each:**
* **Use WSGI (Sync):** Standard CRUD APIs (like movie watchlists, reviews, accounts), forms, and standard admin panels.
* **Use ASGI (Async):** Real-time WebSockets (chat, live notifications), long-polling, or views waiting on slow 3rd-party network calls (OpenAI/Gemini APIs, payment webhooks).