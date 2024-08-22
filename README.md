<br/>

[![Stargazers](https://img.shields.io/github/stars/naijadeveloper/maket.svg?style=for-the-badge)](https://github.com/naijadeveloper/maket/stargazers) [![LinkedIn](https://img.shields.io/badge/-enoch_enujiugha-blue?style=for-the-badge&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/enoch-enujiugha) [![Twitter](https://img.shields.io/badge/-follow_me-gray?style=for-the-badge&logo=X&logoColor=white)](https://www.x.com/naijadeveloper) [![Portfolio website](https://img.shields.io/badge/-portfolio-seagreen?style=for-the-badge)](https://naijadev.vercel.app/) [![Support me](https://img.shields.io/badge/buy_me_a_coffee-FFDD00?logo=buymeacoffee&style=for-the-badge&logoColor=black)](https://www.buymeacoffee.com/mmejuenoch)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />
<br/>
<br/>
<div align="center">
  <a href="https://github.com/naijadeveloper/Docket">
    <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">
    <img src="https://user-images.githubusercontent.com/74038190/213844263-a8897a51-32f4-4b3b-b5c2-e1528b89f6f3.png" width="50px" />
    <span>Maket</span>
    <img src="https://user-images.githubusercontent.com/74038190/213844263-a8897a51-32f4-4b3b-b5c2-e1528b89f6f3.png" width="50px" />
  </h1>
  <a href="https://maket-three.vercel.app/"><b>CHECK OUT WEBSITE</b></a>

  <p align="center">
    A simple 'online marketplace' with <b>django!</b>
    <br />
    <a href="https://github.com/naijadeveloper/maket/issues">Report Bug</a>
    <strong>·</strong>
    <a href="https://github.com/naijadeveloper/maket/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#contributing">Contributing</a>
      <ul>
        <li><a href="#Note">Note</a></li>
      </ul>
    </li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
      </ul>
    </li>
  </ol>
</details>
<br/>
<br/>
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

<!-- ABOUT THE PROJECT -->

## About The Project

The website features user authentication, profile management, item listings and ratings, messaging between sellers and buyers, search functionality, a shopping cart, media storage and PostgreSQL database management.

The app lets you create an account and management items, you want to sell. Although, the feature "checkout" isn't available. This was a project built for the purpose of understanding the features of 'Django'. A 'pratice project', if you will ✌🏾

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

### Built With

- [![Python](https://img.shields.io/badge/Python-2F75D8?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/)
- [![Django](https://img.shields.io/badge/Django-132030?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/5.1/)
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-brown?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
- [![Supabase](https://img.shields.io/badge/Supabase-darkgreen?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

## Contributing

1. Fork the Project
2. Clone project to local device
3. Create a virtual evironment and install the packages (`pip install -r requirements.txt`)
4. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

### Note

<em>Some of my struggles</em>

- I don't know if you would ever encouter this, but I struggled for a week or so trying to install `django-cloudinary-storage` package with python 3.12, the problem had something to do with 'building wheel', I tried a lot of solutions, only one worked for me. I installed python 3.10 and used that to install the package globally, and then I tried installing the package again, locally, in my virtual environment with python 3.12 and it worked, why? lol I don't know, shhhhh don't ask questions, if it ain't broken no more leave it lol.
- To allow your app/website communicate with the postgresql database, you need the engine `django.db.backends.postgresql_psycopg2` but this won't work without `pip install psycopg2-binary`.
  Initially I was using sqlite3 for database, then I launched the website on vercel and I met the _500 internal server error_.
  For this I can suggest 3 solutions

1. Make sure you have included your environment variables in vercel
2. Make sure you have this `psycopg2-binary` installed
3. Vercel doesn't support sqlite databases, because it is a serverless environment. [Read more about this here](https://vercel.com/guides/is-sqlite-supported-in-vercel)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

## Contact

- [Twitter@naijadeveloper](https://twitter.com/naijadeveloper)

- [LinkedIn@enoch-enujiugha](https://www.linkedin.com/in/enoch-enujiugha)

- [Portfolio](https://naijadev.vercel.app/)

- mmejuenoch@gmail.com / naijadeveloper@gmail.com

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

## Acknowledgments

- [README Template](https://github.com/othneildrew/Best-README-Template)
- [Gifs for Github](https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" />

### Inspiration

- [Freecodecamp - Learn django by building an online marketplace](https://www.youtube.com/watch?v=ZxMB6Njs3ck&t=1s&pp=ygUTZnJlZWNvZGVjYW1wIGRqYW5nbw%3D%3D)
