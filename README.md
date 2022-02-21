# shopping-cart-project

## Setup

"Clone" or download the remote repository onto your local computer. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/shopping-cart-project
```

Create a virtual environment:

```sh
conda create -n shopping-env python=3.8
```

Activate the virtual environment:

```sh
conda activate shopping-env
```

Install package dependencies (dotenv and sendgrid) within the virtual environment:

```sh
pip install -r requirements.txt
```

## Bonus Challenges Setup

Set the tax rate by creating a .env file and a .gitignore file:
```sh
# this is the ".env" file...

 TAX_RATE=0.0875
```
```sh
# this is the ".gitignore" file...

# ignore the contents of the ".env" file (prevent them from being exposed on GitHub):
.env
```

Send an email receipt:
1. Create a "Single Sender Verification" on SendGrid:
   https://signup.sendgrid.com/
2. Create a SendGrid API Key with "full access" permissions:
    https://app.sendgrid.com/api_keys
3. Store the API Key in an environment variable in a .env file
    ```sh
    # this is the ".env" file...
    SENDGRID_API_KEY="SampleAPIKeyfromSendGrid"
    SENDER_ADDRESS="SingleSenderVerificationAddressfromPart1"
    ```
4. Create an email template by going to the SendGrid website and store the template identifier into an environment variable in your .env file:
    https://sendgrid.com/dynamic_templates
    ```sh
    # this is the ".env" file...
    SENDGRID_TEMPLATE_ID="SampleTemplateUniqueIdentifier"
    ```
5. Paste the following HTML into the "Code" tab of the template
    ```
    <img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

    <h3>Hello this is your receipt</h3>

    <p>Date: {{human_friendly_timestamp}}</p>

    <ul>
    {{#each products}}
	    <li>You ordered: ... {{this.name}}</li>
    {{/each}}
    </ul>

    <p>Total: {{total_price_usd}}</p>
    ```
6. Paste the following HTML into the "Test Data" tab of the template
   ```
   {
        "total_price_usd": "$99.99",
        "human_friendly_timestamp": "July 4th, 2099 10:00 AM",
        "products":[
         {"id": 100, "name": "Product 100"},
            {"id": 200, "name": "Product 200"},
            {"id": 300, "name": "Product 300"},
            {"id": 200, "name": "Product 200"},
            {"id": 100, "name": "Product 100"}
        ]
    }
    ```
## Usage

Run the shopping cart program:
```sh
python shopping_cart.py
```
