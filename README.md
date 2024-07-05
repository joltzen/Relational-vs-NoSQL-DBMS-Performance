# Performance Analysis of Relational and Non-Relational Database Management Systems for Searching Attributes in a Web Application

## Project Overview

This project involves the implementation of a coupon web application using Django, a Python-based web framework, and Google Cloud Platform. The application allows users to upload coupons, write comments, create hashtags, vote on coupons, and search for specific coupons based on hashtags. The primary focus of this project is to compare the performance of relational and non-relational database management systems in terms of response times for different search methods.

## Table of Contents

- [How to use](#how-to-use)
- [System Architecture](#system-architecture)
- [Key Design Decisions](#key-design-decisions)
- [Component View](#component-view)
- [Data Schema](#data-schema)
- [Runtime Examples](#runtime-examples)
- [Measurement and Findings](#measurement-and-findings)
- [Measured Results](#measured-results)
- [Conclusion](#conclusion)
- [References](#references)
## How to use:

### Install requirements

To install the necessary packages, run:
```
 pip3 install -r ./requirements.txt
```

### Start server
To start the server, run:
```
python3 manage.py runserver
```

### Update Models
To update the models, run:
```
python3 manage.py makemigrations coupon
python3 manage.py migrate
```

### Admin console
To access the admin console, run:
```
python3 manage.py runserver
```

## System Architecture

The application is built using Django as the backend framework, Google Cloud SQL as the relational database, and Google Firestore as the non-relational database. The application follows a RESTful API architecture for interoperability and flexibility. Below are the key components:
1. **Client-Side**: User interface and web browser.
2. **Server-Side**: Web server and application server.
3. **Database**: Relational database (Google Cloud SQL) and non-relational database (Google Firestore).

## Key Design Decisions
- **Backend Framework**: Django
- **Relational Database**: PostgreSQL
- **Non-Relational Database**: MongoDB
- **Architectural Style**: RESTful API

## Component View
The application is divided into three main components:
1. **Client-Side**: Includes the user interface and web browser
2. **Server-Side**: Includes the web server and application server
3. **Database**: Includes the database management system and the database itself

## Data Schema
The data schema consists of four tables: `user`, `coupon`, `comment`, and `hashtag`.

- User Table:
   - `id` (Primary Key)
   - `username`
   - `first name`
   - `last name`
   - `email`
   - `password`
     
- Coupon Table:
   - `name` 
   - `expiring date`
   - `discount amt`
   - `score`
   - `code`
   - `comments amt`
     
- Comment Table:
   - `text` 
   - `created date`
     
- Hashtag Table:
   - `name`

## Runtime View
The Runtime View is a UML activity diagram that provides an overview of the main use cases of the coupon application. It shows activities such as creating a new coupon, uploading a coupon, and creating a new comment.

## Crosscutting Concepts

- **Caching**: Reduces the number of database queries and improves application performance.
- **Scaling**: Handles increasing amounts of traffic and data.
- **Authentication**: Ensures that only authorized users can access and modify coupon data.
- **Search Functionality**: Allows users to quickly find relevant coupons.
- **Load Testing and Simulation**: Identifies and resolves performance bottlenecks.
- **Database Monitoring**: Tracks and analyzes database performance and health.

## Measurements and Findings
### Experimental Setup
The performance of the coupon application is tested using different scenarios:

- **Simple Read**: Fetch a single document or row based on a unique identifier.
- **Simple Write**: Insert a single document or row with predefined data.
- **Complex Query**: Extract data based on multiple conditions.
- **Bulk Insert**: Insert 1,000 rows or documents.

## Measured Results
The performance of PostgreSQL and MongoDB is compared in terms of execution times for various operations:
- **Simple Read**: PostgreSQL is faster.
- **Simple Write**: MongoDB is faster.
- **Complex Query**: PostgreSQL is faster.
- **Bulk Insert**: PostgreSQL is faster.

## Conclusion
Both PostgreSQL and MongoDB have their strengths. PostgreSQL is generally faster for reading data, complex queries, and bulk inserts, while MongoDB is faster for simple write operations. The choice between them should be made based on the specific needs and context of the application.

## References
[Locust.io](https://locust.io/)
[BANKS: Browsing and Keyword Searching in Relational Databases](https://www.sciencedirect.com/science/article/abs/pii/B9781558608696501141)
[Integrated Environment Based on Anytime Solution Search Algorithms and A Non-Relational Database for Real-Time Intelligent Systems](https://ceur-ws.org/Vol-2648/paper26.pdf)
[Enhanced query processing over semantic cache for cloud-based relational databases](https://link.springer.com/article/10.1007/s12652-020-01943-x)
