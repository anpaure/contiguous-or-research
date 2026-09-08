# Native lower-q1 repair for the split-core pivot, and two-address minimality

Date: 2026-08-01  
Lane: protected pivot / literal source compiler  
Status: unconditional local repair.  The four lower-q1 deficits in the
original split-core factorization are not forced by the owner path.  They can
all be removed inside the existing `4h+1` source positions, without changing
the owner row, insertion charge, old-to-new deck transport, pivot rays,
residence, or either set-valued q1 palette.  No external occurrence is needed
for those four lower-q1 colours.  A preassigned target-labelled compiler on
the *unrepaired* source does not automatically transport and must be
reoptimized.

## 1. The source and its four deficits

Use the notation of
`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md`.
Thus

\[
 B=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,
 \qquad x_L\in X_L,\quad x_R\in X_R,
\]

and

\[
 B^-=(B-\{x_R\})\cup\{q^-\},\qquad
 B^+=(B-\{x_L\})\cup\{q^+\}.
\]

Index the `4h+1` source letters from `0` to `4h`.  The inserted letter `X`
is at position `2h`.  The four relevant old letters are

\[
\begin{array}{c|c}
 p& A_p\\ \hline
 h-1 &(X_R-\{x_R\})\cup\{q^-\},\\
 2h-1&C\cup X_L\cup\{\lambda_h\},\\
 2h+1&C\cup X_R\cup\{\rho_1\},\\
 3h+1&(X_L-\{x_L\})\cup\{q^+\}.
\end{array}                                                \tag{1.1}
\]

The depth-`h` owner row is

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}.
                                                               \tag{1.2}
\]

At four transitions, the union of the `h` shared source letters misses,
respectively,

\[
 C\cup X_L,qquad X_R-\{x_R\},qquad
 X_L-\{x_L\},qquad C\cup X_R.                 \tag{1.3}
\]

The first and fourth sets are always nonempty; the middle two vanish when
the corresponding split shore is a singleton.

## 2. A legal-enlargement lemma

Let `V_0,...,V_n` be a fixed depth-`h` row of a source
`A_0,...,A_(n+h)`, so

\[
                    V_i=\bigcup_{p=i}^{i+h}A_p.          \tag{2.1}
\]

For a source position `p`, put

\[
 E_p=\bigcap_{\max(0,p-h)\le i\le\min(n,p)}V_i.          \tag{2.2}
\]

### Lemma 2.1 (legal enlargement)

Replacing `A_p` by any `A'_p` with

\[
                         A_p\subseteq A'_p\subseteq E_p  \tag{2.3}
\]

leaves every owner `V_i` unchanged.  If the old shared-letter union at an
edge `V_iV_(i+1)` already equals `V_i cap V_(i+1)`, it remains equal after
any collection of legal enlargements.

#### Proof

A source position `p` belongs exactly to the owner windows indexed in
(2.2), and every newly added coordinate belongs to all of those owners.
Thus no owner union grows.  A shared union can only grow, and every legal
addition to one of its positions lies in both adjacent owners.  If it was
already their full intersection, its set value cannot change.  \(\square\)

This is the coordinatewise maximal-envelope principle specialized to a
fixed owner row.

## 3. Four-letter repair with no native q1 sidecar

Replace the four letters in (1.1) by

\[
\begin{array}{c|c}
 p& \widetilde A_p\\ \hline
 h-1 &B^-=(B-\{x_R\})\cup\{q^-\},\\
 2h-1 &(B-\{x_R\})\cup\{\lambda_h\},\\
 2h+1 &(B-\{x_L\})\cup\{\rho_1\},\\
 3h+1 &B^+=(B-\{x_L\})\cup\{q^+\}.
\end{array}                                                \tag{3.1}
\]

All other source letters, including `A_(2h)=X`, are unchanged.

### Theorem 3.1 (native literal-q1 repair)

For every `h>=2` under the ordinary split-core hypotheses, the repaired
source has all of the following properties.

1. Its depth-`h` row is still exactly (1.2).
2. At every owner transition, the union of the `h` shared source letters is
   exactly the owner intersection.  Thus the complete lower q1 palette is
   literal at its native addresses.
3. Every immediate upper colour remains literal, and both set-valued q1
   palettes remain injective.
4. Deleting and reinserting the one letter `X` preserves every old interval
   OR in arbitrary fixed exterior context.
5. The `h` pre-insertion crossing depth cells remain

   \[
       U_j=M_j\cup M_{j+1},\qquad0\le j<h,
   \]

   and the new strict-lower cells remain exactly `X` and the two original
   complete pivot rays.
6. The owner-level residence ledger, clipped endpoint flags, coordinate
   support, source length, and insertion charge are unchanged.

#### Proof: owner row

The additions at the four positions are

\[
 C\cup X_L,quad X_R-\{x_R\},quad
 X_L-\{x_L\},quad C\cup X_R.                 \tag{3.2}
\]

The owner windows containing position `h-1` are exactly
`L_0,...,L_(h-1)`, all of which contain `B^-`.

The owner windows containing position `2h-1` are

\[
 L_{h-1},M_0,\ldots,M_{h-1},
\]

and all contain `B-{x_R}`.  Symmetrically, the windows containing position
`2h+1` are

\[
 M_1,\ldots,M_h,R_0,
\]

and all contain `B-{x_L}`.  Finally, the windows containing `3h+1` are
exactly `R_0,...,R_(h-1)`, all containing `B^+`.

Hence all four changes satisfy Lemma 2.1 and the owner row is unchanged.

#### Proof: lower and upper q1 cells

At the four formerly deficient edges, the repaired shared unions are

\[
\begin{aligned}
 B^-\cup\lambda[1,h-1]
   &=L_{h-2}\cap L_{h-1},\\
 (B-\{x_R\})\cup\lambda[1,h]
   &=L_{h-1}\cap M_0,\\
 (B-\{x_L\})\cup\rho[1,h]
   &=M_h\cap R_0,\\
 B^+\cup\rho[2,h]
   &=R_0\cap R_1.
                                                        \tag{3.3}
\end{aligned}
\]

Every other shared union was already tight and stays tight by Lemma 2.1.
The owner row itself is unchanged, so its lower and upper transition
colours remain separately injective.  The OR of the `h+2` letters spanning
two owner windows is still their union, proving literal upper q1.

#### Proof: monotone insertion and the short-cell ledger

The two repaired old letters adjacent to the inserted position are

\[
 (B-\{x_R\})\cup\{\lambda_h\},\qquad
 (B-\{x_L\})\cup\{\rho_1\}.                            \tag{3.4}
\]

Since `x_L` and `x_R` are distinct,

\[
 (B-\{x_R\})\cup(B-\{x_L\})=B\supseteq X.             \tag{3.5}
\]

Thus every old interval crossing the cut already contains `X`; insertion
does not change its OR.  Intervals away from the cut transport identically.
This proof is independent of exterior letters.

For a new interval of source length at most `h` ending at `X`, the only
repaired letter it can meet is the position `2h-1` letter.  Its added set
`X_R-{x_R}` is already contained in `X`, so the value remains

\[
                B\cup\lambda[h-i+1,h].
\]

The right ray is symmetric because `X_L-{x_L}` is already in `X`.
Positions `h-1` and `3h+1` lie outside every such short interval.  Hence
the singleton and both rays are unchanged.  Equation (3.5), or the standard
crossing-window identity, also leaves every `U_j` unchanged.

Since the owner row did not change, neither did any owner-coordinate run,
q1 collision signature, endpoint flag, or support count.  All repaired
letters are nonempty.  The argument uses no range that disappears at
`h=2`, so the boundary case is included.  \(\square\)

## 4. A two-address repair and its sharp address lower bound

There is a smaller repair if changing singleton source letters is allowed.
Replace only

\[
 \{\lambda_1\}\longmapsto
       (B-\{x_R\})\cup\{\lambda_1\}                    \tag{4.1}
\]

at source position `h`, and

\[
 \{\rho_h\}\longmapsto
       (B-\{x_L\})\cup\{\rho_h\}                      \tag{4.2}
\]

at position `3h`.

The first position belongs exactly to the owner windows
`L_0,...,L_(h-1),M_0`, whose intersection contains `B-{x_R}` and
`lambda_1`.  It lies in both deficient left shared ranges and its added core
is the union of the two left deficits.  The right statement is symmetric.
Thus Lemma 2.1 proves the same conclusions as Theorem 3.1.  These positions
also lie outside every new source interval of length at most `h` containing
`X`, so the pivot rays remain unchanged.

### Theorem 4.1 (two addresses are necessary and sufficient)

Among repairs obtained by enlarging existing source letters while retaining
the fixed owner row, two modified source addresses are necessary and
sufficient to make all native lower q1 cells literal.

#### Proof

The always-nonempty left deficit at `L_(h-2)L_(h-1)` can be supplied only
from its shared source range

\[
                         [h-1,2h-2].                    \tag{4.3}
\]

The always-nonempty right deficit at `R_0R_1` can be supplied only from

\[
                         [2h+2,3h+1].                   \tag{4.4}
\]

These ranges are disjoint for every `h>=2`; hence at least two source
positions must change.  Equations (4.1)--(4.2) achieve the bound. \(\square\)

The four-letter repair (3.1) is nevertheless often preferable: it does not
enlarge any of the displayed lambda/rho singleton letters.  It repairs one
deficit at each adjacent non-singleton seam address instead of merging the
two repairs on each shore.

## 5. Exact compiler and deck scope

Theorem 3.1 proves zero **native lower-q1** sidecar: all four owner
intersections now occur at their own shared cells.  It also proves

\[
 \operatorname {Deck}(A_{\rm repaired}^{-})
       \subseteq
 \operatorname {Deck}(A_{\rm repaired}^{+}),           \tag{5.1}
\]

where `+` inserts `X` and `-` deletes it.

Two address identities must be retained in an exact compiler ledger:

\[
             P_{h-1}=M_0\cap M_1=I_0,
 \qquad      S_{h-1}=M_{h-1}\cap M_h=I_{h-1}.           \tag{5.1a}
\]

Thus each longest pivot ray and the corresponding central lower-q1 target
are one target at one physical cell, not two capacities or two assignments.
The native repair does not duplicate them.

It does not assert

\[
 \operatorname {Deck}(A_{\rm unrepaired})
       \subseteq
 \operatorname {Deck}(A_{\rm repaired}).               \tag{5.2}
\]

Indeed, enlarging a source letter can destroy its former one-letter cell
value and other intervals using it.  In the two-address repair, the local
singleton occurrences `{lambda_1}` and `{rho_h}` disappear.  In the
four-letter repair, every genuinely enlarged letter loses its old
one-letter value locally; the number of such letters is

\[
 2+\mathbf1_{|X_R|>1}+\mathbf1_{|X_L|>1}.               \tag{5.3}
\]

The special labels `q^-`, `lambda_h`, `rho_1`, and `q^+` show directly
that these old one-letter values are not reproduced by an interval through
the corresponding enlarged letter.  Additional unrepaired-to-repaired deck
losses are not excluded.

Consequently a target-labelled compiler fixed before this redesign does not
transport automatically.  There are two proof-safe uses.

1. **Joint scaffold design.**  Build the pre-insertion source and its
   reference compiler using the repaired letters from the outset.  Then
   (5.1), the unchanged pivot rays, and the now-literal q1 cells are the
   relevant invariants.  No external occurrence is required for the four
   q1 colours.
2. **Retrofitting a frozen compiler.**  Recompute or externally reassign
   every old target whose selected occurrence used an interval changed by
   the repair.  Scalar capacity alone does not prove that this matching
   exists.  The two-address theorem shows that at least two source cells
   must change, but it is not a claim that exactly two target occurrences
   suffice for every frozen compiler.

Thus the former four-q1-host requirement is removed from the local packet.
What remains is a global target/cell matching for the redesigned scaffold,
not a native lower-q1 realization problem.

## 6. Updated frontier

The split-core pivot now has, in one literal source:

* the same simple resident owner path;
* both immediate palettes injective and literal;
* the same one-letter `X` insertion and zero old-to-new OR damage;
* the same rank-`r+1` pre-insertion block;
* the same singleton and two strict-lower rays; and
* no native lower-q1 sidecar.

The remaining global theorem is still the protected upper-exact Catalan
Hamilton-path/source completion with one common redesigned compiler,
exterior flag continuation, arbitrary-width upper witnesses, and bounded
regeneration.  This note removes the four lower-q1 deficits from that list;
it does not prove a universal `B+1` word or `B+O(1)` construction.
