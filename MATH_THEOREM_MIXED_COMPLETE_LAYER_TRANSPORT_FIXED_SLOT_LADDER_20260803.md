# Mixed complete-layer transport lifts integrally on every fixed slot ladder

**Date:** 2026-08-03  
**Status:** unconditional fixed-bank theorem. No computation is used. The
result lifts a rank-level transport to an integral named Boolean
containment matching, and it iterates over already chosen time banks. It
does **not** choose the time bank of each named target and does not prove the
balanced named-flag theorem.

## 0. Verdict

Let several disjoint copies of complete Boolean layers form a lower bank
and an upper bank. There is a matching of every lower-bank vertex to a
distinct containing upper-bank vertex if and only if the corresponding
rank types admit the obvious scalar transportation matrix. Thus normalized
Boolean containment has no hidden named-set Hall cut on this face.

Iterating the result gives an integral owner-rooted path cover whenever all
time banks have been fixed in advance as disjoint unions of complete
layers. Every path has at most one target in each time bank, so a ladder of
`d` banks gives depth at most `d`.

The order of quantifiers is essential:

\[
 \boxed{
 \text{fixed complete-layer banks}
 \Longrightarrow \text{integral containment ladder};
 \qquad
 \text{choose each target's bank}
 \not\Longleftarrow \text{the same TU argument}.}
\]

The second assertion is audited in
`MATH_AUDIT_VARIABLE_SLOT_LAYERED_FLOW_NONTU_20260803.md`.

## 1. Rank-typed complete-layer banks

Fix an `n`-element ground set `U`. Let `I` and `J` be finite type sets. For
each `i in I`, prescribe a rank `s_i`, and make a disjoint labelled copy

\[
                 L_i=\{(i,S):S\in {U\choose s_i}\}.
\tag{1.1}
\]

For each `j in J`, prescribe a rank `t_j`, and make a disjoint labelled copy

\[
                 R_j=\{(j,T):T\in {U\choose t_j}\}.
\tag{1.2}
\]

The copies are formal: two types of the same rank still have disjoint
vertices. Join `(i,S)` to `(j,T)` when

\[
                         s_i<t_j,
                 \qquad S\subset T.                    \tag{1.3}
\]

Write

\[
                 N_i={n\choose s_i},
                 \qquad M_j={n\choose t_j}.             \tag{1.4}
\]

A **rank transport** is a nonnegative real matrix
`a=(a_(i,j))` such that

\[
\begin{aligned}
 a_{i,j}&=0 &&\text{unless }s_i<t_j,\\
 \sum_{j\in J}a_{i,j}&=N_i &&(i\in I),\\
 \sum_{i\in I}a_{i,j}&\le M_j &&(j\in J).
\end{aligned}                                           \tag{1.5}
\]

No integrality is required of the entries of `a`.

## 2. Exact mixed-complete-layer coupling

### Theorem 2.1 (rank transport lifts to named containment)

The inclusion graph (1.3) has a matching saturating
`L=sqcup_(i in I)L_i` if and only if a rank transport (1.5) exists.

### Proof

Suppose first that a saturating matching exists. Let `a_(i,j)` be the
number of its edges from `L_i` to `R_j`. Every vertex of `L_i` is matched,
every vertex of `R_j` is used at most once, and an edge can occur only under
the rank condition in (1.3). Hence these integer counts satisfy (1.5).

Conversely, fix any rank transport `a`. For an admissible pair of types
`(i,j)` and an inclusion `S subset T`, give the edge from `(i,S)` to
`(j,T)` weight

\[
 x_{(i,S),(j,T)}
 =\frac{a_{i,j}}
 {N_i{n-s_i\choose t_j-s_i}}.                          \tag{2.1}
\]

A fixed `(i,S)` has exactly
`binom(n-s_i,t_j-s_i)` neighbours of type `j`. Its outgoing
weight is therefore

\[
 \sum_j\frac{a_{i,j}}{N_i}=1.                           \tag{2.2}
\]

A fixed `(j,T)` contains `binom(t_j,s_i)` rank-`s_i` sets. Its incoming
weight from type `i` is

\[
 \frac{{t_j\choose s_i}a_{i,j}}
 {N_i{n-s_i\choose t_j-s_i}}
 =\frac{a_{i,j}}{M_j},                                  \tag{2.3}
\]

where the equality uses

\[
 {n\choose s_i}{n-s_i\choose t_j-s_i}
 ={n\choose t_j}{t_j\choose s_i}.                       \tag{2.4}
\]

Summing (2.3) over `i` gives incoming weight at most one by (1.5). Thus
`x` is a fractional matching saturating the complete lower shore. The
bipartite matching polytope is integral, so it contains an integral
matching saturating that shore. \(\square\)

### Remark 2.2 (what is and is not preserved)

The witness matrix `a` is used only to build a fractional matching. The
integral matching obtained from bipartite integrality need not have exactly
`a_(i,j)` edges in each type pair, even when all `a_(i,j)` are integers.
The theorem preserves the already fixed left and right banks, which is all
that an adjacent ladder interface needs. Preserving every internal
type-pair quota is an additional side-constrained matching problem and is
not asserted.

### Corollary 2.3 (separated unions of ranks)

Let

\[
 A=\bigcup_{s\in P}{U\choose s},
 \qquad
 B=\bigcup_{t\in Q}{U\choose t},
\]

with disjoint formal copies if a rank is repeated. If the scalar rank
transport from `P` to `Q`, supported on `s<t`, can send all of `A` into the
capacities of `B`, then the Boolean inclusion graph has a matching
saturating `A`.

In particular, when every `s in P` is below every `t in Q`, the sole scalar
condition is `|A|<=|B|`. This recovers and slightly generalizes the
separated-unions lemma in
`MATH_THEOREM_IDEAL_CHAINIZATION_NORMALIZED_LADDER_AND_SCD_FRAGMENTATION_GAP_20260801.md`.

## 3. A fixed mixed-layer ladder is integral

Let `A_0` be the complete owner layer `binom(U,r)`. For
`1<=h<=q`, let `A_h` be a bank of named targets which is a disjoint union
of complete-layer copies. Think of `A_1` as the marked time immediately
below the owner and `A_q` as the earliest marked time.

At interface `h`, join `X in A_h` to `Y in A_(h-1)` when `X subset Y`,
where members of `A_0` are owners. Assume that every interface has a
rank transport of the form (1.5) saturating `A_h`.

### Theorem 3.1 (fixed-bank owner-path ladder)

There are injections

\[
 m_h:A_h\longrightarrow A_{h-1}
 \qquad(1\le h\le q),
 \qquad X\subset m_h(X),                                \tag{3.1}
\]

and their union is a family of vertex-disjoint inclusion paths ending at
distinct rank-`r` owners. The paths cover every target in every bank and
contain at most `q` targets each.

### Proof

Apply Theorem 2.1 independently at each interface to obtain `m_h`. Orient
every chosen edge upward, from `A_h` to `A_(h-1)`. Every target has exactly
one upward edge. Injectivity says that it has at most one downward child.
The bank index strictly decreases along upward edges, so directed cycles
are impossible. The components are therefore disjoint paths, each ending
at a different member of `A_0`. There is at most one target from each of
the `q` target banks on a path. \(\square\)

Unused owners are empty paths. Consequently the theorem gives exactly
`W=binom(n,r)` owner particles if empty paths are counted.

### Corollary 3.2 (safe deletion after coupling)

After constructing the ladder, delete any prescribed named targets from
the banks. The retained members of every path remain an inclusion flag,
owner distinctness is unchanged, and all loads weakly decrease. Thus the
theorem also handles arbitrary boundary deletion **after** a suitable
complete-layer ladder has been found.

## 4. Why this does not choose the time banks

For a simple Boolean target family, each named set occurs once. If a
rank-`s` layer is divided among several times, none of those pieces is a
complete-layer copy. Theorem 2.1 then supplies no normalized Hall
inequality for the pieces.

One may restore symmetry fractionally by putting a fraction of every
rank-`s` target into every proposed time. But integralizing those fractions
requires constraints

\[
                 \sum_{h=1}^{q}z_{S,h}=1
                 \qquad\text{for every named target }S, \tag{4.1}
\]

simultaneously with the path-flow constraints. Equations (4.1) are not
rows of the original network matrix. They are exactly the target-to-time
correlation audited in the companion note.

Assigning every complete rank wholly to one time avoids (4.1), but it is
quantitatively too rigid for the optimal depth: consecutive complete-rank
blocks have the positive `Theta(sqrt(k))` toll proved in the normalized-
ladder theorem. The mixed-complete-layer coupling removes named-set Hall
cuts only after the banks are fixed; it does not remove the bank-selection
gate.

## 5. Proof-safe relation to the four 2026-08-03 inputs

1. The noncontiguous rank-law theorem chooses exact abstract rank patterns,
   but not named time banks.
2. The rank-separated matroid-intersection theorem assigns named targets
   to containing owner/rank ports, but not to nested owner paths.
3. The canonical configuration theorem gives the symmetric fractional
   point after a pattern schedule is fixed, but does not round that
   hypergraph matching; a frozen saturated prechainization has linear
   deficiency.
4. The cross-SCD sparse-top theorem lies on the fixed-bank face of Theorem
   3.1: its residual and socket banks are complete-layer indexed and one
   ordinary containment matching couples them.

Accordingly, Theorems 2.1 and 3.1 are a genuine positive extension of the
known normalized coupling, but they do not prove an integral `W`-path cover
for the adaptively mixed nonboundary target bank.
