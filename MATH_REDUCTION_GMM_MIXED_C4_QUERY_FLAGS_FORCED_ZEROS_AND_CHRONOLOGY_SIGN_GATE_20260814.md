# GMM mixed C4s: exact query-flow cut and chronology sign gate

**Date:** 2026-08-14  
**Status:** exact incidence and chronology reduction; no all-parameter
outgoing-move theorem

## 0. Outcome

Fix `m>=2`, and let `C` be a lower-complete Hamilton cycle of
`J(2m+1,m)`.  For a lower colour `R`, let `H_R` be the selected path
forest on the `m+2` outside labels and put

\[
 \ell_R=|E(H_R)|=1+d(R).
\]

Thus `d(R)>=0`; write `D=sum_R d(R)` and
`supp d={R:d(R)>0}`.

The mixed `C_4` normal form in the preceding GMM note turns every oriented
edge of every surplus `H_B` into `m-1` two-step incidence queries.  This
note proves:

1. the exact query count is

   \[
   2(m-1)\bigl(D+|\operatorname {supp}d|\bigr);
   \]

2. the occurrence count has an exact flag-by-flag decomposition;
3. every target/exception fibre `(P,c)` is exactly a set of surplus-colour
   incidences at the single owner `P+c`, with capacity
   `2-deg_{H_P}(c)`; the scalar sum of these capacities is tautological,
   so a raw global double count cannot prove positivity;
4. if the occurrence count vanishes, no query may land at an internal
   path-forest vertex, a leaf absorbs at most one correctly aligned query,
   and every surplus colour `B` forces at least

   \[
   2\bigl((m-1)\ell_B-c_B\bigr)
   \]

   distinct zero-degree flags, where `c_B` is the number of nontrivial
   path components of `H_B`;
5. the remaining Hamilton chronology is only a sign test: a present mixed
   packet is legal exactly when its two old edges have opposite directions
   in the oriented Hamilton cycle, relative to the packet order.

The zero flags may overlap for different surplus colours.  That overlap is
the unresolved all-`m` gate.  An exact `m=4` lower-complete two-factor with
zero occurrences shows that owner degree two and lower coverage alone do
not force a move.  It has two monochromatic triangle defects, so it does
not satisfy the Hamilton/path-forest hypothesis.  Thus those two defects
pinpoint, rather than remove, the remaining global input.

## 1. Query flags

For every `B` with `d(B)>0`, every ordered edge
`(p,a) in \vec E(H_B)`, and every `b in B`, define a query

\[
 q=(B;b,p,a),\qquad P(q)=B-b+p,qquad \phi(q)=(P(q),a).       \tag{1.1}
\]

The query asks whether `H_{P(q)}` has an edge `{a,c}` with `c!=b`.  Its
allowed exceptional neighbour is `b`, because `{a,b}` makes the two old
Johnson edges meet at the owner `B+p` rather than form a mixed packet.

Let

\[
 \mu(P,a)=|\{q:\phi(q)=(P,a)\}|,
\quad
 \mu(P,a;c)=|\{q:\phi(q)=(P,a),\ b(q)=c\}|.        \tag{1.2}
\]

### Theorem 1.1 (exact query decomposition)

The total number of queries is

\[
 |\mathcal Q|=2(m-1)\sum_{B:d(B)>0}\ell_B
 =2(m-1)\bigl(D+|\operatorname {supp}d|\bigr).     \tag{1.3}
\]

Moreover the mixed occurrence count is exactly

\[
 A_{\rm occ}(C,d)=
 \sum_{P}\sum_{a\notin P}
 \left[
  \mu(P,a)\deg_{H_P}(a)
  -\sum_{c\in N_{H_P}(a)}\mu(P,a;c)
 \right].                                         \tag{1.4}
\]

#### Proof

Every selected edge of `H_B` has two orientations and `|B|=m-1`; summing
`\ell_B=1+d(B)` over the surplus support gives (1.3).  A query contributes

\[
 \deg_{H_{P(q)}}(a)-
 \mathbf1_{\{a,b\}\in E(H_{P(q)})}
\]

to the occurrence count.  Grouping these terms by the target flag
`(P,a)` gives (1.4). \(\square\)

For a zero-degree flag the bracket in (1.4) is zero.  For a leaf with
unique neighbour `c` it is `\mu(P,a)-\mu(P,a;c)`.  For a degree-two flag
with neighbours `c_1,c_2` it is

\[
 2\mu(P,a)-\mu(P,a;c_1)-\mu(P,a;c_2)\ge\mu(P,a),   \tag{1.5}
\]

because every query has only one exceptional label.

### Lemma 1.2 (exact owner-fibre identity)

Fix `P` and `c notin P`.  Put `O=P+c`.  Then

\[
 \sum_{\substack{a\notin P\\a\ne c}}\mu(P,a;c)
 =|\{e\in\delta_C(O):\operatorname{col}(e)\ne P,
                  \ d(\operatorname{col}(e))>0\}|.            \tag{1.6}
\]

Consequently

\[
 \sum_{\substack{a\notin P\\a\ne c}}\mu(P,a;c)
 \le 2-\deg_{H_P}(c).                              \tag{1.7}
\]

Here `col(e)` is the lower colour of a selected Johnson edge.  Indeed, a
query in the left side has source colour `B=P-p+c` and source edge

\[
       P+c\;--\;P-p+c+a.
\]

Conversely every selected incidence at `O` whose lower colour is surplus
and different from `P` uniquely recovers `p`, `a`, and this query.  The
incidences of lower colour `P` at `O` are exactly the
`deg_{H_P}(c)` incidences already excluded on the right.

## 2. The sharp forced-zero structure

### Theorem 2.1 (zero-occurrence flag cut)

If `A_occ(C,d)=0`, then:

1. `\mu(P,a)=0` whenever `deg_{H_P}(a)=2`;
2. if `a` is a leaf of `H_P` with neighbour `c`, then at most one query
   targets `(P,a)`, and that query has exceptional label `b=c`;
3. if `deg_{H_P}(a)=0`, then

   \[
   \mu(P,a)\le2(m+1-\ell_P).                       \tag{2.1}
   \]

#### Proof

The first assertion and the required leaf alignment follow from
(1.4)--(1.5).  If a leaf `(P,a)` has neighbour `c`, every aligned source
edge is incident with the same owner `P+c`.  The leaf edge `{a,c}` already
uses one of its two cycle incidences, so at most one source edge remains.

For the last assertion, sum (1.7) over the `m+1` exceptional labels outside
`P` other than the isolated label `a`, and use
`sum_c deg_{H_P}(c)=2\ell_P`. \(\square\)

There is an equivalent owner-local form.  Let a selected directed
incidence be

\[
             O\longrightarrow O-p+a
\]

and suppose its lower colour `O-p` is surplus.  If `A_occ=0`, then for
every `b in O` with `b!=p`, the label `a` is isolated in `H_{O-b}`, except
possibly
when the other selected incidence at `O` is exactly
`O--(O-b+a)`.  In that exceptional case `a` is a leaf of `H_{O-b}` with
neighbour `b`.  Hence one surplus incidence forces `m-2` isolated flags,
or `m-1` unless its companion incidence has the same entering label.
This is just Theorem 2.1 applied to `q=(O-p;b,p,a)`: the permitted leaf
edge `{a,b}` in `H_{O-b}` is the physical edge
`O--(O-b+a)`, and `O` has only one incidence besides the source edge.

### Corollary 2.2 (one surplus colour forces many distinct zero flags)

Let `c_B` be the number of nontrivial path components of `H_B`.  If
`A_occ(C,d)=0`, the queries sourced at a fixed surplus colour `B` force at
least

\[
 Z_B=2\bigl((m-1)\ell_B-c_B\bigr)                 \tag{2.2}
\]

distinct target flags to have degree zero.  In particular,

\[
                         Z_B\ge2(m-2)\ell_B.       \tag{2.3}
\]

#### Proof

The map from a query sourced at fixed `B` to its target flag is injective:
from `P=B-b+p` one recovers `b=B-P` and `p=P-B`, and the flag remembers
`a`.  Thus all `2(m-1)\ell_B` target flags are distinct.

Fix a nonisolated label `p` of `H_B`.  All leaf exceptions generated by
oriented source edges `(p,a)` use an additional selected edge at the common
owner `B+p`.  Its `deg_{H_B}(p)` source edges are already present, so at
most `2-deg_{H_B}(p)` such exceptions exist.  Summing over the nonisolated
vertices of the path forest gives

\[
 \sum_p(2-\deg_{H_B}(p))=2c_B.                    \tag{2.4}
\]

Every remaining queried flag is zero by Theorem 2.1.  This proves (2.2),
and `c_B<=ell_B` gives (2.3). \(\square\)

Lemma 1.2 gives the sharper capacitated cut, for every set `S` of
target/exception fibres,

\[
 |\{q:(P(q),b(q))\in S\}|
 \le\sum_{(P,c)\in S}\bigl(2-\deg_{H_P}(c)\bigr).  \tag{2.5}
\]

This family is exact at the owner-incidence level.  Its undifferentiated
scalar sum cannot prove a positive occurrence theorem.  Indeed, if
`W=|V(C)|` and `L` is the number of lower colours, then

\[
 \sum_{P}\sum_{c\notin P}(2-\deg_{H_P}(c))
 =2\bigl((m+2)L-W\bigr)=2(m-1)W,                  \tag{2.6}
\]

where `W=(m+2)L/m`.  The query count is
`2(m-1)` times the number of selected surplus-coloured edges, so (2.6)
reduces exactly to the tautology that those edges are a subset of the
`W` selected edges.  Any all-parameter positivity proof must therefore
use the **placement** of the forced isolated flags, not only total owner
capacity.

## 3. Chronology is an orientation-sign gate

Orient the Hamilton cycle `C`.  For an ordered selected edge `(x,y)` of
`H_R`, put

\[
 \epsilon_R(x,y)=
 \begin{cases}
 +1,&C\text{ traverses }R+x\longrightarrow R+y,\\
 -1,&C\text{ traverses }R+y\longrightarrow R+x.
 \end{cases}                                      \tag{3.1}
\]

### Theorem 3.1 (exact mixed-C4 chronology sign)

For an occurrence query `q=(B;b,p,a)` continued by `{a,c}` in
`H_{P}`, where `P=B-b+p` and `c!=b`, the mixed reconnection is Hamilton-safe
if and only if

\[
                     \epsilon_B(p,a)\epsilon_P(a,c)=-1.       \tag{3.2}
\]

When (3.2) holds, the two positive edges are automatically absent from the
retained cycle.

#### Proof

Use the packet order

\[
 K+p+a,\ K+p+c,\ K+p+b,\ K+a+b,
 \qquad K=B-b.
\]

The old edges are `12,34` and the new edges are `23,41`.  Delete the two
old directed cycle edges.  If their directions agree relative to `1->2`
and `3->4`, the new matching closes the two retained paths separately.  If
their directions disagree, it joins the two paths crosswise into one
cycle.  These are exactly the signs in (3.2).  In the crosswise case a new
edge cannot already lie in either retained path component. \(\square\)

Consequently

\[
 A_{\rm legal}(C,d)=
 \sum_q\ \sum_{\substack{c\in N_{H_{P(q)}}(a(q))\\c\ne b(q)}}
 {1-\epsilon_B(p,a)\epsilon_{P(q)}(a,c)\over2}.    \tag{3.3}
\]

Equivalently, make a graph whose vertices are ordered selected-edge tokens
and whose edges are the occurrence continuations.  The legal count is zero
exactly when every relation joins equal signs, or equivalently every
relation component is sign-monochromatic.  In particular, a component
containing both orientations of one selected edge forces a legal move.

## 4. Exact near-obstruction at m=4

There is a lower-complete `2`-factor of `J(9,4)` with

\[
 W=126,qquad |\mathcal L|=84,qquad D=42,qquad A_{\rm occ}=0. \tag{4.1}
\]

It has `21` components of lengths

\[
 3^{15},\ 5^3,\ 8,\ 14,\ 44,                       \tag{4.2}
\]

and nonregular surplus point vector

\[
 (13,14,13,13,14,18,16,14,11),                    \tag{4.3}
\]

whose regular value would be `14`.  Exactly two lower-colour subgraphs
contain a cycle: each defect is a monochromatic triangle.  Hence this is
not a Hamilton-cycle counterexample and does not refute an all-`m`
positive theorem under the full hypotheses.

It does prove a sharp method obstruction: owner degree two, exact lower
coverage, correct surplus mass, and nonregular point defect do not force a
mixed occurrence.  Moreover among the certificate's `335`
cross-component Johnson two-edge reconnections, `165` preserve lower
coverage and none preserve `A_occ=0`.  The simplest component fusion cannot
repair its two colour-cycle defects while staying in the zero-occurrence
fiber.

The compact certificate and independent checker are in

`scratch/verify_gmm_mixed_c4_zero_twofactor_certificate_20260814.py`.

## 5. Frozen gate

The remaining all-parameter question is now narrower than a generic
double count:

> Can the query overlap allowed by (2.1)--(2.6) coexist with every `H_R`
> being a path forest **and** with their union being one Hamilton cycle?

If not, (1.4) should yield a quantitative positive occurrence bound.  If
yes, the first counterexample must evade the forced-zero capacities while
eliminating the two monochromatic cycle defects exhibited above.  After
occurrence, the only remaining `C_4` chronology obstruction is the
sign-monochromatic cut (3.3).
