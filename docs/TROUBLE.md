file describing difficulties along the way and their solutions:

* I cannot use localhost. found I need to run the app differently to use any host. By checking exercise definitions I see using 127.0.0.1 is fine so deciding to move on.
* flask shows warning saying this server should not be used in production. for this point I'm just ac·knowledging it

* flask is not shutting down when terminating the app. saw I can start it differently but since docker will supposed to handle processes I'll leave it for now.

* travis is failing by my first yml definitions. Started from an example and it worked.

* cannot get docker response. it might be related to address change in flasks.
Fixed it by google how to open address in flask.

