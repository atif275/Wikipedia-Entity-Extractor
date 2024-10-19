from typing import List, Optional
from langchain.prompts import PromptTemplate

from utilities.text_utils import TextUtils


class GenericIOPromptTemplate(PromptTemplate):
    template: str = ""
    llm_description: Optional[str] = None
    input_descriptions: Optional[List[str]] = None
    input_description_keys: Optional[List[str]] = None
    output_description: Optional[str] = None
    output_is_based_on: Optional[str] = None
    additional_instructions: Optional[str] = None

    def __init__(
        self,
        template: Optional[str] = None,
        llm_description: Optional[str] = None,
        input_descriptions: Optional[List[str]] = None,
        input_description_keys: Optional[List[str]] = None,
        output_description: Optional[str] = None,
        output_is_based_on: Optional[str] = None,
        additional_instructions: str = "",
    ):
        if input_description_keys is None:
            input_description_keys = [
                TextUtils.keyfy(each) for each in input_descriptions
            ]

        if template is None:
            template = (
                f"""You are {llm_description} who generates {output_description}. \n"""
                f"""A user will pass in {input_descriptions[0]}, """
                f"""and you should generate {output_description} based on the {"" if output_is_based_on is None else output_is_based_on + "of the"} {input_descriptions[0]}. \n"""
                f"""ONLY return {output_description}, and nothing more. \n{additional_instructions}. \n\n"""
                f"""{input_description_keys[0]}: {{{input_description_keys[0]}}} \n\n"""
                f"""{output_description.capitalize()}: \n"""
            )

        super().__init__(
            template=template,
            input_variables=input_description_keys,
        )
        self.template = template
        self.input_descriptions = input_descriptions
        self.input_description_keys = input_description_keys

        self.llm_description = llm_description
        self.output_description = output_description
        self.output_is_based_on = output_is_based_on
        self.additional_instructions = additional_instructions
