# Mixed `H-C6 x D-C10` and `H-C10 x D-C6`: raw terminal completeness, pair rescue, and sound provider pruning

Date: 2026-08-01  
Status: **exact reduction and independent-checker specification; no finite pass or no-go claim**

## 1. Setup

Let $D,H:O\to F$ be the two fixed literal incidence perfect matchings of
candidate29, and put

\[
                              \pi=H^{-1}D.                 \tag{1.1}
\]

An assignment cycle on `D` with owner permutation $\alpha$, and one on
`H` with owner permutation $\beta$, produce endpoint maps

\[
                D'=D\alpha,\qquad H'=H\beta,\qquad
                \pi'=\beta^{-1}\pi\alpha.                 \tag{1.2}
\]

The endpoint permutations do not determine literal voltage or turn colours.
Every incidence label is therefore retained below.

For `H3 x D5`, $\beta$ is a 3-cycle and $\alpha$ is a 5-cycle.  For
`H5 x D3`, their roles are reversed.  Both permutations are even, so

\[
                    \operatorname{sgn}(\pi')=
                    \operatorname{sgn}(\pi).               \tag{1.3}
\]

Thus mixed `3 x 5` has no sign obstruction.  Connectedness still requires
the exact one-cycle test in (1.2).

## 2. Complete raw side banks

Fix one side $M\in\{D,H\}$.  A raw assignment arc is any nonselected
literal incidence from owner $x$ to a facet currently occupied by
$M(y)$, with $y\ne x$.  In particular:

* parallel incidence labels are distinct arcs;
* an arc equal to the opposite matching's selected edge is retained; and
* phase loops $y=x$ are outside the `C6/C10` bank.

A simple directed $t$-cycle, $t\in\{3,5\}$, replaces one old facet by
one new literal at each of its $t$ owners and is automatically a perfect
matching on that side.

### Theorem 2.1 (raw terminal-map completeness)

For each side and $t\in\{3,5\}$, enumerate every simple directed
$t$-cycle in the raw assignment graph and identify two rows only when their
complete owner-to-incidence terminal vectors agree.  Let the resulting banks
be

\[
                 {\cal B}_{H,3},{\cal B}_{H,5},
                 {\cal B}_{D,3},{\cal B}_{D,5}.              \tag{2.1}
\]

Then every simultaneous literal terminal state of type `H3 x D5` occurs
exactly once in

\[
                         {\cal B}_{H,3}\times{\cal B}_{D,5}, \tag{2.2}
\]

and every state of type `H5 x D3` occurs exactly once in the analogous
Cartesian product, before terminal mutual-disjointness is imposed.

#### Proof

A literal simple assignment cycle is, by definition, a simple directed cycle
in the raw graph.  Its terminal side matching is the full incidence vector,
so quotient-parallel choices are neither lost nor spuriously identified.
The two sides are chosen independently relative to the same base state;
hence their complete joint domain is the Cartesian product.  Deduplication by
the terminal vectors removes histories but no terminal state.  

This theorem deliberately does **not** filter a raw side row for collision
with the opposite base matching.  Such a collision can be repaired by the
simultaneous opposite-side cycle.

## 3. Exact pair-rescue criterion

Let $A=\operatorname{supp}(\alpha)$ be the D-owner support and
$B=\operatorname{supp}(\beta)$ the H-owner support.  Define the isolated
conflict sets

\[
 C_D=\{x\in A:D'_x=H_x\},\qquad
 C_H=\{x\in B:H'_x=D_x\}.                                  \tag{3.1}
\]

### Theorem 3.1 (terminal mutual-disjointness)

A raw pair is terminal incidence-disjoint if and only if

\[
 C_D\cup C_H\subseteq A\cap B                              \tag{3.2}
\]

and

\[
                         D'_x\ne H'_x
                         \quad\text{for every }x\in A\cap B. \tag{3.3}
\]

Consequently

\[
                         |C_D\cup C_H|\le |A\cap B|\le3.    \tag{3.4}
\]

A terminal-valid pair is **pair-rescued** exactly when (3.2)--(3.3) hold
and at least one of $C_D,C_H$ is nonempty.

#### Proof

Outside $A\cup B$, both base incidences remain and are distinct.  At an
owner of $A\setminus B$, the H incidence is still $H_x$, so validity is
exactly $D'_x\ne H_x$; this excludes $C_D\setminus B$.  The symmetric
argument excludes $C_H\setminus A$.  At an owner in $A\cap B$, both
incidences change and their exact final inequality is (3.3).  These cases
partition the owners and prove the theorem.  $\square$

Condition (3.3) is not implied by isolated validity: two individually legal
new incidences can coincide.  Conversely, an isolated opposite-base choice
at an overlap owner is not fatal, because the opposite cycle moves that base
edge away.  This is the complete rescue mechanism.

## 4. Owner and facet overlaps are different

The changed lower-turn rows are the owner set

\[
                              A\cup B,                       \tag{4.1}
\]

and both sides change a lower row exactly on

\[
                              O_\times=A\cap B.              \tag{4.2}
\]

The changed D facets are $D(A)$, while the changed H facets are $H(B)$.
Thus the upper mixed rows are

\[
                              F_\times=D(A)\cap H(B).        \tag{4.3}
\]

The two overlap sets are independent and each has size at most three.
Pair rescue depends on $O_\times$, whereas upper cross terms depend on
$F_\times$.  Pruning by owner-support overlap alone is therefore unsound
for the upper palette.

For a lower target $T$, the exact sparse terminal delta is

\[
 \Delta^-_T=\sum_{x\in A\cup B}
 \left({\bf1}\{L(D'_x,H'_x)=T\}-
       {\bf1}\{L(D_x,H_x)=T\}\right).                       \tag{4.4}
\]

For an upper target $T$, it is

\[
 \Delta^+_T=\sum_{f\in D(A)\cup H(B)}
 \left({\bf1}\{U(D'^f,H'^f)=T\}-
       {\bf1}\{U(D^f,H^f)=T\}\right).                      \tag{4.5}
\]

Equations (4.4)--(4.5) already include every nonlinear cross term.  The
terminal palettes are exact if and only if

\[
                       \mu_\pm(T)+\Delta^\pm_T\ge1
                       \quad\text{for every }T.              \tag{4.6}
\]

No isolated palette columns may be added on $O_\times$ or $F_\times$.

## 5. Exact augmented-provider clauses

Let $u=0x0355f$ be the missing upper colour and
$\ell=0x0062f$ the missing lower colour.  Because their base loads are
zero, each must be created on a changed terminal row.

Define the lower one-side and mixed predicates

\[
\begin{aligned}
 P^-_D(x)&:[L(D'_x,H_x)=\ell],&&x\in A\setminus B,\\
 P^-_H(x)&:[L(D_x,H'_x)=\ell],&&x\in B\setminus A,\\
 Q^-_\ell(x)&:[L(D'_x,H'_x)=\ell],&&x\in A\cap B,
\end{aligned}                                                \tag{5.1}
\]

and define $P^+_D,P^+_H,Q^+_u$ analogously at facets, using the disjoint
parts of $D(A),H(B)$ and their intersection $F_\times$.

### Theorem 5.1 (sound and complete hole-provider pruning)

Every terminal repair satisfies both clauses

\[
 \bigvee_{x\in A\setminus B}P^-_D(x)\ \vee
 \bigvee_{x\in B\setminus A}P^-_H(x)\ \vee
 \bigvee_{x\in A\cap B}Q^-_\ell(x),                         \tag{5.2}
\]

\[
 \bigvee_{f\in D(A)\setminus H(B)}P^+_D(f)\ \vee
 \bigvee_{f\in H(B)\setminus D(A)}P^+_H(f)\ \vee
 \bigvee_{f\in F_\times}Q^+_u(f).                          \tag{5.3}
\]

Conversely, (5.2) and (5.3) are exactly the conditions that the two named
holes receive at least one terminal occurrence.  They say nothing about
losses of previously covered colours, which still require (4.6).

#### Proof

An unchanged row cannot create a base-missing colour.  The lower changed
rows partition into $A\setminus B,B\setminus A,A\cap B$, giving (5.2).
The upper changed rows partition in the same way at the facet level, giving
(5.3).  The predicates use final terminal turns, so they include all cross
terms.  $\square$

For implementation, the mixed predicates can be precomputed as exact tables

\[
 {\cal Q}^-_\ell(x)=\{(e_D,e_H):L(e_D,e_H)=\ell\},\qquad
 {\cal Q}^+_u(f)=\{(e_D,e_H):U(e_D,e_H)=u\}.                 \tag{5.4}
\]

These tables are the smallest safe replacement for naive one-side provider
anchoring.

## 6. Candidate29 provider-gap specialization

The frozen provider-gap theorem says that no one-side `C6` contains both a
lower-hole provider arc and an upper-hole provider arc.  A one-side `C10`
can contain both only when their two directed gaps are `(1,2)` or `(2,1)`.

Therefore the following pruning is sound.

* In `H3 x D5`, the two clauses cannot both be witnessed by **unmixed
  one-side H providers**.  If both are witnessed by unmixed one-side D
  providers, the D5 provider gaps must be `(1,2)` or `(2,1)`.
* In `H5 x D3`, interchange H and D.
* If either selected witness is mixed, no provider-gap rejection is valid;
  the exact $Q$-table row must be retained.

This is sharp at the provider-incidence level.  In particular, requiring
one raw side circuit to contain both old one-side providers is incomplete:
one or both holes may be created only by a joint cross term.

A duplicate-free provider-first search may assign each hole its
lexicographically least witness among `D-unmixed`, `H-unmixed`, and `mixed`.
The resulting nine witness-type pairs partition every repair without losing
cross-term solutions.

## 7. Topology, voltage, and exact terminal test

After terminal disjointness and provider pruning, a pair is an immediate
physical repair if and only if:

1. $\beta^{-1}\pi\alpha$ is one quotient cycle;
2. direct literal traversal has nonzero voltage modulo 17; and
3. (4.6) holds for both palettes.

For a contracted topology test, list $A\cup B$ in base-$\pi$ cyclic
order and let $s_0$ be its cyclic successor.  Extending $\alpha,\beta$
by the identity on the other selected owners, the exact contracted successor
is

\[
                              \Phi=\beta^{-1}s_0\alpha.       \tag{7.1}
\]

It must be one cycle.  Voltage is not determined by $\Phi$, because
parallel labels with identical endpoints may have different shifts.

## 8. Independent replay strategy

An independent proof-carrying checker should perform the following steps.

1. Reconstruct the 12,870-edge quotient incidence atlas and the literal
   candidate29 D/H matchings from the frozen factor TSV.
2. Independently enumerate all raw simple H3, H5, D3, and D5 directed cycles,
   retaining opposite-base edges and deduplicating full terminal maps.
3. For each of the two Cartesian products, apply only Theorem 3.1 before
   terminal analysis.  Record isolated-conflict sets, owner overlap, facet
   overlap, and pair-rescue status.
4. Rebuild both terminal matching arrays.  Recompute every lower and upper
   turn directly; do not import primary delta columns.
5. Traverse $\beta^{-1}\pi\alpha$, independently recompute component
   voltages, and require one nonzero-voltage component.
6. Compare the sorted set, or a collision-resistant hash, of complete
   terminal pair keys with the primary emitted table.  Any positive factor
   must then be replayed from its literal TSV.

The Cartesian products are only on the order of the raw `C6` bank times the
raw `C10` bank; a single O3 CPU checker is sufficient.  A resource-limited
run would be `UNKNOWN`, never a no-go.

## 9. Scope

This note proves completeness and the safe pruning rules for simultaneous
`H3 x D5` and `H5 x D3` terminal states.  It does not assert that either
finite bank contains or lacks a repair, and it makes no claim about deeper
shadows, residence, opening, or the compiler.
