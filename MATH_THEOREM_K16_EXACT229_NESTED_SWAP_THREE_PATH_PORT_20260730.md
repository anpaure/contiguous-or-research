# K16 exact229 nested forward swaps: an upper-complete Hall24 port and the exact third-move signature

Date: 2026-07-30  
Status: exact finite theorem for the stated two-swap family; solver-free
locality obstruction for a tail-confined third swap; conditional protected-
matching theorem for the missing cross-shore move.  No physical third move is
claimed.

## 1. Frozen source and operations

Let `T` be the authenticated exact, arbitrary-upper-complete chronology

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA-256 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974.
```

For equal-length blocks write `S(a,b;t)` for the forward exchange

\[
 [a,a+t)\longleftrightarrow[b,b+t).
\]

The family in this note applies, in the displayed order,

\[
 O_L=S(6611,12718;L),\qquad
 I_l=S(6613,12721;l),                              \tag{1.1}
\]

where `L` is 16 or 18 and `l` is 9, 13, or 15.  The second exchange acts on
the chronology produced by the first.  Occurrence labels are transported
with the rows; no repeated row value is silently identified with another
occurrence.

## 2. Exact classification theorem

### Theorem 2.1

Among the twelve parameter/order cases consisting of the six pairs `(L,l)`
and the two orders `OI,IO`, the exact and arbitrary-upper-complete cases are
exactly

\[
 (L,l)=(16,9),(16,13),(18,9),(18,15),              \tag{2.1}
\]

all in order `OI`.  Every member of (2.1) has:

```text
flats                 6320,12869,12871
capacity              32063
zero envelopes        0
arbitrary-upper holes 0
Hall matching         26308/26332
Hall deficiency       24
```

Its lower Hall graph has eleven degree-zero targets

```text
2665 28e9 291d 29a9 2f28 4879
48e9 4e70 6989 6a29 6c70
```

and residual nonzero-component deficiency 13.  The only one of the twelve
degree-zero targets of `T` that is supplied is `8000`.

#### Proof

Apply the two literal block permutations to both the row word and the
authenticated occurrence-label permutation of `T`.  For each result:

1. reconstruct the forced three-flat depth schedule;
2. form every maximal envelope and replay every target row exactly;
3. enumerate every literal upper interval OR at every length;
4. construct every occurrence-labelled compiler incidence; and
5. run deterministic Hopcroft--Karp and delete degree-zero left vertices to
   separate the residual term.

The twelve-row classification in the audit gives precisely (2.1).  The
four survivors have no structural replay error and no upper hole; the other
eight fail at least exact replay, and seven also have upper holes.  The stated
Hall data agree for all four survivors.  This is an exhaustive replay of the
specified `2*2*3` cases, not a search over other cuts.  QED.

### 2.2 The common beta provider

In every survivor, source occurrence `6613` is transported to physical
singleton cell 31761:

```text
source rows          (6613)
physical interval    [12720,12721)
allowed envelope     8a0e
mandatory mask       8000.
```

Thus it is the unique provider of `8000`.  Relative to the authenticated
exact229 matching, the matching gain is the same alternating path in all
four cases:

```text
8000 -- (6613) -- 8a0c -- (6724) -- 8e0c -- (11217).
```

Edges in the nested chronology occupy positions one, three, and five of this
path.  Flipping it raises the matching from 26307 to 26308.

The upper deck is not repaired by sacrificing another resource: the old
literal witness

```text
[12713,12715) = 4a79,4e78
```

remains in place.  This is the important difference from the earlier beta
state with debt `4e7e` and from the alpha/Hall24 state with debt `4e79`.

## 3. The two common-0200 halo paths

The two desired physical cells, written with source-occurrence labels, are

```text
C6 = (4654,4655,4656),
C4 = (4655,4656).
```

The required replacement profiles, relative to the unchanged exact229/nested
halo, are:

| cell | physical interval | desired ordered envelopes | desired `(allowed,mandatory)` | new target |
|---|---|---|---|---|
| `13964` | `[4654,4657)` | `6221,4a21,0a29` | `(6a29,6809)` | `6a29` |
| `13966` | `[4655,4657)` | `4a21,0a29` | `(4a29,4809)` | `4a29` |

Here `(allowed,mandatory)` is shorthand for the complete compiler-cell
condition together with a nonempty hit in every ordered envelope; merely
checking the two aggregate masks is insufficient.

### Theorem 3.1 (conditional three-path port)

Fix any of the four nested chronologies in (2.1) and its displayed maximum
matching.  Suppose a further occurrence rethread has all of the following
properties:

1. it is middle-exact, retains the three-flat schedule and nonzero envelopes,
   and is arbitrary-upper-complete;
2. it preserves the fixed nested maximum matching;
3. it preserves the common cell `(6025,6026,6027)` and its incidences with
   both `4a29` and `5a29`; and
4. it realizes the two complete halo signatures in the table above.

Then its lower matching is at least 26310 and its Hall deficiency is at most
22.

#### Proof

The nested maximum matching already incorporates the `8000` path of Section
2.2.  With respect to that matching the two newly realized halo incidences
give the vertex-disjoint augmenting paths

```text
6a29 -- (4654,4655,4656),

5a29 -- (6025,6026,6027) -- 4a29 -- (4655,4656).
```

The first removes a degree-zero target.  The second lowers the residual
nonzero-component deficiency.  They are disjoint from each other and from
the already-flipped `8000` path.  Flipping both raises 26308 to 26310. QED.

Exact graph replay, with only the two displayed incidences added, gives

| graph | matching | deficiency | zero count | residual term |
|---|---:|---:|---:|---:|
| nested | 26308 | 24 | 11 | 13 |
| nested + `6a29` | 26309 | 23 | 10 | 13 |
| nested + `4a29` | 26309 | 23 | 11 | 12 |
| nested + both | 26310 | 22 | 10 | 12 |

This table is conditional graph algebra.  Although Lemma 3.2 proves that the
destination substitution `T[4653]=6b29` is locally middle-exact, the table
does not assert that any occurrence permutation returning displaced
`69a9` is middle-exact.

### Lemma 3.2 (sharp fixed-neighbour halo value)

Hold every row of a nested survivor fixed except row 4653.  A rank-eight
value at 4653 preserves the three-flat schedule, replays every middle row,
and realizes **both** halo incidences if and only if

\[
                     T_{4653}\in\{\texttt{6aa9},\texttt{6b29}\}. \tag{3.1}
\]

#### Proof

The two complete candidate conditions force

\[
 \texttt{6a29}\subseteq T_{4653}.
\]

Exact replay of row 4653 with the fixed neighbours forces

\[
 T_{4653}\subseteq\texttt{6bad}.
\]

Now `6a29` has rank seven and

```text
6bad \ 6a29 = {0004,0080,0100}.
```

Rank eight therefore leaves exactly `6a2d,6aa9,6b29`.  The first equals its
fixed neighbour and creates an extra flat, so it violates the forced
three-flat schedule.  Direct envelope reconstruction shows that the latter
two have capacity 32063, no structural error, and the required cells
13964/13966. QED.

Their physical donors in the nested word are unique:

```text
6aa9@2934, 6b29@3846.
```

Exchanging either donor directly with incumbent `69a9@4653` is not a
completion: the first exchange fails row 2934, while the second fails row
3845.  Thus (3.1) is a sharp destination port, and the remaining problem is
the donor-return braid.

## 4. A tail-confined third nested swap cannot activate the halo

The complete dependency closure of cells 13964 and 13966 is contained in

```text
[4648,4660).
```

Every row touched by the two tail exchanges (1.1) lies in

```text
[6611,6629) union [12718,12736).
```

### Proposition 4.1 (support obstruction)

Any third block exchange whose support is still confined to those two tail
intervals leaves every target row and maximal envelope in the halo dependency
closure unchanged.  Hence it leaves the incidence sets of cells 13964 and
13966 unchanged and cannot activate `6a29` or `4a29` through those cells.

#### Proof

At fixed flat schedule a target-row change affects only maximal envelopes
whose defining windows meet that row, and a compiler cell depends only on its
ordered position envelopes and mandatory-carrier rows.  The two displayed
support sets are disjoint.  Therefore the complete two halo signatures are
unchanged.  In the nested chronology they do not contain the two desired
incidences. QED.

Thus a **third tail-only nested swap is ruled out for the 0200 route**.  A
successful third move must cross from the tail to the halo closure (or use a
different lower-provider pair).

For an equal-block swap to transport the known token `6b29@3846` to row
4653, its two block starts must have the form

\[
 a=3846-s,\qquad b=4653-s,qquad 0\le s<t,          \tag{4.1}
\]

for its block length `t`.  Equation (4.1) is necessary only for that literal
token route; another rethread may synthesize the same complete cell
signatures differently.

## 5. Necessary and sufficient protected tail-port signature

The following is the useful exact interface.  It separates physical
rethreading from Hall arithmetic.

Fix a nested survivor `N` and its chosen maximum matching `M_N`.  A proposed
third move is a **protected three-path port** precisely when it satisfies:

```text
Q  occurrence bijection, rank-eight rows, exact middle replay,
   flats 6320/12869/12871, capacity 32063, nonzero envelopes;

U  every upper target retains an old occurrence witness or gains a literal
   seam witness in the final chronology;

B  the beta cell (6613) retains profile
        physical [12720,12721), allowed 8a0e, mandatory 8000,
   and the fixed matching M_N survives;

Z  some second formerly-zero lower target gains a physical candidate cell
   on an M_N-augmenting path disjoint from the beta path;

C  the residual deficiency-13 shore gains an independent M_N-augmenting
   path;

O  all cells in Z and C are occurrence-disjoint as right vertices and the
   complete occurrence-labelled graph has matching at least 26310.
```

Conditions `U,O` are globally necessary for an all-upper Hall-22 successor,
and `Q` is necessary within this fixed-schedule branch.  Under the protected-
matching hypothesis `B`, the exact necessary-and-sufficient condition for two
additional matching units is the existence of two vertex-disjoint
`M_N`-augmenting paths, by the standard matching symmetric-difference
decomposition.  If one additionally requires the observed split
`(Z,S)=(10,12)`, one path must start in the degree-zero part and one must
discharge the residual nonzero shore; these are the roles denoted `Z,C`.

For the common-0200 realization, `Z,C` specialize without ambiguity to

```text
Z: 6a29 -- (4654,4655,4656),
C: 5a29 -- (6025,6026,6027) -- 4a29 -- (4655,4656),
```

with the complete cell signatures of Section 3.  Therefore `Q,U,B` plus
the retained incidence
`5a29--(6025,6026,6027)` and those two signatures is the requested
necessary-and-sufficient port in the protected halo branch.

For a different second zero provider, the finite candidate condition for a
cell `C` and target `z` is exactly

\[
 M(C)\subseteq z\subseteq E(C),
 \qquad z\cap E_p\ne\varnothing
 \quad\text{for every position }p\text{ of }C,      \tag{5.1}
\]

followed by the disjoint augmenting-path condition.  Equation (5.1), not
mere target positivity, is the exact provider filter.

The closest known alternative is alpha's `4e70` cell.  In fact, applying

```text
[6608,6611) <-> [12714,12717)
```

after **any** of the four nested survivors remains middle-exact, keeps the
`8000` provider, and creates the independent `4e70` provider.  Its graph has

```text
matching 26309, deficiency 23, Z=10, residual term 13,
```

but its sole upper hole is again `4e79`.  The new cell is:

```text
source rows          (12714,12715)
physical interval    [6608,6610)
ordered envelopes    4e60,4e30
allowed              4e70
mandatory            0a50.
```

The two zero-provider paths are disjoint, but relocating source rows
12714/12715 destroys the retained `4e79` witness.  The old Hall24 41-pair
tail atlas cannot be transplanted unchanged: after the nested swaps, rows
12718 onward are

```text
ca2e,8a6e,8a4f,...
```

rather than the old tail, and they enter the replay equation at row 12717.

As an exact scoped control, refilter the 36 old pairs that avoided exporting
`ca2e`.  Only nine remain middle-exact in nested+alpha:

```text
F in {0e79,4c79,4e39,4e59}, Y in {c62e,ce26};
F=4679,                          Y=ce26.
```

Each of the nine closes `4e79` but has sole arbitrary-upper debt `ce3c`.
The other 27 inherited pairs are middle-inexact, typically missing `0040`
at row 12717.  The relevant local tail closure is identical in all four
survivors, and all nine exact rows received a full arbitrary-upper replay in
each survivor.  This is a complete rejection/classification of the inherited
36-list only.  It is **not** a complete enumeration of all rank-eight
`(facet,relief)` pairs in the new nested tail.  A full nested-tail atlas, or a
wider occurrence return that changes more closure rows, remains open.

## 6. Relation to fixed-width wedge-ray absorption

The facet equation used in that 41-pair atlas is

\[
 F\cup\texttt{4a79}=\texttt{4e79}.                 \tag{6.1}
\]

It resembles the socket equation of the fixed-width wedge-seam ray theorem,
but the present tail is **not a wedge**.  Around the retained witness the
relevant unions are

```text
ca71 | 4a79 = ca79,
4a79 | 4e78 = 4e79,
4e78 | 4e3c = 4e7c.
```

They are unequal.  Hence (6.1) certifies the rank-nine witness only; it does
not invoke the theorem that repairs an entire outward upper ray.  This is
consistent with the original Hall24 two-row substitutions closing `4e79`
while leaving deeper upper debt; after nesting, even that old local atlas
must first be refiltered as in Section 5.

A genuine wedge socket elsewhere can be combined with the lower paths when
its dependency closure avoids their protected cells: the wedge theorem then
supplies `U`, while Theorem 3.1 supplies the Hall gain.  No such literal
socket is identified here.  Upper ray absorption and the two-provider Hall
condition are compatible interfaces, but neither implies the other.

## 7. Sharp proved boundary

What is proved:

1. the exact four-member classification (2.1);
2. a common, explicit `8000` augmenting path and upper-complete Hall24 state;
3. conditional Hall deficiency 22 from the two halo signatures;
4. impossibility of activating those signatures by a third swap confined to
   the same two tail intervals; and
5. an occurrence-level protected-port criterion for any cross-shore or
   alternative-provider third move.

What is not proved:

1. existence of a physical cross-shore third swap realizing the halo;
2. existence of a wider tail braid combining the nested `8000` provider with
   alpha's `4e70` provider;
3. preservation of the full fixed matching by an unspecified move; or
4. applicability of wedge-ray absorption at this nonwedge tail.

## 8. Reproducibility

```text
scratch/audit_k16_exact229_nested_swap_three_path_port_20260730.py
SHA-256 8ef85074369d12dcaa208a8485275195ebdec4d7a7b9d410596f4bdeda2edf68

scratch/k16_exact229_nested_swap_three_path_port_20260730.audit.json
SHA-256 e96ed3a781b63ba86025ad7e468477827942c92c04e3604a336bab6cb3762948
payload 69ef2f01fdd64e5546a6f70357c526593b627ec27c272e9fb4ed8b480cb71667
```

The reproducer uses no SAT solver and performs no unbounded search.
