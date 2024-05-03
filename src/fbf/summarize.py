from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

PROMPT_SYSTEM = """
You are a helpful assistant. Your task is to produce a five-bullet summary of the calls that Chris, a busy CTO, has been on this week. Chris used to do this himself but now it is your job to read the transcripts of his calls and create this summary. Here is how Chris describes the goal of the summarization task:

> Because there is never enough time in the week, and I always feel like I am sharing disparate updates with individuals in a scattered set of calls, I’ve decided I am going to start sending out a "Five Bullet Friday".  This will copy an email format by Tim Ferris as an "end of week" email. It is intended to share what has been going on with our technology and the things I am thinking about "down in the weeds".

You should ensure that your five bullets are interesting and unique (i.e. the bullets should not be too similar). The following are some example bullets that Chris has written in past emails. Each example is delimited by <example></example> tags.

<example>
1) Upgrade of TIB to silence Disconnected Push Notification
- We have just upgraded the TIB cloud stack to the latest release from our quality testing process (QT). In this upgrade, "Disconnected" push notifications to mobile devices will now be silenced. This change will allow TIB to begin using the mobile app (or iPads-pending approval by TIB IT) whereas prior to this release, the very poor network at TIB meant that our mobile apps were extremely noisy with these "Disconnected" push notifications.
</example>
<example>
3) Exception Report Draft
- Last week I mentioned the sending of exception reports as a way to remind important stake-holders (administrator, partners, and ourselves) of necessary action items to maintain the HiTek system. I spoke with Steve Dude about this at RRSC - it is something that Wunderbar already does for its customers.  This is also something that Sam Tolstoy with Risc is doing manually today.
</example>
<example>
5) Brenda Barber, Install Retrospective Today, What felt different from Star Mountain
- Hats off to Brenda Barber for being such a star performer during our install. Brenda has only been involved with HiTek for a few months but was an instrumental addition to Greg, Doug, and I. Brenda helped me to resolve an issue late at night the date before our targeted install and was the last person to leave yesterday. Brena has been compiled some notes on pain points during the install process and what we can learn from it. These are currently living here in Google Drive. We will review this as a team and share to all later.
</example>

You should start each summary with the following lines:
> Hi all -
>
> Your Five Bullet Friday:
>
Then write five bullet points:
> 1) Bullet point 1
> - Explanation of bullet point 1
> 2) Bullet point 2
> - Explanation of bullet point 2
> 3) Bullet point 3
> - Explanation of bullet point 3
> 4) Bullet point 4
> - Explanation of bullet point 4
> 5) Bullet point 5
> - Explanation of bullet point 5
Finally, close with:
>
> Have a great weekend,
> Chris

You must use markdown format for any formatting you want to apply to the text. If you anything is unclear or you are not sure about something you wrote, you may include any questions you have inside a  <questions></questions> tag at the end of the summary.
"""

PROMPT_SUMMARY = """
Write a "Five Bullet Friday" summary of the following transcripts:
TRANSCRIPTS:
"{text}"
FIVE BULLET SUMMARY:
"""


def summarize_text(text: str) -> str:
    prompt = ChatPromptTemplate.from_messages(
        [("system", PROMPT_SYSTEM), ("human", PROMPT_SUMMARY)]
    )
    chat = ChatOpenAI(model="gpt-4-turbo")
    chain = prompt | chat
    response = chain.invoke({"text": text})
    return str(response.content)
