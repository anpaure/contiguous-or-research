# K16 top-bit phase trace and exact portal ownership

Date: 2026-07-31  
Status: **exact reduction and light audit; no new K16 upper bound**

## 1. Exact phase-trace theorem

Let `z` be a new coordinate and write every nonempty letter of a word `W`
uniquely as

\[
                 w_i=p_i\cup \epsilon_i\{z\},
 \qquad p_i\subseteq V,\quad \epsilon_i\in\{0,1\}.
\]

For an interval `I=[a,b]`, put

\[
 P(I)=\bigcup_{i\in I}p_i,
 \qquad E(I)=\max_{i\in I}\epsilon_i.
\]

Define

\[
 \mathcal C_e(P,\epsilon)
   =\{P(I): I\text{ is an interval and }E(I)=e\}
 \qquad(e=0,1).
\]

### Theorem 1.1 (phase-trace criterion)

`W` is universal on `V union {z}` if and only if

\[
 2^V\setminus\{\varnothing\}\subseteq\mathcal C_0(P,\epsilon),
 \qquad
 2^V\subseteq\mathcal C_1(P,\epsilon).                 \tag{1.1}
\]

#### Proof

An interval whose phase maximum is zero contains no `z`, and its union is
exactly `P(I)`.  An interval whose phase maximum is one contains `z`, and
its union is exactly `P(I) union {z}`.  These are the two possible target
types.  This proves both directions.  QED.

This is the phase-free form of the lift gate: all dependence on the new
coordinate is carried by one binary trace.  In particular, deleting or
replacing collar cells cannot be assessed from the old projected word alone;
it changes both projected owners and the set of intervals admitted to the two
families in (1.1).

## 2. Prefix--suffix ownership for an arbitrary phase trace

For a `z`-bearing position `u`, let `G_u^-` be the maximal zero-phase block
immediately preceding `u`; it may be empty.  Define `G_v^+` analogously
after a `z`-bearing position `v`.  Prefix and suffix OR state sets include
the empty state zero.

### Theorem 2.1 (exact marked-owner decomposition)

The marked projected cover is

\[
 \mathcal C_1(P,\epsilon)=
 \bigcup_{\substack{u\le v\\ \epsilon_u=\epsilon_v=1}}
 \left(
    \operatorname{Suff}(P|G_u^-)
    \vee \{P([u,v])\}
    \vee \operatorname{Pref}(P|G_v^+)
 \right).                                                   \tag{2.1}
\]

The unmarked projected cover is simply

\[
 \mathcal C_0(P,\epsilon)=
 \bigcup_G\operatorname{IntOR}(P|G),                         \tag{2.2}
\]

where `G` ranges over maximal zero-phase blocks.

#### Proof

For a marked interval, let `u` and `v` be its first and last `z`-bearing
positions.  Its part before `u` is a suffix of the zero block immediately
preceding `u`; its part after `v` is a prefix of the zero block immediately
following `v`; the complete middle is `[u,v]`.  Conversely every choice in
(2.1) is represented by the corresponding physical interval.  An unmarked
interval lies wholly in one maximal zero block, proving (2.2).  QED.

Thus a multi-phase braid is not merely a more complicated presentation of a
one-boundary lift: every additional phase boundary creates an additional
indexed prefix--suffix portal family.  Its state set may coincide with or be
contained in an existing family; nonredundancy must be checked separately.

## 3. The single-switch splice

Specialize to

```text
L | [z] | (z union H),
```

where `L,H` are words on the old ground.  Then (1.1)--(2.2) reduce exactly
to

\[
 \operatorname{IntOR}(L)=2^V\setminus\{\varnothing\},          \tag{3.1}
\]

and

\[
 2^V\subseteq
 \operatorname{IntOR}(H)\ \cup\
 \bigl(\operatorname{Suff}(L)\vee\operatorname{Pref}(H)\bigr).
                                                                  \tag{3.2}
\]

Here the empty suffix and prefix are included, so (3.2) also contains the
projection zero of the singleton `[z]`.

If `n=nu(|V|)` and the total length is `2n-3`, (3.1) gives `|L|>=n`, hence
the transformed old-projection shore has length at most `n-4`.  Therefore a
three-cell compression of the recurrence cannot be justified by saying that
the second shore is merely another nearly complete copy: every old target
lost internally by that shore must be owned by the *one nested portal* in
(3.2).

The exact precedence reduction in
`MATH_THEOREM_K16_REPEATFREE_CYCLIC_GAP_RELATIVE_PERM_NOGO_20260730.md`
is precisely (3.2) written coordinatewise.  If `R` is the set of old masks
missing internally from `H`, `p_R` is the largest contained prefix state,
and `q_R=R-p_R`, then a suffix portal exists exactly when all coordinates of
`q_R` enter the suffix chain before every coordinate outside `R`.  Opposite
requirements form a directed cycle and rule out the splice.

## 4. What the six authenticated K15 seeds say

The six length-6,438 parents are all independently verified optimal K15
words with exact middle row.  Their width-three rank-seven projected decks
are:

| seeds | distinct rank-seven masks | junk | repeat excess |
|---|---:|---:|---:|
| `1,5` | 6,435 | 1 | 0 |
| `0` | 6,435 | 0 | 1 |
| `2,3,4` | 6,434 | 1 | 1 |

Thus seeds `1,5` are the two repeat-free perfect-deck parents.  Nevertheless,
the complete cyclic-gap/relative-permutation audit checks all

\[
 6\cdot2\cdot6438=77,256
\]

single-switch configurations, including all 25,752 configurations from
seeds `1,5`, and every row contains an explicit directed two-cycle in its
portal precedence graph.  Hence perfect deck and repeat-freeness do **not**
imply compressibility in this audited cyclic four-cell-gap single-switch
class.

This is the clean answer to the seed question:

> the good K15 seed removes the inherited width-three ghost, but the audited
> cyclic-gap construction still fails its sole suffix--prefix portal chain
> for every tested parent, orientation, and rotation.  A successful word
> must leave that precise class—for example by separated edits, rethreading,
> or additional phase portals.  The audit is not a no-go for every possible
> single-switch word.

## 5. The live multi-phase collar and a new one-hole incumbent

The independently verified 19-cell V/V `5/9/5` control is a literal
length-12,874 universal word.  Its actual top-bit trace has six runs:

```text
0^6437 1^1 0^3 1^6430 0^1 1^2.
```

Its first long zero run misses exactly the two old masks

```text
2879 287d,
```

both supplied by the three-cell interior zero run.  Its long marked run
misses 22 projected targets; all 22 are supplied by the other phase runs or
their portals.  This is a literal demonstration of why the extra phase
boundaries matter.

Deleting physical position 1, which is in the first free window, gives a
length-12,873 V/V `4/9/5` word with exactly one hole:

```text
2c6d.
```

Its canonical SHA-256 is

```text
e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676.
```

The fixed bodies after deletion are exactly

```text
X[6:6436],     z union X[7:6432],
```

and the three free windows have sizes `4/9/5`.  Therefore this is an
authenticated one-hole incumbent in the V/V TH495 fibre listed as UNKNOWN in
`AUDIT_K16_RAW_SPLICE_18CELL_SCOPE_LEDGER_20260730.md`.  It is distinct from
the known delete-position-1 one-hole basin built from
`answers/k16_upper12874.word`.

This does not solve K16.  It promotes V/V TH495 to a particularly sharp live
fibre: one must reassign its eighteen free cells so as to install `2c6d`
without destroying any of the 65,534 already covered masks.  The exact
necessary-and-sufficient condition for such a reassignment is the
host-intersection/core gate of
`MATH_THEOREM_R_K16_REPEATFREE_COLLAR_ARBITRARY_EXTENSION_AND_CORE_GATE_20260730.md`.

By contrast, the seed5/self RF495 `4/9/5` fibre is completely closed: its
twenty-one mandatory rank-eight targets have only twenty nested oriented
anchors.  That deficiency-one theorem is fibre-specific and does not apply
to the V/V incumbent above.

## 6. Current conclusion

The symbolic picture is now exact.

1. One top-bit switch is fully characterized by (3.1)--(3.2) and is closed
   for every authenticated cyclic-gap parent, including both repeat-free
   perfect-deck seeds.
2. Multiple phase runs enlarge the owner family exactly by (2.1); the
   verified 12,874 control uses those additional portals essentially.
3. At length 12,873, the V/V `4/9/5` fibre already reaches one hole, so the
   remaining issue is an eighteen-cell simultaneous owner compatibility
   problem, not a missing counting identity.
4. Only one repeat-free `4/9/5` fibre has a proved no-go.  No global K16
   obstruction follows.

The authoritative numerical bracket remains

\[
                         \boxed{12873\le\nu(16)\le12874}.
\]

## 7. Superseding fixed-ghost correction

The description of V/V TH495 as a live eighteen-cell compatibility problem
in Sections 5--6 is superseded by an independent deadline audit.  In the
V/V fibre, the immutable triples at zero-based positions
`[11726,11728]` and `[12826,12828]` first reach rank eight at their final
positions and both have OR `0xc279`; their prefix-rank traces are `(2,7,8)`
and `(6,7,8)`.  The deadlines `11728` and `12828` are distinct, so every
word in the fixed fibre has a first-middle ghost extra `G>=1`.

Every universal K16 word of length `12873` has `G=0`, since the
architecture-free deadline inequality

\[
 26332\le(3-G)(12873+G)
\]

fails already at `G=1`.  Hence the complete V/V TH495 `4/9/5` fibre is
solver-free UNSAT.  The authenticated `e4a7ad4e...` word remains a valid
one-hole calibration: it satisfies fifty-nine of the sixty fixed-body
residual rows and misses only `0x2c6d`.

The distinct delete-p1 `collar594` fibre has the same two immutable
`0xc279` first deliveries outside its free windows, and is excluded by the
same argument.  This is a fixed-fibre theorem, not a proof that
`nu(16)>12873`; an equality construction may edit a ghost occurrence or use
a different crop.
