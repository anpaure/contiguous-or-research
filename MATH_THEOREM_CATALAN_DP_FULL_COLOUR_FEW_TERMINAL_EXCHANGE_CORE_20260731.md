# The full conflict-free colouring contains a few-terminal four-valent exchange core

Date: 2026-07-31  
Status: exact colouring identities, quantitative two-colour extraction, and
exact component-switch calculus.  This is a deterministic consequence of the
full Delcourt--Postle colouring of the fixed-`Q` capacity-slot hypergraph.  It
does **not** give a bounded-support absorber, a serializable ear system, exact
cover-down, or `nu=B`.

## 0. Verdict

Fix any admissible synchronized common basis `Q`, and let `G_Q` be one
punctured-shore four-uniform capacity-slot hypergraph.  Retain the **whole**
Delcourt--Postle colouring, not only its largest colour class.

There are two colour classes which, after deleting one edge from every long
physical cycle, give linear forests `F_0,F_1` such that

\[
 |F_i|=P-o(P),\qquad
 |R(F_0)\mathbin\triangle R(F_1)|=o(P),                \tag{0.1}
\]

where `R(F)` is the set of all four host resources used by `F` (lower,
upper, and occurrence-labelled owner slots).

Their difference has an exact canonical form.  Join an atom of `F_0` to an
atom of `F_1` once for every common host resource, and retain a half-edge for
every resource in the symmetric difference in (0.1).  Then

* all but `o(P)` atom vertices are four-valent;
* at most `o(P)` connected components have a terminal half-edge;
* every terminal-free component is an exact count-neutral four-resource
  trade; and
* the support-preserving two-colour switches are **exactly** the unions of
  terminal-free connected components.

This is the strongest unconditional exchange statement furnished by the
whole colouring.  It is global, not local.  The exchange graph has an
extensive four-valent core, and all terminals may belong to one connected
component.  Thus Delcourt--Postle does not itself give alternating paths,
bounded `C6/C8` packets, or a serializable cover-down.  The literal locked
`C6` example in

```text
MATH_THEOREM_CATALAN_DP_COLORING_EXCHANGE_CALCULUS_AND_LOCKED_C6_OBSTRUCTION_20260731.md
```

shows that this distinction occurs inside the actual capacity-slot geometry.

## 1. Exact full-colouring identities

Use

\[
 N={2n\choose n-1},\qquad P={2n\choose n-2},\qquad
 C=\operatorname {Cat}_{n+1},
\]

and put

\[
 D=2(n+1)(n+2),\qquad
 V_*=|V(G_Q)|=2P+2N-C.                                 \tag{1.1}
\]

Let

\[
 E_*=|E(G_Q)|,
\]

and let `phi:E(G_Q)->[q]` be a proper colouring of the line graph together
with the short-cycle configuration hypergraph.  Write

\[
 M_c=\phi^{-1}(c),\quad m_c=|M_c|,\quad
 d(v)=d_{G_Q}(v),\quad R_c=R(M_c).                     \tag{1.2}
\]

Because every colour class is a matching and there are exactly `P` lower
and `P` upper resources,

\[
                         m_c\le P.                    \tag{1.3}
\]

### Lemma 1.1 (class and pair ledgers)

For every proper colouring,

\[
 \sum_c m_c=E_*,\qquad
 \sum_c(P-m_c)=qP-E_*,                                \tag{1.4}
\]

and

\[
 \boxed{\quad
 \sum_{c<d}|R_c\mathbin\triangle R_d|
       =\sum_{v\in V(G_Q)}d(v)(q-d(v)).
 \quad}                                                \tag{1.5}
\]

#### Proof

Equation (1.4) is the partition of the atom set into colours.  At a fixed
host resource `v`, properness gives `d(v)` distinct colours which cover it
and `q-d(v)` colours which do not.  Exactly `d(v)(q-d(v))` unordered colour
pairs disagree at `v`.  Sum over `v`.  `square`

Thus (1.5) is an exact deterministic substitute for any independence
heuristic about colour classes.

## 2. Uniform numerical bounds

The fixed-`Q` edge ledger gives

\[
 E_*\ge4P{n\choose2}-2C(n^2-1),\qquad
 \Delta(G_Q)\le D.                                    \tag{2.1}
\]

The Catalan ratios simplify the vertex count to

\[
 {N\over P}={n+2\over n-1},\qquad
 {C\over P}={2(2n+1)\over n(n-1)},\qquad
 \boxed{V_*=(4+2/n)P}.                                \tag{2.2}
\]

Two useful consequences of (2.1)--(2.2) are

\[
 DP-E_*\le P\left(16n+16+{4\over n}\right),           \tag{2.3}
\]

and

\[
 D V_*-4E_*
 \le P\left(68n+76+{24\over n}\right).               \tag{2.4}
\]

These follow by direct substitution; no probability law on `Q` occurs.

Suppose now that the colouring uses

\[
 q\le D(1+\epsilon),                                  \tag{2.5}
\]

where a ceiling may be absorbed into `epsilon`.  Properness at each host
vertex and (2.4) also give

\[
 q\ge\Delta(G_Q)\ge {4E_*\over V_*}=D-O(n),           \tag{2.6}
\]

so `q=(1+o(1))D` whenever `epsilon=o(1)`.

### Lemma 2.1 (average class and pair defects)

Uniformly in `Q`,

\[
 {1\over q}\sum_c(P-m_c)
       =O\left(P(\epsilon+n^{-1})\right),             \tag{2.7}
\]

and

\[
 {1\over {q\choose2}}\sum_{c<d}
       |R_c\mathbin\triangle R_d|
       =O\left(P(\epsilon+n^{-1})\right).             \tag{2.8}
\]

#### Proof

From (1.4), (2.3), and (2.5),

\[
 qP-E_*\le P\left(\epsilon D+16n+16+4/n\right),       \tag{2.9}
\]

which proves (2.7) using (2.6).

Since `d(v)<=D`,

\[
 q-d(v)\le \epsilon D+(D-d(v)).                       \tag{2.10}
\]

Equations (1.5) and (2.4) therefore give

\[
\begin{aligned}
 \sum_{c<d}|R_c\triangle R_d|
 &\le \epsilon D\sum_vd(v)+D\sum_v(D-d(v))\\
 &\le4\epsilon D^2P
   +DP\left(68n+76+24/n\right).                       \tag{2.11}
\end{aligned}
\]

Divide by `{q choose 2}` and use (2.6).  `square`

### Corollary 2.2 (two large close classes)

There are distinct colours `a,b` for which

\[
 |M_a|,|M_b|=P-O\left(P(\epsilon+n^{-1})\right)        \tag{2.12}
\]

and

\[
 |R_a\triangle R_b|
       =O\left(P(\epsilon+n^{-1})\right).             \tag{2.13}
\]

#### Proof

By (2.7), at least three quarters of the colours have deficiency at most
four times the average in (2.7).  Restrict (2.8) to the pairs among those
colours.  They still form a positive constant fraction of all pairs, so
one restricted pair satisfies (2.8) up to an absolute constant.  `square`

For the Delcourt--Postle colouring, `epsilon=D^{-alpha}` for fixed cycle
cutoff `L` and some `alpha=alpha(L)>0`.  Hence both errors in
(2.12)--(2.13) are `o(P)`.

## 3. Two close linear forests

Every physical projection of a colour class has maximum degree two, is
simple, and has no cycle of length at most `L`.  Delete one atom from every
remaining physical cycle of `M_a` and `M_b`, obtaining `F_a,F_b`.  Then

\[
 |F_i|\ge |M_i|-{|M_i|\over L+1},                     \tag{3.1}
\]

and deleting one atom changes its four-resource support in four places.
Consequently

\[
 |F_i|=P-O\left(P(\epsilon+n^{-1}+L^{-1})\right),      \tag{3.2}
\]

\[
 |R(F_a)\triangle R(F_b)|
   =O\left(P(\epsilon+n^{-1}+L^{-1})\right).          \tag{3.3}
\]

Choose `L` first and then `n`; equivalently take the usual sufficiently
slow diagonal `L=L(n)->infinity`.  Equations (3.2)--(3.3) become (0.1),
uniformly in `Q`.

This is stronger than the existence of one `P-o(P)` forest: the full
colouring supplies two almost-complete forests which differ on only
`o(P)` host resources.

## 4. Exact few-terminal exchange decomposition

For any two matchings `F_0,F_1` in a four-uniform host, form the labelled
exchange incidence multigraph `Xi(F_0,F_1)` as follows.

* Its ordinary vertices are the atoms of `F_0` and `F_1`.
* Every host resource used by both matchings gives an edge between its
  unique two incident atoms, labelled by that resource.
* Every host resource used by exactly one matching gives a terminal
  half-edge at its unique atom.

Parallel edges are retained.  Every atom has total degree four when
ordinary edges and terminal half-edges are counted together.

### Theorem 4.1 (component switches and exact support trades)

Let `K` be a connected component of `Xi(F_0,F_1)`, and write

\[
 A_i(K)=K\cap F_i.                                     \tag{4.1}
\]

Then replacing `A_0(K)` by `A_1(K)` gives another host matching.  Its
resource support differs from that of `F_0` exactly at the terminal
half-edges of `K`.  Component switches commute.

Moreover, a two-colour switch preserves the complete four-resource support
if and only if it is a union of terminal-free connected components.  Every
such component is count-neutral:

\[
                         |A_0(K)|=|A_1(K)|.            \tag{4.2}
\]

#### Proof

Every conflict between an atom of `F_1` in `K` and an atom of `F_0` is a
shared host resource and hence an ordinary edge of `Xi`; connectedness puts
both atoms in `K`.  Thus after all `F_0` atoms of `K` are removed, all
`F_1` atoms of `K` can be inserted.  Resources on ordinary edges remain
covered, and terminal resources change status.  Distinct components share
no host resource, proving commutativity.

For an arbitrary support-preserving switch, put indicator one on every
removed `F_0` atom and every inserted `F_1` atom.  At a shared resource,
support preservation forces its two endpoint indicators to agree.  At a
terminal resource it forces the incident indicator to be zero.  Hence the
indicator is constant on each connected component and vanishes on every
terminal component.  The converse is immediate.

Finally, a terminal-free component uses the same resource set in both
phases.  Counting its four incidences gives
`4|A_0(K)|=4|A_1(K)|`.  `square`

There is also an exact typed boundary law.  Let
`b_i^D(K),b_i^V(K),b_i^S(K)` count the terminal lower, upper, and slot
resources belonging to phase `i`.  Then

\[
 |A_0|-|A_1|=b_0^D-b_1^D=b_0^V-b_1^V,
\qquad
 2(|A_0|-|A_1|)=b_0^S-b_1^S.                         \tag{4.3}
\]

This follows by counting each resource type separately.

### Corollary 4.2 (few terminals, extensive four-core)

For the pair in Section 3, `Xi(F_a,F_b)` has

* `o(P)` terminal half-edges;
* at most `o(P)` terminal connected components; and
* all but `o(P)` of its `2P-o(P)` atom vertices incident only with four
  ordinary exchange edges.

#### Proof

The terminal count is (3.3).  Every terminal component contains a terminal,
and every atom of ordinary degree below four is incident with at least one
terminal half-edge.  `square`

Thus the deterministic object extracted from the full colouring is a
nearly four-regular branching exchange core with few terminals.  It is not
a union of alternating paths.

## 5. What is still missing

The theorem gives a genuine global reservoir:

1. two near-spanning linear physical forests;
2. an exact component packetization of their difference;
3. only `o(P)` terminal resources and terminal packets; and
4. exact count-neutral trades on every closed component.

But it does not give the requested protected cover-down.

* A single terminal component may contain `Theta(P)` atoms.
* A terminal-free component may also have `Theta(P)` atoms; its only
  support-preserving phases can be the two whole phases.
* Switching a component preserves slot matching but need not preserve
  physical acyclicity at intermediate or final partial phase choices.
* The common holes of `F_a,F_b` are not repaired merely because their
  supports are close.
* No component is guaranteed to avoid a prescribed residence, seam, or
  downstream-compiler bank.

The infinite connected four-regular example and the literal locked-`C6`
fixture in the exchange-calculus note prove that bounded local ears do not
follow from proper colouring and small codegree, even in the relevant
four-uniform setting.

The precise next statement is therefore a **multi-colour four-core
splitting theorem**: use at least three colour classes and the Boolean
Johnson geometry to split the few-terminal exchange core into protected,
graphic-safe packets while routing all terminal debt.  Calling the raw
Delcourt--Postle colouring itself an absorber would skip exactly this
theorem.
