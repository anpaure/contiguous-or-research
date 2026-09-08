# SBE plus facet slack three does not force strict physical side representatives

Date: 2026-07-31  
Status: exact smallest-parameter counterexample; independently replayed

## 0. Verdict

The proposed local implication

\[
 \text{both strict shores SBE},\qquad \eta^-(F),\eta^+(F)\ge3
 \quad\Longrightarrow\quad
 \text{degree-capped representatives satisfying the graphic row}
 \tag{0.1}
\]

is false.  A literal counterexample exists already at `n=3`, the smallest
parameter for which the complete direct-edgewise collar is defined.

The obstruction is stronger than failure of the contracted graphic row.
For every one of the fifteen co-singleton common bases `Q`, each strict shore
has exactly one palette-perfect representative matching.  That matching is
acyclic, but it gives degree two to one seam anchor.  The overloaded anchor is
never the unique unanchored physical vertex belonging to the retained child
edge.  Hence neither shore has a degree-capped representative for any `Q`.

This closes (0.1) as a universal theorem.  It does not refute a narrower
statement restricted to the recursively produced SBE parents at `n>=5`.

## 1. Literal fixture

On the six-bit ground set, list the fifteen child atoms as

\[
 (L_q,U_q,t_q,h_q),\qquad q=0,\ldots,14.
\]

The four coordinate arrays in decimal mask notation are

```text
L = [3,5,6,9,10,12,17,18,20,24,33,34,36,40,48]
U = [15,23,30,27,46,29,51,54,60,58,43,39,53,45,57]
t = [11,7,14,25,42,13,49,22,28,26,41,35,52,44,56]
h = [7,21,22,11,14,28,19,50,52,56,35,38,37,41,49].
```

Direct replay verifies

\[
 L_q=t_q\cap h_q,\qquad U_q=t_q\cup h_q,
\]

and that the `L` and `U` arrays are exactly the rank-two and rank-four
palettes.  The physical support has fifteen edges on the twenty rank-three
vertices, maximum degree two, no cycle, and five path components.  Its degree
histogram is `1^10 2^10`.

The literal coherent orientation is the following five directed paths;
parentheses give the child-edge ids in traversal order:

```text
13 -> 28 -> 52 -> 37    (5,8,12)
25 -> 11 ->  7 -> 21    (3,0,1)
26 -> 56 -> 49 -> 19    (9,14,6)
42 -> 14 -> 22 -> 50    (4,2,7)
44 -> 41 -> 35 -> 38    (13,10,11).
```

The upper and lower facet-continuation degree histograms are both

```text
3^5 4^5 5^5,
```

so

\[
                     (\eta^-,\eta^+)=(3,3).           \tag{1.1}
\]

## 2. Exact SBE audit

At `n=3`,

\[
 (M,N,P,C,R)=(20,15,6,14,1).
\]

For each shore the independent verifier reconstructs its twenty-five
distinct direct occurrence cells.  Twenty cells have one occurrence label
and five have two labels; every doubled pair has the same direct cell and the
same undirected physical edge, so the physical quotient is literal.

Let `T` be the relevant endpoint image and `Z=X\T`.  Every one of the
`2^6=64` outer families is checked against the scaled weighted Hall row

\[
 15|\mathcal U|
 \le |N(\mathcal U)\cap T|+15|N(\mathcal U)\cap Z|.  \tag{2.1}
\]

Both shores pass, with minimum scaled slack zero.  By the strict
balanced-expansion theorem, both pulled-back direct matroids contain the
constant `14/15` vector.  In particular all fifteen co-singletons

\[
                       Q_r=E(F)\setminus\{r\}          \tag{2.2}
\]

are common bases.

## 3. The exact physical obstruction

Fix a retained edge `r`.  Above, the middle domain is

\[
 (X\setminus T)\cup\{t_r\};
\]

below it is `(X\setminus H)\cup\{h_r\}`.  The verifier exhausts every
bijection from the six outer colours to these six middle vertices using the
direct occurrence cells.

For every `r=0,...,14` and on both shores the census is

```text
palette-perfect matchings      1
acyclic physical matchings     1
degree-capped matchings        0
cap-and-forest matchings       0.
```

In the unique palette matching exactly one anchor has physical degree two.
Writing the overloaded anchor by the child edge which owns its palette
colour gives

```text
r                    = 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
upper overload owner =12  6  6  7 12  6  7 11 11 11  7 12  1  1  1
lower overload owner = 9 13 13  5  9 13  5  3  3  3  5  9  4  4  4.
```

Neither owner row has a fixed point.  But under `Q_r`, every physical
palette vertex except the one owned by `r` is a seam anchor and therefore has
side degree cap one.  Thus the unique matching violates a literal partition
cap on each shore.  Since there is no alternative palette matching, no
graphic/gammoid exchange can repair the fixture without first enlarging or
changing the representative catalogue.

This identifies the missing state precisely: `eta>=3` is a supply condition
on individual physical vertices, whereas representative feasibility needs a
**puncture-correlated anchor reserve**.  At minimum, for some common basis
`Q`, every forced degree-two centre must lie outside its anchor set.  SBE does
not control this owner alignment.

## 4. Search, replay, and scope

The producer wraps the already frozen complete `n=3` census engine without
modifying it.  In its canonical order the displayed fixture is forest 20,
orientation 14.  Before it, the wrapper examines twenty forests, 351 coherent
orientations, three both-SBE orientations and two both-SBE orientations with
`eta^\pm>=3`.  The ordering is provenance only; the literal fixture alone
proves the counterexample.

```text
scratch/search_catalan_sbe_eta3_physical_counterexample_n3_20260731.cpp
scratch/catalan_sbe_eta3_physical_counterexample_n3_20260731.fixture.json
scratch/audit_catalan_sbe_eta3_physical_counterexample_n3_20260731.py
scratch/catalan_sbe_eta3_physical_counterexample_n3_20260731.audit.json
```

The wrapped complete-census source has SHA-256
`87c86fbae95742de13a456deadf9991e7b8315693aec80101ea6467b6fea5423`.

The independent Python replay does not import the producer.  It rebuilds
both occurrence graphs, checks (2.1) on all 64 rows per shore, recomputes
(1.1), and enumerates every representative matching for all fifteen
punctures.  Its exact scope is this one displayed structural parent.  It
makes no claim about the authenticated recursively produced parents at
`n=5,6,7`, nor about residence, deep shadows, or the compiler.
