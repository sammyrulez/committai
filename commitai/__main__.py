import os
import time
from typing import List
import openai

stream = os.popen('git --no-pager diff  --cached')
output = stream.read()
from rich.progress import track, Progress
from rich.prompt import IntPrompt
from rich.text import Text
from commitai.console import console
from git import Repo

# const CONVENTIONAL_REQUEST = conventionalCommit ? `following conventional commit (<type>: <subject>)` : '';
# TODO

def call_openai(diff:str) -> List[str]:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    """response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Suggest a commit message for my changes\n\n {diff} \n",
    temperature=0.7,
    max_tokens=96,
    top_p=1,
    best_of=3,
    frequency_penalty=0,
    presence_penalty=0,
    n=3
    )
    print(response['choices'])
    return [c['text'] for c in response['choices']]"""
    return ["Add main.py file with os.popen method for git diff"," Add main.py file with git diff command","Add main.py file to project"]

commit_opts = []
with console.status("Working..."):
    commit_opts.extend(call_openai(output))

for n, msg in enumerate(commit_opts):
    text = Text()
    text.append(f"{1+n}", style="bold magenta")
    text.append(f" {msg}")
    console.print(text)


def main():
    msg_n = IntPrompt.ask("Choose a commit message", default=1)
    print(commit_opts[msg_n-1])
    repo = Repo(".")
    index = repo.index
    index.commit(commit_opts[msg_n-1])


main()