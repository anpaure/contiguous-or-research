# QRE predecessor-profile entropy and the absence of an expansion gap

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let the ordered owner profile have (b=m/d+O(1)) macroblocks and two
half-count coordinates per block.  At depth

\[
                         q=A\sqrt m+O(1),
 \qquad                  d=\Theta(\log m),                         \tag{0.1}
\]

the number of ordered target profiles which can precede one fixed owner
profile is at most

\[
                         P_{b,q}:=\binom{2b+q-1}{q}.               \tag{0.2}
\]

This upper bound is sharp on the central core: for all but (o(1)) of
the raw owners in a central profile, the number of predecessor profiles
actually visible from that one owner is

\[
                         (1-o(1))P_{b,q}.                          \tag{0.3}
\]

Moreover,

\[
 \log P_{b,q}
 =q\log{2eb\over q}+O(q^2/b+\log q)
 =\left({A\over2}+o(1)\right)\sqrt m\log m.          \tag{0.4}
\]

Thus predecessor congestion has exactly the same leading entropy as the
ordered-profile expansion scale certified by the score theorem.  The
explicit lower bound used in the
present ordered-profile theorem,

\[
                         K_{m cert}
 =\binom{\rho b}{q}(7/6)^q,qquad \rho=1/13,          \tag{0.5}
\]

is in fact smaller than (0.2) by

\[
 \log{P_{b,q}\over K_{m cert}}
 =q\log{12\over7\rho}+O(q^2/b+\log q)=\Theta(q).     \tag{0.6}
\]

Even the balanced full-block benchmark has no entropy surplus: its
collision-free score (2^q\binom bq) is exactly the number of
one-hit predecessor profiles visible from a central raw owner.

Consequently the large value of the unweighted within-profile score does
not beat cross-profile competition by counting.  Exact overlap alignment
survives at the profile and raw-owner levels.  What remains is the
weighted component inequality

\[
 \sum_\lambda c_{\tau,kappa(\lambda)}R_\lambda(T)\ge1,           \tag{0.7}
\]

not an unweighted comparison between (K_\tau) and the number of
predecessor profiles.

## 1. Exact predecessor generating functions

Write one middle owner profile as

\[
                         \kappa=((a_j,c_j))_{j=1}^b.              \tag{1.1}
\]

A lower target profile preceding (kappa) is obtained by choosing
nonnegative integers (alpha_j\le a_j), (gamma_j\le c_j), with
(sum_j(\alpha_j+\gamma_j)=q), and replacing
((a_j,c_j)) by ((a_j-\alpha_j,c_j-\gamma_j)).  Distinct allocation
vectors give distinct ordered target profiles.  Hence the exact count is

\[
 P_q^-(\kappa)
 =[z^q]\prod_{j=1}^b
   (1+z+\cdots+z^{a_j})(1+z+\cdots+z^{c_j}).          \tag{1.2}
\]

For an upper target, the available increments are bounded by
(d-a_j) and (d-c_j), so

\[
 P_q^+(\kappa)
 =[z^q]\prod_{j=1}^b
   (1+z+\cdots+z^{d-a_j})(1+z+\cdots+z^{d-c_j}).      \tag{1.3}
\]

Removing all caps gives the universal upper bound

\[
                         P_q^\pm(\kappa)
                         \le\binom{2b+q-1}{q}.                    \tag{1.4}
\]

If all relevant lower, respectively upper, half capacities are positive,
then restricting every half-coordinate increment to (0) or (1)
gives

\[
                         P_q^\pm(\kappa)\ge\binom{2b}{q}.          \tag{1.5}
\]

If one additionally allows at most one edited half per macroblock, the
number is exactly

\[
                         Q_{b,q}:=2^q\binom bq.                    \tag{1.6}
\]

The distinction between (1.5) and (1.6) is a two-edits-in-one-block
correction.  It is only (exp(O(q^2/b))), but must not be silently
dropped in an exact profile count.

The same formulas apply to both signs.  On the upper sign the missing
endpoint of an (A)-singleton is a (C)-increment and conversely, but
this merely permutes the two half variables in every block.

## 2. Sharp Gaussian entropy

Put (N=2b).  Since (q=o(b)), Stirling expansion gives

\[
\begin{aligned}
 \log\binom Nq
 &=q\log{Ne\over q}-{q(q-1)\over2N}
   +O(q^3/N^2+\log q),\\
 \log\binom{N+q-1}q
 &=q\log{Ne\over q}+{q(q-1)\over2N}
   +O(q^3/N^2+\log q).                              \tag{2.1}
\end{aligned}
\]

Thus (1.4)--(1.5) imply, uniformly on the two-sided central core,

\[
 \log P_q^\pm(\kappa)
 =q\log{2eb\over q}+O(q^2/b+\log q).                \tag{2.2}
\]

At (0.1),

\[
\begin{aligned}
 q\log{2eb\over q}
 &=q\left({1\over2}\log m-\log d
                  +\log{2e\over A}+o(1)\right),\\
 {q^2\over b}&=A^2d+o(d).                            \tag{2.3}
\end{aligned}
\]

This proves (0.4), including the lower-order
(-A\sqrt m\log d+O_A(\sqrt m)) term.

For the one-edit-per-block count,

\[
 \log Q_{b,q}
 =q\log{2eb\over q}-{q(q-1)\over2b}
  +O(q^3/b^2+\log q).                                \tag{2.4}
\]

Consequently

\[
 \log{P_{b,q}\over Q_{b,q}}
 ={3q^2\over4b}+O(q^3/b^2+\log q)=O_A(d).           \tag{2.5}
\]

The collision corrections are polynomial in (m) when
(d=\Theta(\log m)); they are not a new
(exp(\Theta(\sqrt m))) entropy source.

## 3. A typical raw owner realizes the full profile entropy

Fix one raw middle owner (X) in profile (kappa).  In block (j),
measure its source-rank matching statuses and let

\[
                         p_j=\#\{A\hbox{-single edges}\},
 \qquad                  s_j=\#\{C\hbox{-single edges}\}.        \tag{3.1}
\]

For the lower sign, deleting (alpha_j) occupied (A)-single
endpoints and (gamma_j) occupied (C)-single endpoints produces a
target in the corresponding predecessor profile.  For the upper sign,
adding the missing endpoints to those singleton edges produces the
corresponding successor target profile.  Therefore the number of ordered
profiles actually visible from (X), on either sign, is

\[
 V_q(X)
 =[z^q]\prod_{j=1}^b
   (1+z+\cdots+z^{p_j})(1+z+\cdots+z^{s_j}).          \tag{3.2}
\]

This is an exact profile-visibility count.  It counts profiles, not raw
neighbors and not multiplicity of deletions inside one profile.

Suppose

\[
                         p_j,s_j\ge L\qquad(j\le b).              \tag{3.3}
\]

Among all weak compositions of (q) into (N=2b) parts, those violating
one fixed cap (L) are counted by
(inom{N+q-L-1}{q-L}).  Hence

\[
 1-{V_q(X)\over P_{b,q}}
 \le N,{\binom{N+q-L-1}{q-L}\over\binom{N+q-1}q}
 \le N\left({q\over N}\right)^L.                  \tag{3.4}
\]

On the central core choose (L=c d) for a sufficiently small absolute
(c>0).  Since (q/N=\Theta(d/\sqrt m)),

\[
 N(q/N)^L
 =\exp[-\Theta((\log m)^2)]=o(1).                  \tag{3.5}
\]

It remains to verify (3.3) for almost every owner.  Assume, for example,

\[
             \eta d\le a_j,c_j\le(1-\eta)d         \tag{3.6}
\]

with fixed (eta>0).  For a uniformly chosen local owner with these
half counts, the full-edge count in any fixed matching is
hypergeometric, and

\[
 \mathbb E p_j={a_j(d-c_j)\over d}\ge\eta^2d,
 \qquad
 \mathbb E s_j={c_j(d-a_j)\over d}\ge\eta^2d.       \tag{3.7}
\]

A hypergeometric lower-tail bound, with
(L=\eta^2d/2), gives

\[
                         \Pr\{p_j<L\text{ or }s_j<L\}
                         \le2e^{-c_\eta d}.                        \tag{3.8}
\]

The uniform measure on one ordered owner profile factors over blocks.
Under the usual condition (b e^{-c_\eta d}=o(1)), a union bound shows
that (3.3) holds for all but (o(1)) of its raw owners.  This statement
is deterministic in the matching array: changing a local bijection only
permutes the hypergeometric status classes.

Equations (3.2)--(3.8) prove

\[
                         V_q(X)=(1-o(1))P_{b,q}                    \tag{3.9}
\]

for almost every owner in every retained central profile.  Thus the
predecessor-profile upper bound is not merely a formal stars-and-bars
count.  One raw owner typically realizes essentially all of it.

Restricting to at most one edit per block gives the simpler exact lower
bound

\[
                         V_q(X)\ge2^q\binom bq                    \tag{3.10}
\]

whenever every block has both singleton sides nonempty.

## 4. Comparison with the ordered-profile score

The currently certified pointwise score is (0.5).  From (2.1),

\[
\begin{aligned}
 \log K_{\rm cert}
 &=q\log{\rho eb\over q}+q\log(7/6)
     +O(q^2/b+\log q),\\
 \log{P_{b,q}\over K_{\rm cert}}
 &=q\log{12\over7\rho}+O(q^2/b+\log q).             \tag{4.1}
\end{aligned}
\]

For (ho=1/13), the exponential base in the second line is
(156/7>1).  Hence the proved lower bound (K_{m cert}) is
exponentially too small, on the (q)-scale, to dominate the raw incoming
profile count.

There is also an exact balanced benchmark.  If the collision-free
one-block scores are (r_j=2), then

\[
                         e_q(r_1,\ldots,r_b)
                         =2^q\binom bq=Q_{b,q}.                    \tag{4.2}
\]

By (3.10), this is exactly the one-edit-per-block predecessor-profile
count of a raw owner having both singleton sides in every block.  At the
central hypergeometric mean, the actual one-block lower and upper scores
are (2+O(d^{-1})); for typical local status they are
(2+O(d^{-1/2})).  Thus the natural full score and the natural raw-owner
congestion match, rather than separate, at the collision-free scale.

Multi-edit allocations enlarge the **number of allocation labels** and
the raw predecessor-profile count by only the collision factor in (2.5)
at the level of profile entropy.  Individual component ratios
(R_\lambda(T)) can of course differ substantially from one; no
pointwise comparison follows by counting terms.  The exact averaged
identity is instead

\[
 {1\over|\tau|}\sum_{T\in\tau}{\cal R}_\tau(T)
 ={1\over|\tau|}\sum_{\kappa}E_{\tau\kappa},
 \qquad E_{\tau\kappa}\le|\kappa|,                 \tag{4.3}
\]

where (E_{\tau\kappa}) is the visible source mass on that arc.  This
identity retains profile sizes and cannot be replaced by an unweighted
predecessor count.

## 5. Why exact overlap alignment survives

For a fixed target profile, different allocations lead to disjoint
ordered source profiles, so their component expansion scores add.  For a
fixed source profile, the direction is reversed: (3.9) shows that the
same raw owner participates in essentially every algebraically possible
predecessor profile.  Adding unweighted expansion scores over those
profiles therefore reuses that owner capacity (P_{b,q}) times.

This is precisely the distinction between

\[
                         {\cal R}_\tau(T)=\sum_\lambda R_\lambda(T)
                                                                    \tag{5.1}
\]

and the weighted score

\[
                         {\cal R}_{\tau,c}(T)
 =\sum_\lambda c_{\tau,kappa(\lambda)}R_\lambda(T),              \tag{5.2}
\]

where

\[
                         \sum_\tau c_{\tau\kappa}\le1.           \tag{5.3}
\]

The entropy calculation proves that no spare exponential factor is
available to make (5.3) automatic.  The rank-independent literal cut in
`MATH_AUDIT_QRE_WITHIN_PROFILE_EXPANSION_AND_TWO_LEVEL_HALL_20260726.md`
shows that component alignment can be exact.  Independent rank matchings
break that particular common-full-edge invariant, but they neither
reduce (1.2)--(1.3) nor the raw-owner visibility (3.9).  Their remaining
possible benefit must be a genuinely weighted decorrelation of the
component ratios in (5.2).

Therefore the minimum surviving theorem is still the weighted
allocation-score inequality (0.7), or an equivalent component-level
congestion theorem.  Predecessor-profile counting, even at its sharp
entropy scale, cannot prove global QRE.

This note does not assert a pointwise upper bound
\({\cal R}_\tau(T)\le P_{b,q}\).  Exceptional component ratios can make
the full score larger than its number of allocation labels.  It proves
instead that such a gain, if useful, must come from the **weighted**
ratios (R_\lambda(T)); there is no combinatorial entropy gap, and the
same owner capacity is visible to essentially all predecessor profiles.

This conclusion concerns the maximal raw graph only.  It makes no
selected-axis, diverse-order packet, or chronological completion claim.
