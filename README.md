# Master Project Repository

thesis title :
> Being Polite is a Choice: Trying to Create Immersion through Conversational Inputs and adequate Reactions to the Player’s Manners in Role-Playing Games

thesis sketch : [on github](documentation/files/Schmele_Tristan-Master_Projektskizze-v2.pdf)\
thesis paper : [on github](documentation/files/Schmele_Tristan_Masters_Thesis_2025-03-10.pdf)

---

## thesis

### abstract

> This thesis investigates the correlation between a conversational input method and the player's immersion in role-playing video games. Communicating with digital assistants using natural language is becoming commonplace, resulting in the perception of computers as social actors. This thesis utilizes this effect to intentionally humanize the characters in a role-playing game to create an immersive experience.
>  
> A prototype based on conversational inputs was play tested by 15 participants. After testing the prototype, the participants documented their experiences in a questionnaire with emphasis on their immersion and emotions during their game session. Their responses were analyzed for correlation between the conversational input-method and their immersion. The analysis shows possible correlations between the input-method and the player's empathy for the characters, as well as between the player's immersion and their empathy. 
> 
> This thesis concludes that conversational inputs can influence the player's immersion, by strengthening their emotional connection with the characters. While the sample size limited this studies generalizability, the findings provide a relevant foundation and direction for further research. After validating and generalizing these findings through larger studies, they will become applicable in research and development of video games and digital assistants.

---

## repository structure

documentation

- thesis pdfs
- collected data

docker_server

- Docker files for politeness-evaluation server
- local variation of the server

game_prototype

- ren'py project of the game 'finding-liv'
- pre-built version of the game to work with the local server

convotest / sockettest

- proof-of-concepts for ConvoKit and socket

---

## prototyp

### how to run - server

1 install dependencies with ``pip install -r ./docker_server_/requirements.txt``

2 run ``python ./docker_server/socket-server-local.py``

3 wait for 'Listening on ('127.0.0.1', 5000)'

### how to run - game (pc)

1 unpack ``./game_prototpy/distribution/finding_liv-1.0.3-pc.zip``

2 run ``finding_liv.exe``

---
