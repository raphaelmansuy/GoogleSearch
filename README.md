 Project Name

This is a Python project that uses pip to manage dependencies.

## Installation

1. Clone the repository
2. Install pipenv by running `pip install pipenv` if you don't already have it
3. Navigate to the project directory
4. Install the project dependencies by running `pipenv install`
5. Activate the virtual environment by running `pipenv shell`
6. Run the Python script by running `python google-search.py --query "search query"`

## Usage

Example:

```bash
python google-search.py --query "pandassur"
```

Result:
```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "Pandassur: Assurance emprunteur au meilleur prix",
      "link": "https://www.pandassur.fr/",
      "displayed_link": "pandassur.fr\nhttps://www.pandassur.fr",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAhFBMVEVHcEwaGhoVFRULCwsYFxcZGRn+///6/Pz9///9///9///+///T1NQXFhYVFRUYGBgBAQH8/f39///////4+vr///+trq59fn6RkpKys7PDxMQWFhYaGhqdnp7o6Ojk5eXi4uLw8PBsbGzX2Ng7OzsfHx+srKxRUlJYWFgbGxseHh4fHx//FXBsAAAALHRSTlMAXer/uBY0W5eyxH4aSsws/+r///6gXf//////d/v//9P//////4r/maaN42NiUosAAAG8SURBVHgBZZCJopsgEEXHLXuUBPpESfChmZLl//+vlyBp+zxZWO5hHKFIlhdlhXG13mx3u+1+fSA65kXdpLwoClEf9qezPEfUry+BzZwiJXLRnkKSkEoLKMco1Mi7dDghOxjZ/AgheuRLw9DMBeeXyGuThFXIl5wOSdjFE1J+xjjZpAJx23a9QiSHvp8VFfPDd8jdKIQwVkqNMb3U6p1PLsi3cDMIJGOSjDWBbwtBdu9tgeI3DIW4qST8tkMQrti89rfwiHHyQvAgUfaLqOmTIFjKSaIZJ7sk3Inuk7UWwoTCo5IhPoe5f79PSdWIPDYx6kGqlnlUqh/bIQi6pqx1dkAJrMDZoUN2MhCqck2P0dnAeWbyfkr3qLypqfY4P+DjflwzmvUFl5Sb3r4ZOxWzWVMdG+YHsQldoooWvrNwYiuT9oLBk3I2OnThemOE8a2+XnU7olXDgQu9mEU0PLZMuO6iMDEFGZUMw/fOuU7wkiNdGBj2Wt8ML2moiRPURr6kIjSx4PFIsxcRZWlRcqJpPiqBFNCTIzVRnVQCVT5vV/PTnkSXT4FAkxaXz7EqnqloNjIQFlngSOCYtv4ApdlVJNagPf8AAAAASUVORK5CYII=",
      "description": "pandassur est une Société par Actions Simplifiée au capital de 6 000.00 €, inscrite au registre du commerce et des sociétés de Bar-le-Duc sous le numéro 910 702 ...",
      "snippet": "pandassur est une Société par Actions Simplifiée au capital de 6 000.00 €, inscrite au registre du commerce et des sociétés de Bar-le-Duc sous le numéro 910 702 ...",
      "source": "pandassur.fr"
    },
    {
      "position": 2,
      "title": "Launch of pandassur.fr",
      "link": "https://www.elitizon.com/2023/19-04-pandassur/",
      "displayed_link": "elitizon\nhttps://www.elitizon.com › 19-04-pandassur",
      "favicon": "data:image/png;base64,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",
      "description": "18 Apr 2023 — Welcome to Pandassur, a groundbreaking loan insurance broker in France that aims to make the process of obtaining insurance more accessible, ...",
      "snippet": "18 Apr 2023",
      "source": "elitizon"
    },
    {
      "position": 3,
      "title": "pandassur",
      "link": "https://www.youtube.com/channel/UCJ8sMmrJKw4W0bibuZaeaNw",
      "displayed_link": "YouTube\nhttps://www.youtube.com › channel",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAA3ElEQVR4Ae2WIQzDIBBFEdPV6Ip6L2Y3Me9NMzuB98GbWrysqHf1otWYismm+vYFTRCEhXXjJrjkmSslLwHgi8vjxkoRKAL/J0BCSHAHGhjQgxHMwIKnY/Px+taNHd2/Bmg3p4wKuIH0Y1RQAB+ugDJxDgn0GQVMSMBmFJhDApSTYwLLQtR13xNAo0oWINS6ErXtpxInX0CmC3g1TURNkypQ+QL1IYG9hiFFRPIL8C8B/ybkO4bsFxH7Vcz+GLE/x5yBRL+LZDVQkTi2Ochn70dimQpFspKKi0AReAF/IVUTZ3/BGQAAAABJRU5ErkJggg==",
      "description": "pandassur. pandassur. @pandassur. @pandassur ‧ ‧ 2 subscribers ‧ 1 video ... pandassur.fr. Home. Videos. Playlists. Channels.",
      "snippet": "pandassur. pandassur. @pandassur. @pandassur ‧ ‧ 2 subscribers ‧ 1 video ... pandassur.fr. Home. Videos. Playlists. Channels.",
      "source": "YouTube"
    },
    {
      "position": 4,
      "title": "Raphaël MANSUY'S Post - Pandassur",
      "link": "https://ug.linkedin.com/posts/raphaelmansuy_pandassur-n%C3%A9o-courtier-en-assurances-activity-7054707612583395328-w4cw",
      "displayed_link": "LinkedIn\nhttps://ug.linkedin.com › posts › raphaelmansuy_pandass...",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABDUlEQVR4AWP4////gOLB44D6nTcsGIo33QHi/zTGd0B2YTiAPpYjHIHNAf/piQk6wGPW8f/rLz8HYRCbXg5AWI4GQGJ0cwDY12gAJDbcHUA4CkZAIqQUK7Ts/m/SfxBMs5RupswBaACr+P47b/5zlG/5DyzZ/r/+8hNF7vuvP//nn3r0X6JhJ+0ccPrR+/+H7735jw9cf/n5v0D1Nuo5gBxQve06zR0AjoL7b7/+//zjN4bc+ScfaOeA33///k9Yfg4mDw7u/Xdeo6uhnQP6D93FMNxlxjF0ZbRzgMXEQ9iyI90cALIMJoccDXRzAK6CZog6YNQBow6gIx54Bwx4x2RAu2bAysoEZu9o7xgAQrvkxt3WZi0AAAAASUVORK5CYII=",
      "description": "Data Engineering | DataScience | AI & Innovation | Follow me for deep dives on data-engineering and AI. Don't forget to use ! 2mo.",
      "snippet": "Avec pandassur, économisez jusqu'à 15 000 euros sur votre prêt immobilier ! On vous explique tout ici pandassur.fr ​​À part ça, j'adore les vieux 33t, ...",
      "source": "LinkedIn"
    },
    {
      "position": 5,
      "title": "Elitizon",
      "link": "https://www.facebook.com/elitizonltd/?locale=ms_MY",
      "displayed_link": "Facebook\nhttps://www.facebook.com › ... › Elitizon",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAD30lEQVR4AayShW4cMRCGLQgzHArKDK9xor5KnyDMSZmZmZmZRWWuKMy8e3y7U8/KvXG6PlR+6dM3Wtv/tElYulnzHXI918HnvQZ7PNfgGfdvz1XQEJzFtz14B++y+crCO+D2XoG97ssw475swhwuGWSOK26T3zX24luWbZbehTxe1uS+YOiuCzGwOB+3mA2yAvcFU8cO7Mrsf30R3Lz4nfMcL+eglZyNkm3QGXZhJ0snzrOw3nE61uc4zQs4wmKOxC3PaIszZA4/I2On6zSsY8ni4P9Kx6loX/WJMCCOk5G47dCZ+r79HLtxR8LfueN45F318TDEORYiW4TJHBcvbf8QhT/TJoRiJkQME2bCJvRpJnwaM8TbuX24Q/k3wS82VR0JwRwOB8nSjF5xJgRvhgxIEtEj3kngLibHcQzc1YdDetWhICSj8iD5UW8MUsX+PoBGdNzJ/qXqQHBv5f4AVHCEBX4yp1LMG26EIJ2I+2hpFn18J8OsuQi5lXv9MxV7/ZAul35HIY0k7cCduJtV7tN95bt0sNgdt5g1sjR/GrX/+E9+j8DyI35xV7eh6q/cpftY2Q5tDwfSoVxYj5jwf5Yf4qV0j+bknXtY2bbZZxxIh9KtlkERfjaD52QFcgdSvl17xkq3zP4u3TwDSAlZAZ2pgmeZgrtZ6aZpraRrGpR0kuVZFTpXv1eBu1lpx5RW3DEFFu1kmWzSM21AiehC04wWc/uUxorbpn4XtU6CiuLWKcvZ5HVPxN7ZQkZwNytqnnxW1DwBSGETWSabnPsSkjuV4G5W2DC+hwPJyCZdL/22ngLJYt7DihonfAW1Y2BRR5bJJhtvaeL9OFoJ7mZrGiC3sHb8b6vlcdswFATRL2ZCDagAX12H+3DOOWe7A8d2fFQZlsRMXpzu6z8kVnGdPcDgDbRJ5InP/nFB3lFOTMlck1TVuW8gD8wzcRO3FeQfFvfeQUbeQU5M2K0yOGBJXlVjcmaO1HFTsernecPZTd/c3ZQ0CeTM7M+S3L0MNWbpT/a94abql7ebXDrburidECiZa5LsspZUZO+kzNI2Z31r9JPsmlx7M2namzHZG7J1vaQkp6qBff09csYN3FKS6jt5w1mPA2stos8sCb/b6zFzIPMcduOG+kzORjpurUaBtRKRuRwSsz8LqnpWQuaoV8MAu9V3VF/MG9Zi2DQXAxrwUlhSENeZA7aWwyY/+bc1tkKu/hOXxkLwZswHVLlTUlINNW0mjFnswC71W+FtGLOd+9ps+7k2qw/MtEmSrlNZB+c6z5jBrPo3nZNjzXQm1FTrjgSp6dYDakr3oFd9U+9y1lO9tTZT6gAAAABJRU5ErkJggg==",
      "description": "https://www.elitizon.com/2023/19-04-pandassur/ Welcome to Pandassur, a groundbreaking loan insurance broker in France that aims to make the",
      "snippet": "https://www.elitizon.com/2023/19-04-pandassur/ Welcome to Pandassur, a groundbreaking loan insurance broker in France that aims to make the",
      "source": "Facebook"
    },
    {
      "position": 6,
      "title": "Tour on demand!",
      "link": "https://www.instagram.com/p/Crio7VJP1nU/?hl=fr",
      "displayed_link": "Instagram\nhttps://www.instagram.com › ...",
      "favicon": "data:image/png;base64,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",
      "description": "Tour on demand! · New dates for our Thai Island hopping tour! · Stop canceling plans because someone else won't go! You'll never go on vacation if you're waiting ...",
      "snippet": "",
      "source": "Instagram"
    },
    {
      "position": 7,
      "title": "Pandassur Thierville sur Meuse - Assurance (adresse)",
      "link": "https://www.pagesjaunes.fr/pros/62277584",
      "displayed_link": "PagesJaunes\nhttps://www.pagesjaunes.fr › pros",
      "favicon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAMFBMVEX/6wD/6wD/6wD/6wD/7QDw3wDAsgDWxgBGQQAAAAD/8QCuoQArKACQhQB7cgBrYwA2QtBwAAAABHRSTlMo1/8pj0Wn4AAAAMdJREFUeAFjYFRCAcIMQqgCigxKaIBaAiowjgtEQCUsBMJXKXeCqOjsggisnlkCFlA9OQkisHbmLrCAK7qAystfKAJAPU4QM6ECCLAOTUBl/cwsVBUroNYqrVoEURE5JwRiy45dYAGtnfMXQd0xDaxkKZCGumPmJicgpTezFeq5+Jnzi5ascn0JtARiqNPPmTNuZ/+cOXsRLDxWn5wJArvgIaYV2zlz5pznixBB6BW+926qC3KYuqyCuA7hdBUXoqMBI7IxkgMAhLd1j6d98dMAAAAASUVORK5CYII=",
      "description": "Localisation 122 Ter avenue P Goubet et J Van Heeghe 55840 Thierville sur Meuse - Y aller. Voir plus de coordonnées. C'est mon entreprise, je mets à jour ...",
      "snippet": "",
      "source": "PagesJaunes"
    }
  ]
}
```

## How to deploy with modal.com

```bash
model deploy google-search-modal.py
```


## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
