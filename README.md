# Real-Time Mood Tracker using Celery, MQTT (EMQX), and Python

## Project Overview

This project is a **Real-Time Mood Tracker** built entirely with **Python**, **Celery**, and **MQTT (EMQX)**. It simulates an automated system where users are asked for their mood at regular intervals. Their responses are collected, processed asynchronously, and stored for later analysis.

---

## Objective

* Track a user’s mood periodically.
* Send notifications asking for the user’s current mood.
* Collect and process mood responses in real-time.
* Use asynchronous processing to ensure non-blocking operations.
* Provide a simple mood history per user.

---

## Key Features

* Automated reminders to collect user moods.
* Real-time mood submission via MQTT.
* Asynchronous task handling using Celery.

---

## Use Case

### "A Day in the Life of a User"

* A user registers and sets a reminder interval (e.g., every 4 hours).
* The system sends a mood request every 4 hours using MQTT.
* The user replies via a simple interface (web, terminal, or app etc).
* The system stores the mood and updates their mood history.
* If no reply is received, a retry or follow-up can be scheduled.

---

## System Workflow

* **User Register**: Enters name and chooses how often they want to be reminded.
* **Reminder Triggered**: Celery Beat fires every interval.
* **Mood Prompt Sent**: MQTT publishes a message to user-specific topic.
* **User Responds**: User replies with a mood (e.g., Happy, Sad).
* **Response Captured**: MQTT Subscriber receives mood.
* **Celery Worker**: Asynchronously saves it to the database.
* **Repeat Loop**: Process repeats as per user interval.

---

## System Architecture

![Architecture Diagram](images/03-celery.excalidraw.png)


---

## System Interaction Workflow


![Sequence Diagram](images/mood_tracker.png)

---

## 4-Day Project Schedule

###  Day 1: Project Setup & Mood Input API
* Set up project structure and folder layout
* Initialize FastAPI backend with required dependencies
* Design user and mood schema for MongoDB or PostgreSQL
* Create API to accept user mood and set mood-check frequency
* Configure EMQX MQTT broker via Docker

###  Day 2: MQTT Communication + Notification Triggers
* Connect FastAPI to EMQX via MQTT for mood prompts
* Implement MQTT publishing to send mood request notifications
* Define topic patterns for user-specific prompts
* Set up MQTT subscriber for receiving mood data 

###  Day 3: Celery Integration + Analytics Engine
* Set up Celery workers for:
  - Scheduled mood check notifications
  - Reminder logic based on user-set intervals
  - Processing incoming mood data for trends
* Store mood history for each user in the database
* Begin analytics development to calculate mood insights

###  Day 4: Dashboard APIs + Final Documentation
* Create endpoints to fetch analytics insights and history
* Write complete README with setup, usage, and contribution guide
* Clean codebase 




		

