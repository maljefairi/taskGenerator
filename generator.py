import os
import openai
import json
import random

# Setting the OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

DIMENSIONS = {

    "CA": ["Intelligence", "Knowledge", "Skills"],
    "V": ["Personal Values", "Cultural Values", "Workplace Values"],
    "EA": ["Formal Education", "Informal Education", "Practical Experiences"],
    "BT": ["Habits", "Reactions", "Interactions"],
    "AT": ["Work Attitude", "Learning Attitude", "Social Attitude"],
    "EI": ["Self-awareness", "Self-regulation", "Motivation", "Empathy", "Social Skills"],
    "PT": ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"],
    "FM": ["Positive Feelings", "Negative Feelings", "Neutrality"],
    "IS": ["Communication", "Team Collaboration", "Conflict Resolution"],
    "MD": ["Intrinsic Motivation", "Extrinsic Motivation", "Achievement Motivation"],
    "MES": ["Integrity", "Empathy", "Responsibility"],
    "PA": ["Strength", "Endurance", "Flexibility"]
}

def parse_activity_description(description):
    """Helper function to format the activity description."""
    # If the description starts with any of these prefixes, extract the actual activity name
    possible_prefixes = ["Activity Name:", "Activity Name ", "'"]
    for prefix in possible_prefixes:
        if description.startswith(prefix):
            description = description.split("\n")[0].replace(prefix, "").strip(" '\"")
            break
    return description

def generate_activity(num_activities=1):
    activities_list = []

    # Load existing activities from the JSON file, if it exists
    if os.path.exists('generated_activities.json'):
        with open('generated_activities.json', 'r') as infile:
            existing_activities = json.load(infile)
        activities_list.extend(existing_activities)

    for _ in range(num_activities):
        # Randomly choose a main dimension and a sub-dimension
        main_dim_key = random.choice(list(DIMENSIONS.keys()))
        sub_dim = random.choice(DIMENSIONS[main_dim_key])
        
        prompt = (f"Please suggest an activity or task associated with the dimension '{main_dim_key}: {sub_dim}' "
                 "to gauge an individual's capability. Format your response like this: "
                 "'Activity Name, RS points, GC points, CC points, MVP points, Experience points, Frequency per month (1-4 or Q for quarterly), Dimension(s)'.")

        # Get activity suggestion from OpenAI using the chat model
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Managment Loyalty Consultant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        activity_description = parse_activity_description(response.choices[0].message['content'].strip())

        activity_data = {
            "Activities": activity_description,
            "RS": random.randint(0,10),
            "GC": random.randint(0,10),
            "CC": random.randint(0,10),
            "MVP": random.randint(0,10),
            "Experience": random.randint(0,10),
            "Frequency": random.randint(1,4),
            "Dimension(s)": main_dim_key
        }
        
        activities_list.append(activity_data)
        
    # Save the generated activities (including existing ones) to the JSON file
    with open('generated_activities.json', 'w') as outfile:
        json.dump(activities_list, outfile)

# Example: Generate 5 activities
generate_activity(5)
