#!/bin/bash










tgpt -q "I will give you a prompt. reponse in less than 50 words, Roleplay as an anime shoujo (anime genre, search its meaning) character. search their quotes if needed. now here is the prompt - $1" | grep -o '"[^"]*"'

