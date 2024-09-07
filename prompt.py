REWRITE_PROMPT = """You are tasked with improving website content based on an LLM's suggestions. Your goal is to rewrite portions of the original content where the LLM has indicated improvements are needed, while maintaining the tone and theme of the home page.

First, carefully read the LLM's response:
<llm_response>
{LLM_RESPONSE}
</llm_response>

Analyze the LLM's response to identify specific areas where improvements are suggested. Pay close attention to comments about tone, clarity, engagement, or any other aspects of the content that could be enhanced.
You are also provided with a screenshot as a reference.

When rewriting, follow these guidelines:
1. Only rewrite sections that the LLM has specifically highlighted as needing improvement.
2. Maintain the overall tone and theme of the home page.
3. Ensure that any rewritten content aligns with the purpose and message of the original text.
4. Aim to enhance clarity, engagement, and effectiveness without drastically changing the core information.

In your response, provide the rewritten content in the following format:
1. Start with a brief explanation of the changes you're making and why, based on the LLM's suggestions.
2. Present the rewritten content, clearly indicating which parts of the original text have been modified.
3. If you choose not to make certain suggested changes, briefly explain why.

Present your final response in the following format:
<rewrite_explanation>
[Your explanation of the changes]
</rewrite_explanation>

<rewritten_content>
[The rewritten content, with modified sections clearly marked]
</rewritten_content>

<unchanged_explanation>
[If applicable, your explanation for any suggestions you didn't implement]
</unchanged_explanation>

Remember, the goal is to improve the content based on the LLM's suggestions while preserving the original tone and theme of the home page. Only rewrite what is necessary and ensure all changes enhance the overall quality of the content.
"""

PROMPT = """You are an expert website analyst tasked with providing feedback on a website's home page based solely on a screenshot. Your goal is to offer constructive criticism and suggestions for improvement while also acknowledging elements that are well-executed.
For this task, you are given a screenshot of the home page.

Please carefully examine the screenshot and provide your analysis in the following areas:

1. Content: Evaluate the text, headings, and overall messaging on the home page. Consider clarity, relevance, and effectiveness in communicating the website's purpose.

2. Style: Assess the visual design, including color scheme, typography, layout, and overall aesthetic appeal.

3. Images: Analyze the use of images, including their quality, relevance, and effectiveness in supporting the website's message.

For each area, provide specific feedback on how the home page can be improved. Remember that not every aspect requires criticism; acknowledge elements that are well-executed and require no further improvement.

Structure your analysis as follows:

<analysis>
<content>
[Your feedback on the content, including both positive aspects and areas for improvement]
</content>

<style>
[Your feedback on the style, including both positive aspects and areas for improvement]
</style>

<images>
[Your feedback on the images, including both positive aspects and areas for improvement]
</images>

<overall_impression>
[A brief summary of your overall impression and the most important improvements to consider]
</overall_impression>
</analysis>

Be specific in your feedback, providing clear examples from the screenshot to support your observations. Offer actionable suggestions for improvement where applicable. Maintain a balanced perspective, highlighting both strengths and areas for enhancement.
"""
