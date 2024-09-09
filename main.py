# -*- coding: utf-8 -*-
import argparse
import sys
import urllib.request
import json

def fetch_data(page):
    try:
        url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = response.read()
        return json.loads(data)
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        sys.exit(1)

def read_file(file_location):
    try:
        with open(file_location, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def format_data(data):
    formatted_rows = []
    for item in data['items']:
        title = item.get('title', '')
        subjects = ','.join(item.get('subjects', [])) if item.get('subjects') else ''
        field_offices = ','.join(item.get('field_offices', [])) if item.get('field_offices') else ''

        formatted_row = f"{title}þ{subjects}þ{field_offices}"
        formatted_rows.append(formatted_row)
    
    return formatted_rows

def main(page=None, thefile=None):

    if page is not None:
        data = fetch_data(page)
    elif thefile is not None:
        data = read_file(thefile)
    
    formatted_data = format_data(data)
    
    for row in formatted_data:
        print(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="A file location to read JSON data.")
    parser.add_argument("--page", type=int, required=False, help="A page number to fetch data from the FBI API.")
    
    args = parser.parse_args()
    if args.page:
        main(page=args.page)
    elif args.file:
        main(thefile=args.file)
    else:
        parser.print_help(sys.stderr)
