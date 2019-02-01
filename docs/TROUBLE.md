file describing difficulties along the way and their solutions:

* I cannot use localhost. found I need to run the app differently to use any host. By checking exercise definitions I see using 127.0.0.1 is fine so deciding to move on.
* flask shows warning saying this server should not be used in production. for this point I'm just ac·knowledging it

* flask is not shutting down when terminating the app. saw I can start it differently but since docker will supposed to handle processes I'll leave it for now.

* travis is failing by my first yml definitions. Started from an example and it worked.

* cannot get docker response. it might be related to address change in flasks.
Fixed it by google how to open address in flask.
* readline returns bytes and need to cut newline. Fix casting issue and trimming.
* cannot get curl response from docker on travis. I'm trying to use the local python version.

* travis doesn't have python 3.7.2 and run into conflicts with my code. I found working example to work with 3.5 and changed to it. 
* python on travis doesn't recognize flask run command. I'm changing to python command.
* python 3.5.6 on travis doesn't work correctly with urllib. I saw I should use same travis version to solve the issue. because 
* everything is working correctly between local and docker environments, and because I prefer using the new module I'm trying to * install python new version on travis. --> succeed installing the correct version on travis...
* new problem emerge - travis new python cannot recognize modules. I'm checking what is travis default python version and writing again everything in that.



