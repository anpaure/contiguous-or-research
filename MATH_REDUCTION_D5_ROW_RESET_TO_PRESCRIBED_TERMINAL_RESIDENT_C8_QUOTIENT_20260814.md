# The resident complementary-square C8 closes the abstract D5 row reset; prescribed terminals remain

**Date:** 2026-08-14
**Status:** exact reduction from the frozen D5 three-state gate to a
prescribed-terminal embedding problem.  It reuses an independently audited
resident all-width actuator.  It does not claim that its private sockets have
already been identified with the D5 occurrences.

## 0. Outcome

The frozen D5 union graph has 477 changed rows.  Its proper three-colouring
splits them into 265 pass rows and 212 reset rows.  At a reset row the tail
has state `a` and the old/new heads have the other states `b,c`; the required
local action is

\[
                         1_a\times(b\ c).             \tag{0.1}
\]

The complementary-square C8 of
`MATH_THEOREM_COMMON_MATE_C8_COMPLEMENTARY_SQUARE_RESIDENT_ALLWIDTH_HOST_20260813.md`
already realizes `(b c)` on two alternating marked first-return sockets.
Its two states have one simple owner/lower/upper bank, are two-sided
resident, and have zero owner-union current at every width.  An untouched
spectator wire supplies `1_a`.

Thus no new abstract odd switchbox, serial C8--C6 tube, or tag clock is
needed for the row-private route.  The remaining rows are exactly:

1. identify the private marked C8 sockets and spectator with each prescribed
   D5 tail/head occurrence triple;
2. repair the exact four-target lower/intersection q2 deficit and audit every
   graft-crossing collar;
3. make all 212 occurrence embeddings owner/lower/upper compatible, including
   the three external roles of multiplicity four.

## 1. Exact marked-socket action

In the complementary-square theorem, the old bank is four closed protected
cycles with incoming sockets `R_0,R_1,R_2,R_3`.  Before the switch every
socket first returns to itself.  After the C8 switch the four-socket return
map is

\[
                          i\longmapsto i+1\pmod4.     \tag{1.1}
\]

Mark only the alternating sockets

\[
                              R_0,R_2.                \tag{1.2}
\]

Under `(1.1)`, the first marked socket encountered after `R_0` is `R_2`,
and conversely.  Hence the marked first-return maps are

\[
             \mathrm{id}_{\{R_0,R_2\}}\quad\hbox{and}\quad(R_0\ R_2)
                                                               \tag{1.3}
\]

in the pass and switched states.  Relabel `R_0,R_2` as `b,c` and take the
direct sum with a fixed spectator `a`.  Equation `(1.3)` becomes exactly
`(0.1)`.  The inverse uses the same bank because the C8 matching switch is
an involution.

This is a literal first-return quotient, not an assignment of an abstract
odd sign.  It also explains why a single C8 suffices here although a
full four-port outer permutation fixing both `a` and a dummy would require
an additional even router.

## 2. Interface ledger

The audited complementary-square theorem gives the following exact ledger.

| D5 reset requirement | complementary-square C8 |
|---|---|
| same owner bank in pass/swap | proved |
| same immediate-lower bank | proved and simple |
| same immediate-upper bank | proved and simple |
| old and switched residence | two-sided through the chosen depth |
| head transposition | literal marked first-return transposition `(1.3)` |
| upper/union q2 support | zero current at every owner-window width |
| lower/intersection q2 support | four singleton losses; exact current below |
| prescribed D5 terminal identity | not proved |
| graft-crossing collars/current | not proved |

The distinction in the last three rows is load-bearing.  Equality of the
immediate-lower palette controls width one; it does not by itself identify
the intersections of consecutive lower-owner windows after a graft.
Likewise, a private isomorphic socket is not yet the named D5 occurrence.

### Theorem 2.1 (exact lower-q2 current)

Use the notation of the complementary-square theorem, with indices modulo
four.  Let `S_i=G_(i,n-2)` be the owner preceding `R_i`, and let `F_(i,1)`
be the first forward owner after `U_i`.  Put

\[
\begin{aligned}
 A_i^-&=(C-t_i)+q_i+q_{i+1},\\
 A_i^+&=(C-t_i)+q_{i+1}+q_{i+2},\\
 B_i&=(C-c_{i+1})+q_i+q_{i+1}.
\end{aligned}                                      \tag{2.1}
\]

The two old lower triple-intersections meeting the switched incidence are

\[
 S_i\cap R_i\cap U_i=A_i^- ,\qquad
 R_i\cap U_i\cap F_{i,1}=B_i,                     \tag{2.2}
\]

whereas the new ones are

\[
 S_i\cap R_i\cap U_{i+1}=A_i^+ ,\qquad
 R_i\cap U_{i+1}\cap F_{i+1,1}=B_{i+1}.           \tag{2.3}
\]

Consequently the complete signed lower-q2 occurrence current is

\[
                 \sum_{i=0}^3([A_i^+]-[A_i^-]).    \tag{2.4}
\]

The `B` family cancels by cyclic reindexing.  The eight `A` values are
distinct.  Moreover, in the displayed closed bank every `A_i^-` has old
load one and new load zero.  Thus the C8 loses exactly four lower-q2
support values and creates four.

#### Proof

The terminal formulas give

\[
 S_i=(C-t_i)+d_i+q_i+q_{i+1}+q_{i+2},
\]

while `F_(i,1)` deletes `c_(i+1)` from `U_i` and inserts `z_0`.
Intersecting gives `(2.2)--(2.3)`.  Summation proves `(2.4)`.

For the support statement, a triple intersection equal to some `A_i^+` or
`A_i^-` must contain `|C|-1` core labels and no `a` or `Z` label.  Away from
the two endpoint neighbourhoods of a path, every window either contains a
neutral label in its intersection or misses at least two core labels.
Direct intersection of the terminal triples gives only the following
candidates with the required signature:

\[
\begin{aligned}
 D_i&=(C-t_i)+q_i+q_{i+2},\\
 A_i^-&=(C-t_i)+q_i+q_{i+1},\\
 B_i&=(C-c_{i+1})+q_i+q_{i+1}.
\end{aligned}                                      \tag{2.4a}
\]

The active pair distinguishes these families and the missing core label
distinguishes their indices.  In the switched concatenation, the `D_i`
family is copied, the `B_i` family is cyclically permuted, and `A_i^-` is
replaced by `A_i^+`.  Hence `(2.2)` is the unique old witness of `A_i^-`
and none survives.  The same enumeration proves the four births. \(\square\)

This is a constant defect, not a new growing-width obstruction.  A valid
D5 box needs four literal lower-q2 backups in addition to its prescribed
terminal connectors.

### Theorem 2.2 (four explicit resident backup cycles)

The four losses in Theorem 2.1 admit a fixed resource-simple repair inside
the same ground set.  Put

\[
 K_i=A_i^--c_0,qquad
 \sigma_i=(c_0,a,q_{i+2},q_{i+3},z_0,z_1,z_2),     \tag{2.5}
\]

and let indices on the seven entries of `sigma_i` be cyclic.  Define the
seven-owner tight cycle

\[
 \mathcal B_i=\bigl(K_i+\sigma_{i,r}+\sigma_{i,r+1}
                         +\sigma_{i,r+2}:r\in\mathbb Z_7\bigr). \tag{2.6}
\]

Then:

1. the four cycles have 28 distinct owners, 28 distinct immediate-lower
   facets, and 28 distinct immediate-upper colours;
2. those three banks are disjoint from the complementary-square bank;
3. the owner, lower, and upper coordinate traces have nonconstant cyclic
   run/gap pairs `(3,4)`, `(2,5)`, and `(4,3)`, respectively; and
4. `A_i^-` is one lower triple intersection on \(\mathcal B_i\).

Keeping all four cycles unchanged in both states therefore restores every
old lower-q2 support value while adding zero signed current.

#### Proof

Consecutive 3-windows of a cyclic 7-set overlap in 2 points and have union
of size 4, proving the Johnson-cycle assertion and the three run pairs.  The
intersection of three consecutive 3-windows is one point.  Taking that point
to be `c_0` gives

\[
                         K_i+c_0=A_i^- .             \tag{2.7}
\]

For simplicity, intersect a displayed resource first with `C`.  It misses
`t_i` and misses `c_0` precisely when the corresponding cyclic window does
not contain `c_0`.  Thus resources from distinct `i` are separated by their
missing `t_i`; resources with the same `i` are separated by their cyclic
window in `sigma_i`.  The same argument after taking a consecutive
2-window or 4-window proves lower- and upper-bank simplicity.

Disjointness from the main bank follows from the finite signature

\[
 (|V\cap C|,|V\cap Q|,{\bf1}_{a\in V},|V\cap Z|,
                         V\cap\{z_0,z_1,z_2\}).      \tag{2.8}
\]

Along `(2.6)` its seven owner rows are respectively

```text
(|C|-1,3,1,0), (|C|-2,4,1,0), (|C|-2,4,0,1),
(|C|-2,3,0,2), (|C|-2,2,0,3), (|C|-1,2,0,2),
(|C|-1,2,1,1).
```

The main forward path deletes core labels in its fixed cyclic order while
inserting `Z`, and changes active labels only in its last two steps; the
return path reverses these roles and has the three explicit tail states
from equation `(1.15)` of the complementary-square theorem.  Comparing
the seven rows above leaves only the last signature.  There the main owner
would have to be `U_i-c_(i+1)+z_0`, whereas `(2.6)` misses `t_i=c_(i+q)`;
these differ because `q>=5`.  The consecutive 2-window and 4-window versions
of the same table give the lower and upper claims.  Hence all three banks
are disjoint. \(\square\)

The four backup cycles add only 28 owners and have exposure bounded by a
constant.  They close the internal lower-q2 row of the abstract C8 quotient;
only the prescribed terminal connectors and their crossing windows remain.

## 3. Quantitative simultaneous-host row

One complementary-square bank at ambient semilength `M` has

\[
              e_M=16M-16,\qquad \alpha_M,\beta_M\le8. \tag{3.1}
\]

Suppose the 212 prescribed copies, including their four-target backup
packets, have first been embedded as one vertex-disjoint protected bank,
with only the declared occurrence coalescences.  Assume the added connectors
and backups together have `O(M)` incidences and `O(1)` exposure.  Then
conservatively

\[
 e_M\le212(16M-16)+O(M)=O(M),\qquad
 \alpha_M,\beta_M\le212\cdot8+O(1)=O(1).           \tag{3.2}
\]

Consequently

\[
                 e_M=2^{o(M)},\qquad
                 \alpha_M=o(M),\qquad
                 \beta_M=o(M).                    \tag{3.3}
\]

The subexponential low-exposure coinstantiation theorem would then place
the whole phased bank in one spanning middle-levels two-factor.  Thus
ordinary factor completion is not an additional asymptotic obstacle after
the literal joint embedding is constructed.

Equation `(3.2)` is conditional: it prices a completed disjoint bank; it
does not prove that arbitrary prescribed D5 sockets admit those 212
embeddings.  The latter is an occurrence-level linkage problem.

## 4. Exact prescribed-terminal gate

The C8's two marked owners have the special form

\[
\begin{aligned}
 R_0&=C+q_0+q_1+q_2,\\
 R_2&=C+q_2+q_3+q_0,
\end{aligned}                                      \tag{4.1}
\]

so they are adjacent in the Johnson graph, with common facet
`C+q_0+q_2`.  A coordinate relabelling therefore identifies them directly
only with a prescribed adjacent pair of the same intersection type.  The
D5 certificate supplies two exact terminal types.  Among the 212 reset
rows, 48 have pairwise Johnson distances

\[
 (d(a,b),d(a,c),d(b,c))=(1,1,1),                  \tag{4.2a}
\]

while 164 have

\[
 (d(a,b),d(a,c),d(b,c))=(1,1,2).                  \tag{4.2b}
\]

The marked C8 pair always has distance one.  Hence the 164 rows in `(4.2b)`
are literal coordinate-relabel counterexamples: they require connector
paths.  The 48 rows in `(4.2a)` have the correct abstract top-type triangle,
but their spectator identity and graft collars still need a physical audit.
Every connector must be included in the lower/intersection-current and
collar ledger.

The exact remaining row-private theorem is therefore:

\[
\boxed{
\begin{array}{l}
\text{For each of the 212 D5 reset occurrences, link its prescribed}\\
\text{tail/head ports to one marked complementary-square C8 quotient;}\\
\text{make the 212 linked banks jointly resource-simple (with the declared}\\
\text{multiplicity-four occurrence splitting), q2-biresident, and}\\
\text{restore the four lower-q2 losses and preserve lower/upper support}\\
\text{across every connector seam.}
\end{array}}
\tag{4.3}
\]

Suppressing boxes satisfying `(4.3)` recovers the frozen switched factor,
so the independently verified `372 -> 1` component action is then retained.

## 5. Alternative global topology

The row-private reduction is sufficient, not necessary.  The complete D5
permutation is even.  Its circuit histogram has 25 odd-length and 16
even-length cycles on 477 rows, so it has an algebraically minimal
3-cycle factorization of size

\[
                              (477-25)/2=226.         \tag{5.1}
\]

A globally coordinated open-C6 atlas could therefore replace the 212
private odd boxes.  It would need a new common resource and collar schedule;
the known closed inverse-C6 carrier has identity outer monodromy and cannot
be used unchanged.  The two routes should remain distinct:

\[
\text{212 prescribed C8 quotients}
\qquad\text{or}\qquad
\text{226 globally coupled open C6 routers}.        \tag{5.2}
\]

The first route has all internal residence and upper-current algebra already
proved; its bottleneck is prescribed-terminal linkage plus four lower-q2
backups per copy.  The second has easier global parity but a substantially
larger unpriced chronology problem.

## 6. H100 replay

The independent lower-q2 and backup verifier is
`scratch/audit_common_mate_c8_lower_q2_current_20260814.py`.  It rebuilt the
complete old and switched banks for 63 parameter pairs from `m=18` through
`m=80`, using `q=max(5,floor(sqrt(m))+1)`, checked `(2.1)--(2.4)` and the four
singleton losses, then constructed `(2.5)--(2.6)` and checked resource
disjointness, residence, and zero residual support loss.  All substantive
execution and hashing were on H100.

```text
verifier SHA-256  bf4662fc1e921014907408df1a82e471ce93bbb415d86235287cec112c2b7bd1
output SHA-256    9e1fe95b14eef108fd0a0ca2e2ff1522885e8f5e1206990717f30fb36131c001
```
