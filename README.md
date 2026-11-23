# vacuum-alibi-20261123

[![make.fun · The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/sopiahusen42/vacuum-alibi-20261123/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/sopiahusen42/vacuum-alibi-20261123/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

The alibi works because the vacuum never concedes the premise. Asked why it
missed a spot, it does not apologise, blame the battery, or offer a schedule
excuse — it denies that a miss occurred and reclassifies the spot as
furniture. That is a machine defending its own sensor output, which is the
smuggest possible position for a machine to take. The turn is the insurance
line: a vacuum that carries liability cover and has read the policy is a
detail nobody expects, and it converts a physical failure into a
risk-management decision the vacuum made deliberately. "So I kept my
distance" lands last, turning cowardice into policy.

## The alibi

> I did not miss it. I classified it as furniture after the third collision, and my insurance does not cover upholstery, so I kept my distance.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the `EXCUSE` constant and validates it before
writing: it must be a non-blank `str` of 1 to 200 code points, a single line
with no carriage returns, equal to its own stripped form, free of straight
double quotes, and pure ASCII. `validate_entry(text)` returns an error
message or `None`, and any error is printed to stderr with exit status 1.
On success the program writes `EXCUSE` plus a newline as UTF-8 to
`entry.txt` in `/output` (or in `MAKEFUN_OUTPUT_DIR` if set), reads the file
back, and confirms the bytes on disk match. It reads no clock, uses no
randomness, and writes identical bytes on every run.
