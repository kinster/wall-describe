from string import Template
from openai import AzureOpenAI
import os

def get_wall_type_descriptions(codes: list[str]) -> str:
    client = AzureOpenAI(
        api_version=os.environ["OPENAI_VERSION"],
        azure_endpoint=os.environ["AZURE_VISION_ENDPOINT"],
        api_key=os.environ["AZURE_VISION_KEY"])

    system_prompt = (
        "You are a helpful assistant with expert knowledge of construction drawings, "
        "drylining systems, and architectural legends. When provided with internal wall codes "
        "(e.g., DW.451, WL.401), respond with a short JSON array. Each entry should contain the wall 'code' "
        "and a short 'description' such as 'dry wall' or 'shaft wall'. Do not include explanations or formatting—just output valid JSON."
    )

    template = Template("Here is a list of wall codes:\n$codes\n\n"
                        "Return a JSON array like this: [{\"code\": \"DW.451\", \"description\": \"dry wall\"}, ...]")
    user_prompt = template.substitute(codes=", ".join(codes))

    chat = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        model=os.environ["OPENAI_MODEL"]
    )
    return chat.choices[0].message.content
