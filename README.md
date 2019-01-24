# Welcome to SuperUp DevOps challenge

### Prerequisites

* A GitHub account
* A [TravisCI](https://docs.travis-ci.com) account 
* A [Docker hub](https://hub.docker.com) account
* Local Docker installation

### Instructions

File devops-challenge.txt contains an encrypted text to be decrypted using AES 128 bit algorithm and a secret key.
With the language of your choice follow these instructions in the next 72 hours to show the decrypted text:

1. Create your own GitHub repo with the code `github.com/<GitHub_User>/<Challenge_Project>`  - clone this project, change its name and restructure it as you see fit in a maintainable logic way, you may use `/example`  folder as a general guidline.
2. Write an application that will extract the encrypted message from devops-challenge.txt file.
3. The key and link to the file have been provided separately, DO NOT COMMIT THEM, if they will be exposed to GitHub you will be disqualified.
4. Create a docker container that will:
* Return `{ message: <DECRYPTED_MESSAGE> }` to http://127.0.0.1:5000/message
* Return `{ status: completed, container: <LINK_TO_DOKERHUB>, project: <LINK_TO_GITHUB> }` to http://127.0.0.1:5000/status
* **Tip**: *use different routers*
5. Running docker-compose up should get everything up and running.
6. Contain a minimal test suite.
7. Create a [Travis CI](https://travis-ci.org/) account, and add a `.travis.yml` that will build, test and deploy your code and container/s.
8. Travis process should run on push to `master` branch and `publish` the container to your own docker hub account.
9. Project should contain a well documented code, informative commit messages, and `SUMMARY.md` file explaining each step of the development process.
10. Contain a `TROUBLE.md` describing difficulties along the way and their solutions.
11. Contain a `INSTRUCTIONS.md` explaining a cloning user how to use the repo - running, testing etc.
12. `verification.sh` should run instantly, if you used a `.env` file, share it privately in the returning email
13. To test the decryption you can use https://aesencryption.net/
14. Once completed, reply to the challenge email:
```
Subject: SuperUp DevOps Challenge complete
Content: Name:      <YOUR_NAME>
         Project:   <LINK TO GITHUB PROJECT>
Attached: `.env` (if you used one)

```
```
michael@superup.me
```
