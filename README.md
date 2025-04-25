# Mailchimp Migrator

## Overview

This application helps migrate data from Mailchimp to HubSpot by facilitating the export and import of:

- Contacts
- Contact Lists
- Email Subscription Preferences

## Prerequisites

- Python 3.6+
- Mailchimp API access (API URL and API Key)
- HubSpot Private App Key

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mailchimp-migrator
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following variables:
   ```
   API_URL=https://your-mailchimp-api-endpoint
   API_KEY=your-mailchimp-api-key
   PRIVATE_APP_KEY=your-hubspot-private-app-key
   ```

## Scripts

### Data Export Scripts

These scripts extract data from Mailchimp and store it in CSV files in the `output` folder:

- **export-contacts.py**: Exports all contacts from Mailchimp to a CSV file
  ```
  python export-contacts.py
  ```

- **export-subscription-types.py**: Exports a list of unique subscription types from Mailchimp
  ```
  python export-subscription-types.py
  ```

### Migration Scripts

These scripts migrate data directly from Mailchimp to HubSpot:

- **migrate-lists.py**: Migrates all Mailchimp lists to HubSpot
  ```
  python migrate-lists.py
  ```

- **migrate-subscriptions.py**: Migrates all contact subscription preferences to HubSpot
  ```
  python migrate-subscriptions.py
  ```

### Functions

The `functions` directory contains helper modules that encapsulate the core functionality:

- **Contact Management**: 
  - `get_contacts.py`: Retrieves contacts from Mailchimp
  - `get_contact_hs_ids.py`: Maps Mailchimp contact IDs to HubSpot IDs

- **List Management**: 
  - `get_lists.py`: Retrieves lists from Mailchimp
  - `get_contacts_in_list.py`: Gets all contacts in a specific list
  - `create_hubspot_list.py`: Creates a list in HubSpot
  - `add_contacts_to_list.py`: Adds contacts to a HubSpot list
  - `get_hubspot_list_id.py`: Retrieves a HubSpot list ID by name

- **Subscription Management**:
  - `get_subscriptions.py`: Retrieves subscription preferences from Mailchimp
  - `get_hs_subscription_types.py`: Gets subscription types from HubSpot
  - `update_hubspot_subs.py`: Updates subscription preferences in HubSpot

- **Utilities**:
  - `write_to_csv.py`: Writes data to CSV files in the output directory

## CSV Output

All exported data is stored in the `output` directory with timestamped filenames in the format:
`{data_type}_{YYYYMMDD_HHMMSS}.csv`