## Developed by :

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>    
    <td align="center"><a href="https://github.com/cmenke42/"><img src="https://avatars.githubusercontent.com/u/122057895?v=4"" width="100px;" alt=""/><br /><sub><b>Carlos Menke(cmenke)</b></sub></a><br /><a href="https://profile.intra.42.fr/users/cmenke" title="Intra 42"><img src="https://img.shields.io/badge/Wolfsburg-FFFFFF?style=plastic&logo=42&logoColor=000000" alt="Intra 42"/></a></td>
    <td align="center"><a href="https://github.com/AndersLazis/"><img src="https://avatars.githubusercontent.com/u/130859506?v=4" width="100px;" alt=""/><br /><sub><b>Andrei Putiev(aputiev)</b></sub></a><br /><a href="https://profile.intra.42.fr/users/aputiev" title="Intra 42"><img src="https://img.shields.io/badge/Wolfsburg-FFFFFF?style=plastic&logo=42&logoColor=000000" alt="Intra 42"/></a></td>
    <td align="center"><a href="https://github.com/Ahsanbaloch/"><img src="https://avatars.githubusercontent.com/u/39459572?v=4" width="100px;" alt=""/><br /><sub><b>Ahsan Abdul Salam(ahsalam)</b></sub></a><br /><a href="https://profile.intra.42.fr/users/ahsalam" title="Intra 42"><img src="https://img.shields.io/badge/Wolfsburg-FFFFFF?style=plastic&logo=42&logoColor=000000" alt="Intra 42"/></a></td>
   
  </tr>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Code stats : 

- 3 contributors
- Total 11 702 lines
  - Typescript : x lines, x%
  - Python : x lines, x%
  - CSS : x lines, x%
  - Shell : x%
  - Other (dockerfiles, envs, configs...) : x%
- Git
  - x branches
  - x pull requests
  - x commits

## Project

ft_transcendence is the final project of the 42 school curriculum, challenging students to create a fully-featured web application. This project focuses on building a single-page application which includes a real-time multiplayer game of pong and a live chat.

## Features

### User Management Features:

On this website, users are able to:

- Sign up and login using their credentials,
- Sign up or login via the School 42 or Google OAuth API,
- Enable or disable 2FA,
- Customize their profile with a unique username and avatar,
- Change color theme,
- Add and remove friends,
- Block or unblock users,
- Keep track of their stats, match history and leaderboard ranking,
- Multiple language support (English, German, Urdu, Russian).
- manage users accounts via Admin panel

### Pong Game Features

The game of Pong features:

- Responsive, 1v1, 3D online game of pong,
- Matchmaking system,
- Ability to invite other players to a game,

### Chat Features

The live chat features:

- Creation of private chats between two users,
- Ability to block individual users so as not to see messages from blocked accounts,
- Context menu enabling users to challenge others to a game of pong.

## Technologies

Technologies are used:

- Frontend: [Angular 17](https://angular.dev/)
- Backend: [Django Rest Framework](https://www.django-rest-framework.org/)
- Database: [Postgresql](https://www.postgresql.org/)
- Deployment: [Docker & Docker-Compose](https://www.docker.com/)
- Web server: [NGINX](https://nginx.org/en/)
- WebSockets: [Django Channels](https://channels.readthedocs.io/)
- Authorization: [Oauth 2.0](https://oauth.net/2/)
- API Documentation: [Swagger](https://swagger.io/)
- Password Hashing: [Argon2](https://github.com/P-H-C/phc-winner-argon2)

## HOW TO RUN
Test server: You can try our project on https://<transcendence.com>

Or run it on your Linux machine:
Before start, please replace marked variables in .env file in root directory with your own.
Then, run the following command:
```
make
```
To access site, go to localhost(by default) with port 4010 or your IP address(if your specified it in .env file):
```
https://localhost:4010
```
To access admin panel simply login as admin user with DJANGO_SUPERUSER credentials from .env file.
To access `pgadmin` site, use to 5432 port of localhost (or your IP address if your specified it before):
```
https://localhost:5432
```
To access API specification, use:
```
https://localhost:6010/api/schema/swagger-ui/
```
or 
```
https://localhost:6010/api/schema/redoc/
```

