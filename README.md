# Netflix Crawler

Small crawler made with Python and Docker. The response is saved inside result directory in json format with the movies.

Ex: 
```
[
{"genre": "TV Shows", "title": "Shooter", "page": "Netflix Originals", "thumbnail": "https://occ-0-516-420.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABeJudc4EH-VTvKy92phX_GAEFmHRhewSD1HblwZhc11hVMKXa66oMXoCuy8GR5DsXE-zY9mhLobgEixoLmWy8fG1HFW-AWCQ518Ageba0aO0nn3XCa72Euw6cDtw6dnM9O3BrZ_XkA.jpg"},
{"genre": "TV Shows", "title": "Elite", "page": "Netflix Originals", "thumbnail": "https://occ-0-516-420.1.nflxso.net/dnm/api/v5/rendition/412e4119fb212e3ca9f1add558e2e7fed42f8fb4/AAAABZqhOQxN6vDzJV66iPMlnNTnYyVJ-fgS6ty6p_fbAKjrKR_pdqJSL4oH9AlZbOFRLN1xb-P7Lhr5U08t7A9oamc9UcncaI24Fx4GhOizXxThHuIVaR4qAGGx1mT-z1-ynWIzJNRdkg.jpg"},
...
```


## How to use

Install [Docker](https://www.docker.com/get-started), clone this repository and execute:

```
$ mkdir result
$ docker build -t nfcrawler .
$ docker run --name=nfcrawler -v <path>\result:/results nfcrawler
```
