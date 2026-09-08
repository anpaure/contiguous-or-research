# K17 v7 rich-L3 fixed-bank child-clean local no-go

Date: 2026-08-01  
Status: exact catalogue audit for the fixed v7 thirty-eight-socket bank plus
the mandatory target-14309 length-five child.  This is not a no-go for a
jointly reselected incumbent bank, longer sockets, or `k=17`.

## Result

The rich catalogue contains 283,836 authenticated length-three compact
socket rows for the 100 rank-ten colours having zero residence-extendable
seam support after literal materialization of v7.

Each row was independently tested against the fixed incumbent bank for:

1. exact component-option compatibility;
2. nonempty guard-option domains;
3. facet--facet nonoverlap;
4. facet--guard and guard--guard nonoverlap;
5. extra-boundary/guard compatibility;
6. zero unsupported child colours.

There are 33,865 individually compatible, child-clean rows.  Nevertheless,
five target colours have no child-clean compatible row:

\[
       \boxed{70650,\ 75749,\ 77748,\ 81081,\ 81578.}
\]

Hence no simultaneous selector using this fixed incumbent bank and requiring
every chosen length-three row to be child-clean can repair all 100 colours.
A recursive joint selector may still use a row with a nonzero child when
that child is another selected target group; this audit does not exclude
that stronger model.

The overlapping row-rejection counts are:

| reason | rows |
|---|---:|
| fixed physical conflict | 186,620 |
| unsupported child | 154,662 |
| incompatible fixed guard option | 88,267 |
| incompatible fixed exact option | 83,384 |

The next sound quantifier is to choose the incumbent 38 socket rows jointly
with the 100 repair rows and recursively represented children, or to add
longer/incumbent-changing child-clean rows for the five zero targets.

## Artifacts

* Audit source:
  `scratch/audit_k17_v7_rich_l3_individual_compatibility_20260801.cpp`,
  SHA-256
  `ce7ebe5a01a95036083b9449cde9560d49b7e78707ec5fa3912b4cf3c3b7bad6`.
* Audit JSON:
  `scratch/k17_v7_rich_l3_individual_compatibility.audit.json`, SHA-256
  `f4fefcd9f706a0d73bdda0b5bf566a79030f1e42d2e552dc3fc0da3107966fd5`.
* Rich input catalogue on the H100 host: SHA-256
  `685e8900e632b6215c09f3614ac96f6c0562b6aa88166453264082f3e54df419`.

The enumeration and audit were run with native `-O3` C++ on the H100 host's
CPU; no heavy local computation was used.
