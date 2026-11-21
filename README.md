[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/axzss/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/axzss/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

# Velmara — The Poster for a Place That Isn't There

A program that writes one travel poster to `/output/entry.png`.

## The poster

**Velmara — The Isles Above the Sea.** A travel poster for a place that
does not exist: floating green islands with waterfalls spilling into a sea
of cloud, one white lighthouse tower, sailboats drifting below at golden
hour. The place's name is set into the picture in large cream type on a
deep teal band, with the line "THE ISLES ABOVE THE SEA" beneath it.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program uses only the Python standard library, makes no network
calls, and writes the same bytes on every run. The image is 1024 by 1024
pixels and 321,900 bytes (under the 1 MiB limit).

## Entry

Built for the make.fun bounty
[the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539):
write the best travel poster for a place that does not exist. The entry is
this repository at one commit plus the AI session transcripts that wrote it.
