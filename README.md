# `moviedb_api`

`moviedb_api` is a Django-based backend API for managing movie data using The Movie Database (TMDB) API. This project provides endpoints for accessing popular movies, searching for movies, retrieving detailed information, and more.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

`moviedb_api` is designed to provide a robust backend solution for a movie database application. It leverages the TMDB API to fetch movie data and offers features like caching and pagination for enhanced performance and usability.

## Features

- **List Movies**: Retrieve a list of movies from the local database.
- **Retrieve Movie Details**: Get detailed information about a specific movie using its TMDB ID.
- **Popular Movies**: Fetch a list of popular movies from the TMDB API.
- **Search Movies**: Search for movies by title or query string using the TMDB API.
- **Movie Details**: Get detailed information about a specific movie from the TMDB API.
- **Caching**: Reduce API calls and improve performance with caching.
- **Pagination**: Navigate through large lists of movies with pagination.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **TMDB API**: The Movie Database API for movie data.
- **Requests**: HTTP library for making API requests.
- **Redis** (optional): In-memory data structure store for advanced caching.

## Installation

To set up the `moviedb_api` project, follow these steps:

1. **Clone the repository:**

   ```bash
    git clone https://github.com/yourusername/moviedb_api.git
    cd moviedb_api
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate