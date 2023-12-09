
import openai
import pandas as pd
import random
from dotenv import load_dotenv
import os

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
housing_prices_dataset = pd.read_csv("housing.csv")

def generate_description():
    #зададим названия нужных столбцов
    required_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
                        'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
    if not all(col in housing_prices_dataset.columns for col in required_columns):
        print("Error: Dataset is missing required columns.")
        return

    property_entry = housing_prices_dataset.sample().iloc[0]

    #добавляем инструкции
    user_message = (
    f"Create an Instagram real estate account description for a {property_entry['bedrooms']} bedroom, "
    f"{property_entry['bathrooms']} bathroom {property_entry['furnishingstatus']} property in "
    f"{'a preferred' if property_entry['prefarea'] == 'yes' else 'an non-preferred'} area, "
    f"priced at ${property_entry['price']} with an area of {property_entry['area']} sqft."
)
     #указания для фичей
    if property_entry['prefarea'] == 'no': 
        user_message += (
        "Highlight the unique features and advantages of the property, "
        "despite its location in a non-preferred area."
    )
    if property_entry['airconditioning'] == 'yes':
        user_message += " Include information about air conditioning services."
    if property_entry['hotwaterheating'] == 'yes':
        user_message += " Mention the availability of hot water heating."
    if property_entry['parking'] > 0:
        user_message += f" The property includes {property_entry['parking']} parking space(s)."
    if property_entry['mainroad'] == 'yes':
        user_message += " It is located on the main road."
    if property_entry['basement'] == 'yes':
        user_message += " Features a basement."
    if property_entry['guestroom'] == 'yes':
        user_message += " Includes a guest room."
    if property_entry['stories'] > 1:
        user_message += f" It has {property_entry['stories']} stories."
        
    furnishing_status_map = {
        'furnished': 'fully furnished',
        'semi-furnished': 'semi-furnished',
        'unfurnished': 'unfurnished'
    }

    user_message += f" The property is {furnishing_status_map.get(property_entry['furnishingstatus'].lower(), 'not specified')}."

    #зададим модель
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message},
        ],
        temperature=0.9,  
        max_tokens=400,  
    )

    # вывод результатов
    assistant_reply = response['choices'][0]['message']['content']
    print(f"Instagram Description: {assistant_reply}")

#екзекюшн
generate_description()
