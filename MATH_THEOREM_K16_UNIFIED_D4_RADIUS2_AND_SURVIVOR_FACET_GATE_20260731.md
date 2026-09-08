# K16 unified D4 radius-two theorem and survivor-facet gate

Date: 2026-07-31  
Lane: D  
Status: exact structural synthesis; no D5 claim or computation  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Single theorem

Let

```text
U = answers/k16_upper12874.word,
|U| = 12874,
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

For a zero-based source position `d`, let `W^d` be `U` with cell `d`
deleted, and let `H_d` be the nonzero masks not represented as interval ORs
of `W^d`.  Define

\[
 D_{\le4}=\{d:|H_d|\le4\}.
\]

> **Unified D4 radius-two and survivor-facet theorem.**
>
> 1. The exact deletion census gives `|D_{<=4}|=191`, split as
>
>    ```text
>    |H_d|=1:   1 row,
>    |H_d|=2:   3 rows,
>    |H_d|=3:   3 rows,
>    |H_d|=4: 184 rows.
>    ```
>
>    For every `d in D_{<=4}`, every two distinct post-deletion sites
>    `p,q`, and every nonzero masks `x,y`, replacing `W^d_p,W^d_q` by
>    `x,y` does not give a universal word.  Values equal to incumbents are
>    included through the authenticated delete-plus-one-substitution
>    theorem.  Equal new values `x=y` are allowed.
>
> 2. More generally, let `Z` be any nonuniversal intermediate word and
>    suppose replacing one cell of `Z` by a nonzero mask `y` makes it
>    universal.  Then every hole of `Z` contains `y`:
>
>    \[
>       H(Z)\subseteq\uparrow y=\{T:y\subseteq T\}.       \tag{1.1}
>    \]
>
>    Consequently, for every coordinate `b in y`, `Z` already covers the
>    entire coordinate facet
>
>    \[
>       F_b=\{T\ne0:b\notin T\}.                         \tag{1.2}
>    \]
>
>    Equivalently, `J(Z)=intersection H(Z)` is nonzero iff `Z` covers
>    `F_b` for at least one bit `b`.
>
> 3. In a provider-first delete-plus-two-edit completion, choose any bit
>    `b` of the actual second value `y`.  The same bit couples the two
>    edits: the first edit must supply or preserve every affected target
>    omitting `b`, while every target whose witnesses are all forced through
>    the second site contains `b`.  This is a deletion-independent
>    16-colour normal form.  It is not, by itself, a coupling between
>    different deletion choices and does not prove the global `+1` lower
>    bound.
>
>    More strongly, if `S=supp(y)` and `empty != A subseteq S`, the cells of
>    the intermediate word avoiding every bit of `A` concatenate to a
>    universal word on the other `16-|A|` coordinates.  Hence
>
>    \[
>       N_A(Z)=|\{i:Z_i\cap A=\varnothing\}|\ge\nu(16-|A|),       \tag{1.3}
>    \]
>
>    and for `1<=a<=|S|`,
>
>    \[
>       \sum_i {|S\setminus Z_i|\choose a}
>       \ge {|S|\choose a}\nu(16-a).                            \tag{1.4}
>    \]

Here `D3` is a subset of `D4`: “D3+D4” means their union, which is the same
191-row set `D_{<=4}`, not 198 rows.  The word “exact” above identifies the
complete certified index set.  It does not assert that a deletion outside
`D_{<=4}` admits a repair.

## 2. Exact closed deletion set

The rows with fewer than four holes are

```text
|H_d|=1: 1
|H_d|=2: 0, 3, 12873
|H_d|=3: 6389, 6441, 12871.
```

The 184 four-hole rows are

```text
2, 112, 130, 134, 425, 521, 538, 740, 760, 853, 947, 964, 1140, 1166,
1355, 1374, 1390, 1561, 1612, 1703, 1705, 1707, 1834, 1838, 1987, 2038,
2133, 2226, 2242, 2418, 2444, 2464, 2472, 2557, 2633, 2652, 2686, 2690,
2839, 2844, 2870, 2890, 2983, 3078, 3094, 3265, 3411, 3485, 3504, 3520,
3542, 3691, 3696, 3911, 3930, 3946, 4148, 4168, 4259, 4261, 4263, 4356,
4372, 4390, 4394, 4543, 4548, 4574, 4594, 4687, 4769, 4782, 4798, 4816,
4969, 5000, 5111, 5115, 5208, 5242, 5395, 5426, 5446, 5454, 5537, 5539,
5672, 5821, 5852, 5963, 5967, 6060, 6076, 6094, 6396, 6420, 6429, 6440,
6550, 6568, 6572, 6959, 6960, 7178, 7198, 7385, 7402, 7578, 7604, 7793,
7812, 7828, 7999, 8143, 8145, 8272, 8276, 8425, 8476, 8569, 8571, 8664,
8680, 8856, 8882, 8902, 8910, 8995, 9090, 9124, 9128, 9277, 9308, 9328,
9421, 9516, 9532, 9703, 9849, 9923, 9942, 9980, 10129, 10134, 10349,
10384, 10406, 10586, 10606, 10699, 10701, 10794, 10828, 10832, 10986,
11125, 11220, 11236, 11254, 11407, 11438, 11549, 11553, 11646, 11680,
11833, 11864, 11884, 11892, 11975, 11977, 12110, 12259, 12290, 12401,
12405, 12498, 12514, 12532, 12827, 12834, 12858, 12867, 12872.
```

The hashed machine-readable source is
`scratch/k16_upper12874_delete_basins_le4_20260730.tsv`.

## 3. Proof of the survivor-facet statement

Let the second edited site be `q`.  If `T` is a hole of `Z`, any witness of
`T` in the final word must contain `q`; an interval avoiding `q` is unchanged
from `Z`.  Such a witness contains the new cell `y`, so `y subseteq T`.
This proves (1.1).  If `b in y`, no target omitting `b` can contain `y`, so
no such target is a hole of `Z`; hence `Z` covers `F_b`.

Conversely, a bit `b` belongs to `J(Z)` exactly when every hole contains
`b`, which is exactly the assertion that no hole lies in `F_b`.  This proves
the stated equivalence.  It is an equivalence for nonzero debt intersection,
not a sufficient condition for a completing second edit.

There is an exact block form.  Split `Z` at all cells containing `b`, and let
`B_1,...,B_s` be the maximal nonempty blocks of cells omitting `b`.  If
`Lang(B_i)` is the set of interval ORs within `B_i`, then

\[
       Z\text{ covers }F_b
       \quad\Longleftrightarrow\quad
       \bigcup_i Lang(B_i)=F_b.                          \tag{3.1}
\]

An interval whose OR omits `b` cannot cross a cell containing `b`, proving
both directions.  Equation (3.1) is collective: it does not say that one
block is itself universal.

Concatenating the blocks preserves all their internal witnesses, so their
concatenation is an ordinary 15-coordinate universal word.  In particular,

\[
       |\{i:b\notin Z_i\}|\ge\nu(15)=6438.              \tag{3.2}
\]

Thus every survivor bit occurs in at most `12873-6438=6435` cells of a
length-12,873 intermediate word.

For the full hierarchy, let `S=supp(y)` and choose nonempty `A subseteq S`.
Every target avoiding `A` fails to contain `y`, hence is already represented
in `Z`.  Split at cells meeting `A` and concatenate the remaining blocks.
The same argument gives (1.3).  Summing (1.3) over all `a`-subsets `A` of
`S`, and counting for each cell the subsets of `S` it avoids, gives (1.4).
These moment inequalities are the strongest deletion-independent incidence
coupling currently extracted from the survivor theorem.  They forget order
and are necessary, not sufficient.

For the fixed parent there is also an exact transport law.  Let `s` be the
surviving source index edited first and
`Z=(U minus U_d)[s<-x]`.  Then

\[
 N_A(Z)=N_A(U)
 -\mathbf1[U_d\cap A=\varnothing]
 -\mathbf1[U_s\cap A=\varnothing]
 +\mathbf1[x\cap A=\varnothing].                       \tag{3.3}
\]

Combining this identity with (1.3) is a cheap exact cut on `(d,s,x,S)`.
It transports the deletion-independent moment bound into every fixed-parent
repair fibre, but remains marginal: it does not prove the necessary targets
occur as consecutive interval ORs.

## 4. Exact first/second-column coupling

Fix deletion `d`, first site `p`, and bit `b`.  For a target `T`, let
`C^d_T(p)` be the OR of the maximal `T`-compatible suffix immediately left
of `p` and prefix immediately right of `p`, and put

\[
       I^d_T(p)=[T\setminus C^d_T(p),T].                 \tag{4.1}
\]

Let `V^d_p` be the covered targets whose every witness in `W^d` contains
`p`.  Define

\[
\begin{split}
 L_{d,p,b}&=\bigvee_{\substack{T\in H_d\cup V^d_p\\b\notin T}}
                    (T\setminus C^d_T(p)),\\
 U_{d,p,b}&=\bigcap_{\substack{T\in H_d\cup V^d_p\\b\notin T}}T.
                                                               \tag{4.2}
\end{split}
\]

The first values producing a `b`-facet-complete intermediate word form
exactly the Boolean interval `[L_{d,p,b},U_{d,p,b}]`.  The provider-first
domain is its intersection with

\[
       \bigcup_{h\in H_d} I^d_h(p).                     \tag{4.3}
\]

For an actual completion, orient a one-site provider first and choose
`b in y`, where `y` is the second value.  Then its first value lies in
(4.2)--(4.3).  In the resulting intermediate word `Z`, if
`R_Z(q)` denotes every target whose all witnesses cross `q`, then

\[
       R_Z(q)\subseteq\{T:b\in T\},\qquad
       b\in y\subseteq J_Z(q)=\bigcap_{T\in R_Z(q)}T.    \tag{4.4}
\]

Together with the exact through-site condition

\[
       R_Z(q)\subseteq\Gamma^Z_q(y),                    \tag{4.5}

where `Gamma` is the literal suffix/prefix OR language through `q`, these
relations are an exact two-column formulation.  They retain intervals
containing both edits and their nonadditive `x OR y` term.

## 5. Does this give a deletion-independent global coupling?

There are two answers.

**Yes, within one proposed repair.**  The same bit `b` belongs to the second
value, forces first-column coverage of every affected `b`-free target, and
forces every second-column demanded target into the star `{T:b in T}`.
This is a genuine deletion-independent 16-colour separator and the strongest
coupling exposed by the survivor index.

**Yes, as a shared fixed-parent automaton.**  For each target `T`, mark the
source cells contained in `T` and decompose them into maximal compatible
blocks.  Coverage, witness cores, service intervals, and every deletion
transition follow from this one target-first catalogue.  A target becomes a
hole after deleting `d` exactly when it has a unique full compatible block
and `d` uniquely carries some coordinate in that block.  Consequently one
target has at most `rank(T)` hole-producing deletions and

\[
       \sum_d |H_d|\le 16\,2^{15}=524288.               \tag{5.2}
\]

For the frozen parent the shared automaton exactly reconstructs all 116,073
hole incidences from 51,154 targets.  This genuinely removes repeated
per-deletion geometry and is useful for a fixed-parent all-deletion engine.
It is a data-structure coupling, not a constraint forcing different deletion
choices to consume a common resource.

**No, across alternative deletions.**  The literal domains in (4.2) depend
on all of

```text
H_d        original deletion holes,
V^d_p      deletion-specific witness cores,
C^d_T(p)   deletion-specific compatible seam contexts.
```

A candidate chooses one deletion; it is not required to make simultaneous
choices for other deletions.  Algebraically, the action family is a disjoint
union over `d`, with the existential bit chosen inside each deletion fibre.
The common set of 16 labels therefore gives a colouring, not a Hall or
capacity constraint across deletion rows.

The strongest tempting deletion-only shortcut is false.  If
`K_d=intersection H_d`, the authenticated D3 audit contains exactly 2,754
first actions for which

\[
       J(Z)\cap K_d=\varnothing.                         \tag{5.1}

The per-deletion counts are

```text
d=0:352, d=1:263, d=3:228, d=6389:1143,
d=6441:524, d=12871:127, d=12873:117.
```

Thus the survivor bit cannot be assigned from the original common-hole mask.
Newly ejected targets can determine a different common residual bit.

Across all 191 closed rows there are 23,251,836 first-provider actions;
22,304,824, or 95.9271517%, survive the nonzero debt-intersection test.  The
survivor index alone therefore removes only 947,012 actions.  The decisive
negative information in D4 comes from the deletion-specific second-site
context/target-core test, not from a scalar survivor capacity.

## 6. Exact remaining global `+1` gate

The facet formulation is potentially useful, but it is not a global
`nu(16)>=12874` proof.  Either of the following additional theorems would
make it global:

1. a normalization/proximity theorem placing every hypothetical universal
   length-12,873 word in a certified fixed-parent repair fibre; or
2. a source-independent strengthening of the collective facet/moment bounds
   (1.3)--(1.4), synchronized with the exact second-site condition, strong
   enough to contradict the length/waste ledger for every word.

Neither follows from D3 or D4.  Extending the finite census to D5 would only
enlarge the fixed-parent local ball and would not supply this missing global
coupling.  No D5 work is undertaken in this note.

## 7. Authentication

The exact membership and count extraction is independently frozen in

```text
scratch/threadD_audit_k16_d4_unified_survivor_star_20260731.py
scratch/threadD_k16_d4_unified_survivor_star_20260731.audit.json
```

The detailed structural proof is independently recorded in
`THREAD_D_K16_D4_SURVIVOR_FACET_COUPLING_20260731.md`.  The underlying D4
composition remains
`scratch/threadD_k16_upper12874_d4_radius2_20260731/independent.audit.json`.
The shared target-first source automaton is frozen in
`MATH_THEOREM_K16_ALL_DELETION_TARGET_BLOCK_AUTOMATON_20260731.md`.
