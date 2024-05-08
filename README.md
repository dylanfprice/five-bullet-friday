# Five Bullet Friday 

Playing around with [whisper](https://github.com/openai/whisper) and the [chatgpt api](https://platform.openai.com/docs/api-reference).

It's a simple cli tool that will transcribe a set of audio files then summarize them in a specific five bullet format.

## Setup

You need [poetry](https://python-poetry.org/docs/). Then simply

```bash
poetry install
poetry run five-bullet-friday --help
```

## Example usage

<details>
<summary>Zoom call between Chris and Dylan</summary>

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

### Rendered version

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
</details>

<details>
<summary>Apple WWDC 2023</summary>

```bash
$ ls audios/
apple-wwdc-2023.mp3
$ ls transcripts/
$ OPENAI_API_KEY=... poetry run five-bullet-friday audios/ transcripts/
Hi all -

Your Five Bullet Friday:

1) **Introduction of the 15-inch MacBook Air**
   - Apple announced the launch of the new 15-inch MacBook Air, which is described as the world's best 15-inch laptop due to its thin and light design, exceptional performance, and all-day battery life. It features the M2 chip, making it significantly faster than the fastest Intel-based MacBook Air models.

2) **Mac Studio and Mac Pro Updates**
   - The Mac Studio has been updated to include the M2 Max and the new M2 Ultra chips, enhancing its performance significantly for professional use in fields like video processing and 3D rendering. The Mac Pro now integrates Apple Silicon with M2 Ultra, offering substantial performance improvements and flexibility with PCI expansion.

3) **Enhancements in iOS 17**
   - iOS 17 introduces new features focused on improving user communication with updates to the Phone, FaceTime, and Messages apps. Notable additions include personalized contact posters, live voicemail transcriptions, and more immersive and interactive ways to share content through AirDrop.

4) **Revolutionary Apple Vision Pro**
   - Apple unveiled the Vision Pro, a new AR platform that blends digital content with the real world, creating immersive experiences. It operates with a fully three-dimensional interface controlled by eyes, hands, and voice, aiming to redefine personal computing, work, and entertainment.

5) **Advancements in macOS Sonoma**
   - macOS Sonoma will feature enhanced gaming experiences, better personalization through interactive widgets, and new productivity tools for video conferencing. It also includes significant updates to Safari for improved browsing privacy and efficiency.

Have a great weekend,

Chris
```

### Rendered version

Hi all -

Your Five Bullet Friday:

1) **Introduction of the 15-inch MacBook Air**
   - Apple announced the launch of the new 15-inch MacBook Air, which is described as the world's best 15-inch laptop due to its thin and light design, exceptional performance, and all-day battery life. It features the M2 chip, making it significantly faster than the fastest Intel-based MacBook Air models.

2) **Mac Studio and Mac Pro Updates**
   - The Mac Studio has been updated to include the M2 Max and the new M2 Ultra chips, enhancing its performance significantly for professional use in fields like video processing and 3D rendering. The Mac Pro now integrates Apple Silicon with M2 Ultra, offering substantial performance improvements and flexibility with PCI expansion.

3) **Enhancements in iOS 17**
   - iOS 17 introduces new features focused on improving user communication with updates to the Phone, FaceTime, and Messages apps. Notable additions include personalized contact posters, live voicemail transcriptions, and more immersive and interactive ways to share content through AirDrop.

4) **Revolutionary Apple Vision Pro**
   - Apple unveiled the Vision Pro, a new AR platform that blends digital content with the real world, creating immersive experiences. It operates with a fully three-dimensional interface controlled by eyes, hands, and voice, aiming to redefine personal computing, work, and entertainment.

5) **Advancements in macOS Sonoma**
   - macOS Sonoma will feature enhanced gaming experiences, better personalization through interactive widgets, and new productivity tools for video conferencing. It also includes significant updates to Safari for improved browsing privacy and efficiency.

Have a great weekend,

Chris
</details>

## Whisper vs Whisper.cpp

I was curious about speedup. See [here](./whisper-vs-whisper-cpp.md).

## License

See the [LICENSE](./LICENSE.md) file for license rights and limitations (MIT).
