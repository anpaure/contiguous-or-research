# The \(k=11\) complemented-PBBS alpha atlas: 38 pure chart orbits and one isolated component

Date: 2026-07-27

Method: symbolic cyclic-parenthesis analysis only.  No search or program is
used.

## 0. Outcome

Let (F_{\mathrm{PBBS}}^{c}) be the complemented centered PBBS transition factor on

\[
 \binom{[11]}6 .
\]

It has twelve components, every rank-five lower colour exactly once, and
rank-seven upper loads in \(\{1,2,3\}\).  Every alpha switch considered
below preserves that complete lower--middle--upper marginal vector exactly.

The cyclic-parenthesis structure gives a large explicit alpha atlas.  There
are

\[
 19
\]

translation-orbits of **forward-pure** alpha charts and, by reflection,
another \(19\) translation-orbits of **reverse-pure** charts.  Thus these two
canonical subatlases contain \(38\) quotient charts, or \(418\) labelled
charts.

This supply does not span the twelve components.  The alternating PBBS
component is incident with **no alpha chart whatsoever**, including mixed
charts outside the two pure subatlases.  Consequently:

> The initial complemented PBBS factor admits no static absorbing alpha tree.
> Any alpha-based Hamiltonization must first create an alpha portal to the
> alternating component, or must touch that component by a larger
> marginal-preserving trade.

This is a statewise obstruction, not a counting shortfall.  It identifies the
smallest residual gate more sharply than ordinary component-quotient
connectivity: **dynamic portal creation** is required before interlacement or
delay-three seam selection can even become the final issue.

## 1. The PBBS factor in sigma form

For a five-set (Z\subset\mathbb Z_{11}), let (p_+(Z)) and (p_-(Z)) be
the unique forward- and reverse-unmatched zeros in the two cyclic
parenthesis matchings.  The PBBS map obeys

\[
 f(Z)=Z^c-\{p_+(Z)\},
 \qquad
 f^{-1}(Z)=Z^c-\{p_-(Z)\}.
 \tag{1.1}
\]

After complementing the centered PBBS edge, the chord indexed by the lower
colour (Z) is

\[
 e_Z=
 \big\{Z+p_+(Z),\ Z+p_-(Z)\big\},
 \tag{1.2}
\]

and hence

\[
 \boxed{\sigma_{\mathrm{PBBS}}(Z)=Z+\{p_+(Z),p_-(Z)\}.}
 \tag{1.3}
\]

Thus the alpha question is a question about the two unmatched-zero maps and
nothing else.

Fix a four-set (R).  For (x\notin R), abbreviate

\[
 \epsilon_R(x)
 :=\{p_+(R+x),p_-(R+x)\}.
 \tag{1.4}
\]

An alpha chart with core (R), triangle (I=\{i,j,k\}), and spare
coordinate \(\ell\) is present in (F_{\mathrm{PBBS}}^c) exactly when, for one of
the two cyclic permutations \(\pi\) of (I),

\[
 \boxed{
  \epsilon_R(x)=\{\ell,\pi(x)\}
  \quad(x\in I).}
 \tag{1.5}
\]

Switching replaces \(\pi\) by \(\pi^{-1}\).  Formula (1.5) is the exact
endpoint-map form of the PBBS alpha atlas.

## 2. A complete pure family from one dominant Dyck block

Write the deficit-three cyclic decomposition of (R) as

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,
 \tag{2.1}
\]

where the (D_i)'s are Dyck words of total semilength four.  Put

\[
 h_i=\operatorname{ht}(D_i).
\]

The standard clean-label calculation gives

\[
 p_+(R+z_i)=z_{i+2}
 \qquad(i\bmod3).
 \tag{2.2}
\]

For a nonempty Dyck block (D_s), let (q_s) be the down-step immediately
following its rightmost maximum.

### Theorem 2.1 (dominant-block alpha criterion)

The three rows indexed by the forward-unmatched zeros form a
forward-pure alpha chart if and only if, for some cyclic index \(s\),

\[
 \boxed{
 h_s\ge h_{s+1}+2,
 \qquad
 h_s\ge h_{s+2}+1,}
 \tag{2.3}
\]

In that case

\[
 p_-(R+z_0)=p_-(R+z_1)=p_-(R+z_2)=q_s.
 \tag{2.4}
\]

Consequently the three present PBBS chords form an alpha side on

\[
 Q=\{z_0,z_1,z_2,q_s\}.
\]

More explicitly, after cyclically relabelling so that (s=0), the present
assignment is

\[
 R+z_i
 \longmapsto
 R+\{z_i,z_{i+2},q_0\}
 =R+Q-\{z_{i+1}\},
 \tag{2.5}
\]

and the alpha switch replaces (i+1) by (i+2).

#### Proof

Rotate (R+z_i) to start at its changed symbol.  Its height word is

\[
 1D_i\,0_{z_{i+1}}D_{i+1}\,0_{z_{i+2}}D_{i+2}.
 \tag{2.6}
\]

The reverse survivor is the down-step following the rightmost global
maximum.  For (s=0), the three regional maximum heights are respectively

\[
\begin{array}{c|ccc}
i& D_i&D_{i+1}&D_{i+2}\\ \hline
0&h_0+1&h_1&h_2-1\\
1&h_1+1&h_2&h_0-1\\
2&h_2+1&h_0&h_1-1.
\end{array}
 \tag{2.7}
\]

Ties are resolved in favour of the later block.  The second row of (2.7)
is the restrictive one: (D_0) wins there precisely under

\[
 h_0-1\ge h_1+1,
 \qquad h_0-1\ge h_2.
\]

These inequalities imply the two other rows as well and are exactly (2.3).
Changing the baseline of a Dyck block does not change the location of its
rightmost internal maximum, so all three reverse survivors equal (q_0).
Equations (2.2) and (2.4) give (2.5).

Conversely, in a forward-pure chart the common reverse survivor is not one
of the three forward-unmatched labels, so it lies in a unique Dyck block
\(D_s\).  That same block must contain the rightmost global maximum in all
three rotated words (2.6).  Taking the rotation in which \(D_s\) is last
gives exactly \(h_s-1\ge h_{s+1}+1\) and
\(h_s-1\ge h_{s+2}\), which is (2.3).  Hence the criterion is also
necessary.
\(\square\)

The chart in Theorem 2.1 is called **forward-pure**: the three varying
endpoints are the forward survivors, while the common spare is the reverse
survivor.  Reflection of the coordinate circle exchanges (p_+) and
(p_-) and gives the reverse-pure family.

## 3. Exact count at semilength four

The height distributions of Dyck words through semilength four are

\[
\begin{array}{c|ccccc}
s\backslash h&0&1&2&3&4\\ \hline
0&1&0&0&0&0\\
1&0&1&0&0&0\\
2&0&1&1&0&0\\
3&0&1&3&1&0\\
4&0&1&7&5&1.
\end{array}
 \tag{3.1}
\]

Count ordered triples ((D_0,D_1,D_2)) of total semilength four satisfying

\[
 h_0\ge h_1+2,
 \qquad h_0\ge h_2+1.
\]

The contribution according to the semilength of (D_0) is

\[
\begin{array}{c|ccc}
|D_0|&2&3&4\\ \hline
\#&1&5&13.
\end{array}
\tag{3.2}
\]

Indeed:

* at size two the unique possibility is height pattern ((2,0,1));
* at size three the height-three word permits both allocations of the one
  remaining atom, while the three height-two words permit only
  ((2,0,1)), giving (2+3=5);
* at size four every nonalternating Dyck word works, giving
  (14-1=13).

Therefore

\[
 \boxed{1+5+13=19.}
 \tag{3.3}
\]

The cyclic decomposition (2.1) is defined up to rotation of its three
unmatched zeros.  A dominant block is unique, so (3.3) counts each
translation-orbit of forward-pure charts once.  Translation acts freely on
four-sets in \(\mathbb Z_{11}\), yielding

\[
 \boxed{19\cdot11=209}
 \tag{3.4}
\]

labelled forward-pure charts.  Reflection gives another 209 reverse-pure
charts.  The two pure families are disjoint: in (2.3), (q_s) is an
internally matched forward zero and hence is not one of the forward-unmatched
labels.

Thus the canonical pure atlas has exactly

\[
 \boxed{38\text{ quotient chart orbits and }418\text{ labelled charts}.}
 \tag{3.5}
\]

This is the complete forward- and reverse-pure atlas.  It does not claim
that mixed charts do not exist.

## 4. What the 19 forward types do at the action-profile level

For a Dyck word (D), write

\[
 \mathbf a(D)
 =\bigl(\operatorname{pk}(D),
        \operatorname{pk}(\partial D),\ldots\bigr).
\]

For the three chart rows, the normalized roots are

\[
 E_i=D_{i+2}\,1D_i0\,D_{i+1},
\]

and hence

\[
 \mathbf a(E_i)
 =\sum_j\mathbf a(D_j)+\mathbf e_{h_i+1}.
 \tag{4.1}
\]

The first six chart types in (3.2) have pairwise distinct heights:

* four types have profile triple
  \[
  (3,1,1),\quad(4,1),\quad(3,2);
  \tag{4.2}
  \]
* two types have profile triple
  \[
  (3,1,1),\quad(2,2,1),\quad(2,1,1,1).
  \tag{4.3}
  \]

Every one of these is therefore a genuine three-component alpha connector.
The thirteen size-four types have height pattern ((h,0,0)); two chart
rows have the same profile, so they are candidates for binary absorption,
but their equality of profile does not prove equality of physical PBBS
component or the favourable cyclic interlacement.

The mountain word (D_0=11110000) gives the profile edge

\[
 (1,1,1,1,1)\longleftrightarrow(2,1,1,1),
 \tag{4.4}
\]

so the pure profile atlas reaches the mountain extreme.  It does not reach
the alternating profile ((5)).  The next section shows that this is not an
artifact of restricting to the pure atlas.

## 5. The alternating component has no alpha portal

Let

\[
 Z=\{1,3,5,7,9\}\subset\mathbb Z_{11}.
 \tag{5.1}
\]

Its cyclic word is (0(10)^5), and

\[
 p_+(Z)=0,
 \qquad p_-(Z)=10.
 \tag{5.2}
\]

The translates of (Z) form the alternating PBBS component.

Indeed, equivariance gives
\(p_+(Z+t)=t\) and \(p_-(Z+t)=t-1\).  The chord at row \(Z+t\)
shares its \(p_+\)-endpoint with the \(p_-\)-endpoint of the row
\(Z+t+2\).  Since (2) generates \(\mathbb Z_{11}\), these eleven rows
form one factor cycle.

### Theorem 5.1 (alpha isolation)

No present PBBS chord indexed by a translate of (Z) belongs to any alpha
chart of (F_{\mathrm{PBBS}}^c).

#### Proof

It is enough to treat (Z).  Suppose an alpha chart contains its row.  Its
core is

\[
 R=Z-\{x\},
 \qquad x=2j-1\in Z.
\]

Direct cyclic reduction gives the forward and reverse clean-label sets

\[
 U_+(R)=\{0,x,x+1\},
 \qquad
 U_-(R)=\{10,x-1,x\}.
 \tag{5.3}
\]

The current endpoint pair of the row (R+x=Z) is ({0,10}).  In an alpha
chart one of these must be the common spare.

Assume first that the spare is (0).  The cyclic partner of (x) is then
(10), so the row (R+10) must also have endpoint (0).

If (x\ne1), then (0\notin U_-(R)).  Moreover cyclic reduction gives

\[
 p_+(R+10)=
 \begin{cases}
 x+1,&x<9,\\
 x,&x=9,
 \end{cases}
 \tag{5.4}
\]

which is never (0).  Thus (R+10) has no endpoint (0), a contradiction.

For the boundary case (x=1), the two forced endpoint pairs are

\[
 \epsilon_R(10)=\{0,2\},
 \qquad
 \epsilon_R(2)=\{1,10\}.
 \tag{5.5}
\]

The first pair forces the third triangle coordinate to be (2), while the
second pair then lacks the common endpoint (0), again a contradiction.

The case in which the spare is \(10\) is the reflected argument.  If
\(x\ne9\), then \(10\notin U_+(R)\).  Reverse cyclic reduction gives
\(p_-(R+0)=x-1\) for \(x>1\), while at \(x=1\) it gives
\(p_-(R+0)=1\); hence the row \(R+0\) has no endpoint \(10\).
In the boundary case \(x=9\), the forced pairs are

\[
 \epsilon_R(0)=\{10,8\},
 \qquad
 \epsilon_R(8)=\{9,0\},
 \tag{5.6}
\]

which again fail at the third row.  Therefore neither possible spare can
occur.  Translation proves the assertion for the whole component.
\(\square\)

The proof uses the exact endpoint condition (1.5), so it excludes pure and
mixed alpha charts alike.

### Corollary 5.2 (no static spanning alpha tree)

The initial complemented PBBS factor has no absorbing alpha tree spanning
its twelve components.

Indeed, the alternating component is an isolated vertex of the initial
alpha-support hypergraph.

This does **not** prove that an adaptive sequence of alpha switches is
impossible.  Switches away from the alternating component may change the
two partner rows in (5.5) or (5.6), thereby creating a later portal while
leaving the alternating chord itself fixed.  What Corollary 5.2 proves is
that such a sequence necessarily contains a preparatory phase; it cannot be
a static disjoint alpha absorption tree selected in the initial state.

## 6. Interlacement and delay three

The six three-profile chart types in Section 4 are ternary absorptions and
need no binary interlacement test.  The thirteen remaining forward-pure
types, and their reverse images, are only *candidates* for binary
absorption.  For each one the two equal-profile rows must still be shown to

1. lie in the same physical (f^{-2})-component;
2. occur in the favourable one of the two port interlacements; and
3. remain flippable after earlier charts have been used.

These are phase/rigging statements, not consequences of the height profile.

Every alpha chart has one favourable seam feature: all three removed and all
three inserted transitions flip the same spare coordinate.  Therefore, on a
two-sided delay-three-fresh carrier, the spare coordinate is absent from the
two-transition collars at every cut.  If no length-three window crosses two
new seams, the spare can create no new delay-three violation.  The remaining
checks involve only the three rotating coordinates and coincidences between
the retained two-transition collars.

The canonical PBBS factor is not globally delay-three-fresh, so a bare alpha
joining sequence cannot by itself prove the delayed OR--Pascal
factorization.  Residence defects must first be cut/rethreaded, or the alpha
charts must be integrated with that operation.  The alternating component
itself is not the source of a short-residence problem: along it the row
indices advance by two modulo eleven, and every inserted coordinate is
deleted six transitions later.

## 7. Smallest residual theorem

The symbolic audit replaces the former generic “alpha supply” question by
the following ordered pair of finite gates.

### Gate A: alternating portal creation

Starting from (F_{\mathrm{PBBS}}^c), find a q1-marginal-preserving preparatory
trade, disjoint from the alternating chord but changing its forced partner
rows, which creates one correctly interlaced alpha chart incident with the
alternating component; or find one larger marginal-preserving trade that
touches the component directly.

### Gate B: phase-resolved absorption on the remaining components

After Gate A, choose translated pure or mixed charts so that the equal-profile
pairs lie in the required physical components with favourable cyclic order,
and so that the resulting charts stay dynamically flippable.  For a final
delay-three construction, impose the two-transition collar tests at the same
time.

Gate A is logically prior: without it the initial alpha-support hypergraph
is disconnected regardless of the abundance (418).  Thus the first useful
next object is not another scalar chart count; it is a **portal-creating
commutator** (most naturally an alpha/four-trade composition) whose net
three marginals vanish and whose final state admits an alpha edge to the
alternating component.
