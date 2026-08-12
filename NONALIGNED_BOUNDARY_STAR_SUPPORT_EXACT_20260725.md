# Exact boundary-star enumeration for arbitrary-support seed invariance

Date: 2026-07-25

Method: pure combinatorics and generating functions only.

## 0. Outcome

This report gives both requested sides of the arbitrary-support gate:

* an exact theorem for every transposition graph, reducing multistep seed
  survival to unions of graph components;
* an explicit nonaligned connected support whose invariant suspended-seed
  count is known in closed form, falls below the FSP scale on logarithmic
  support, and becomes exactly zero on support (m-2).

Retain

\[
 n=2m+1,
\]

the canonical MSW factor, and the complete suspended-seed universe

\[
 \{UAV,UBV,UDDV\},
 \qquad U\in\mathcal D_u,\quad V\in\mathcal D_v,\quad u+v=m-4.
                                                                    \tag{0.1}
\]

Its common finite-coordinate lower-target word is

\[
 \ell(U,V)=U\,S_0\,\overline V,
 \qquad S_0=01000010,                                           \tag{0.2}
\]

and every target also contains the distinguished coordinate
(\infty).

Choose integers (k,j\ge0), put

\[
 b=1+k+j,
\]

and let the connected support be

\[
 B_{k,j}
 =\{\infty\}
  \cup\{1,2,\ldots,k\}
  \cup\{2m-j+1,\ldots,2m\}.                                   \tag{0.3}
\]

Take any tree of coordinate transpositions on (B_{k,j}), for example
the star centred at \(\infty\).  This support is nonaligned in the exact
sense excluded from the earlier aligned-prefix theorem: it contains the
distinguished coordinate, and for (j>0) it simultaneously uses both
ends of the finite-coordinate line.

Let (K_{m;b}) count pairs ((U,V)) in (0.1) whose target is invariant
under \(\operatorname{Sym}(B_{k,j})\).  Then the count depends only on
(b=1+k+j), not on the split between the two ends, and is

\[
 \boxed{
 K_{m;b}
 =[z^{m-b-3}]C(z)^{b+1}.
 }                                                               \tag{0.4}
\]

Equivalently, when (0\le b\le m-3),

\[
 \boxed{
 K_{m;b}
 =\frac{b+1}{2m-b-5}
   \binom{2m-b-5}{m-b-3}.
 }                                                               \tag{0.5}
\]

The boundary cases are especially informative:

\[
 \boxed{K_{m;m-3}=1,\qquad K_{m;b}=0\quad(b\ge m-2).}            \tag{0.6}
\]

Thus the explicit connected support

\[
 \{\infty,1,2,\ldots,m-4,2m\}
\]

has size (m-2), uses only (m-3) transpositions, and kills **every**
target in the complete suspended-copy universe of the audited seed.

Uniformly for (b=o(\sqrt m)),

\[
 \boxed{
 \frac{K_{m;b}}{\operatorname{Cat}_m}
 =\frac{b+1}{64\,2^b}
  \left(1+O\left(\frac{(b+1)^2}{m}\right)\right).
 }                                                               \tag{0.7}
\]

Consequently already

\[
 \boxed{
 \frac{2^b}{b+1}\gg\sqrt m
 }                                                               \tag{0.8}
\]

makes *all invariant copies of this seed*, not just one selected matching,
number

\[
 o(\!\operatorname{Cat}_m/\sqrt m).
\]

The logarithmic threshold is therefore real for a fixed canonical
labelling; it is not an artefact of the earlier simultaneous relabelling
argument.

There is an even sharper existential bound which keeps the canonical
factor fixed.  Among all connected supports (B) of size (b) containing
(\infty), some support satisfies

\[
 \boxed{
 K_m(B)
 \le \operatorname{Cat}_{m-3}
 \frac{\binom{m-2}{b-1}}{\binom{2m}{b-1}}.
 }                                                               \tag{0.9}
\]

Uniformly for (b=o(\sqrt m)), the last ratio is

\[
 2^{1-b}\left(1+O(b^2/m)\right).                                \tag{0.10}
\]

Thus there are fixed-labelling nonaligned supports for which merely

\[
 2^b\gg\sqrt m                                                  \tag{0.11}
\]

drives the complete invariant suspended-seed universe below the FSP
scale.  Unlike the earlier relabelling-average theorem, (0.9) changes the
support while leaving the canonical factor untouched.

## 1. The exact graph-invariance theorem

Let (T) be an arbitrary set of coordinate transpositions, let
(G_T) be their graph on ([n]), and let its connected components be

\[
 \mathcal C(T)=\{C_1,\ldots,C_r\}.
\]

The generated coordinate group is

\[
 \langle T\rangle
 =\operatorname{Sym}(C_1)\times\cdots\times
  \operatorname{Sym}(C_r).                                     \tag{1.1}
\]

### Theorem 1.1 -- component-union criterion

A Boolean target (S\subseteq[n]) is fixed by every permutation in
(\langle T\rangle) if and only if

\[
 \boxed{
 S\text{ is a union of connected components of }G_T.
 }                                                               \tag{1.2}
\]

If an initial exact factor contains three distinct rows owning such an
(S), then after every finite adaptive sequence of exact component
switches using transpositions from (T), the three row descendants remain
distinct and all own (S).

#### Proof

On one connected component (C_i), the edge transpositions generate the
full symmetric group.  Its only invariant subsets of (C_i) are
(\varnothing) and (C_i), proving (1.2).

The bijective row-lineage theorem gives each initial row (E) one final
descendant (g_EE), with (g_E\in\langle T\rangle).  If (E) owns
(S), then (g_EE) owns (g_ES=S).  Bijective lineage preserves
distinctness of the three rows. \(\square\)

Thus, for any fixed row-disjoint canonical seed matching
(\mathscr M), the strongest lower bound supplied solely by
group-invariant lineage is exactly

\[
 \#\{P\in\mathscr M:
       \text{the common target of }P
       \text{ is a union of }T\text{-components}\}.             \tag{1.3}
\]

No relabelling is implicit in (1.3): both the canonical factor and the
coordinate graph retain their given labels.

## 2. Exact enumeration for the boundary star

Because every target (0.2) contains \(\infty\), invariance under the
connected component (B_{k,j}) is equivalent to containing all of
(B_{k,j}).  On finite-coordinate words this says

\[
 \ell(U,V)_1=\cdots=\ell(U,V)_k=1                              \tag{2.1}
\]

and

\[
 \ell(U,V)_{2m-j+1}=\cdots=\ell(U,V)_{2m}=1.                   \tag{2.2}
\]

Since the first bit of (S_0) is zero, (2.1) holds exactly when the
Dyck word (U) begins with (k) up-steps.  Put

\[
 V^*=\operatorname{rev}(\overline V).
\]

This is again a Dyck word.  Condition (2.2) holds exactly when (V^*)
begins with (j) up-steps.

The generating function for Dyck words beginning with (a) prescribed
up-steps is

\[
 \boxed{z^aC(z)^{a+1}.}                                        \tag{2.3}
\]

One proof repeatedly removes the first up-step and decomposes at the
matching down-step; the (a) nested arches expose (a+1) arbitrary Dyck
gaps.

The prefix (U) therefore contributes (z^kC^{k+1}), the transformed
suffix (V^*) contributes (z^jC^{j+1}), and the fixed seed contributes
(z^4).  Their product is

\[
 z^{k+j+4}C^{k+j+2}
 =z^{b+3}C^{b+1}.                                               \tag{2.4}
\]

Extracting total semilength (m) proves (0.4).  The generalized Catalan
identity

\[
 [z^a]C(z)^r
 =\frac r{2a+r}\binom{2a+r}{a}                                \tag{2.5}
\]

gives (0.5).  If (b=m-3), (0.4) is the constant coefficient of
(C^{m-2}), namely one.  If (b\ge m-2), the requested coefficient has
negative index and is zero.  This proves (0.6).

## 3. Uniform asymptotics

Put

\[
 a=m-b-3,
 \qquad r=b+1.
\]

Using (0.5) and

\[
 \operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m},
\]

write the quotient as a product of (O(b)) factors.  Uniformly for
(b=o(\sqrt m)), Taylor expansion of their logarithms gives an accumulated
relative error

\[
 1+O((b+1)^2/m).
\]

The leading powers are equivalently read from the square-root singularity
of (C):

\[
 [z^{m-b-3}]C^{b+1}
 \sim (b+1)2^b4^{-(b+3)}\operatorname{Cat}_m.
\]

Since

\[
 (b+1)2^b4^{-(b+3)}
 =\frac{b+1}{64\,2^b},
\]

this proves (0.7).  Equation (0.8) follows immediately.

## 3.1 Averaging the support, not the factor

Let (B=\{\infty\}\cup R), where (R) is a uniformly random
((b-1))-subset of the (2m) finite coordinates, and connect (B) by an
arbitrary tree of transpositions.  A suspended-seed target has finite part
of size exactly (m-2).  Since it contains (\infty), it is invariant
under \(\operatorname{Sym}(B)\) exactly when (R) is contained in that
finite part.  For every one of the

\[
 \sum_{u+v=m-4}\operatorname{Cat}_u\operatorname{Cat}_v
 =\operatorname{Cat}_{m-3}
\]

suspended pairs, this event has probability

\[
 \frac{\binom{m-2}{b-1}}{\binom{2m}{b-1}}.                      \tag{3.1}
\]

Linearity of expectation proves that some fixed (R) satisfies (0.9).
No target distinctness is needed: the count is over suspended pairs, so it
is already an upper bound for every row-disjoint submatching.

Finally,

\[
 \frac{\binom{m-2}{b-1}}{\binom{2m}{b-1}}
 =\prod_{i=0}^{b-2}\frac{m-2-i}{2m-i}
 =2^{1-b}\left(1+O(b^2/m)\right)
\]

uniformly for (b=o(\sqrt m)).  This proves (0.10)--(0.11).

## 4. Consequences and limitations

Theorems 1.1 and (0.4) give a precise answer for one explicit nonaligned
support geometry:

* with (b\asymp\frac12\log_2m), invariant copies approach the FSP
  threshold;
* with (b\ge m-2), the complete suspended-seed universe contains no
  invariant target at all;
* every adaptive choice of exact-factor component signs is already
  included, because the argument uses only the generated coordinate group.

This refutes any proposed lower bound depending only on the number of
switch steps while ignoring their generated component geometry.  It also
shows why an existential common relabelling is not a uniform theorem for
one fixed canonical factor.

What it does not prove is equally important.  When a target is not
(G_T)-invariant, the three row-dependent images may still coincide by a
mechanism not visible to invariant lineage.  Other collision seeds and
deeper ranks may also survive.  Hence the boundary star is an escape from
this **certificate**, not a construction of an FSP endpoint.

The next travel-between-cubes theorem must therefore charge either

1. recoalescence of non-invariant row images;
2. the simultaneous destruction of many differently positioned seeds; or
3. an intrinsic distance/cost for growing the transposition graph from one
   conjugate cube to the next.

## 5. Exact random-placement law for every component structure

There is a clean generalization which quantifies the role of the number of
transpositions.

Fix an abstract transposition graph whose nontrivial connected components
have sizes

\[
 s_1,\ldots,s_k\ge2,
 \qquad b=s_1+\cdots+s_k.
\]

Place its (b) vertices uniformly without replacement on ([n]), leaving
the other (n-b) coordinates isolated.  For one fixed rank-(r) target
(S), the probability that (S) is a union of graph components is

\[
 \boxed{
 p_{n,r}(s_1,\ldots,s_k)
 =\frac{[x^r](1+x)^{n-b}\prod_{i=1}^k(1+x^{s_i})}
        {\binom nr}.
 }                                                               \tag{5.1}
\]

Indeed, choose a subfamily (J\subseteq[k]) of nontrivial components to
place inside (S).  Their total size is

\[
 a_J=\sum_{i\in J}s_i,
\]

and the remaining (r-a_J) elements of (S) must be isolated vertices.
Summing

\[
 \binom{n-b}{r-a_J}
\]

over (J) gives (5.1).

For the depth-one rank

\[
 r=m-1,\qquad n=2m+1,
\]

and uniformly for (b=o(\sqrt m)), each summand obeys

\[
 \frac{\binom{n-b}{r-a_J}}{\binom nr}
 =\frac{(r)_{a_J}(n-r)_{b-a_J}}{(n)_b}
 =2^{-b}\left(1+O(b^2/m)\right).                               \tag{5.2}
\]

There are (2^k) choices of (J).  Hence

\[
 \boxed{
 p_{2m+1,m-1}(s_1,\ldots,s_k)
 =2^{k-b}\left(1+O(b^2/m)\right).
 }                                                               \tag{5.3}
\]

Let

\[
 d=b-k.
\]

This is the rank of a spanning forest of the nontrivial component graph,
or equivalently the number of independent equality constraints imposed on
a Boolean target.  Formula (5.3) is simply

\[
 p=2^{-d}(1+O(b^2/m)).                                         \tag{5.4}
\]

Apply linearity of expectation to the complete suspended-seed universe,
which has (operatorname{Cat}_{m-3}) indexed pairs.  Some fixed placement
of the abstract graph therefore satisfies

\[
 \boxed{
 K_m(T)
 \le
 p_{2m+1,m-1}(s_1,\ldots,s_k)\operatorname{Cat}_{m-3}.
 }                                                               \tag{5.5}
\]

This again keeps the canonical factor fixed and moves only the switch
support.

Consequences:

* a matching of (s) transpositions has (d=s), explaining the
  (2^{-s}) scale in the explicit reflection construction;
* one connected component on (b) coordinates has (d=b-1), explaining
  the (2^{1-b}) scale in (0.9);
* a forest with (e) edges has (d=e), so a suitable placement of only
  
  \[
  e=\frac12\log_2m+\omega(1)
  \]

  transpositions already pushes the **entire invariant suspended-seed
  universe** below (operatorname{Cat}_m/\sqrt m), provided its support
  remains (o(\sqrt m)).

Thus the best possible uniform lower bound based only on the abstract
support/component sizes cannot exceed the right side of (5.5).  Any
stronger travel obstruction must use the actual legal coupling of row
lineages, not merely the number of invariant target cuts.

## 6. Escape from every preselected packet packing

The random-placement law is not special to the audited seed.

Let (F) be any exact factor with (t=operatorname{Cat}_m) rows, and
let (mathscr P) be any preselected fractional packing of packets whose
resources all lie in rank (r).  Give packet (P) weight (w_P\ge0), and
assume row congestion at most one:

\[
 \sum_{P\ni E}w_P\le1
 \qquad(E\in F).                                                \tag{6.1}
\]

Every packet has at least two rows.  Double counting row--packet
incidences gives

\[
 \sum_{P\in\mathscr P}w_P\le\frac t2.                          \tag{6.2}
\]

Randomly place an abstract transposition graph with component sizes
(s_1,\ldots,s_k).  For every fixed packet target, the probability of
being invariant is the same number (p_{n,r}(s_1,\ldots,s_k)) in (5.1).
Therefore

\[
 \mathbb E
 \sum_{\substack{P\in\mathscr P\\
                   \text{target}(P)\text{ invariant}}}w_P
 =p_{n,r}(s_1,\ldots,s_k)
  \sum_{P\in\mathscr P}w_P.                                   \tag{6.3}
\]

Some fixed placement consequently satisfies

\[
 \boxed{
 \sum_{P:\,\text{target}(P)\text{ invariant}}w_P
 \le \frac t2,p_{n,r}(s_1,\ldots,s_k).
 }                                                               \tag{6.4}
\]

At depth one, a forest of (e=o(\sqrt m)) suitably placed transpositions
has (p=2^{-e}(1+o(1))).  Thus

\[
 e=\frac12\log_2m+\omega(1)                                   \tag{6.5}
\]

drives the invariant part of **every packet packing selected before the
support is placed** to (o(t/\sqrt m)).

The order of quantifiers matters.  Equation (6.4) does not exclude a new
packing chosen after seeing the support graph.  The suspended-seed universe
bound (5.5) is stronger for that particular seed because it controls all
of its submatchings simultaneously.  A genuinely uniform obstruction must
likewise construct its packet resources in response to the support, or
prove a min--max theorem coupling all supports at once.

## 7. An adaptive bound for all invariant depth-one packets

At the cost of one additional factor (n), the quantifiers can be reversed
completely.

Let (F) be any exact factor, and let (mu_1(S)) be the number of its rows
owning the depth-one target (S).  Every row owns exactly (n) cyclic
depth-one intervals, so

\[
 \sum_{S\in\binom{[n]}{m-1}}\mu_1(S)=nt=W.                     \tag{7.1}
\]

For a randomly placed abstract transposition graph, each fixed target is
invariant with probability (p=p_{n,m-1}(s_1,\ldots,s_k)).  Therefore

\[
 \mathbb E
 \sum_{S\text{ invariant}}\mu_1(S)
 =pW.                                                           \tag{7.2}
\]

Some fixed placement has invariant owner-incidence mass at most (pW).
Now reveal that placement and allow an adversary to choose an arbitrary
fractional packet packing supported on **all** invariant depth-one targets.
Each packet consumes at least two owner incidences.  Hence its total weight
is at most

\[
 \boxed{
 \frac12\sum_{S\text{ invariant}}\mu_1(S)
 \le\frac{pW}{2}.
 }                                                               \tag{7.3}
\]

This controls the optimum packing chosen *after* the support is known; no
seed catalogue is fixed in advance.

For a forest of (e=o(\sqrt m)) transpositions, (p=2^{-e}(1+o(1))).
Since (W=nt), condition

\[
 \boxed{
 2^e\gg n\sqrt m
 }                                                               \tag{7.4}
\]

makes (7.3) (o(t/\sqrt m)).  Equivalently it is enough to take

\[
 \boxed{
 e=\frac32\log_2m+\omega(1).
 }                                                               \tag{7.5}
\]

Thus a suitably placed (O(\log m))-edge support graph defeats **every
possible invariant-target packet packing at depth one**, even when the
packing is selected adaptively after the graph is exposed.

This still does not construct a good switched factor.  It proves something
more sharply delimited: after (7.5), no proof based solely on targets fixed
by the generated coordinate group can reach the FSP scale.  Any remaining
packet obstruction must come from non-invariant targets whose row-dependent
images recoalesce.

## 8. Sharp row-activation bound: half-logarithmic support already suffices

The incidence estimate in Section 7 is deliberately crude: it counts all
(n) depth-one targets of a row separately.  Their cyclic geometry removes
that factor (n).

Fix **any** exact factor (F), not necessarily canonical, and choose a
uniformly random (b)-subset (B\subset[n]).  Connect (B) by a tree of
coordinate transpositions, so the generated group on (B) is
(\operatorname{Sym}(B)).

Call a row (E\in F) (B)-active if it owns at least one depth-one target
which is invariant under (operatorname{Sym}(B)).

### Theorem 8.1 -- cyclic semicircle bound

For every row (E),

\[
 \Pr_B(E\text{ is }B\text{-active})
 \le
 b\frac{\binom{m+1}{b-1}}{\binom{2m}{b-1}}.                    \tag{8.1}
\]

Consequently some connected support (B) of size (b) satisfies

\[
 \boxed{
 \#\{E\in F:E\text{ is }B\text{-active}\}
 \le
 b\frac{\binom{m+1}{b-1}}{\binom{2m}{b-1}}\operatorname{Cat}_m.
 }                                                               \tag{8.2}
\]

After this (B) is revealed, allow an adversary to choose arbitrary
balanced depth-one quotas and the optimum fractional packing of **all**
packets on (B)-invariant targets.  Its value is at most

\[
 \boxed{
 \frac b2
 \frac{\binom{m+1}{b-1}}{\binom{2m}{b-1}}
 \operatorname{Cat}_m.
 }                                                               \tag{8.3}
\]

Uniformly for (b=o(\sqrt m)), this is

\[
 \boxed{
 \left(b2^{-b}+o(b2^{-b})\right)\operatorname{Cat}_m.
 }                                                               \tag{8.4}
\]

In particular,

\[
 \boxed{
 \frac{2^b}{b}\gg\sqrt m
 }                                                               \tag{8.5}
\]

makes the optimum adaptive invariant-target packing

\[
 o(\!\operatorname{Cat}_m/\sqrt m).
\]

Thus

\[
 b=\frac12\log_2m+\log_2\log m+\omega(1)                      \tag{8.6}
\]

is more than enough.  The support uses only (b-1) transpositions.

#### Proof

Represent the row (E) by its cyclic coordinate order.  Its depth-one
targets are exactly the (n) cyclic intervals of length

\[
 r=m-1.
\]

Such a target (S) is invariant under (operatorname{Sym}(B)) exactly
when either (B\subseteq S) or (B\cap S=\varnothing).

Put

\[
 \ell=n-r=m+2.
\]

If (B\subseteq S), then (B) is contained in an (r)-arc and hence in
an (ell)-arc.  If (B\cap S=\varnothing), then (B\subseteq S^c),
which is itself an (ell)-arc.  Conversely, if (B) is contained in an
(ell)-arc (J), then its complementary (r)-arc is a depth-one target
of (E) disjoint from (B).  Therefore

\[
 E\text{ is }B\text{-active}
 \quad\Longleftrightarrow\quad
 B\text{ lies in some cyclic }(m+2)\text{-arc of }E.            \tag{8.7}
\]

If a (b)-set lies in such an arc, one of its (b) points may be chosen
as the first occupied point of an oriented containing arc; all other
(b-1) points then lie among the next (m+1) cyclic positions.  Counting
the distinguished first point and using a union bound gives at most

\[
 n\binom{m+1}{b-1}
\]

pointed candidates.  Dividing by

\[
 \binom nb
 =\frac nb\binom{n-1}{b-1}
\]

proves (8.1).

Summing (8.1) over the (t=operatorname{Cat}_m) rows and applying
linearity of expectation gives (8.2) for some (B).

Every packet on a (B)-invariant target uses at least two (B)-active
rows.  Under row congestion one, twice the total fractional packing weight
is at most the number of active rows.  This proves (8.3).

Finally,

\[
 \frac{\binom{m+1}{b-1}}{\binom{2m}{b-1}}
 =\prod_{i=0}^{b-2}\frac{m+1-i}{2m-i}
 =2^{1-b}\left(1+O(b^2/m)\right),                              \tag{8.8}
\]

and substitution in (8.3) proves (8.4)--(8.6). \(\square\)

### Interpretation

Theorem 8.1 has the fully adversarial order of quantifiers relevant to the
gate:

\[
 \forall F\quad\exists B\quad\forall
 \text{ invariant-target packet packings}.
\]

It is independent of the canonical seed, the MSW labelling, and the quota
choice.  Therefore a uniform arbitrary-support obstruction cannot be based
solely on targets fixed by the generated coordinate group once the support
reaches the half-logarithmic scale (8.6).

What remains possible is precisely the mechanism excluded from this
count: non-invariant targets may have row-dependent images that collide
again.  Proving or disproving that recoalescence is now the exact next
travel-between-cubes problem.
