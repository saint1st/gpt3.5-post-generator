# gpt3.5-post-generator
A post generator for an Instagram real estate account using the gpt3.5-turbo API
The generator is created based on random entries from the Housing Prices Dataset(https://www.kaggle.com/datasets/yasserh/housing-prices-dataset), providing varied and engaging real estate content.

**Questions:**
- How to mimic the style of *successful* Instagram posts?
- What prompt engineering techniques can improve quality?
- How to ensure the model doesn't invent extra features?
- 
 **Answers:**
 - 1.We can use data from real examples of real estate Instagram posts to train our model. 
 - 2.According to the style of real estate posts, we can specify feature descriptions and relevant information to obtain desirable results.
 - 3.We should lower the 'temperature' of the model. Including more information during prompt engineering would not only improve the quality but also prevent anomalies in the model's response.
