# Hooper Flights Slack Integration

[Hopper Flights](https://www.hopper.com/) is a flight tracking app that also provides buy signals on airline tickets when they feel that the price is very good.
Hopper has an [API](https://api.hopper.com/v2/docs/api#overview) and 

Slack is a messaging platform that many companies use for internal business communication. Slack has a [start building](https://api.slack.com/start/building) section that guides you on how to set up an app.
The section on [bolt](https://api.slack.com/start/building#frameworks) offers some nice support for setting up a server and building a deployment process.

## The Need

There are many professionals at work that need to book flights and would benefit from cost savings on those flights.
Many of these organizations are already on Slack and can leverage the chat platform to organize a stream of messages that relevant employees can watch in order to take advantage of reduces prices.
The data is available through a variety of flight booking websites and Hopper offers the additional prediction of if this price may go down in the future. 

Having a Slack app that can be used to:
- Create a new channel
- Create a saved Hopper flight search
- Publish messages to the channel with regular price updates.
- Create a "buy now" link when it is at it's lowest predicted price.

Would allow companies to build automation for the tracking of flights for any number of projects and any number of people. This can reduce the load on a single "coordinator" to manage and it optimizes for price. 

## The Scope

Build a slack app that can be installed from the Slack app-store. The app would allow creating a flight search and have the cheapest flight published to the channel every 24 hours. 