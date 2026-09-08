# Hostile audit of the graph star--cycle one-owner absorber

**Date:** 2026-08-13  
**Source audited:** attachment
`92d98fcf-75a1-4de4-8d0b-3216490f0909/pasted-text.txt`  
**Scope:** Theorem 1 and its application to the special conformal residue
`B^+-B^-`; compulsory-ticket and global-packing consequences only.  The
later clock-dilated `C_8` theorem is outside this audit.

## Verdict

The graph algebra is **PASS**.  It gives a genuine, explicit, local
common-reserve lift in the named-owner projection:

\[
 \widehat{\mathcal R}_H\sqcup B^+
 \quad\hbox{and}\quad
 \widehat{\mathcal R}_H\sqcup B^-
\]

are each simple owner-disjoint unions of cyclic `q`-window supports, and

\[
 |\widehat{\mathcal R}_H|=(q+1)^2.
\]

The even and odd graph decompositions, the map from graph edges to owners,
the one-owner current, and disjointness from the single special macro all
check exactly.

The advertised conclusion must nevertheless retain two qualifications.

1. The new periods `q+1` and `q+2` give closed Johnson owner cycles and
   positive runs of length `q`, but zero gaps of lengths `1` and `2`.
   Hence they are not biresident rails when the literal column definition
   requires zero runs of length at least `q`.
2. Every period-`q+1` star rail repeats one immediate-upper value exactly
   `q+1` times.  It is therefore not an upper-palette-simple literal rail.
   More generally, the full compulsory-ticket equality is not proved and
   is visibly nonautomatic.

Thus Theorem 1 is proof-safe as a theorem about the **owner, point-degree,
whole-cycle trace, and positive-residence projections**.  It is not yet a
positive lift in the full protected rail semigroup.  It closes the local
owner projection of the special `B^+-B^-` residue, not the global owner
factorization: simultaneous collision-free planting of absorbers for many
owners remains unproved.

## 1. Edge-to-owner map

Put

\[
 |L|=2q,\qquad D=H\setminus L,\qquad
 V=L\sqcup\{u,v\}.
\]

Then

\[
 |D|=R-2q=c-q,qquad |V|=2q+2.
\]

For `ab in binom(V,2)` define

\[
 \Omega(ab)=D\cup(V\setminus\{a,b\}).                 \tag{1.1}
\]

This has size

\[
 (c-q)+2q=R,
\]

and complements recover the edge, so `Omega` is injective.  Moreover

\[
 \Omega(uv)=D\cup L=H.                               \tag{1.2}
\]

If a star has centre `x` and `q+1` cyclically ordered leaves `T`, its core

\[
 D\cup\bigl(V\setminus(\{x\}\cup T)\bigr)
\]

has size `(c-q)+q=c`, and its consecutive `q`-windows are precisely the
owners `Omega(xt)`, `t in T`.  If `Gamma` is a simple `C_{q+2}`, the analogous
core has size `(c-q)+q=c`, and each `q`-window omits one consecutive edge of
`Gamma`; its support is `Omega(E(Gamma))`.  Thus graph-edge disjointness is
exactly owner disjointness.

Both constructions are cyclic Johnson walks.  Since

\[
 M=k-c=k-R+q\ge q+3,
\]

their periods `q+1,q+2` are strictly below the maximal toggle period.  This
establishes nonmaximality; it does not by itself establish every physical
residence or ticket convention.

## 2. Even `q`

Let `L=A sqcup B_0`, with `|A|=|B_0|=q`, and

\[
 B=B_0\sqcup\{u,v\},\qquad S=K_{A,B}+uv.
\]

For every `a in A`, take the star centred at `a` with leaves
`B\setminus\{u\}`.  These stars cover all `A`--`B` edges except the `q`
edges from `A` to `u`.  The last star, centred at `u` with leaves
`A\cup\{v\}`, covers exactly those `q` edges and `uv`.  Hence the `q+1`
stars are edge-disjoint and cover `S`.

Deleting `uv` leaves `G=K_{q,q+2}`.  Here even `q` implies that both part
sizes are even; the desired cycle length is `q+2`,

\[
 \min(q,q+2)\ge (q+2)/2,
 \qquad q+2\mid q(q+2).
\]

These are precisely Sotteau's conditions for a `C_{q+2}` decomposition of
the complete bipartite graph.  The decomposition contains

\[
 |E(G)|/(q+2)=q
\]

cycles.  The even case is therefore PASS.

## 3. Odd `q`

Write `q=2h+1`.  With

\[
 A=\{a_j:j\in\mathbb Z_q\},\qquad
 B_0=\{b_j:j\in\mathbb Z_q\},
\]

the proposed graph after deleting `uv` is

\[
 G=K_{A,B_0}\cup uA\cup uB_0.                        \tag{3.1}
\]

For each `j`, the proposed cycle is

\[
 \Gamma_j=(u,a_j,b_{j+h},a_{j+1},b_{j+h-1},\ldots,
             a_{j+h},b_j,u).                         \tag{3.2}
\]

It contains `u`, `h+1` distinct `A`-vertices, and `h+1` distinct
`B_0`-vertices, hence is a simple `C_{q+2}`.  Its first and last edges
cover `ua_j` and `ub_j`; translating `j` covers every edge incident with
`u` once.

On internal `A`--`B_0` edges the two families of index differences are

\[
 h-2t\quad(0\le t\le h),
 \qquad
 h+1-2t\quad(1\le t\le h).                           \tag{3.3}
\]

Together these are exactly the `q` integers from `-h` through `h`, hence
all residues modulo `q` once.  Translation by `j` therefore covers every
edge of `K_{A,B_0}` exactly once.  Thus the `q` cycles partition `G`.

The star decomposition also checks directly: stars centred at the `a_j`
cover `K_{A,B_0}` and `A u`; the star centred at `u` covers `uB_0` and
`uv`.  The odd case is PASS.

## 4. Exact one-owner current

In both parities the graph `S` has `q+1` disjoint `K_{1,q+1}` pieces and
`G=S-uv` has `q` disjoint `C_{q+2}` pieces.  Hence

\[
 |E(S)|=(q+1)^2,qquad |E(G)|=q(q+2),                 \tag{4.1}
\]

and, after applying `Omega`,

\[
 \sum_{Q\in\mathcal A_H^1} f(Q)
 -\sum_{Q\in\mathcal A_H^0} f(Q)
 =e_{\Omega(uv)}=e_H.                                \tag{4.2}
\]

The point-degree current is consequently exactly `1_H`; the displayed
degree table in the source is consistent with this identity.  Each rail is
a whole cyclic component, so its signed prefix/suffix boundary is zero.
Every active toggle belongs to exactly `q` consecutive owner windows, so
the positive run is exactly `q=d+1`.

## 5. Application to the special conformal macro

For the previously constructed macro, the assumed packed sign shores are

\[
 \operatorname{supp}(Y_H^+)=\{H\}\sqcup B^- ,
 \qquad
 \operatorname{supp}(Y_H^-)=B^+.                    \tag{5.1}
\]

Put

\[
 \mathcal R_H=\Omega(E(G)),\qquad
 \widehat{\mathcal R}_H=\mathcal R_H\sqcup\{H\}.
\]

Equation (4.2) gives the two exact identities

\[
 \widehat{\mathcal R}_H\sqcup B^+
 =\operatorname{supp}(\mathcal A_H^1)
   \sqcup\operatorname{supp}(Y_H^-),                 \tag{5.2}
\]

\[
 \widehat{\mathcal R}_H\sqcup B^-
 =\operatorname{supp}(\mathcal A_H^0)
   \sqcup\operatorname{supp}(Y_H^+).                 \tag{5.3}
\]

The sign placement is correct.

The claimed local disjointness is also correct.  Every edge of `G` touches
`L subset C`, so every reserve owner omits at least one point of `C` and
cannot be an insertion owner, all of which contain `C`.  A star-correction
owner `O` obeys

\[
 |O\cap H|\le 2q,qquad
 \operatorname{dist}_{J(k,R)}(O,H)\ge R-2q=c-q\ge q. \tag{5.4}
\]

Every reserve owner is at Johnson distance one or two from `H`; since
`q>=3`, the two sets cannot meet.  Finally, `H` was removed from `B^-` and
does not occur in `B^+`.  Therefore `widehat R_H` is disjoint from the two
macro shores.

This is a complete proof for one special residue.  It does **not** choose
the data `L,u,v` for a family of roots `H` so that different reserves are
mutually owner-disjoint.  Nor does it prove that such reserves avoid all
other macros in a global rounding.  That missing global packing statement
cannot be inferred from the single-root distance argument.

## 6. Exact physical-column boundary

The short supports have two defects relative to the complete rail columns
used elsewhere in the proof architecture.

First, a period-`q+1` star rail has toggle word `1^q0`.  Its positive run
is `q`, but its zero gap is one.  A period-`q+2` cycle rail has toggle word
`1^q0^2`.  Thus neither meets a two-sided residence rule requiring both
runs to have length at least `q` (for `q>=3`).  They remain valid under a
strictly positive-residence-only projection.

Second, in a star with centre `x` and leaves `t_i`, adjacent owners are
`Omega(xt_i)` and `Omega(xt_{i+1})`.  Their immediate upper union is always

\[
 D\cup(V\setminus\{x\}),                             \tag{6.1}
\]

independently of `i`.  The same named upper ticket occurs `q+1` times.
Hence the star rail is not immediate-upper-palette simple.  By contrast,
a `C_{q+2}` piece contributes

\[
 D\cup(V\setminus\{w_i\})
\]

at the turn through `w_i`, and those values are distinct.

The lower palettes on each individual shore are simple, but their
aggregate currents need not agree.  Therefore a full lift requires the
literal equality

\[
 \sum_{Q\in\mathcal A_H^1}\tau(Q)
 -\sum_{Q\in\mathcal A_H^0}\tau(Q)
 =
 \sum_{Q\in\mathcal Q_H^+}\tau(Q)
 -\sum_{Q\in\mathcal Q_H^-}\tau(Q),                 \tag{6.2}
\]

where `tau` contains every compulsory palette, flag, socket, history, and
cap row.  The owner, point-degree, total-count, and whole-cycle trace rows
satisfy (6.2).  The calculation (6.1) shows that the immediate-upper row
does not follow from the graph identity; the source correctly leaves this
and the other compulsory rows unresolved.

Consequently phrases such as "complete closed rails" are proof-safe only
after specifying that `complete` refers to the projected owner support.
If the active column library requires biresidence or a simple immediate
upper palette, the word "legal" in Theorem 1 must likewise be replaced by
"legal in the owner/closed-trace/positive-residence projection."

## 7. Final proof-safe status

The strongest unconditional result is

\[
 \boxed{
 e_H\text{ has a conformal common-reserve realization by simple cyclic}
 \ q\text{-window owner supports of periods }q+1,q+2.}
\]

Together with the prior conformal macro this proves (5.2)--(5.3), so the
special residue is not a positive-semigroup hole in the **owner
projection**.  It does not establish any of the following:

* membership in the full compulsory-ticket semigroup;
* biresidence of the short absorber rails;
* a global collision-free bank of these absorbers;
* a global owner-disjoint integral factor;
* socket or cap compatibility.

Accordingly the attachment contains a material and correct local advance,
but it does not close the full positive semigroup gate or the global owner
factorization.
