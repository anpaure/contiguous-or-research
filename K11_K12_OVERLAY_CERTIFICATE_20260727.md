# A verified two-sided depth-one path from the k=11/k=12 overlay

Date: 2026-07-27

## 1. Status

There is now an explicit Hamilton path of `J(11,6)` with both depth-one
requirements:

* its 461 intersections are all distinct, so they cover 461 of the 462
  five-sets (the sole hole is `31`);
* its unions cover all 330 seven-sets.

This is a finite, independently checkable existence result.  It is not yet a
length-465 contiguous-OR word, because the path fails the delay-three
factorability condition.

The authoritative artifacts are:

* `scratch/k11_k12_overlay/q1_path.txt` -- the 462 masks in path order;
* `scratch/k11_k12_overlay/q1_augmentation_295_edges.txt` -- the edges used
  by the path but absent from the raw 532-edge overlay;
* `scratch/k11_k12_overlay/q1_certificate_graph_827_edges.txt` -- the raw
  overlay plus those 295 edges;
* `scratch/verify_k11_k12_overlay_certificate.py` -- an independent verifier
  which imports neither SAT generator.

The SHA-256 digest of the path is

```text
973ff76150443807d680345afa57114fc3c0314084624dfd1bb896f34269f789
```

Run

```bash
python3 scratch/verify_k11_k12_overlay_certificate.py
```

to recompute every count below from the two original stored arrays.

## 2. Independently verified source geometry

Starting from the exact k=12 central path and deleting coordinate 12, the
rank-six avoiding section has

\[
462\text{ vertices},\quad 436\text{ edges},\quad 26\text{ components},
\]

and covers 428 of the 462 lower colours and all 330 upper colours.  Overlaying
it with the k=11 near-path gives exactly

\[
532\text{ edges},\quad461\text{ lower colours},\quad330\text{ upper colours}.
\]

This verifies Sections 9--10 of
`EXACT_OPTIMA_BEAUTY_ANALYSIS_20260727.md` independently.

The raw overlay itself cannot contain a feasible path.  Singleton lower- and
upper-colour classes force degree three at the six vertices

\[
243,365,948,1203,1699,1880.
\]

This is a proof-level, statewise obstruction: any selected graph satisfying
all raw singleton colour constraints contains the three forced incident edges
at each displayed vertex, contradicting path degree at most two.

## 3. The sparse augmentation certificate

A bounded SAT search first used a 4,586-edge reservoir: the raw overlay plus
all Johnson realizations of every upper colour occurring at most once in the
old k=11 path (while retaining lower hole 31).  Connectivity cuts produced a
Hamilton path.  This discovery mechanism is experimental; the resulting
certificate is not.

Only 295 selected edges lie outside the raw overlay.  Therefore the raw 532
edges plus those 295 edges form an explicit 827-edge graph containing the
certificate path:

\[
\boxed{827/6930=11.93\%\text{ of }E(J(11,6)).}
\]

The exact path statistics are

\[
\begin{array}{c|c|c}
&\text{load profile}&\mathrm{CPCR}\\ \hline
\text{lower rank five}&1^{461}\ (\text{hole }31)&0\\
\text{upper rank seven}&1^{223}2^{86}3^{18}4^3&54.
\end{array}
\]

Thus the sparse-overlay idea is genuinely compatible with both q=1 colour
marginals.  The earlier `q1_path.txt` was stale and missed twelve upper
colours; the file was replaced only after the new path passed the independent
verifier.

## 4. Exact delay-three obstruction for this path

For a binary coordinate row `T_0,...,T_{461}`, a length-465 factor `A` with

\[
T_i=A_i\lor A_{i+1}\lor A_{i+2}\lor A_{i+3}
\]

exists coordinatewise if and only if every internal one-run of `T` has length
at least four.  Necessity follows because the zero immediately before a run
forces the first three possible factor sites to zero, while the zero
immediately after the run forces the last three to zero.  Sufficiency follows
by placing factor ones, four or fewer sites apart, beginning at the fourth
site of each run and ending at its last site; boundary runs are handled by the
three extra factor positions.

The certificate path has no internal one-run of length one, but it has

\[
83\text{ internal runs of length }2,\qquad
67\text{ internal runs of length }3.
\]

The per-coordinate numbers of short internal runs are

\[
(14,11,13,17,14,11,18,13,18,9,12),
\]

for a total of 150.  Therefore this path is rigorously **not** a third
derivative row of any length-465 word.

## 5. What has and has not been proved

Proved or exhaustively verified:

1. the 26-component projection and all counts in the raw 532-edge overlay;
2. the six-vertex forced-degree obstruction to using the raw overlay alone;
3. existence of the explicit 827-edge augmentation and the depth-one-perfect
   Hamilton path it contains;
4. its exact lower/upper loads, CPCR values, and delay-three failure.

Not proved:

1. that 295 is the minimum possible augmentation;
2. that the 4,586-edge reservoir contains a delay-three path;
3. that any depth-one-perfect delay-three path exists at k=11;
4. that the lower compiler can be attached to a new central path.

The mathematical gain is a clean separation of the remaining gates:
depth-one two-sided compatibility is now witnessed in a very sparse graph;
residence/delay-three compatibility is the unresolved obstruction.

## 6. A useful residence--shadow identity

The failure spectrum suggests a sharper next search than direct run
constraints.  Write a central transition as

\[
T_{i+1}=T_i-\{a_i\}+\{b_i\},
\qquad
L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}.
\]

### Lemma

Assume every internal coordinate one-run has length at least `q`.  Then

\[
L_i^{(q)}=L_{i+1}^{(q)}
\quad\Longleftrightarrow\quad
b_i=a_{i+q},
\]

and the right side says exactly that the one-run born at transition `i` has
length `q`.

### Proof

The residence hypothesis makes the deletions
`a_i,...,a_{i+q-1}` distinct and prevents `b_i` from occurring among
`a_{i+1},...,a_{i+q-1}`.  It also implies that `a_{i+q}`, unless it equals
`b_i`, was already in `T_i` and was not deleted earlier.  Consequently

\[
L_i^{(q)}=T_i\setminus\{a_i,\ldots,a_{i+q-1}\},
\]

whereas `L_{i+1}^{(q)}` is obtained from this set by doing nothing when
`a_{i+q}=b_i`, and otherwise by replacing `a_{i+q}` with `b_i`.  This proves
the equivalence.

For `q=1`, distinct immediate lower colours therefore force residence at
least two.  This explains a previously unnoticed feature of the certificate:
although it has 150 short internal runs, none has length one.  With that fact
in place, its 83 length-two runs are exactly the 83 adjacent equalities in
the depth-two intersection row.

This gives a staged route to delay three which is weaker than demanding full
multidepth coverage:

1. retain the already-rainbow depth-one lower row (this kills length one);
2. forbid only adjacent repeats in the depth-two lower row (this kills length
   two);
3. then forbid only adjacent repeats in the depth-three lower row (this kills
   length three).

Thus the next connector search need not solve the whole lower-shadow problem.
It needs only two local consecutive-shadow constraints on top of the verified
q=1 path.

## 7. The certificate is locally rigid under 2-opt

As a small exact diagnostic, the verifier enumerates every internal segment
reversal.  Of the roughly 106,000 possible reversals, 1,006 have both new
seams in `J(11,6)`.  Only **two** preserve simultaneously

* 461 distinct lower colours, and
* surjectivity onto all 330 upper colours.

Neither reduces the 150 short-run score.  This is only a statewise finite
fact about the displayed path, not a no-go theorem for larger switches, but
it rules out the cheapest possible repair.  The delay-three stage needs at
least a 3-opt/alternating-circuit move or a fresh globally constrained path.
