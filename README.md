# Genraft AI

⚠️ This project is work in progress, reaching 0.1.0 version end of November 2023!

If it becomes popular, further work will be made on this project, it depends on the support made by you guys.

<div style="text-align: center;">
  <img src="misc/genraft_ai_icon.png" alt="Genraft AI Framework Logo" style="max-width: 30%; height: auto; display: block; margin: 0 auto;">
</div>

## Introduction

The Genraft AI Toolkit is a dynamic resource for creating sophisticated backend and frontend web solutions, utilizing the power of Python and the official OpenAI API to develop conversational agents. This toolkit harnesses the capabilities of generative AI to facilitate the development of responsive and intelligent agent interactions.

## Features

- Direct integration with the official OpenAI API to enable advanced conversational capabilities.
- Comprehensive backend and frontend development modules tailored for web applications.
- A user-friendly interface for easy management and interaction with the AI models.
- Highly extendable and customizable to cater to diverse web development needs.
- Focuses on accelerating the development cycle of web-based platforms with AI-driven interactions.

## Available Convenience

- Dockerfile supported 
- Docker Compose supported
- kubernetes supported
- MonoRepo Project supported
- Separate Services for Frontend and Backend supported 

## Getting Started

### Tech-Stack

#### General

- [Git](https://git-scm.com) [Version Control]
- [Docker](https://www.docker.com/get-started) [Containerization]
- [GitHub](https://github.com/) [Code Hosting]
- [GitHub Actions](https://github.com/features/actions) [CI/CD]

#### Frontend

- [Typescript](https://www.typescriptlang.org/) [Programming Language]
- [NodeJs](https://nodejs.org) [Javascript runtime]
- [SvelteKit](https://kit.svelte.dev/) [Full-Stack Framework]
- [Svelte](https://svelte.dev/) [Frontend Framework]
- [TailwindCSS](https://tailwindcss.com/) [CSS Framework]
- [DaisyUI](https://daisyui.com/) [Tailwind Component Library]

#### Backend

- [Python](https://www.python.org/downloads/) [Programming Language]
- [FastApi](https://fastapi.tiangolo.com/) [Backend Framework]
- [OpenAI GPT](https://openai.com/) [Language Processing]

### Prerequisites

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [NPM](https://www.npmjs.com/)
- [Nodejs](https://nodejs.org)
- [Python](https://www.python.org/downloads/)

---

### Installation

#### Clone

```bash
https://github.com/kamyabnazari/genraft-ai.git
```

#### Setup

Please create the services after another in order and follow the instructions in the README.md files.

When you run them individually you have to use localhost to access and connect them to each other.

Or Use Docker Compose to create all of it and connect them together.

```bash
docker-compose up --build
```

Please setup in the following order:

1. Setup [Backend](backend/README.md)

2. Setup [Frontend](frontend/README.md)

---

### Wiki
How is the process and worklflow behind the generative software development? Read more on the [Wiki](WIKI.md) page.

---

### License
This project is licensed under the [Apache-2.0 license] License - see the LICENSE file for details.

---

### Acknowledgments

Special thanks to the OpenAI team for providing the API that powers our intelligent agents.

Additionally inspired by [ChatDev]("https://github.com/OpenBMB/ChatDev")