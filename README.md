# Joy of Painting player

## Usage

### Basic Usage

The Joy of painting player is meant to help you stop wasting time on trying to find the perfect episode of Bob Ross! You can now query by colors that he uses or by what he is drawing in his pictures. The website is very simple to use and query. You can then select a video to play

![Alt text](dist/assets/websitepic.png?raw=true "Title")

# Database Documentation
## About

A MySQL AWS RDS DB is used in this projcet and it has three tables each relating the episode title of each episode.

### Colors Used
This table has lists of every single color Bob Ross has used in each one of his episodes. This table is also important because it has the youtube url links which my frontend uses to display Youtube videos.

### Subject Matter

This table is used to query the episodes based on what Bob Ross is drawing in his episodes. For example if he draws a fire, river, grass, or etc. Combining this with what colors he uses can help narrow down choices.

### Episode Dates

This table is used to query the episodes based on date that the episode came out. In my frontend I used this information to query episodes based on time of season.


# API Documentation

## About

This API is created to query the database and return youtube Urls based on query information. It does not use query parameters but instead you send them as a data object through POST calls.

## Routes

### /seasons
Returns a dictionary of episode urls depending on the time of the year of the query

### /episodes
Returns all the episodes in the database

### /subject_matter

Uses subject matter query to return title and url for frontend

### /colors_used

Uses the colors used query to return title and url of each episode found with the said colors
## Copyright and License

Copyright 2013-2022 Start Bootstrap LLC. Code released under the [MIT](https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE) license.
