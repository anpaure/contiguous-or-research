# Protected two-factor completion needs an age-filtered second matching

**Date:** 2026-08-07  
**Status:** exact resident-factor reduction and generic post-completion
no-go.  Ordinary protected two-factor existence does not imply that its
components can be oriented, reordered, or opened into a resident owner
chronology.  After fixing one matching phase and signed owner ages,
resident completion is exactly one forced perfect-matching Hall problem
in an age-filtered successor graph.

## 1. Outcome

Work in

\[
 G=ML_{m+1}=(X,Y;E),
\qquad
 X=\binom{[2m+1]}m,\quad
 Y=\binom{[2m+1]}{m+1},
\tag{1.1}
\]

and put

\[
 r=m+1,\qquad |X|=|Y|=W,\qquad L=d+2.
\tag{1.2}
\]

The new \(C_4\)--spectral protected-factor theorem proves that the complete
clean packet bank is contained in some spanning two-factor for every
sufficiently large optimal parameter.  That closes the uncoloured factor
cut.

Residence is not a property of the uncoloured degree sequence.  It is a
spacing condition on the directed Johnson exchanges around every factor
component.  Rotation or reversal of a closed component preserves all
cyclic run lengths.  Opening an intact component can hide or merge only
the runs meeting its chosen cut; every other short run survives.

The proof-safe replacement for an ordinary factor cut is therefore:

\[
 \boxed{
 \text{choose one factor matching phase and signed ages, then satisfy
 Hall in the age-compatible residual successor graph}.}
\tag{1.3}
\]

This note proves that criterion exactly.

## 2. Two-matching normal form for a factor

Every spanning two-factor of the bipartite graph \(G\) is a disjoint union
of even cycles and hence decomposes into two perfect matchings

\[
 F=M_0\mathbin{\dot\cup}M_1.
\tag{2.1}
\]

Fix \(M_0\).  Regard it as a bijection \(M_0:X\to Y\).  Define a directed
bipartite successor graph \(D_{M_0}\) with a tail and a head copy of \(X\):

\[
 T\longrightarrow T'
 \quad\Longleftrightarrow\quad
 T'\subset M_0(T),\qquad T'\ne T.
\tag{2.2}
\]

Every tail and every head has degree

\[
 r-1=m.
\tag{2.3}
\]

Indeed, \(M_0(T)\) has \(r\) rank-\(m\) subsets, one of which is \(T\);
dually a fixed head \(T'\) lies below \(r\) upper vertices, and the one
matched to \(T'\) corresponds to the excluded self arc.

A perfect matching \(N\) of \(D_{M_0}\) defines

\[
 M_1=\{\,M_0(T)T':(T,T')\in N\,\}.
\tag{2.4}
\]

Then \(M_1\) is a perfect matching of \(G\), disjoint from \(M_0\), and
\(M_0\cup M_1\) is a spanning two-factor.  Its oriented owner successor
permutation is

\[
 \sigma_N(T)=T'.
\tag{2.5}
\]

Conversely, every factor decomposition (2.1), after orienting its cycles,
arises this way.

A directed clean packet path

\[
 T_-\subset J_-\supset T_0
       \subset J_+\supset T_+
\tag{2.6}
\]

can be phased so that

\[
 T_-J_-,\ T_0J_+\in M_0,
\qquad
 J_-T_0,\ J_+T_+\in M_1.
\tag{2.7}
\]

Thus its two owner transitions become the forced successor arcs

\[
 T_-\longrightarrow T_0,\qquad
 T_0\longrightarrow T_+.
\tag{2.8}
\]

For a resource-disjoint packet bank these arcs form a matching between
the tail and head copies of \(X\), although the head of the first arc is
the tail of the second in the un-split owner set.

## 3. Why post-hoc component ordering fails generically

Let \(I\) be any rank-\((m-1)\) set and let \(a,b,c\notin I\) be distinct.
The owners

\[
 I\cup\{a\},\qquad I\cup\{b\},\qquad I\cup\{c\}
\tag{3.1}
\]

together with their three pairwise unions form a six-cycle in \(G\).
Its projected owner component is a triangle.

For coordinate \(a\), the cyclic owner trace is \(100\), up to rotation;
the analogous statement holds for \(b\) and \(c\).  Hence the component
has positive runs of length one and negative runs of length two.  It is
not \(L\)-biresident for any \(L\ge3\).

Rotation and reversal do not change those cyclic run lengths.  If the
triangle is opened into a three-owner linear path, at most two of
\(a,b,c\) can place their singleton positive runs at the two global
endpoints.  The third remains an internal singleton.  Thus no orientation,
rotation, or intact-component ordering makes this component resident.

Moreover, if the six-cycle is protected, every one of its vertices already
has degree two inside the protected graph.  Every spanning two-factor
completion retains it as a separate component.  The ordinary protected
extension theorem applies to such a constant-size protected cycle for
large \(m\).  It can also be added disjointly to the \(O(m)\)-edge clean
packet bank while remaining below the theorem's fixed
\(\alpha r<r\) edge budget.

Therefore:

\[
 \boxed{
 \text{a spanning two-factor containing the clean bank need not admit
 any resident post-hoc ordering of its intact components}.}
\tag{3.2}
\]

The example does not say that every completion is bad.  It proves that
ordinary factor existence and arbitrary post-processing are insufficient;
residence must be imposed during factor selection or by a further
edge-changing rethread.

## 4. Exact signed-age state

For each owner \(T\in X\) and coordinate \(z\in[2m+1]\), a signed capped
age state consists of

\[
 \epsilon_T(z)=\mathbf1_{\{z\in T\}},
\qquad
 \alpha_T(z)\in\{1,\ldots,L\}.
\tag{4.1}
\]

Here age \(L\) means “at least \(L\).”  If

\[
 T'=T-x+y,
\tag{4.2}
\]

call the directed arc \(T\to T'\) **age-legal** when

\[
 \begin{array}{c|c|c}
 \text{coordinate}&(\epsilon_T,\alpha_T)&
                    (\epsilon_{T'},\alpha_{T'})\\ \hline
 x&(1,L)&(0,1)\\
 y&(0,L)&(1,1)\\
 z\notin\{x,y\}&(\epsilon,\alpha)&
                    (\epsilon,\min\{L,\alpha+1\}).
 \end{array}
\tag{4.3}
\]

Let

\[
 D_{M_0,\alpha}\subseteq D_{M_0}
\tag{4.4}
\]

be the subgraph consisting of the age-legal arcs.

### Lemma 4.1 (age legality is exact)

Let \(N\) be a perfect matching of \(D_{M_0,\alpha}\).  Every owner cycle
of the factor \(M_0\cup M_1(N)\) has all positive and negative coordinate
runs of length at least \(L\).

Conversely, every oriented \(L\)-biresident spanning two-factor has a
decomposition \(M_0\cup M_1\) and actual capped ages \(\alpha\) for which
its successor matching lies in \(D_{M_0,\alpha}\).

#### Proof

Along every selected successor arc, (4.3) is exactly the deterministic
capped run-age update.  A sign change is permitted only from age \(L\),
so every closed run has length at least \(L\).  Since the same state
\(\alpha_T\) is used by the incoming and outgoing arcs at owner \(T\),
the update closes consistently around every permutation cycle.

If a coordinate never changes sign on a component, cyclic consistency
forces its age to be \(L\), which correctly represents the all-constant
trace.

Conversely, orient the resident factor components and alternately colour
their incidence edges \(M_0,M_1\).  Record the actual signed capped age at
each owner.  Every successor transition obeys (4.3), so its arc lies in
\(D_{M_0,\alpha}\).  \(\square\)

For a clean packet, its fixed-core collar determines legal incoming and
outgoing ages for the exchanged labels.  Merely protecting (2.6) does not
carry those ages.  A resident completion must choose \(\alpha\) so that
the forced arcs (2.8) lie in \(D_{M_0,\alpha}\), with the collar's
source-tail halo imposed separately.

## 5. Age-filtered protected completion theorem

Let

\[
 Q\subseteq D_{M_0,\alpha}
\tag{5.1}
\]

be a forced matching of successor arcs.  Write \(Z_Q\) for its tail set
and \(H_Q\) for its head set.

### Theorem 5.1 (exact resident completion cut)

There is an \(L\)-biresident spanning two-factor

\[
 F=M_0\cup M_1
\tag{5.2}
\]

whose directed successor matching contains \(Q\) and whose owner ages are
\(\alpha\) if and only if

\[
 \boxed{
 |N_{D_{M_0,\alpha}}(S)\setminus H_Q|
 \ge |S|
 \qquad
 (S\subseteq X\setminus Z_Q).}
\tag{5.3}
\]

When (5.3) holds, the completion is integral.

#### Proof

Delete the forced tails and heads.  Extending \(Q\) is exactly a perfect
matching of

\[
 D_{M_0,\alpha}
   [\,X_{\mathrm{tail}}\setminus Z_Q,\
      X_{\mathrm{head}}\setminus H_Q\,].
\tag{5.4}
\]

Hall's theorem is precisely (5.3).  Add \(Q\), use (2.4) to obtain
\(M_1\), and apply Lemma 4.1.  Conversely, the successor matching of any
such factor restricts to a perfect matching of (5.4), so Hall is
necessary.  \(\square\)

This is the weakest exact signed-age addition to the factor cut after
\(M_0\) and \(\alpha\) are fixed.  It is still existential globally:
one must choose a matching phase \(M_0\) and age labelling \(\alpha\)
compatible with all protected collars.

### Corollary 5.2 (Hamilton strengthening)

Write \(z_{TT'}\in\{0,1\}\) for the successor matching selected in
\(D_{M_0,\alpha}\), including the forced arcs of \(Q\).  The resulting
resident two-factor is one Hamilton cycle if and only if, in addition to
the perfect-matching equations, it satisfies

\[
 \boxed{
 \sum_{\substack{T\in S\\T'\notin S}}z_{TT'}\ge1
 \qquad
 (\varnothing\ne S\subsetneq X).}
\tag{5.5}
\]

#### Proof

The successor matching is a permutation of \(X\).  Its cycles are exactly
the projected owner components of \(M_0\cup M_1\).  A proper nonempty
union of permutation cycles has no selected arc leaving it.  Conversely,
if the permutation has more than one cycle, the vertex set of one cycle
violates (5.5).  \(\square\)

Thus Hall condition (5.3) is exact for a resident spanning two-factor.
It does not imply the subtour inequalities (5.5); resident Hamilton
completion is a strictly stronger selection problem.

## 6. Quantitative extension criterion

The unfiltered graph \(D_{M_0}\) is \(m\)-regular.  For
\(S\subseteq X\setminus Z_Q\), define its ordinary forced-matching
surplus

\[
 \gamma_Q(S)
 =|N_{D_{M_0}}(S)\setminus H_Q|-|S|,
\tag{6.1}
\]

and the number of residual neighbor values lost to the age filter

\[
 \lambda_\alpha(S)
 =
 \left|
 \bigl(N_{D_{M_0}}(S)\setminus H_Q\bigr)
 \setminus
 \bigl(N_{D_{M_0,\alpha}}(S)\setminus H_Q\bigr)
 \right|.
\tag{6.2}
\]

Then (5.3) is equivalently

\[
 \boxed{
 \lambda_\alpha(S)\le\gamma_Q(S)
 \quad
 (S\subseteq X\setminus Z_Q).}
\tag{6.3}
\]

This is an exact quantitative separation between ordinary factor slack
and age damage.

For a coarser size-profile criterion, put

\[
 \Gamma_Q(t)
 =\min_{\substack{S\subseteq X\setminus Z_Q\\|S|=t}}
       \gamma_Q(S),
\qquad
 \Lambda_\alpha(t)
 =\max_{\substack{S\subseteq X\setminus Z_Q\\|S|=t}}
       \lambda_\alpha(S).
\tag{6.4}
\]

The inequalities

\[
 \boxed{
 \Lambda_\alpha(t)\le\Gamma_Q(t)
 \qquad
 (0\le t\le W-|Z_Q|)}
\tag{6.5}
\]

are sufficient for a resident protected completion.  The per-set form
(6.3), rather than the separated extrema in (6.5), is necessary and
sufficient.

The ordinary \(C_4\)--spectral protected-factor theorem verifies an
unfiltered degree-two factor cut.  It gives no bound on
\(\lambda_\alpha(S)\): a poorly chosen age labelling can delete every
successor of a tail.  Therefore that theorem cannot simply be rerun after
the words “and resident” are appended.  A successful proof must co-select
\(M_0,\alpha\) so that age loss stays below the actual cut surplus.

## 7. Component interpretation

For an already fixed factor \(F\), orientation and rotation of one
projected owner component do not alter the cyclic distances between
successive exchanges of a coordinate.  Those distances are exactly its
positive and negative run lengths.  Hence:

\[
 \boxed{
 F\text{ is componentwise \(L\)-biresident}
 \iff
 \text{every coordinate's successive exchange edges on every component
 are cyclically at distance at least }L.}
\tag{7.1}
\]

This condition is necessary and sufficient for each component to have its
own cyclic width-\(L\) antecedent, subject to the harmless nonempty
\(L\)-owner-intersection condition.

It is not yet one global word.  To merge components, one must change
successor matching edges.  Theorem 5.1 is precisely the factor-level
mechanism for making those choices with ages present.  Reordering intact
components without changing their factor edges does not create the
required middle-level incidences and cannot repair internal short runs.

If a linear rather than cyclic chronology is used, initial and terminal
runs may be treated as exported boundary states.  An opened component can
therefore hide only runs meeting its one cut.  The exact finite interface
is the signed capped age vector at both ends; a Hamilton ordering of
components is sufficient only when every internal run is already clean
and every connector composes those endpoint age states legally.

## 8. PBBS scope

The complete clean packet bank now has an unconditional uncoloured
spanning two-factor host.  Upgrading it to a resident factor requires:

1. phase the protected paths into \(M_0\) and a forced successor matching
   \(Q\);
2. choose signed ages matching every clean collar's input/output halo;
3. prove the age-filtered cuts (5.3), or the quantitative domination
   (6.3);
4. impose the pinned source-tail criterion after the owner chronology is
   selected; and
5. connect/open the resident factor in the form required by one PBBS word.

Deep-upper coverage is deliberately a separate row.  Once an owner
chronology is fixed, every length-\((L+q)\) source union is
\(\bigcup_{j=0}^{q}T_{i+j}\); the age-filtered factor can preserve that
inventory but does not prove that it is complete or one-copy.

Thus the next precise theorem is not another ordinary protected-factor
extension.  It is an **age-filtered protected second-matching theorem**:
co-select \(M_0\) and a collar-compatible age labelling for which the
age loss on every residual Hall cut is absorbed by the unfiltered
successor surplus.
