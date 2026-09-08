# Punctured Catalan side forests: tight enumerations and exact `C6` augmentation

Date: 2026-07-31  
Status: exact all-`n` fixed-cycle equivalence and augmentation criterion;
complete audit of the published GMM implementation for `n=3,4,5,6`;
complete strict-`C6` frontier and a two-`C6` repair at `n=4`.  No all-`n`
prescribed-common-basis side-forest theorem is claimed.

## 0. Verdict

There is a clean tight-enumeration sufficient subclass of the remaining
`a=1` side-forest gate.

Suppressing the rank-`(n+2)` vertices of a tight enumeration of levels
`{n+1,n+2}` gives a Hamilton cycle `H` in `J(2n,n+1)`.  Mark one edge for
every rank-`(n+2)` vertex.  The marked edges form the required punctured
side matching exactly when their rank-`n` intersections are distinct.  They
automatically form a spanning linear forest.  A prescribed seam anchor is
legal exactly when it is incident with at most one marked edge.

This does **not** follow from the published tight-enumeration theorem.  In
the Hamilton cycles emitted by the vendored GMM implementation, the full
upper-versus-intersection occurrence matching has ranks

```text
n                         3       4        5         6
upper target count P      6      28      120       495
maximum occurrence rank   6      25       98       385
deficiency                 0       3       22       110.
```

For `n=4,5,6`, the displayed deficiency is already forced by upper colours
having a unique occurrence and colliding on the same intersection.  Thus
no re-marking of the fixed GMM Hamilton cycle can work.

At `n=4`, one strict alternating physical `C6` is still insufficient: all
`1477` such Hamilton outputs have occurrence rank at most `27/28`.  Two
explicit, physically vertex-disjoint `C6` switches raise the rank

```text
                         25 -> 27 -> 28
```

and the repaired cycle has a perfect marking with only `12` double-incidence
owners, below the available nonanchor budget `14`.  This refutes the guess
that one `C6` can improve the deficiency by at most one.

The correct all-`n` augmentation theorem is a common-core linkage theorem:
after deleting all old packet occurrences, the new occurrences must carry
all augmenting paths from the exposed upper colours.  Physical disjointness
of the `C6` packets does not make this linkage automatic.

The finite repair has enough **unprescribed** anchor capacity.  It does not
show that its legal anchor set is the upper-colour image of a common basis
of a supplied child Catalan forest.  That correlation remains the exact
recursive gate.

## 1. The occurrence graph of a Hamilton cycle

Let `Omega=[2n]` and put

\[
 {cal L}={\Omega\choose n},\qquad
 {cal X}={\Omega\choose n+1},\qquad
 {cal U}={\Omega\choose n+2},
\]

\[
 M=|{\cal L}|={2n\choose n},\quad
 N=|{\cal X}|={2n\choose n+1},\quad
 P=|{\cal U}|={2n\choose n+2},\quad
 C=M-P.                                                     \tag{1.1}
\]

For an edge `e=XY` of `J(2n,n+1)`, define

\[
                    \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.    \tag{1.2}
\]

The pair `(ell(e),u(e))` determines `e`: if
`u(e)-ell(e)={a,b}`, then the physical endpoints are
`ell(e)+a` and `ell(e)+b`.

For a Hamilton cycle `H` on `cal X`, let `O(H)` be the simple bipartite
**occurrence graph** on `cal U sqcup cal L` with one edge
`u(e) ell(e)` for every `e in E(H)`.

### Theorem 1.1 (exact fixed-cycle equivalence)

Fix a set `B subset cal X` of seam anchors.  The following are equivalent.

1. There is a tight cyclic enumeration of levels `{n+1,n+2}` which
   suppresses to `H`, whose mediated edges have distinct rank-`n`
   intersections, and in which every `b in B` is incident with at most one
   mediated edge.
2. `O(H)` has a matching `J` saturating `cal U` such that

   \[
                 d_{E_J}(b)\le1\qquad(b\in B),               \tag{1.3}
   \]

   where `E_J` is the corresponding set of physical edges of `H`.

Whenever these conditions hold, `E_J` is a spanning linear forest on
`cal X`, has `P` edges and `N-P` components, and is a punctured side
matching with lower palette `ell(E_J)` and complete upper palette `cal U`.

#### Proof

Suppress the rank-`(n+2)` vertices of a tight enumeration.  Equality in
the flip budget forces every such vertex `U` to lie between two distinct
rank-`(n+1)` facets `X,Y`; suppression replaces `X,U,Y` by the Johnson
edge `XY`, labelled by `u(XY)=U`.  The remaining transitions are direct
Johnson edges.  Thus the suppressed order is a Hamilton cycle and the
mediated occurrences use every upper label once.  Their intersections are
distinct exactly when the occurrence pairs form a matching in `O(H)`.
Condition (1.3) is literally the seam-anchor degree cap.

Conversely, given `J`, traverse `H` and insert `u(e)` between the endpoints
of every selected edge `e`.  Every member of `cal U` is inserted exactly
once, all other vertices are the members of `cal X`, every inserted step is
an inclusion step and every unselected step is a Johnson step.  The cyclic
Hamming length is

\[
                 2P+2(N-P)=2N
 =|{\cal X}|+|{\cal U}|+\bigl||{\cal X}|-|{\cal U}|\bigr|,
\]

so this is a tight enumeration.  Since `P<N`, `E_J` is a proper subset of
one cycle.  It therefore is a spanning linear forest, with isolates
included, and has `N-P` components. \(\square\)

This theorem is an equivalence for the **fixed-Hamilton-cycle subclass**.
An arbitrary punctured side forest need not be Hamilton-completable, so it
is not asserted to be equivalent to a tight enumeration.

### Corollary 1.2 (unprescribed anchor capacity)

Let `d_2(J)` be the number of vertices of `H` incident with two selected
edges.  Some anchor set of order `C` satisfies (1.3) if and only if

\[
                              d_2(J)\le N-C.           \tag{1.4}
\]

If the selected edges form `b(J)` cyclic runs, then

\[
                  d_2(J)=P-b(J),qquad
                  (1.4)\iff b(J)\ge M-N=\operatorname{Cat}_n. \tag{1.5}
\]

#### Proof

Every double-incidence vertex must be outside the anchor set, and all other
vertices are eligible.  This proves (1.4).  A run of `s` selected edges has
`s-1` internal vertices incident with two of them; summing over runs gives
`d_2=P-b`.  Substitution in (1.4) gives (1.5). \(\square\)

For a prescribed child basis, merely meeting (1.4) is not enough: its
specific anchor image must avoid every double-incidence vertex.

## 2. Why the GMM theorem does not close the gate

The vendored implementation was compiled directly from
`tmp/cos/code/bits` and run as

```text
cycle -n(2n) -k(n+1) -l(n+2) -t2 -s1.
```

The exact audit gives:

| `n` | `M` | `N` | `P` | default intersection excess | default anchor deficiency | `rank O(H)` | deficiency |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 20 | 15 | 6 | 1 | 2 | 6 | 0 |
| 4 | 70 | 56 | 28 | 7 | 5 | 25 | 3 |
| 5 | 252 | 210 | 120 | 35 | 14 | 98 | 22 |
| 6 | 924 | 792 | 495 | 151 | 42 | 385 | 110 |

Here `default` means the edges mediated in the literal output.  The default
intersection multiplicity is never above two in these four cases.

More strongly, let `S` be the set of upper vertices having degree one in
`O(H)`.  Its unique-neighbour Hall row is:

| `n` | `|S|` | `|N(S)|` | `|S|-|N(S)|` | total matching deficiency |
|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 0 | 0 |
| 4 | 15 | 12 | 3 | 3 |
| 5 | 79 | 57 | 22 | 22 |
| 6 | 364 | 254 | 110 | 110 |

Thus, for `n=4,5,6`, the degree-one Hall set proves that **no** placement
of the upper vertices on the fixed suppressed GMM cycle can have distinct
intersections.  This is a property of the concrete published construction,
not an impossibility theorem for other tight enumerations.

There is a second independent failure in the literal GMM marking.  Its
number of selected-edge runs is short of the Catalan requirement (1.5) by

```text
                         2, 5, 14, 42
```

at `n=3,4,5,6`, respectively.  These are `Cat_(n-1)` in the audited range.
The table is a finite fact; no all-`n` formula for this implementation is
claimed here.

At `n=3`, the Hamilton cycle itself is repairable without changing any
physical edge.  Exactly `48` upper-saturating intersection-rainbow markings
exist.  Their double-incidence histogram is

```text
                         1^19  2^23  3^6.
```

The minimum value one equals the available nonanchor budget
`N-C=1`, so nineteen markings satisfy the unprescribed anchor-capacity
test.  The default GMM insertion is simply not one of them.

This already separates three statements which must not be conflated:

1. a tight enumeration exists (published theorem);
2. its suppressed Hamilton cycle admits an intersection-rainbow marking;
3. such a marking is compatible with a prescribed recursive anchor set.

Only item 1 is unconditional in the literature.

## 3. Exact `C6` augmentation

Let `H,H'` be Hamilton cycles of `J(2n,n+1)`, and put

\[
 A=E(H)\setminus E(H'),\qquad B=E(H')\setminus E(H),\qquad |A|=|B|=t.
                                                               \tag{3.1}
\]

For a strict alternating physical `C6`, `t=3`; the three old edges have
six distinct physical endpoints, the three new edges are wholly new, and
their union is one alternating six-cycle.

Let

\[
                  O_0=O(H-A)=O(H'-B).                 \tag{3.2}
\]

### Theorem 3.1 (common-core augmentation criterion)

Let `Q` be a maximum matching of `O_0` and put

\[
                  r=P-|Q|.                            \tag{3.3}
\]

Then `O(H')` has a matching saturating every member of `cal U` if and only
if `O_0+O(B)` contains `r` mutually vertex-disjoint `Q`-augmenting paths
which start at all `Q`-exposed upper vertices and end at `Q`-unmatched lower
vertices.

In particular, a `t`-edge packet can supply at most `t` such paths, and

\[
          \operatorname{rank}O(H')\le\operatorname{rank}O_0+t. \tag{3.4}
\]

If a terminal matching `J'` is supplied, it also obeys a prescribed anchor
set `B_0 subset cal X` exactly when

\[
                       d_{E_{J'}}(b)\le1\quad(b\in B_0).        \tag{3.5}
\]

#### Proof

If the paths exist, augment `Q` along all of them.  They are vertex-disjoint,
so the result is a matching of size `|Q|+r=P`, saturating the `P` upper
vertices.  Conversely, take any upper-saturating terminal matching `J'`.
The symmetric difference `Q triangle J'` is a disjoint union of alternating
cycles, equal-size alternating paths, and exactly `r` augmenting paths from
the upper vertices exposed by `Q` to unmatched lower vertices.  Since `Q`
is maximum in `O_0`, every augmenting path uses at least one new occurrence
from `O(B)`.  Distinct paths use distinct matching edges, proving (3.4).
Equation (3.5) is Theorem 1.1. \(\square\)

### Corollary 3.2 (disjoint packet basis: exact boundary)

A family of physically vertex-disjoint alternating `C6` packets is a valid
rank-augmentation basis precisely when

1. their simultaneous physical switch is still one Hamilton cycle; and
2. their combined new occurrence edges satisfy Theorem 3.1.

Physical disjointness makes the edge replacements commute, but it implies
neither condition 1 nor condition 2.  If the individual augmenting linkages
are also occurrence-vertex-disjoint in the common graph, their rank gains
add.

The naive stronger claim that one strict `C6` reduces occurrence deficiency
by at most one is false: the first packet in Section 4 reduces it by two.
The universal bound supplied by (3.4) is three.

## 4. The complete `n=4` frontier

For the suppressed GMM cycle at `n=4`, the audit enumerates every strict
six-distinct-owner alternating `C6` which leaves one Hamilton cycle.  There
are exactly `1477` terminal edge sets, with occurrence-rank histogram

```text
rank 23 :  13
rank 24 : 215
rank 25 : 966
rank 26 : 241
rank 27 :  42
rank 28 :   0.
```

Hence one strict `C6` cannot repair this fixture.

Two switches do repair it.  In decimal bitmask notation, first replace

```text
old  203-211, 87-91, 206-214
new  203-206, 91-211, 87-214,
```

and then replace

```text
old  93-117, 199-213, 103-115
new  115-117, 103-199, 93-213.
```

The two six-owner supports are disjoint.  The rank trajectory is

\[
                              25\longrightarrow27\longrightarrow28. \tag{4.1}
\]

In the combined switch, the common occurrence graph has rank `24`.  One
terminal perfect matching is obtained from four augmenting paths.  Three
are the singleton new occurrences

```text
U119-L113,       U215-L86,       U219-L83,
```

and the fourth is

```text
U235 - L225 - U231 - L71 - U95 - L89,
```

where the middle edge `U231-L71` is new and the other edges alternate
between the common matching and terminal matching.  There is also the
equal-size exchange component

```text
                         L153-U221-L85.
```

The selected perfect marking has `12` double-incidence owners.  Since

\[
                    N-C=56-42=14,                    \tag{4.2}
\]

Corollary 1.2 supplies an anchor set of the required size.  No claim is
made that this set equals the upper-port image of the common basis required
by a particular child Catalan forest.

The finite result nevertheless identifies the right move scale.  The first
GMM Hall defect is not repaired by a single local hexagon, but it is repaired
by two commuting hexagons whose occurrence linkages interact through the
common core.

## 5. Consequence for the `a=1` recursion

The automatic common-basis theorem closes the synchronized diagonal
**incidence** row.  This note shows that a tight enumeration can close one
physical side row if one can choose, jointly,

1. a Hamilton cycle `H` on the rank-`(n+1)` owners;
2. an upper-saturating matching of `O(H)` whose lower image is the required
   diagonal complement;
3. a marking satisfying the prescribed seam-anchor caps; and
4. on the two shores together, a contracted attachment forest.

The GMM Hamilton cycle is not a black-box solution: from `n=4` onward it
fails item 2 before the prescribed anchor set is even consulted.  The local
`C6` theorem turns repair into a bounded-width augmenting-linkage question,
but no all-`n` supply theorem for enough compatible packets is presently
proved.

The shortest surviving target is therefore:

> **Forest-compatible common-basis cycle theorem.**  Choose the guaranteed
> common basis and two Hamilton cycles so that their occurrence matchings
> realize its two diagonal complements, obey the two inherited anchor sets,
> and make the contracted two-shore attachment graph acyclic.

The `n=4` repair proves that physical asymmetry and interacting `C6`
linkages can supply the missing occurrence rank.  It does not yet supply
the common-basis correlation uniformly in `n`.

## 6. Reproducible audit

The standard-library audit is

```text
scratch/audit_catalan_punctured_side_tight_enumeration_gmm_c6_20260731.py
```

It compiles the vendored C++ sources in a temporary directory, verifies
every tight word and all occurrence ranks independently with Kuhn and
Hopcroft--Karp algorithms, exhausts the `n=3` re-markings, exhausts every
strict `n=4` `C6`, and replays the two-switch certificate.  It writes

```text
scratch/catalan_punctured_side_tight_enumeration_gmm_c6_20260731.audit.json.
```

The audit is complete for the scopes stated above.  It is not a census of
non-strict alternating closed trails, two-`C6` combinations other than the
displayed witness, other Hamilton cycles at `n>=5`, or prescribed child
common bases.
