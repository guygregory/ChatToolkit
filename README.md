# Azure Open AI sample Python application - "ChatPTS"

![](media/ChatPTS.png)

The [Azure OpenAI Service](https://azure.microsoft.com/en-in/blog/general-availability-of-azure-openai-service-expands-access-to-large-advanced-ai-models-with-added-enterprise-benefits/) provides businesses and developers with high-performance AI models at production scale with industry-leading uptime. This is the same production service that Microsoft uses to power its own products, including [GitHub Copilot](https://github.com/features/copilot/?culture=en-us&country=us), an AI pair programmer that helps developers write better code, [Power BI](https://news.microsoft.com/source/features/innovation/from-conversation-to-code-microsoft-introduces-its-first-product-features-powered-by-gpt-3/?culture=en-us&country=us), which leverages GPT-3-powered natural language to automatically generate formulae and expressions, and the recently-announced [Microsoft Designer](https://designer.microsoft.com/), which helps creators build stunning content with natural language prompts.

As a Partner Technololgy Strategist (PTS) at Microsoft, I wanted to create a simple app to demonstrate the simplicity of the new Azure OpenAI service to our partners and customers. I'm not an experienced developer, so I utilized the GPT-3 model and the [GPT-3 Playground in Azure OpenAI Studio](https://oai.azure.com/portal/playground) to co-create the code for this application.

![](media/Playground.png)

Here were six things that I didn't have to do, thanks to the Azure OpenAI service:

1. I didn't have to write the underlying code for the API call, because it was generated from the [Azure OpenAI Studio](https://oai.azure.com/portal/playground)
2. I didn't have to write the Tkinter UI, because GPT-3 wrote it for me
3. I didn't have to figure out how to resize the text boxes, because GPT-3 showed me how to do it, and provided the updated code
4. GPT-3 helped me to apply word wrapping within the text boxes
5. GPT-3 advised me how to change the font style
6. I didn't have to work out how to extract the 'text' value from the returned JSON, because GPT-3 wrote the code to extract the value for me

As a result:

* 44% (16 lines) of code in this sample came from the Sample Code in GPT-3 Playground in [Azure OpenAI Studio](https://oai.azure.com/portal/playground)
* 56% (20 lines) of code in this sample app were generated by GPT-3, based on my natural language prompts

## How to use - Prerequisites

* Before deploying Azure OpenAI, please gain approval for your Azure Subscription. [Here's the form](https://aka.ms/oai/access) (currently managed customers/managed partners/MSFT internal only)
* Once you've had approval, you'll need to deploy the Azure OpenAI service into your subscription. [Instructions are on the Microsoft Docs page.](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal)
* Next, you'll need to [deploy at least one model](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model), text-davinci-003 is recommended

![](media/Models.png)

## How to use - Downloading and running the application
* The script requires that you have Python installed, which can be downloaded [here](https://www.python.org/downloads/)
* Required modules: Tkinter, Open AI (example: pip install openai)
* Download/clone the script onto your local computer
* Update the openai.api_key and openai.api_base variables, using the details from your own Azure OpenAI resource. You will also need to edit the model name, unless you named it 'text-davinci-003'
* When running the .py script, a Tkinter form should appear as per the screenshot:

## Please note

* When building applications using Azure OpenAI, developers must adhere to the [code of conduct and responsible AI principles.](https://learn.microsoft.com/legal/cognitive-services/openai/code-of-conduct?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext)
* This is not an official Microsoft code sample, and is intended as a conversation starter, not as a production-ready application.

## Feedback

*  Reach me on [Twitter @guygregory](https://twitter.com/guygregory) or [LinkedIn](https://linkedin.com/in/guygregory)
*  Found a bug? Have a suggestion? Please create a [new issue](https://github.com/guygregory/ChatPTS/issues)!
