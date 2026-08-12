# PBBS support-matched trade search

Date: 2026-07-27

> **Update.**  The six-factor value \(547/8\) below was the first output of
> the trade layer.  Exhaustive generation of every geometric wreath touching
> at most five current base blocks first lowered the verified value to
> \(185/4\). Coupled adjacent/double-swap circulation beams subsequently
> lower it to \(289/8\). Sections 7--10 record the stronger results.

## 1. Exact normal form

Let \(F\) be an exact wreath factor and write \(\mathcal M(C)\) for the
middle support of a wreath \(C\).  A pair \((R,A)\), with \(R\subseteq F\)
and \(A\cap F=\varnothing\), is a **closed trade** when

\[
 \bigsqcup_{C\in R}\mathcal M(C)
 =
 \bigsqcup_{C\in A}\mathcal M(C).                 \tag{1.1}
\]

Then \((F\setminus R)\cup A\) is another exact wreath factor.  Conversely,
if \(G\) is any exact factor drawn from a fixed wreath catalogue, then

\[
 R=F\setminus G,\qquad A=G\setminus F
\]

satisfy (1.1).  Thus exact-factor search inside a catalogue is equivalent to
closed-trade search around any one factor in that catalogue.

`scratch/search_pbbs_factor_trades.py` implements this equivalence directly.
It maps every alternative wreath to the base-factor blocks touched by its
middle support.  A depth-first search maintains

* the base blocks that have become required;
* the middle owners already covered by alternatives; and
* the first uncovered owner of minimum current alternative degree.

A trade is anchored at its least removed base block.  Hence changing the
order in which its alternatives are selected does not duplicate it.  Every
terminal family is independently checked for disjoint support equality,
exact middle ownership, PBBS retention, MWB, CPCR, balanced \(L^1\), zero
cells, and PCap.

Subject to `--max-blocks`, the enumeration is exact unless the reported node
or trade limit is hit.  This is a structural search, not a stochastic local
optimizer and not a SAT relaxation.

## 2. The high-overlap catalogue does not supply small trades

Take the closest known \(m=5\) factor

```
scratch/m5_nearest_pbbs_wreath_seed71.txt
```

with PBBS retention 195.  Form the catalogue consisting of

1. all 3105 wreaths having PBBS overlap at least eight (generated exactly by
   at most three PBBS paths); and
2. the five other known exact \(m=5\) factors.

Relative to the base this gives 3177 distinct alternative wreaths.  Exact
closed-trade enumeration through six removed base blocks is complete.  It
finds 46 trades, with size and retention-change histograms

\[
\begin{array}{c|rrrrr}
|R|&2&3&4&5&6\\ \hline
\#&5&7&8&16&10,
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrrrrr}
\Delta h&-11&-10&-9&-8&-7&-6&-5&-4&-3&-2&0\\ \hline
\#&2&2&10&8&4&7&4&3&2&3&1.
\end{array}
\]

No trade touches a path-catalogue wreath: every one is assembled entirely
from the five known factors.  In particular, the overlap-at-least-eight
catalogue creates no new closed trade of size at most six and no positive
retention trade at that scale.  This explains why enlarging the old
high-overlap exact-cover instance did not move the nearest factor.

## 3. A genuine shadow-descent network

The lower-overlap mixed-factor trades do move the shadow objective.  Starting
from the retention-195 factor and repeatedly choosing the best exact closed
trade gives the following verified primary scores:

\[
\frac{683}{8},\ rac{641}{8},\ rac{611}{8},\
\frac{587}{8},\ rac{577}{8},\ rac{567}{8},\
\frac{565}{8},\ \boxed{\frac{547}{8}}.
\]

The last step is an eleven-wreath trade.  Its certificate and terminal factor
are

```
scratch/m5_known_factor_best_trade_round7wide_certificate.json
scratch/m5_known_factor_best_trade_round7wide.txt
```

The terminal metrics are

\[
\begin{array}{c|r}
\text{PBBS retention}&152\\
\text{weighted MWB}&547/8\\
\text{CPCR pairs}&486\\
\text{balanced }L^1&167\\
\text{zero cells}&24\\
\text{PCap at every lower depth}&0.
\end{array}
\]

This improves the previous best weighted value \(567/8\).  It also proves
that PBBS proximity and shadow balance are competing, rather than nested,
objectives: retention falls from 195 to 152 while weighted MWB falls from
\(683/8\) to \(547/8\).

## 4. Global finite optimum in the six-factor union

The union of the closest factor and the five previous shadow-search factors
contains 114 distinct wreaths.  Relative to the new factor, 42 are current
and 72 are alternatives.  Running the closed-trade search with
`--max-blocks 42` completes after 310 DFS nodes and enumerates all 73
nontrivial exact alternatives in this catalogue.  None improves the new
factor's weighted MWB; the best alternative ties \(547/8\) but loses the
lexicographic tie-break.

Consequently the displayed factor is a global minimum of weighted MWB among
all exact factors contained in this 114-wreath union (and the selected
lexicographic optimum among ties).  This is a finite catalogue statement,
not an asymptotic proof.

## 5. Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/search_pbbs_factor_trades.py \
  --verify scratch/m5_known_factor_best_trade_round7wide_certificate.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/search_pbbs_factor_trades.py \
  --m 5 \
  --base-factor scratch/m5_known_factor_best_trade_round7wide.txt \
  --alternative-factor scratch/m5_nearest_pbbs_wreath_seed71.txt \
  --alternative-factor m5_switch_vertical_wreath_factor_seed77.best.txt \
  --alternative-factor m5_switch_vertical_wreath_factor_seed42.best.txt \
  --alternative-factor m5_switch_vertical_wreath_factor_seed7.best.txt \
  --alternative-factor m5_switch_vertical_wreath_factor.best.txt \
  --alternative-factor m5_wreath_breakout_seed101.best.txt \
  --max-blocks 42 --objective hybrid
```

## 6. Mathematical consequence for the next search

Uniform high-overlap thresholds are now doubly misaligned with the actual
finite geometry:

1. the complete overlap-at-least-eight catalogue has no exact factor; and
2. those wreaths do not even enter a closed trade of size at most six around
   the nearest factor.

The next catalogue should therefore be generated by support closure and
signed shadow gain, allowing lower-overlap wreaths, rather than by a PBBS
overlap cutoff.  The return-cut and path-sewing bounds remain useful as
certificates and generators, but PBBS retention should be a diagnostic, not
the primary objective.

## 7. Complete geometric neighbourhood through four blocks

`scratch/census_wreath_base_block_signature.cpp` removes the remaining
catalogue restriction at bounded trade size.  It enumerates all

\[
\frac{(n-1)!}{2}
\]

geometric wreaths (rotation fixed by putting coordinate zero first and
reversal fixed canonically), maps each middle owner to its current base
wreath, and emits exactly those candidates touching at most \(K\) base
blocks.  Any trade removing at most \(K\) base wreaths can use only such a
candidate.  Combining this census with the anchored support-closure DFS is
therefore complete for every trade of size at most \(K\).

At \(m=5\), the first four signature layers around the initial
six-factor-union optimum have sizes

\[
42,\quad 595,\quad 5216,\quad 32132.
\]

The first term consists exactly of the 42 base wreaths.  Iterated complete
2-, then 3-, then 4-trade descent produces

```
scratch/m5_entire_universe_four_block_mwb_round1.txt
```

with independently verified metrics

\[
\begin{array}{c|r}
\text{PBBS retention}&156\\
\text{weighted MWB}&391/8\\
\text{CPCR pairs}&271\\
\text{balanced }L^1&116\\
\text{zero cells}&16\\
\text{PCap at every lower depth}&0.
\end{array}
\]

The preceding exact move is recorded in

```
scratch/m5_entire_universe_four_block_mwb_round1_certificate.json
```

and the exhaustive no-improvement audit is

```
scratch/m5_entire_universe_four_block_mwb_round2_report.json
```

The latter enumerates all 118 nontrivial closed trades of size at most four
around the final factor and reports `complete_through_max_blocks: true`; none
improves the lexicographic objective MWB, CPCR, balanced \(L^1\), zero cells,
then PBBS retention.  Thus the factor is a genuine local optimum in the
entire geometric wreath universe through trade size four, not merely within
a supplied catalogue.

The residual weighted overload is concentrated at depth two:

\[
\begin{array}{c|rrrr}
q&1&2&3&4,5\\ \hline
O_q&14&59&43&0\\
O_q/c_q&14&59/2&43/8&0.
\end{array}
\]

This changes the finite structural diagnosis.  Depth one is no longer the
dominant obstruction after exact support trades; the remaining cost is a
depth-two compatibility defect.  Any asymptotic trade theorem should
therefore control the joint \((q=1,q=2)\) signature rather than optimize the
endpoint shadow alone.

## 8. Five-block extension and compensation audit

After compressing candidates to owner and base-block bitmasks, the complete
five-block catalogue is practical.  Around the four-block local optimum it
contains 172,669 alternatives, and exact closure visits 91,755 states.  Three
complete descent rounds give the current verified factor

```
scratch/m5_entire_universe_five_block_round3.txt
```

with

\[
\begin{array}{c|r}
\text{PBBS retention}&153\\
\text{weighted MWB}&371/8\\
\text{weighted CPCR}&663/8\\
\text{CPCR pairs}&224\\
\text{balanced }L^1&105\\
\text{zero cells}&17\\
\text{PCap at every lower depth}&0.
\end{array}
\]

The last certificate is

```
scratch/m5_entire_universe_five_block_round3_certificate.json
```

and includes the exact coherent-gain/noise decomposition from
`MATH_LEMMA_SUPPORT_MATCHED_TRADE_DIRICHLET_IDENTITY_20260727.md`.  At the
last move the weighted coherent gain is 14, weighted noise is \(99/8\), and
weighted CPCR therefore falls by \(13/8\).  The full catalogue's *mean*
weighted noise is almost twice its mean coherent gain, so uniform random
trades worsen the potential.  The improvement comes from a structured
minority of favorable trades.

This is not yet a five-block local optimum; further finite descent is
possible.  Its mathematical value is the identification of the correct
asymptotic assertion: above linear CPCR excess, some compatible trade must
have coherent gain strictly exceeding its Dirichlet noise.  A rate of descent
is unnecessary for an existence proof.

## 9. Linear adjacent-carrier replacement for the factorial search

The final five-block improvement is a directed cycle of five literal
adjacent-swap moves.  Each move changes two middle windows, and the five
signed pairs circulate among five distinct factor rows.  Therefore exact
middle ownership is automatic.

The structural catalogue has only \(W=462\) rows and finds exactly three
carrier cycles at the source factor.  Its best cycle is identical to the best
trade found in the complete 172,909-wreath catalogue, and a second carrier
step lowers the verified score further to \(185/4\).  The terminal factor and
certificate are

```
scratch/m5_adjacent_carrier_next.txt
scratch/m5_adjacent_carrier_next_certificate.json
```

The construction and proof are in
`MATH_LEMMA_ADJACENT_CARRIER_CYCLE_TRADES_20260727.md`.  This is the first
successful finite mechanism here whose candidate supply is exactly linear in
\(W\), whose decoration is built in, and whose every cycle is an integral
exact-factor trade.

## 10. Coupled arities and nonmonotone beam descent

Adjacent moves alone are globally rigid at the (185/4) factor: complete
support-closure enumeration through all 42 removable rows finds exactly the
three whole-pair cycles and no split circulation. The report is

```text
scratch/m5_adjacent_owner_circulations_full_report.json
```

The rigidity disappears when the (W) separated-double-swap atoms are added.
The first improving mixed trade has six rows: two arity-three atoms close a
four-step path of arity-two adjacent atoms. Its exact owner-transition matrix
is recorded in `MATH_LEMMA_COUPLED_LOCAL_MOVE_CIRCULATIONS_20260727.md`, and
the linear generator `scratch/mixed_wreath_carrier_paths.py` reproduces all
three such trades around the base factor.

Greedy mixed descent reaches (87/2), but the more important effect is that
the mixed state graph supports nonmonotone paths. The bounded tabu/beam driver
`scratch/search_wreath_carrier_closure.py --move-atlas mixed` gives two
independently replayable eight-step improvements,

\[
 185/4\longrightarrow319/8\longrightarrow289/8.
\]

The current best factor and certificate are

```text
scratch/m5_mixed_beam_best_round2.txt
scratch/m5_mixed_beam_best_round2_certificate.json
```

with

\[
(O_1,O_2,O_3)=(12,40,33),\qquad
\sum_qO_q/c_q=289/8,
\]

CPCR 193, balanced (L^1=85), 15 holes, and zero PCap. A subsequent
depth-eight, width-128 beam visits 6157 additional states without improving
this value. This is a bounded search fact, not a local- or global-optimality
claim.

The asymptotic lesson is sharper than “use larger trades.” Pair paths are
abundant but noncyclic; arity-three atoms supply one-owner junctions that can
close them. The missing theorem is a quantitative supply-and-orientation
bound for these junctions relative to the current shadow imbalance.
