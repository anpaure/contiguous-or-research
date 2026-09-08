# Audit of the PBBS paired-hexagon atlas and the surviving exchange cut

Date: 2026-07-26

Method: theorem-level mathematics only.  No computation, finite search, or
web input is used.

Audited note:
`MATH_THEOREM_PBBS_PAIRED_C6_COMPLETE_CLASSIFICATION_20260726.md`.

## 0. Verdict

Put

\[
 n=2r+1,\qquad {
 \cal X}=\binom{[n]}r,\qquad
 W=|{\cal X}|,\qquad B={W\over n}=\operatorname {Cat}_r,
\]

and let \(f\) be the canonical PBBS permutation.  The complete
classification in the audited note is correct:

\[
 \boxed{
 \#\{\hbox{legal paired alternating }C_6\}
 =\binom{2r+1}{r-1}-(2r+1).}
 \tag{0.1}
\]

The exceptional cores are exactly the labelled rotations of

\[
                         000(10)^{r-1}.                     \tag{0.2}
\]

The orientation of the exchange arcs, the rightmost-maximum tie, and the
passage from disjoint center triples to physically vertex-disjoint incidence
hexagons all pass audit.  In particular, there is a disjoint reservoir of
size

\[
 {\binom{2r+1}{r-1}-(2r+1)\over 3r-2}
      =\left({2\over3}+o(1)\right)B.                       \tag{0.3}
\]

This note adds two unconditional facts.

1. Every center belongs to at least one of the star candidates.  Hence at
   most \(3n\) centers have legal-hexagon degree zero, and at most three
   PBBS monodromy components are completely inactive.
2. No proper union of PBBS monodromy components is closed in the full legal
   exchange digraph.  Thus there is no absolute component cut at the level
   of exchange arcs.  The resulting crossing alternating circuit can be
   long, however, and need not decrease the component count.

Neither statement proves the required Catalan-edit Hamiltonization.  The
remaining gate is still a constant-length, component-transversal routing
statement, together with an even-circuit parity bridge when \(B\) is even.

## 1. Exact exchange parameterization

For \(Z\in{\cal X}\), write

\[
 p(Z)=r_+(Z),\qquad f(Z)=Z^c-p(Z),\qquad U_Z=Z^c.
\]

The natural paired matchings are

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z).
\]

If the lower endpoint \(f(Z)\) of the \(M_1\)-edge at \(U_Z\) is moved
to \(U_X\), incidence requires \(f(Z)\cap X=\varnothing\).  The new edge
must be different from the fixed \(M_0\)-edge at \(U_X\), which excludes
\(X=f^2(Z)\).  Excluding the old slot \(X=Z\) as well gives the exchange
digraph

\[
 Z\longrightarrow X
 \iff f(Z)\cap X=\varnothing,
       \quad X\notin\{Z,f^2(Z)\}.                          \tag{1.1}
\]

Since

\[
                         f(Z)^c=Z+p(Z),                     \tag{1.2}
\]

every nonloop candidate is the Johnson move

\[
                         X=Z-a+p(Z),\qquad a\in Z.          \tag{1.3}
\]

This confirms that the audited note uses the correct orientation: the tail
is the old \(M_1\)-slot and the head is its proposed new upper slot.

## 2. The unique star triangle

Fix \(C\in\binom{[n]}{r-1}\).  Its three forward-unmatched zeros give

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,                     \tag{2.1}
\]

where the \(D_i\) are Dyck words.  Put \(Z_i=C+z_i\).  Contracting the
matched pairs in all three blocks leaves \(100\) after \(z_i\) is flipped,
so

\[
                         r_+(Z_i)=z_{i+2}.                  \tag{2.2}
\]

Consequently the sole star candidate is

\[
                         Z_0\to Z_2\to Z_1\to Z_0.         \tag{2.3}
\]

There is no top-type directed triangle.  Indeed, if its three vertices were
the \(r\)-facets of one \((r+1)\)-set \(Q\), every directed source \(Z\)
would satisfy \(Z+p(Z)=Q\), hence \(f(Z)=Q^c\).  Two sources would then
have the same \(f\)-image, contrary to bijectivity.

These two observations exhaust all Johnson triangles and verify the local
classification.

## 3. Audit of the exceptional family

For \(u\notin C\), put

\[
 \alpha_C(u)=r_+(C+u),\qquad \beta_C(u)=r_-(C+u).
\]

The side \(Z_i\to Z_{i+2}\) of (2.3) is the forbidden fixed-matching edge
exactly when \(Z_{i+2}=f^2(Z_i)\).  With \(T=[n]\setminus C\),

\[
 f(Z_i)=T-\{z_i,z_{i+2}\},
\]

whereas

\[
 f^{-1}(Z_{i+2})
   =T-\{z_{i+2},\beta_C(z_{i+2})\}.
\]

Thus

\[
 Z_i\to Z_{i+2}\text{ is forbidden}
 \iff \beta_C(z_{i+2})=z_i.                               \tag{3.1}
\]

Set \(j=i+2\) and rotate \(C+z_j\) to

\[
 1D_j\,0_{z_{j+1}}D_{j+1}\,0_{z_{j+2}}D_{j+2}.           \tag{3.2}
\]

For a word of total height \(-1\), its reverse-unmatched zero is the
down-step following the rightmost global prefix maximum.  If
\(h_i=\operatorname {ht}(D_i)\), the three regional maxima in (3.2) are

\[
                         1+h_j,\qquad h_{j+1},qquad
                         h_{j+2}-1.                         \tag{3.3}
\]

The height just before \(z_{j+1}\) is one.  It is the rightmost global
maximum if and only if

\[
 D_j=D_{j+1}=\varnothing,qquad h_{j+2}\le1.              \tag{3.4}
\]

The equality case in the last region has been handled correctly: (3.3)
then gives height zero, strictly below the candidate maximum one.  By
contrast, a nonempty \(D_{j+1}\) reaches height one *after* the candidate
and therefore invalidates the rightmost condition.

The total semilength of the three blocks is \(r-1>0\).  Under (3.4), the
remaining block is the unique height-at-most-one Dyck word of that length,
namely \((10)^{r-1}\).  This proves (0.2).  Its final zero joins the initial
three zeros into a unique cyclic run of four zeros, so it has full period
\(n\); the number of labelled exceptional cores is exactly \(n\).

## 4. Physical packing audit

Let \({\cal H}_r\) have the centers \({\cal X}\) as vertices and the legal
triples \(\{C+z_0,C+z_1,C+z_2\}\) as hyperedges.  Two distinct triples
share at most one center, because two shared centers recover their common
intersection \(C\).  A fixed center \(Z\) can occur only for one of the
\(r\) cores \(Z-a\), \(a\in Z\).  Hence

\[
                         \Delta({\cal H}_r)\le r.           \tag{4.1}
\]

A greedy hypergraph matching therefore loses at most
\(1+3(r-1)=3r-2\) triples per choice, proving (0.3).

It is important that center-disjointness really is physical disjointness.
The six incidence vertices of the hexagon indexed by
\(\{Z_0,Z_1,Z_2\}\) are

\[
                         U_{Z_0},U_{Z_1},U_{Z_2},qquad
                         f(Z_0),f(Z_1),f(Z_2).              \tag{4.2}
\]

Both \(Z\mapsto U_Z\) and \(Z\mapsto f(Z)\) are bijections.  Therefore
two center-disjoint triples share neither an upper nor a lower incidence
vertex.  The denominator \(3r-2\), rather than the coarser \(6r-5\), is
valid.

## 5. Every center has a star candidate

### Lemma 5.1

Every \(Z\in{\cal X}\) lies in at least one (not necessarily legal) star
triangle from Section 2.

#### Proof

Rotate the deficit-one word of \(Z\) to its unique forward-unmatched zero:

\[
                              0_pD,                         \tag{5.1}
\]

where \(D\) is a nonempty Dyck word of semilength \(r\).  Let its first
symbol be \(1_a\), write \(D=1_aE\), and put \(C=Z-a\).  Then

\[
                              C=0_p0_aE.                     \tag{5.2}
\]

The word \(E\) has total height \(-1\), every prefix has height at least
\(-1\), and it ends in a zero.  Its ordinary forward reduction therefore
leaves one zero and no one.  The two displayed initial zeros cannot be
consumed.  Thus cyclic forward reduction of (5.2) leaves \(p,a\), and one
further zero.  In particular \(a\) is one of the three forward-unmatched
zeros of \(C\), so the star triple on \(C\) contains \(C+a=Z\). \(\square\)

Only the \(n\) exceptional triples are illegal.  They contain at most
\(3n\) distinct centers.  Lemma 5.1 consequently gives

\[
 \boxed{
 |\{Z:d_{{\cal H}_r}(Z)=0\}|\le3n.}                       \tag{5.3}
\]

An \(f\)-orbit has length \(\ell n\).  The cycles of \(f^{-2}\) on it
have length \(\ell n/\gcd(2,\ell)\), which is at least \(n\).  Therefore:

\[
 \boxed{
 \text{at most three PBBS monodromy components have no incident legal
 }C_6.}                                                     \tag{5.4}
\]

This does not say that a legal triangle incident with a component is
component-transversal; it may lie wholly inside that component.

The bound (5.4) can in fact be sharpened to zero for \(r\ge3\).

### Lemma 5.2 (exact center-activity classification)

Normalize \(Z\) as in (5.1), and factor its Dyck word into primitive
components

\[
                         D=P_1P_2\cdots P_k.                 \tag{5.5}
\]

An occupied coordinate \(x\) gives a star candidate containing \(Z\), with
core \(Z-x\), if and only if \(x\) is the first up-step of one of the
primitive factors \(P_j\).

For \(r\ge3\), the centers of legal degree zero are exactly the \(n\)
spatial phases whose normalized Dyck word is

\[
                         D=1(10)^{r-1}0.                     \tag{5.6}
\]

#### Proof

Before the changed up-step \(x\), the height of \(D\) is unchanged.  After
turning that up-step into a down-step, the suffix height is lowered by two.
The new down-step \(x\) is one of the forward-unmatched zeros precisely when
it makes the first new negative record, namely precisely when its old
preheight was zero.  These are exactly the first steps of the primitive
factors.

Write

\[
                         P_j=1A_j0.                          \tag{5.7}
\]

For the core obtained by changing its first step, the three Dyck blocks in
the deficit-three decomposition are

\[
 P_1\cdots P_{j-1},\qquad A_j,\qquad P_{j+1}\cdots P_k.     \tag{5.8}
\]

By the audited exceptional-core criterion, this candidate is illegal if and
only if two words in (5.8) are empty and the third has height at most one.
If \(k=1\), this is exactly (5.6).  If \(k\ge2\), it can occur only at an
endpoint factor \(P_j=10\), with every factor on the other side also equal
to \(10\).  Consequently the only additional possibility is
\(D=(10)^r\), and then only the first and last primitive factors are
illegal.  For \(r\ge3\), a middle factor gives a legal candidate.  This
proves the classification. \(\square\)

The canonical PBBS two-step quotient map sends (5.6) to

\[
 \tau\bigl(1(10)^{r-1}0\bigr)=1100(10)^{r-2}.               \tag{5.9}
\]

Indeed, the first step reaching the global maximum is the first one of the
displayed internal \((10)\)'s, the terminal outer zero is the first return
to height zero, and the first-deepest formula applies.  The word on the
right has more than one primitive factor and is neither \((10)^r\) nor
(5.6), so it has positive legal degree for \(r\ge3\).  Every degree-zero
center therefore has an active \(f^2\)-neighbor in its own monodromy
component.  Hence

\[
 \boxed{\text{every }f^{-2}\text{-component is incident with a legal }C_6
        \quad(r\ge3).}                                     \tag{5.10}
\]

Again, (5.10) is raw incidence only.  It does not say that the other two
vertices occupy two different components.

### Theorem 5.3 (no soliton-profile cut)

For \(r\ge4\), no nonempty proper union of complete PBBS soliton-profile
sectors is closed under the legal star triangles.

#### Proof

Use the iterated peak-pruning profile \({\bf a}\) from the audited PBBS
semiconjugacy.  Such profiles are naturally integer partitions of \(r\): a
concatenation of Dyck mountains

\[
                         M_s=1^s0^s
\]

with heights equal to the parts realizes every partition.  Concatenation
adds profiles, while wrapping a Dyck word of height \(h\) in \(1D0\) adds
one unit in pruning coordinate \(h+1\).  These are exactly the identities
proved in the action-profile audit of the star atlas.

Let \(\lambda\vdash r\) contain a part \(x\ge2\).  Make a core with blocks

\[
 D_0=M_{x-1},\qquad D_1=\varnothing,qquad
 D_2=\prod_{y\in\lambda\setminus\{x\}}M_y.                 \tag{5.11}
\]

One star vertex wraps \(D_0\), and hence has profile \(\lambda\).  A second
wraps the empty block, and hence has the profile

\[
                \lambda'=(\lambda\setminus\{x\})cup\{x-1,1\}.             \tag{5.12}
\]

The core is legal.  If \(D_2\ne\varnothing\), only one block is empty.  If
\(D_2=\varnothing\), then \(\lambda=(r)\) and the one nonempty block has
height \(r-1>1\), whereas the exceptional-core theorem requires height at
most one.

Thus every profile with a part at least two is joined by a legal triangle
to the profile obtained by splitting off a part one.  Iteration reaches
\((1,1,\ldots,1)\).  The undirected profile quotient is connected, proving
the assertion. \(\square\)

This theorem eliminates every obstruction depending only on the conserved
PBBS action/soliton partition.  A surviving closed union, if one exists,
must distinguish the phase or rigging components inside at least one common
profile.

## 6. No proper monodromy union is exchange-closed

Let \(O_r=KG(2r+1,r)\).  It is connected: every Johnson move
\(A\to A-a+b\) lifts to a two-edge walk through the unique \(r\)-set
disjoint from both endpoints, and the Johnson graph is connected.  It is
nonbipartite: the sets

\[
 A_i=\{i,i+2,\ldots,i+2(r-1)\}\pmod n
\]

form an odd \(n\)-cycle.

### Lemma 6.1 (strict neighbor inequality)

In a connected, nonbipartite, regular graph \(G\), every nonempty proper
vertex set \(A\) satisfies

\[
                              |N_G(A)|>|A|.                  \tag{6.1}
\]

#### Proof

Regularity gives \(|N(A)|\ge|A|\) by counting all oriented edges out of
\(A\).  If equality held, all degree capacity in \(N(A)\) would be filled
by edges from \(A\), so \(N(N(A))=A\).  Thus \(A\cup N(A)\) is closed.
Connectedness makes it the whole vertex set.  If \(A\cap N(A)\ne\varnothing\),
that intersection is itself closed, forcing \(A=N(A)=V(G)\).  If the
intersection is empty, \(A,N(A)\) form a bipartition.  Both alternatives
contradict the hypotheses. \(\square\)

Identify the paired monodromy components with the cycles of \(f^{-2}\) on
\({\cal X}\), and let \(S\) be a nonempty proper union of them.  Then
\(f^2(S)=S\).  Suppose that the exchange digraph (1.1) had no arc from
\(S\) to its complement.  For each \(Z\in S\), all \(r+1\) odd-graph
neighbors of \(f(Z)\) are

\[
 Z,\quad f^2(Z),\quad\text{and the }r-1\text{ exchange outneighbors of }Z.
\]

They would all belong to \(S\), so

\[
                              N_{O_r}(f(S))\subseteq S.      \tag{6.2}
\]

But \(|f(S)|=|S|\), and Lemma 6.1 makes (6.2) impossible for proper
\(S\).  Hence

\[
 \boxed{
 e_{D_f}(S,{\cal X}\setminus S)>0
 \quad\text{for every proper union of monodromy components}.}             \tag{6.3}
\]

The exchange digraph is \((r-1)\)-in/out-regular.  Consequently every one
of its arcs belongs to a directed circuit: the condensation of a balanced
digraph has no nontrivial source or sink.  Thus (6.3) also supplies an
alternating circuit crossing every proper component union.

No length bound follows.  Moreover the monodromy derivative of a crossing
circuit need not reduce the number of cycles.  Therefore (6.3) is not the
missing \(O(B)\)-edit theorem.

## 7. Exact invariant and remaining lemma

A \(C_6\) switch left-multiplies the monodromy by a three-cycle.  It follows
that

\[
                              c(F)\pmod2                    \tag{7.1}
\]

is invariant under every sequence of paired hexagon switches.  Initially

\[
                              c(F_{\rm PBBS})\equiv B\pmod2,
\]

whereas a Hamilton factor has one component.  Hence a \(C_6\)-only
Hamiltonization is impossible whenever \(B\) is even.  At least one legal
even circuit is then necessary.  The separately proved and independently
audited \(2n\)-slot directed bridge supplies exactly this parity change at
cost \(O(r)=o(B)\); parity is therefore no longer the construction gate.

There is no separate coordinate-count obstruction.  In every perfect
matching between ranks \(r\) and \(r+1\), the number of matched edges whose
added coordinate is a fixed \(x\) is forced to be

\[
 \binom{2r}{r}-\binom{2r}{r-1}
 =\operatorname {Cat}_r=B.                                 \tag{7.2}
\]

Thus the PBBS coordinate homomesy agrees with a universal matching identity
and cannot distinguish it from a Hamilton paired state.

There is a sharper sufficient gate for ordinary quotient connectivity.
Let

\[
                         \Psi({\bf a})=\sum_{s\ge1}(s-1)a_s.
\]

Suppose every nonalternating \(f^{-2}\)-component contains a normalized
state

\[
                         D=1A0Q,\qquad A\ne\varnothing,     \tag{7.3}
\]

whose first-primitive-factor star is legal.  That star joins the old profile

\[
 {f a}(A)+{f a}(Q)+{f e}_{\operatorname {ht}(A)+1}
\]

to the empty-wrap profile

\[
                         {f a}(A)+{f a}(Q)+{f e}_1,
\]

strictly decreasing \(\Psi\).  The unique zero-profile sector consists of
the rotations of the alternating word and is one \(f^{-2}\)-component.
Induction would therefore prove connectivity of the component quotient.
Call (7.3) the **descending-portal lemma**.  It is unproved; unlike raw
component activity, it is a statement about the phase/rigging chronology of
each individual PBBS orbit.

The final Hamiltonization hypothesis is consequently not local supply,
packing, parity, a conserved-action cut, or a sealed exchange cut.  It is
the following construction-specific routing statement:

> The explicit legal-star hypergraph has a dynamically compatible,
> component-transversal loose forest after the optional explicit parity
> bridge, reducing all \(f^{-2}\)-cycles to one component.  The total number
> of changed matching slots is \(O(B)\).

That hypothesis implies an \(O(B)\)-edit Hamiltonization and hence preserves
the centered PBBS triple-union defect at \(O(B)\).  It remains unproved.
