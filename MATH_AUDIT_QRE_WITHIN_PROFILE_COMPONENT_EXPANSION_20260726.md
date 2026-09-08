# Audit of QRE within-profile component expansion

Date: 2026-07-26

Audited source:
`MATH_THEOREM_QRE_WITHIN_PROFILE_COMPONENT_EXPANSION_20260726.md`.

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

The within-profile theorem is correct.  In a safe diffuse ordered lower
profile, after deleting a family of relative mass at most

\[
                         2q e^{-cd},
\]

every arbitrarily block-labelled target subfamily has neighborhood at
least \((3/2)^q\) times its size in the maximal rank-twisted graph.  The
upper statement is also correct.  Under the displayed hypotheses on
\(d,q\), the union of the deleted, unsafe, and nondiffuse target families
has size \(o(N_q)\).

The theorem does **not** combine formally with the ordered-profile Hall
flow to prove QRE.  The local proof expands one target profile into a
union of many source-profile shores.  For two different target profiles,
those raw source neighborhoods may overlap.  The quotient flow controls
only their aggregate profile capacities and does not provide a common
raw kernel whose load is at most one at every source.  Thus cross-profile
competition remains the exact missing step.

The minimum sufficient composition statement is recorded in Section 6
below.  It asks for arc kernels with prescribed quotient marginals and a
pointwise source-capacity bound.  Neither the audited within-profile
expansion nor the ordered-profile visibility lemma supplies those kernels.

## 1. Lower one-block ratios

Fix one selected lower block, with target half-ranks \((a,c)\), total
rank \(t=a+c\le d\), and source-rank matching

\[
                         M=\pi_{j,t+1}.
\]

If a target has \(f\) full, \(p=a-f\) \(A\)-single,
\(s=c-f\) \(C\)-single, and

\[
                         z=d-a-c+f
\]

empty matching edges, fix the *set* of its full edges.  Adding one
endpoint of an empty edge does not change that set.

On the shore which adds an \(A\)-endpoint, every target has degree \(z\),
while every source has reverse degree \(p+1\): reverse the move by choosing
the \(A\)-single edge whose occupied endpoint is deleted.  Hence edge
counting gives, for every subfamily in the fixed-full-set component,

\[
                         |N_A(\mathcal D)|
             \ge {z\over p+1}|\mathcal D|.
\]

The \(C\)-shore analogously has ratio \(z/(s+1)\).  The two source shores
have different ordered half-ranks, \((a+1,c)\) and \((a,c+1)\), so they
are disjoint.  Therefore the exact local factor is

\[
 R^-(f)=z\left({1\over a-f+1}+{1\over c-f+1}\right).
\tag{1.1}
\]

For a uniform local target with prescribed half-ranks,

\[
                         F\sim\operatorname{Hyp}(d,c,a),
 \qquad \mathbb EF={ac\over d}.
\]

Writing \(x=a/d,y=c/d\), the large-\(d\) value of (1.1) at the mean is

\[
 {1-x\over x}+{1-y\over y}.
\tag{1.2}
\]

On

\[
 {1\over4}\le x,y\le{3\over4},\qquad x+y\le1,
\]

(1.2) is at least two.  Indeed its minimum under \(x+y\le1\) is attained
at \(x=y=1/2\).  Uniform continuity, including the harmless \(+1\) in
the denominators of (1.1), gives fixed \(\eta,c>0\) such that

\[
 |F-ac/d|\le\eta d\quad\Longrightarrow\quad R^-(F)\ge{3\over2},
\]

and the hypergeometric tail outside this event is at most \(2e^{-cd}\).
All inequalities and their directions are correct.

## 2. Tensorization for arbitrary subsets

Choose \(q\) below-centre blocks \(J\).  Fix the exact target outside
\(J\), and in every selected block fix the exact full-edge set.  For a
side word \(\sigma\in\{A,C\}^J\), the corresponding graph is the tensor
product of the one-block biregular graphs.  It is itself biregular, so for
an arbitrary subfamily \(\mathcal D\) of this global component,

\[
 |N_\sigma(\mathcal D)|
 \ge \prod_{j\in J}R^-_{\sigma_j}(F_j)|\mathcal D|.
\tag{2.1}
\]

Different side words have different ordered source half-rank profiles and
hence disjoint source shores.  Summing (2.1) over all side words gives

\[
 |N(\mathcal D)|
 \ge \prod_{j\in J}
       \bigl(R_A^-(F_j)+R_C^-(F_j)\bigr)|\mathcal D|.
\tag{2.2}
\]

This step is valid for an arbitrary subset \(\mathcal D\); no product
assumption on \(\mathcal D\) is used.  It follows solely from
biregularity and the disjointness of the side-word shores.

Different fixed-data components also have disjoint source neighborhoods.
The exterior target is unchanged by all selected moves, and every full
edge in a selected block remains full.  Thus two components differing in
the exterior or in a full-edge set cannot acquire a common source.  This
justifies summing (2.2) over arbitrary families spread among components.

The uniform measure in one ordered profile is the product of the uniform
local half-count measures.  A union bound over the \(q\) selected blocks
therefore deletes relative mass at most \(2q e^{-cd}\).  On every
remaining component, (2.2) is at least \((3/2)^q\).  This proves the
lower theorem exactly.

## 3. Upper-shore audit

For an upper target with \(t=a+c\ge d\), use

\[
                         M=\pi_{j,t-1}.
\]

Deleting one endpoint of a full edge preserves the exact set of empty
edges, so empty-edge sets index the components.  If the deleted endpoint
is the \(C\)-endpoint, the source has one additional \(A\)-single edge.
The forward target degree is \(f\), and the reverse source degree is
\(p+1\).  This gives \(f/(p+1)\); the other shore gives \(f/(s+1)\).
Thus

\[
 R^+(f)=f\left({1\over a-f+1}+{1\over c-f+1}\right).
\tag{3.1}
\]

At \(f=ac/d\), its limiting value is

\[
                         {y\over1-y}+{x\over1-x}.
\tag{3.2}
\]

On the safe region \(x+y\ge1\), (3.2) is at least two, again with minimum
at \(x=y=1/2\).  The same uniform-continuity and hypergeometric-tail
argument gives \(R^+(F)\ge3/2\) outside relative mass \(2e^{-cd}\).
The component tensorization is identical, now using exact empty-edge sets.
Hence the upper statement passes without a sign or denominator error.

## 4. Safe diffuse profiles have full mass

Let \(b=m/d+O(1)\), first suppressing the \(O(d)\) residual coordinates.
Under the independent Bernoulli law of density

\[
                         p_-={m-q\over2m}<1/2,
\]

the \(b\) block ranks are independent \(\operatorname{Bin}(2d,p_-)\)
variables.  The probability of rank at most \(d\) is bounded below by an
absolute positive constant.  Therefore the probability of having fewer
than \(c b\) below-centre blocks is \(e^{-\Omega(b)}\).  Since
\(q=o(b)\), this implies the required availability of \(q\) blocks.

Conditioning on total rank \(m-q\) costs only
\(O(\sqrt m)\), because this is the mean of the Bernoulli total and its
point probability is \(\Theta(m^{-1/2})\).  The exponentially small
failure probability remains \(o(1)\).  The upper proof uses
\(p_+=(m+q)/(2m)>1/2\) and block rank at least \(d\).

For either sign, a half-count exits \([d/4,3d/4]\) with probability
\(e^{-c_0d}\).  A union bound over \(O(m/d)\) halves gives

\[
                         O((m/d)e^{-c_0d})=o(1).
\]

The \(O(d)\) residual coordinates merely change the conditioned core rank
by \(O(d)\).  The same estimates are uniform outside \(o(N_q)\) target
mass.  Thus the safe/diffuse mass assertion is correct.  Taking the
constant in the hypothesis no larger than the tail constant in Sections
1 and 3 also makes

\[
                         q e^{-cd}=o(1),
\]

because \(q=o(m/d)\).

## 5. Why the quotient flow does not finish QRE

Let \(\tau\) denote a target half-rank profile and \(\kappa\) a middle
owner half-rank profile.  The audited quotient theorem gives numbers
\(F_{\tau\kappa}\) with

\[
 \sum_\kappa F_{\tau\kappa}=w_T(\tau),
 \qquad
 \sum_\tau F_{\tau\kappa}
       \le(e^{-A^2}+o(1))w_X(\kappa).
\tag{5.1}
\]

The within-profile theorem does not realize these particular arc masses.
For one \(\tau\), it selects one set of \(q\) below-centre blocks and
obtains expansion by summing over all \(2^q\) endpoint-side words.  Those
words land in many source profiles.  The theorem supplies no prescribed
split of a raw target's unit mass among the arcs \((\tau,\kappa)\) in
(5.1).

More importantly, if \(\mathcal A_\tau\) and
\(\mathcal A_{\tau'}\) lie in two target profiles, the two separate bounds

\[
 |N(\mathcal A_\tau)|\ge(3/2)^q|\mathcal A_\tau|,
 \qquad
 |N(\mathcal A_{\tau'})|\ge(3/2)^q|\mathcal A_{\tau'}|
\]

give no upper bound on
\(|N(\mathcal A_\tau)\cap N(\mathcal A_{\tau'})|\).  Quotient capacity
does not repair this, because it records aggregate incidences/profile
visibility rather than the common raw source load created by two
arbitrarily selected subfamilies.  Hence neither theorem implies

\[
 \left|N\left(\bigcup_\tau\mathcal A_\tau\right)\right|
       \ge\sum_\tau|\mathcal A_\tau|.
\]

This is not a defect in either proof; it is the surviving cross-profile
competition problem.

## 6. Exact sufficient composition lemma

The following is the minimum direct fractional lift of (5.1).

### Lemma 6.1 (arc-kernel lift)

Suppose that for every retained quotient arc \((\tau,\kappa)\) there is
a nonnegative kernel \(K_{\tau\kappa}(T,X)\), supported only on literal
compatible pairs with \(T\in\tau\), \(X\in\kappa\), such that

\[
 \sum_{X\in\kappa}K_{\tau\kappa}(T,X)
       ={F_{\tau\kappa}\over w_T(\tau)}
       \quad(T\in\tau),                                      \tag{6.1}
\]

and

\[
 \sum_{T\in\tau}K_{\tau\kappa}(T,X)
       \le {F_{\tau\kappa}\over w_X(\kappa)}
       \quad(X\in\kappa).                                    \tag{6.2}
\]

Then the maximal raw compatibility graph has a fractional matching which
saturates every retained target and uses at most
\(e^{-A^2}+o(1)<1\) of every source.

#### Proof

Put

\[
                         K(T,X)=\sum_{\tau,\kappa}
                                      K_{\tau\kappa}(T,X).
\]

For \(T\in\tau\), (6.1) and the first identity in (5.1) give

\[
                         \sum_XK(T,X)=1.
\]

For \(X\in\kappa\), (6.2) and the second inequality in (5.1) give

\[
 \sum_TK(T,X)
 \le {1\over w_X(\kappa)}\sum_\tau F_{\tau\kappa}
 \le e^{-A^2}+o(1)<1.
\]

Thus \(K\) is the required fractional matching.  Bipartite matching
integrality then gives a raw injection. \(\square\)

For a genuinely biregular arc graph, the uniform edge kernel satisfies
(6.1)--(6.2).  The rank-twisted graph between two coarse half-rank
profiles is not biregular; its matching-overlap coordinates have
\(\Theta(\sqrt d)\) fluctuations.  The within-profile theorem obtains
expansion only after summing several refined shores and therefore does
not furnish the separate kernels in Lemma 6.1.

Consequently Lemma 6.1, or an equivalent common-source isoperimetric
inequality, is the precise remaining raw Hall gate.  Selected-axis
retention and compiler chronology are logically later and are not part of
this audit.

## 7. Minor textual corrections

There is one nonmathematical rendering artifact in the source around its
equation (2.2): `\bigr` contains a stray control character.  Replacing it
by `\bigl` restores the intended display.  No estimate depends on this
typo.

The phrase “no \(\Omega(W)\) raw Hall counter-cut can be supported inside
one retained diffuse ordered profile” is correct only with the theorem's
uniform quarantine understood.  Summing the relative quarantine over all
profiles costs \(o(N_q)=o(W)\); it does not authorize ignoring a different
exceptional family for each subsequently chosen cut.

## 8. Final boundary

Verified unconditionally:

1. the lower local ratio sum and its \(3/2\) safe bound;
2. tensorization for every arbitrary subset, not only product families;
3. disjointness of side-word and fixed-data source components;
4. the complete upper-sign analogue;
5. the relative \(2qe^{-cd}\) component quarantine; and
6. full asymptotic mass of safe diffuse profiles.

Not implied:

1. a common raw source-capacity bound across different target profiles;
2. the arc kernels of Lemma 6.1;
3. QRE; or
4. selected-packet or chronological completion.

The theorem is therefore a genuine strict reduction: all within-profile
block-labelled cuts are eliminated, and only cross-profile competition
remains at the maximal raw Hall stage.
