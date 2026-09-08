# The coupled upper-residue circuit at `k=11`

Date: 2026-07-27

## 1. Outcome

The twelve missing rank-seven masks in
`k11_upper549_rank_exact_flag.txt` cannot be changed by editing only the
factor labels while retaining the central row.  If

\[
                         T=D^3A,
\]

then identically

\[
                         D^4A=DT,
 \qquad                  D^5A=D^2T.                 \tag{1.1}
\]

Thus the rank-seven and internal rank-eight profiles are invariants of the
central chronology.  A genuine repair must change the Hamilton path `T`.

An exhaustive, bounded circuit census now gives the first exact local
support threshold.

> **Three-cut obstruction.** Among all paths obtained from the stored
> central path by deleting at most three path edges and reconnecting the
> resulting segments in arbitrary order and orientation, none both
>
> 1. retains a one-hole rank-five rainbow with its hole absorbable at an
>    endpoint;
> 2. has delay-three factorability (internal one-runs have length at least
>    four); and
> 3. reduces the twelve rank-seven holes.

Consequently the first upper-improving alternating circuit compatible with
the lower compiler has support at least four.  This is a neighborhood
obstruction, not a global no-go.  The proof is a complete enumeration of
the finite three-cut normal form described below.

There is one particularly informative three-cut near-circuit.  It reduces
the rank-seven defect from twelve to ten while keeping the exact lower
rainbow and endpoint hole, but it creates precisely five residence-three
violations.  Adding one arbitrary fourth cut and reconnecting all five
segments in every possible way never retains this gain together with
residence.  This identifies residence, rather than colour supply, as the
first active coupling.

## 2. Circuit normal form

Let

\[
 P=(T_0,T_1,\ldots,T_{461})
\]

be the rank-six central path, and colour every Johnson edge by

\[
 \ell(XY)=X\cap Y\in\binom{[11]}5,
 \qquad
 u(XY)=X\cup Y\in\binom{[11]}7.                    \tag{2.1}
\]

The seed uses 461 distinct lower colours and omits only `31`.  After cuts
at `i<j<k`, the path splits into four directed segments.  Every path using
the internal edges of those segments is obtained by a permutation and an
orientation of the four segments.  Modulo reversing the whole path, there
are exactly

\[
                         \frac{4!2^4}{2}=192         \tag{2.2}
\]

templates.

If the removed lower colours are `c_i,c_j,c_k`, the reconnected path is
lower-rainbow if and only if its three new lower colours are distinct and
belong to

\[
                         \{31,c_i,c_j,c_k\}.         \tag{2.3}

Exactly one colour in (2.3) is then omitted.  Boundary absorption at depth
one requires that colour to be contained in one of the two new endpoints.
These are exact tests, not relaxations.

Residence also has a purely local test.  Write

\[
 a_i=T_i\setminus T_{i+1},\qquad
 b_i=T_{i+1}\setminus T_i,
\]

and

\[
 L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}.
\]

Then

\[
L_i^{(q)}=L_{i+1}^{(q)}\quad\Longleftrightarrow\quad b_i=a_{i+q}. \tag{2.4}
\]

The equality on the right says that the coordinate inserted at step `i`
has an internal residence run of length `q`.  Hence delay three is exactly
the exclusion of (2.4) for `q=1,2,3`.  In the executable census this was
cross-checked against the direct run-length calculation.

At depths two and three there is a further necessary compiler test.  Any
missing rank-four or rank-three intersection not contained in either path
endpoint cannot occur in a boundary factor cell.  Such a path cannot compile
all lower masks, regardless of how the factor entries are shrunk.

## 3. Exact census

The program `scratch/search_k11_general_three_opt.cpp` enumerates every cut
triple and all 192 templates.  On the rank-exact seed it reports

```text
Johnson templates                         26,767,124
lower-rainbow templates                   18,278,199
endpoint-compatible templates             17,791,618
nontrivial residence-safe templates          114,425
```

The rank-seven hole histogram on those 114,425 templates is

```text
12 holes       1,400
13 holes     111,618
14 holes       1,406
15 holes           1
```

In particular its minimum is the original value twelve.  The additional
depth-two/depth-three endpoint-ideal necessary test retains 114,418
templates and has the same minimum.

Before residence is imposed, the endpoint-compatible histogram begins

```text
10 holes           1
11 holes          19
12 holes  17,538,619
```

so upper-improving colour trades do exist; they are killed by the residence
condition.

The census contains every path differing in one, two, or three edges: any
smaller exchange can be represented by inserting dummy cuts and rejoining
the corresponding old edges.  A separate direct two-opt audit in
`scratch/analyze_k11_upper_circuits.py` gives the sharper calibration

```text
legal Johnson 2-opt templates             1,028
lower-rainbow templates                        1
endpoint- and residence-compatible             0
```

and only one admissible Posa endpoint rotation exists; it increases the
upper defect to thirteen.

## 4. The unique ten-hole near-circuit

The unique endpoint-compatible three-cut template with ten upper holes has

```text
cuts          158,168,372
segment order 0,2,1,3
orientations  0,0,1,0
missing lower 31
```

Its changed edges are

```text
removed edge       lower  upper
429--1452           428   1453
492--748            236   1004
1212--1260         1196   1276

added edge         lower  upper
429--492             428    493
748--1260            236   1772
1212--1452          1196   1468
```

All three removed upper colours have another witness, so the move fills
the previously missing colours `493` and `1468` at no upper cost.  Its
rank-seven defect is therefore ten and its lower hole remains `31`.

It is nevertheless not factorable at delay three.  Formula (2.4) holds for
`q=3` at exactly

```text
i=155  coordinate 9
i=157  coordinate 8
i=360  coordinate 6
i=371  coordinate 6
i=372  coordinate 7
```

and there are no `q=1` or `q=2` hits.  Equivalently, it creates five
internal one-runs of length three.

For every fourth cut `l`, all

\[
                         \frac{5!2^5}{2}=1920
\]

reconnections of the five resulting segments were checked.  Among 953
lower-rainbow and endpoint-compatible reconnections, the best
residence-safe value is twelve holes, attained by the original seed up to
reversal.  Thus this first improving circuit cannot be repaired
by refining it with one further cut.

A second exhaustive three-cut census starting from this ten-hole path found
only one residence-safe template, again with twelve holes.  This is a local
basin statement, not an exclusion of unrelated four- or higher-cut moves.

## 5. The rank-eight mirage

There is a residence-safe three-cut path whose consecutive triple unions
cover all 165 rank-eight masks:

```text
cuts          136,217,307
segment order 2,1,0,3
orientations  0,1,0,0
missing lower 31
endpoints      1000,63
```

It replaces

```text
497--1008, 940--1000, 952--1968
```

by

```text
497--504, 940--952, 1008--1968.
```

This fills rank-seven colour `956`, loses rank-seven colour `1009`, and
eliminates the sole rank-eight hole `958`.  It therefore keeps twelve
rank-seven holes while making the upper depth-two row perfect.

However, its consecutive triple intersections omit the rank-four mask
`432`.  That mask is contained in neither endpoint `1000` nor endpoint
`63`, so no boundary cell of any factor of this central path can equal it.
The apparent rank-eight repair therefore cannot coexist with the complete
lower compiler.  This is a useful warning: residence plus the immediate
lower rainbow is not enough; the deeper endpoint ideals are active even in
a three-edge move.

## 6. The reduced gate

For this seed, a successful coupled repair must now contain a circuit of
support at least four satisfying simultaneously:

1. the new lower colours are a rainbow transversal of the removed colours
   plus the old missing colour;
2. the resulting missing lower colour is boundary-absorbable;
3. (2.4) has no solution for `q=1,2,3`;
4. every lower depth-two/depth-three hole lies in the endpoint ideals and
   passes the exact pin/Hall completion test; and
5. at least one of the twelve missing rank-seven colours is inserted without
   deleting its last witness elsewhere.

This is the smallest exact reservoir gate exposed by the fixed `k=11`
braid.  It is strictly smaller than rebuilding the word, but it is genuinely
coupled: the unique colour-improving three-cut circuit fails only at the
residence identities, while the unique rank-eight-perfect three-cut circuit
fails only at a deeper lower boundary colour.

The independently checked distance-15 certificate in
`K11_DISTANCE15_AUDIT.md` gives the complementary global fact: a path with
complete rank-seven coverage and the immediate lower/end-point conditions
must replace at least sixteen seed edges.  The present audit says where the
first incremental move must begin; that certificate says a complete repair
cannot remain in a tiny neighborhood.

## 7. Reproduction

```bash
python3 scratch/analyze_k11_upper_circuits.py

c++ -O3 -std=c++20 scratch/search_k11_general_three_opt.cpp \
  -o /tmp/search_k11_general_three_opt
/tmp/search_k11_general_three_opt k11_upper549_rank_exact_flag.txt

# Exact second census from the ten-hole near-circuit:
/tmp/search_k11_general_three_opt k11_upper549_rank_exact_flag.txt pre

# Exact refinement of the ten-hole near-circuit by one arbitrary cut:
python3 scratch/audit_k11_pretrade_fourth_cut.py
```

The exploratory four-cut sampler
`scratch/search_k11_targeted_four_opt.cpp` is deliberately not used for an
impossibility claim.  Its bounded 800,000-sample run found 15,698
lower/endpoint/residence-compatible templates and no upper improvement, but
that is only negative search evidence.
