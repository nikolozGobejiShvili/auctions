# Django Auction Website

This is a Django-based auction website that allows users to create posts, place bids, add items to their watchlist, and comment on listings.

## Installation

1. Clone the repository to your local machine:
2. Install the required dependencies:

## Configuration

1. Navigate to the project directory:
2. Apply the database migrations:
3. Create a superuser account:
4. Start the development server:
5. Open a web browser and access the website at `http://localhost:8000`.

## Usage

- Register a new account or log in with an existing account.
- Browse the listings on the homepage and click on a listing to view its details.
- Place bids on active listings if you meet the bid requirements.
- Add listings to your watchlist for quick access.
- Comment on listings to engage in discussions.
- Create new listings and set the starting bid and optional image.
- Close your own listings to determine the winning bidder and update the listing price.

## Folder Structure

- `auctions/` - Contains the Django application code.
- `auctions/models.py` - Defines the database models for User, Post, AuctionListing, Bid, Category, and Comment.
- `auctions/forms.py` - Contains the form classes for creating posts, creating comments, and placing bids.
- `auctions/templates/auctions/` - Contains the HTML templates for rendering the website pages.
- `auctions/urls.py` - Defines the URL patterns for the application.
- `auctions/views.py` - Contains the view functions for handling HTTP requests and rendering templates.

## Customization

Feel free to customize the code according to your requirements. You can add new features, modify the HTML templates, or extend the existing models and views to enhance the functionality of the auction website.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the GitHub repository.


