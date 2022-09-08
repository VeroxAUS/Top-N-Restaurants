# About The Program

Top Number of Restaurants is a simple program designed to find the top N restaurants based on their combined average score using a locally stored file named scores.txt with the accompanying data.

## Installation

1. Make sure we extracted the program into a clean working directory
2. Create a scores.txt file with the required restaurants and scores, make sure you follow this format
```sh
restaurant,score
restaurant,score
restaurant,score
```

## Usage

Usage of this program is pretty simple, first we require a scores.txt file to be made in the same directory as the top_n.py program, and the formatting should look something like so:

```sh
Romantika,4.1
El Mundo,3.05
Pony,2.75
Curry House,3.93
Camellia,4.93
```

Once done we can run the program by opening a shell terminal and making sure we're in the correct directory, and typing top_n.py and we should get something a little like this:

```sh
Welcome to ReviewMe!

1. Find the rating of a restaurant.
2. List top n restaurants.
3. Exit
```

Simply follow the onscreen prompts to use the program as required.

## Roadmap

- Condensing our choice implementation, choice 2 had gotten very out of hand very quickly and is definitely worth a refactoring later down the line when problems start to arise.
- General code clean up, it's a very messy code base if I'm being honest and I would like to come back at some point and fix things up.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Distributed under the GNU GPLv3 License.](https://choosealicense.com/licenses/gpl-3.0)
