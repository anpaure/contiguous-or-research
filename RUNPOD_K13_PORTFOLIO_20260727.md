# Bounded RunPod portfolio for the `k=13` depth-three gate

Date: 2026-07-27

The user supplied three idle CPU pods.  Kissat is single-threaded, so the
GPU pod was deliberately not used.  Each CPU pod received the same three
exact CNFs:

| CNF | meaning |
|---|---|
| `sigma_sat_k13_h3_automaton.cnf` | global q1/q2, Hamilton, voltage-capable, exact residence through depth 3 |
| `sigma_sat_k13_h3_auto_lns100.cnf` | exact depth-3 automaton with 100 quotient choices free around the h2-clean hint |
| `sigma_sat_k13_h3_auto_lns110.cnf` | corresponding 110-free neighbourhood |
| `sigma_sat_k13_h3_lowerq3_auto.cnf` | global exact h3 automaton plus compact coverage of every lower-q3 orbit |

The exact recent-coordinate automaton contributes 88,512 clauses at
`k=13`; it was independently calibrated at `k=11`, where it found an h3-clean
both-q2 Hamilton certificate in 8.89 seconds.

## Portfolio

Every run has a 900-second solver limit.

| pod label | h3 global seeds | LNS seed | h3 + lower-q3 seeds |
|---|---|---|---|
| amber | 101, 103 | 100-free 107; 110-free 109 | 127, 131 |
| rose | 211, 223 | 100-free 227; 110-free 229 | 239, 241 |
| purple | 307, 311 | 100-free 313; 110-free 317 | 331, 337 |

There are eighteen independent single-threaded searches.  SAT output will be
downloaded and decoded against the original choice catalogue; UNKNOWN or a
timeout carries no mathematical inference.  Restricted UNSAT applies only
to the named LNS neighbourhood, never to the global `k=13` problem.

## First-wave outcome

All eighteen 900-second runs returned `UNKNOWN`.  This is a timing result
only.  In particular, none supplies an UNSAT claim for the global instance
or for an unrestricted residence/shadow problem.

## Corrected joint-q3 wave

The first wave did not encode upper-q3 coverage.  A later exact audit also
found that the recent-coordinate state of the freshly inserted/deleted
coordinate needed selected-arc false clauses.  The corrected joint formula

```text
sigma_sat_k13_h3_bothq3_auto_corrected.cnf
```

simultaneously enforces q1/q2 coverage, forward residence through depth 3,
lower-q3 coverage, upper-q3 coverage via the dual recent-deletion automaton,
and compact Hamilton connectivity.  It has

```text
211755 variables
1923877 clauses
SHA-256 f8089c68ff51086f796fce8ff798c1e2cc2bd076305c77bed266f00d1f62987a
```

The corrected formula was calibrated by fixing the exact k=11 certificate,
where it is SAT and independently gives complete lower and upper q3 shadows.

Sixteen independent 3600-second runs were launched on the three CPU pods:

| pod label | seeds |
|---|---|
| amber | 401, 409, 419, 421, 431, 433 |
| rose | 503, 509, 521, 523 |
| purple | 601, 607, 613, 617, 619, 631 |

The GPU pod remains unused because this solver workload is CPU-bound.  As
before, a timeout is only `UNKNOWN`; any SAT output must be decoded and
audited independently before it changes the finite frontier.

### Oriented-lazy follow-up

The Hamilton orientation has now been separated from connectivity.  The
automata need one incoming and one outgoing selected arc, but they do not
need the quadratic unary-MTZ ranks: connectedness can be imposed afterwards
by exact subtour cuts.  This reduces the zero-defect joint formula to

```text
194463 variables
1181772 clauses
```

and the corresponding residence-budget-20 stepping-stone to

```text
315957 variables
1424740 clauses.
```

Twenty additional 1800-second raw SAT runs were launched (ten for each
formula).  A raw SAT model is only an oriented 2-factor; it must be decoded,
cut if disconnected, and checked for nonzero voltage.  Its purpose is to
seed that exact lazy loop, not to bypass connectivity verification.
