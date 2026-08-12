# A coatom fan contains canonical diamond witnesses and their native sockets

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local literal construction.  One phase-common
coatom block has an explicit optimal depth-`d` inverse containing `d-1`
canonical prefix/suffix diamonds and `d-1` pairwise capacity-disjoint
native owner--q1 socket pairs.  The complete local polarized bundles are
therefore materialized before type acceptance.  Embedding the two inverse
halos in the full packet chronology, external cap acceptance, and
regeneration remain open.

## 0. Coatom block

Let `d>=2`, put `n=d+2`, take a nonempty core `C`, and let

\[
                         F=\{f_0,\ldots,f_{n-1}\}
\tag{0.1}
\]

be disjoint from `C`.  Put

\[
 Z=C\cup F,
 \qquad O_i=Z\setminus\{f_i\}\quad(0\le i<n).
\tag{0.2}
\]

In the mixed-coatom tensor, `C=K union V` and
`(O_0,...,O_(n-1))` is exactly the coatom block `B(V)`.  At any of the four
phase-identical active positions, this owner block is pointwise common to
the two tensor phases.

## 1. An explicit optimal inverse

Define a source word of length `2d+2` by

\[
 A_p=C\cup\{f_{(p+1)\bmod n}\},
                         \qquad 0\le p\le2d+1.
\tag{1.1}
\]

The residue sequence in (1.1) is

\[
 f_1,f_2,\ldots,f_{d+1},f_0,f_1,\ldots,f_d.
\tag{1.2}
\]

### Theorem 1.1 (literal coatom rotor inverse)

For every `0<=i<n`,

\[
                         \bigcup_{p=i}^{i+d}A_p=O_i.
\tag{1.3}
\]

Hence

\[
                         D^dA=(O_0,\ldots,O_{n-1}).
\tag{1.4}
\]

The source length is exactly `n+d=2d+2`, and every letter is nonempty.

#### Proof

The `d+1=n-1` consecutive residues

\[
                         i+1,i+2,\ldots,i+d+1\pmod n
\]

run through every member of `Z/nZ` except `i`.  Their source union is
therefore `C union (F-{f_i})=O_i`.  Nonemptiness follows from the fixed
nonempty core.  \(\square\)

## 2. Native interval diamonds

For `0<=i<n-1`, define the four physical interval addresses

\[
\begin{aligned}
 p_i&=[i+1,i+d],&
 o_i&=[i,i+d],\\
 o_{i+1}&=[i+1,i+d+1],&
 q_i&=[i,i+d+1].
\end{aligned}
\tag{2.1}
\]

### Theorem 2.1

The addresses in (2.1) form the literal Boolean diamond

\[
\begin{aligned}
 \operatorname{OR}_A(p_i)&=Z\setminus\{f_i,f_{i+1}\}=:L_i,\\
 \operatorname{OR}_A(o_i)&=O_i,\\
 \operatorname{OR}_A(o_{i+1})&=O_{i+1},\\
 \operatorname{OR}_A(q_i)&=Z.
\end{aligned}
\tag{2.2}

Thus both source--owner--q1 routes

\[
 p_i\longrightarrow o_i\longrightarrow q_i,
 \qquad
 p_i\longrightarrow o_{i+1}\longrightarrow q_i
\tag{2.3}
\]

are literal interval-containment chains and Boolean Hasse chains.

#### Proof

The owner identities are Theorem 1.1.  The length-`d=n-2` residue interval
for `p_i` contains every filler label except the two consecutive labels
`f_i,f_(i+1)`.  The length-`d+2=n` residue interval for `q_i` contains every
filler label.  Address containment in (2.1) is immediate.  The ranks differ
by one at each step, proving the Hasse assertion.  \(\square\)

## 3. The canonical antidiagonal witnesses already occur

For every `1<=j<d`, put

\[
 X_j=C\cup\{f_1,\ldots,f_j\},
 \qquad
 Y_j=C\cup\{f_{j+1},\ldots,f_d\},
 \qquad
 U=C\cup\{f_1,\ldots,f_d\}.
\tag{3.1}
\]

These are the canonical diamond values

\[
                         X_j\cap Y_j=C,
 \qquad X_j\cup Y_j=U.
\tag{3.2}

Define their addresses by

\[
 x_j=[d+2,d+j+1],
 \qquad
 y_j=[j,d-1].
\tag{3.3}

### Theorem 3.1 (literal antidiagonal bank)

For all `1<=j<d`,

\[
                         \operatorname{OR}_A(x_j)=X_j,
 \qquad \operatorname{OR}_A(y_j)=Y_j.
\tag{3.4}

The `2(d-1)` addresses in (3.3) are pairwise distinct.  They are also
distinct from every native port, owner, and q1 address in (2.1), because
their lengths are at most `d-1`, whereas those three address types have
lengths `d,d+1,d+2`.

#### Proof

On the right half of (1.2), positions `d+2,...,d+j+1` carry exactly
`f_1,...,f_j`.  On the left half, positions `j,...,d-1` carry exactly
`f_(j+1),...,f_d`.  Prefix addresses are nested at the right, suffix
addresses are nested at the left, and the two position ranges are disjoint,
so all addresses are distinct.  The length comparison proves the final
claim.  \(\square\)

Physical intervals may overlap in source positions without competing for
capacity: the OR-word occurrence model assigns capacity to interval
addresses, not to every singleton position contained in an interval.

## 4. Deterministic complete bundle bank

For ticket `j`, `1<=j<d`, choose the all-left native route at turn
`i=j-1` and form the occurrence record

\[
 \mathcal B_j=(x_j,y_j; p_{j-1},o_{j-1},q_{j-1}).
\tag{4.1}
\]

It contains exact upstream witnesses of the two incomparable values
`X_j,Y_j`, together with the native nested occurrence pair

\[
 \operatorname{OR}_A(o_{j-1})=O_{j-1}
                         \subset Z=\operatorname{OR}_A(q_{j-1}).
\tag{4.2}

### Theorem 4.1 (capacity-disjoint canonical socket bundles)

The `d-1` records in (4.1) are pairwise disjoint in every finite occurrence
coordinate.  Therefore, in any one cap/phase/guard state which accepts the
polarized native code for these records, they instantiate `d-1`
simultaneous canonical two-coordinate tickets with no additional word
cell.

#### Proof

Theorem 3.1 makes all upstream coordinates distinct and separates them by
address length from the native coordinates.  The selected ports
`p_0,...,p_(d-2)`, owners `o_0,...,o_(d-2)`, and q1 cells
`q_0,...,q_(d-2)` are separately injective.  The three native address
families have different lengths.  Thus all finite occurrence coordinates
in different records are disjoint.

Equations (3.2) and (4.2) supply respectively the exact Boolean diamond and
the native nested pair.  The deterministic polarized-socket theorem now
applies under the stated state-aware acceptance premise.  \(\square\)

The construction is stronger than raw terminal replication: the upstream
literal target witnesses and the downstream native socket pairs occur in
one explicit source word, already paired by `j`.

## 5. Phase stability

If `V` is one of the four phase-identical active blocks of the mixed-coatom
tensor, then the owner block (0.2) is identical at the same addresses in
both phases.  The source word (1.1) depends only on that common block data.
Hence the entire local bundle bank (4.1) has a common realization in both
phases, with the same values and relative addresses.

This is a local common inverse.  It does not yet prove that the ambient
source word of the complete `12d+35`-owner packet restricts to (1.1).

## 6. Exact halo gate

The inverse (1.1) uses `d` source positions to the left and `d` to the right
of the central part of the owner block.  In a longer depth-`d` chronology,
those positions also participate in neighbouring owner windows.  Replacing
them by (1.1) is therefore legal at zero extra length only if the two halo
words satisfy all neighbouring reconstruction equations.

Accordingly the local theorem leaves exactly these physical rows open:

1. **ambient halo planting:** embed (1.1) in the full packet inverse without
   changing the adjacent owners;
2. **complete cap acceptance:** accept the polarized code and all guards for
   the already paired records (4.1);
3. **background coexistence:** keep the transported compiler matching
   disjoint from the displayed occurrence coordinates; and
4. **whole-host regeneration:** preserve or recreate the packet slot in the
   next recursive state.

No source, owner, q1, address-count, or native terminal-multiplicity problem
remains inside the isolated block.

## 7. Dependencies

- `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`
- `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
- `MATH_THEOREM_COATOM_FOUR_FAN_OCCURRENCE_SOCKET_REPLICATION_20260804.md`

