# Five Bullet Friday 

```bash
poetry install
```

## Example usage

```
$ ls audios/
GMT20240503-181236_Recording.mp4
$ ls transcripts/
$ OPENAI_API_KEY=... poetry run five-bullet-friday audios/ transcripts/
Hi all -

Your Five Bullet Friday:

1) **Innovative Use of AI for Meeting Summaries**
   - Dylan has creatively utilized OpenAI's Whisper model and the GPT-4 through the Langchain library to transcribe and summarize our Zoom call recordings into concise bullet points. This automation aims to streamline the summary process that was previously done manually.

2) **Exploration of Effective Prompt Engineering**
   - One of the key successes this week has been refining the prompts used in GPT-4 to generate more precise and useful summaries. This ‘prompt engineering’ is crucial as it greatly influences the quality of automated outputs and is also less straightforward than traditional coding.

3) **Cost Analysis of AI Tools**
   - Dylan reviewed the cost-effectiveness of using various AI tools for transcription and summarization tasks. The focus was on understanding the token usage and financial implications of using OpenAI's services versus others like Grok, highlighting a trend towards more affordable AI solutions.

4) **Challenges in AI Summary Generation**
   - Despite the breakthroughs, generating interesting and unique bullet points from limited content remains challenging. This reflects a need for richer content or more context to produce valuable summaries, emphasizing the importance of tailored data input for AI-powered tasks.

5) **Future Directions and Improvements**
   - Looking ahead, there are plans to refine the summarization process further by possibly automating comparative analyses using benchmarks. This would help in quantitatively measuring and improving the performance of different models and prompting strategies.

Have a great weekend,
Chris
```

## Rendered version

Hi all -

Your Five Bullet Friday:

1) **Innovative Use of AI for Meeting Summaries**
   - Dylan has creatively utilized OpenAI's Whisper model and the GPT-4 through the Langchain library to transcribe and summarize our Zoom call recordings into concise bullet points. This automation aims to streamline the summary process that was previously done manually.

2) **Exploration of Effective Prompt Engineering**
   - One of the key successes this week has been refining the prompts used in GPT-4 to generate more precise and useful summaries. This ‘prompt engineering’ is crucial as it greatly influences the quality of automated outputs and is also less straightforward than traditional coding.

3) **Cost Analysis of AI Tools**
   - Dylan reviewed the cost-effectiveness of using various AI tools for transcription and summarization tasks. The focus was on understanding the token usage and financial implications of using OpenAI's services versus others like Grok, highlighting a trend towards more affordable AI solutions.

4) **Challenges in AI Summary Generation**
   - Despite the breakthroughs, generating interesting and unique bullet points from limited content remains challenging. This reflects a need for richer content or more context to produce valuable summaries, emphasizing the importance of tailored data input for AI-powered tasks.

5) **Future Directions and Improvements**
   - Looking ahead, there are plans to refine the summarization process further by possibly automating comparative analyses using benchmarks. This would help in quantitatively measuring and improving the performance of different models and prompting strategies.

Have a great weekend,

Chris

## Whisper vs Whisper.cpp

I was curious about speedup. See [here](./whisper-vs-whisper-cpp.md).

## License

See the [LICENSE](./LICENSE.md) file for license rights and limitations (MIT).
