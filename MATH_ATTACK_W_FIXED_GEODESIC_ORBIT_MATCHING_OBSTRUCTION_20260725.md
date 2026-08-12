# Fixed geodesic template orbits: exact weighted reduction and the growing-rank obstruction

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or web input is
used.

## 0. Outcome

Fix one bounded-displacement geodesic template, including its tag, middle
owners, and calibrated protected targets, and take its full coordinate orbit
under \(G=S_{2m}\).  Keep only one simple copy of each resulting augmented
edge.  There are five conclusions.

1. **The weighted problem disappears exactly inside one orbit.**  If
   \(\nu\) is the unweighted matching number of the full orbit \(E\), then
   for every nonnegative edge weight \(w\), including a weight supported on
   an arbitrary residual subcatalogue,
   \[
      \nu_w\ge {\nu\over |E|}w(E).
      \tag{0.1}
   \]
   The constant is sharp, by taking \(w\equiv1\).  Thus all weighted
   residual cuts with the **original full-orbit denominator** are equivalent
   to one unweighted orbit matching ratio.

2. There is an exact tag-capacity split.  For a carrier-tagged rigid
   \(g\)-step return-free chunk, with \(s=g+1\) middle masks and
   \(M=m+H\), the tag degree is
   \[
      A={M!\over a_F(m-g)!(H-g)!},
      \tag{0.2}
   \]
   while the tag and middle capacity ratios are respectively
   \[
      T_{\rm tag}=N=\binom{2m}{M},
      \qquad T_{\rm mid}={W\over s}.
      \tag{0.3}
   \]
   Thus one short carrier-tag orbit has \(T_*=N\) and cannot cover a
   positive fraction of the middle row when \(s=o(M)\).  A full
   \(M\)-owner trajectory is balanced.  A short-chunk architecture must
   supply an explicit transitive enlargement by about \(M/s\) carrier-copy
   tags.  Inert copy labels form different \(S_{2m}\)-orbits.  They can be
   made edge-transitive under an enlarged abstract group \(S_{2m}\times
   S_q\), but only after proving that the \(q\) copies are legitimate
   distinct physical tags and introduce no hidden common carrier resource.
   The calibrated augmented edge rank in either balanced realization is
   \[
      K=(\sqrt\pi+o(1))s\sqrt m.
      \tag{0.4}
   \]

3. Conditional on having one genuinely balanced augmented orbit, the
   actual pair geometry is favorable at every fixed order but does not
   overcome the growing rank.  The maximum normalized target-pair codegree is
   \[
      {\Delta_2\over D}=\Theta(1/m),
      \tag{0.5}
   \]
   caused by an intended adjacent-rank cover pair; same-rank pairs are only
   \(O(m^{-2})\).  More precisely, the target-sector pair-overlap mass of
   every orbit edge is
   \[
      {1\over D}\sum_f\binom{|C(e)\cap C(f)|}{2}
      =\Theta(K/m).
      \tag{0.6}
   \]
   Consequently the distinct-tag target-conflict graph has degree
   \[
      (1-o(1))KD.
      \tag{0.7}
   \]
   Thus almost all of the \(K D\) individual target-star incidences lead
   to different blocking edges; the geometry does not secretly reduce the
   effective rank.  This statement is not applied to the scalar-unbalanced
   one-copy short orbit.

4. Every currently available full-codegree nibble is quantitatively
   powerless here.  Since the full edge has codegree one, the standard
   full-codegree scale \(B_*\) satisfies
   \[
      B_*\le D^{1/(K-1)}=1+o(1).
      \tag{0.8}
   \]
   Since every codegree is at most \(D\), also \(B_*\ge1\), and hence
   \(B_*=1+o(1)\).  Also
   \[
      {K\over\log D}\longrightarrow\infty,
      \tag{0.9}
   \]
   which is the opposite of the growing-uniformity condition in the
   quantitative pair-codegree matching theorem used for polylogarithmic
   atoms.

5. The owner projection is genuinely better: its complete weighted
   overlap hierarchy is summable.  However, there is no nontrivial
   \(S_{2m}\)-equivariant quotient which contracts even one family of
   vertical Boolean cover pairs.  Such a quotient collapses both adjacent
   Boolean ranks into a single class.  Occurrencewise column contraction
   avoids that collapse only by duplicating physical targets, and therefore
   no longer implies target-disjointness.

The exact remaining theorem is
\[
   \boxed{\nu(H_F)\ge (1-o(1/Q))T_*},
   \qquad T_*={|E|\over D},
   \tag{0.10}
\]
for one augmented template orbit.  It is not proved here, and no actual
full-orbit counterexample is proved.  What is proved is that edge
transitivity removes the arbitrary-weight issue completely, while the
known pair-, cube-, and full-codegree mechanisms do not prove (0.10).  A
proof must be a global multirank design or structured alternating
augmentation theorem.

## 1. Exact symmetrization of every weighted residual

Let a finite group \(G\) act on a finite hypergraph \(H=(V,E)\), and
assume it is transitive on the labelled edge set \(E\).  Parallel copies
are permitted only if the group is also transitive on their copy labels.
For \(w:E\to\mathbb R_{\ge0}\), put
\[
   \nu_w(H)=\max_{M\text{ a matching}}\sum_{e\in M}w_e.
   \tag{1.1}
\]

### Theorem 1.1 (lossless orbit symmetrization)

Let \(\nu=\nu(H)\).  For every \(w\ge0\),
\[
   \boxed{\nu_w(H)\ge {\nu\over |E|}w(E).}
   \tag{1.2}
\]
Moreover,
\[
   \boxed{
   \inf_{w\ge0,\ w\ne0}{\nu_w(H)\over w(E)}
   ={\nu(H)\over |E|}.}
   \tag{1.3}
\]

#### Proof

Fix a maximum unweighted matching \(M_0\), so \(|M_0|=\nu\).  For a
uniform \(\sigma\in G\), every fixed member of \(M_0\) is uniform on
\(E\).  Hence
\[
   \mathbb E_\sigma w(\sigma M_0)
   =\sum_{e\in M_0}{w(E)\over |E|}
   ={\nu\over |E|}w(E).
   \tag{1.4}
\]
Some translate attains at least the expectation, proving (1.2).  Taking
\(w\equiv1\) gives \(\nu_w/w(E)=\nu/|E|\), proving (1.3).  \(\square\)

An arbitrary residual \(E'\subseteq E\) is included by extending a weight
on \(E'\) by zero on \(E\setminus E'\).  No invariance of \(E'\) is
required.

Equivalently, let \(\Gamma\) be the conflict graph whose vertices are the
orbit edges and whose independent sets are hypergraph matchings.  It is
vertex-transitive, and (1.3) is the dual identity
\[
   \boxed{\chi_f(\Gamma)={|E|\over\alpha(\Gamma)}
          ={|E|\over\nu(H)}.}
   \tag{1.4a}
\]
Indeed, all translates of one maximum independent set, with uniform
weight, give a fractional coloring of cost \(|E|/\alpha\); the uniform
vertex weight gives the reverse fractional-clique bound.

Taking \(w=\mathbf1_{\mathcal A}\) also gives, for every subfamily
\({\cal A}\subseteq E\),
\[
   \boxed{
   {\nu({\cal A})\over|{\cal A}|}
   \ge {\nu(E)\over|E|}.}
   \tag{1.4b}
\]
Thus a local obstruction can refute the desired orbit ratio only when its
own edge/matching ratio already exceeds the full denominator.  In
particular, a clique must have more than \(D\) edges, and a blown-up
\(C_{2r+1}\) must carry more than \(rD\) total edge mass, up to the desired
\(o(1/Q)\) accuracy.

Now suppose
\[
   V=V_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}V_r
\]
and \(G\) is transitive on every \(V_i\).  Let one orbit edge contain
exactly \(k_i\) vertices of \(V_i\).

### Proposition 1.2 (exact capacities)

Every vertex of \(V_i\) has degree
\[
   D_i={|E|k_i\over |V_i|}.
   \tag{1.5}
\]
If
\[
   D=\max_iD_i,
   \qquad
   T_*={|E|\over D}=\min_i{|V_i|\over k_i},
   \tag{1.6}
\]
then the constant point \(x_e=1/D\) is a fractional matching of value
\(T_*\), and every integral matching has size at most \(T_*\).

#### Proof

Double count edge--\(V_i\) incidences to get (1.5).  The constant point
has vertex load \(D_i/D\le1\).  A matching of size \(t\) uses \(tk_i\)
distinct vertices of \(V_i\), so \(t\le |V_i|/k_i\) for every \(i\).
\(\square\)

Define the exact orbit defect
\[
   \delta_{\rm orb}=1-{\nu(H)\over T_*}.
   \tag{1.7}
\]
Theorems 1.1 and Proposition 1.2 give, sharply,
\[
   \boxed{
   \nu_w(E')\ge(1-\delta_{\rm orb}){w(E')\over D}}
   \tag{1.8}
\]
for every residual and every nonnegative weight.  Conversely \(w\equiv1\)
shows that no smaller loss than \(\delta_{\rm orb}\) is possible.

### Scope correction 1.3 (the denominator does not rescale)

The \(D\) in (1.8) is the original full-orbit degree.  It cannot be
replaced by the maximum degree of \(E'\).  For example, let the full orbit
be \(K_n\), \(n\) even, viewed as a two-uniform hypergraph.  It has
\(D=n-1\) and a perfect matching.  A residual triangle has recalculated
degree \(D'=2\), but its matching number is one, whereas
\(|E'|/D'=3/2\).  Orbit averaging gives only the correct original-denominator
bound \(|E'|/(n-1)\).

The theorem also applies to one edge orbit only.  A union of different
gap-schedule or priority-profile orbits need not be edge-transitive.

## 2. The fixed rigid geodesic orbit

Put \(n=2m\).  Fix an oriented return-free geodesic template with
\(g\) transitions:
\[
 X_t=C\cup\{a_{t+1},\ldots,a_g\}
          \cup\{b_1,\ldots,b_t\},
 \qquad 0\le t\le g,
 \tag{2.1}
\]
where
\[
 [2m]=C\mathbin{\dot\cup}
      \{a_1,\ldots,a_g\}\mathbin{\dot\cup}
      \{b_1,\ldots,b_g\}\mathbin{\dot\cup}D,
 \qquad |C|=|D|=m-g.
 \tag{2.2}
\]
Thus the template has
\[
   s=g+1
   \tag{2.3}
\]
distinct middle owners.  Add one tag vertex and a fixed common-priority
selection of lower and upper flags through depth \(Q\).  Let \(k_q\) be
the number of claimed phase columns at each signed depth \(q\ge1\).

The calibrated profile used below has
\[
 k_q\le s{N_q\over W},
 \qquad N_q=\binom{2m}{m-q},
 \tag{2.4}
\]
with total floor/deadline discrepancy \(o(s\sqrt m)\), and
\(Q/\sqrt m\to\infty\), \(Q=o(m^{2/3})\).  The exact augmented rank is
\[
   K=1+s+2\sum_{q=1}^Qk_q.
   \tag{2.5}
\]

### Proposition 2.1 (exact carrier-tagged orbit and the scalar split)

Now let the tag be a carrier \(U\) of size
\[
   M=m+H.
   \tag{2.6}
\]
Write the persistent exterior in (2.2) as
\[
   D=R\mathbin{\dot\cup}O,
   \qquad |R|=H-g,\quad |O|=m-H,
   \tag{2.7}
\]
where \(R\subset U\) and \(O=[2m]\setminus U\).  Let \(a_F\) be the
automorphism group induced by the augmented template on its \(2g\) active
coordinates.  The simple carrier-tagged orbit and its tag degree are
exactly
\[
   \boxed{
   |E|={ (2m)!\over
      a_F(m-g)!(H-g)!(m-H)!},}
   \tag{2.8}
\]
\[
   \boxed{
   A=d(U)={M!\over a_F(m-g)!(H-g)!}.}
   \tag{2.9}
\]
The tag and middle capacity ratios are
\[
   \boxed{
   T_{\rm tag}=N:=\binom{2m}{M},
   \qquad T_{\rm mid}={W\over s}.}
   \tag{2.10}
\]

#### Proof

The three inactive blocks are intrinsic incidence-signature classes:
\(C\) is the intersection of all middle masks, \(R\) is the part of the
tag lying outside their union, and \(O\) is outside the tag.  Hence every
edge stabilizer preserves \(C,R,O\) setwise.  Conversely, arbitrary
permutations inside these blocks fix the augmented edge.  After quotienting
them, every remaining stabilizer acts on the \(2g\) active coordinates and
is, by definition, one of the \(a_F\) active automorphisms.  Thus the full
stabilizer has exactly
\(a_F(m-g)!(H-g)!(m-H)!\) elements, and orbit--stabilizer gives (2.8).
Dividing by the number \(N\) of carrier tags gives (2.9).
Proposition 1.2 gives (2.10), because an edge has one tag and \(s\) middle
targets.  \(\square\)

At the crossing calibration \(MN=W-o(W)\).  Consequently, when
\(s=o(M)\),
\[
   T_*\le T_{\rm tag}=N=(1+o(1)){W\over M}
   =o(W/s).
   \tag{2.11}
\]
Even a perfect matching of this one orbit covers only
\[
   sN=(1+o(1)){s\over M}W=o(W)
   \tag{2.12}
\]
middle targets.  This is a scalar obstruction, before integrality.

To use short chunks at width scale, one needs about \(M/s\) distinct
carrier-copy tags.  If their copy labels are fixed by \(S_{2m}\), they are
different coordinate orbits.  An abstract product action
\(S_{2m}\times S_q\) is edge-transitive on \(q\) identical copy layers,
so Theorem 1.1 can symmetrize them if those layers are genuine distinct
tag resources.  The unproved point is physical: one must justify the copy
tags integrally and include any common carrier-capacity vertex they really
share.  Alternatively, one may construct an actual combinatorial copy mark
on which \(S_{2m}\) itself acts transitively.  **Neither physical tag
construction is proved in this report.**

There are therefore two cases in the remainder.

1. A full carrier trajectory has \(s=M\), so the tag and middle capacities
   agree up to the audited scalar crossing deficit.
2. For a short chunk, assume conditionally that a literal transitive tag
   enlargement has been supplied and that all active stratum degrees are
   \((1-o(1))D\).  Every statement explicitly labelled “balanced orbit”
   is conditional on this scalar construction, not on the matching.

For the first case the orbit data are especially clean.  Let \(a_F^{\rm
full}\) be the automorphism group of the fixed full schedule on the
carrier.  Then
\[
   |E_{\rm full}|={ (2m)!\over a_F^{\rm full}(m-H)!},
   \qquad
   D_{\rm tag}={M!\over a_F^{\rm full}}.
   \tag{2.13}
\]
Furthermore
\[
   {D_0\over D_{\rm tag}}={MN\over W}=1-o(1),
   \qquad
   {D_q\over D_{\rm tag}}={k_qN\over N_q}\le1.
   \tag{2.14}
\]
Thus \(D=D_{\rm tag}\), \(T_*=N\), and
\[
   \log D\le\log M!=(1+o(1))m\log m.
   \tag{2.15}
\]
These identities use the tag explicitly and do not invoke the short
target-support quotient.

For the ordinary carrier tag, (2.9) gives the useful entropy bound
\[
\begin{aligned}
   \log A
   &\le (H+g)\log{eM\over H+g}+2g\log M\\
   &=O((H+g)\log m).
\end{aligned}
   \tag{2.16}
\]
For a full \(M\)-owner carrier trajectory the simpler exact bound is
\(A\le M!\), so \(\log A\le(1+o(1))m\log m\).

For comparison, if the tag does **not** distinguish \(R\) from \(O\), the
target-support orbit has
\[
   |E_{\rm sup}|={ (2m)!\over a_F(m-g)!^2},
   \qquad
   D_{\rm mid}={s(m)_g^2\over a_F}.
   \tag{2.17}
\]
This is the exact formula used for the owner-only orbit in Section 6; it
must not be substituted for the carrier-tagged orbit (2.8).

### Proposition 2.2 (exact augmented rank asymptotic)

Under (2.4), \(Q/\sqrt m\to\infty\), and \(Q=o(m^{2/3})\),
\[
   \boxed{K=(\sqrt\pi+o(1))s\sqrt m.}
   \tag{2.18}
\]

#### Proof

Uniformly for \(q=o(m^{2/3})\), the central product expansion gives
\[
   {N_q\over W}=\exp(-q^2/m+o(1))
   \tag{2.19}
\]
on every fixed Gaussian scale.  Hence the Riemann sum is
\[
   \sum_{q=1}^Q{N_q\over W}
   =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m.
   \tag{2.20}
\]
For completeness, the exact ratio
\[
   {N_{q+1}\over N_q}={m-q\over m+q+1}
   \tag{2.20a}
\]
implies \(N_q/W\le \exp(-c q^2/m)\) uniformly for
\(q=o(m)\).  Thus, after proving the Riemann limit on
\(q\le L\sqrt m\), the remaining tail is
\(O(\sqrt m\,e^{-c'L^2})\); let \(L\to\infty\).  This justifies the
passage from the local expansion to the full sum in (2.20).
The summed floor and deadline discrepancy is \(o(s\sqrt m)\) by
hypothesis.  Substitute in (2.5).  \(\square\)

For any genuinely balanced augmented orbit, the full-orbit theorem required
for coefficient-accurate extraction is
\[
   \nu(H_F)\ge T_*-o(T_*/Q).
   \tag{2.21}
\]

## 3. Exact pair profile and conflict degree

Let \(d(S)\) and \(d(S,T)\) denote orbit degrees of protected target
vertices.  Suppose the fixed phase schedule has displacement at most a
constant \(B\).  Throughout Sections 3 and 5, assume either the balanced
full-trajectory orbit or the conditional balanced short-tag enlargement
from Section 2, and write \(D\) for their common maximum degree.  The
active target degrees are \((1-o(1))D\).  In Section 5 the conditional
short enlargement is also required to retain the natural fibre-entropy
bound \(\log D=O((H+g)\log m)\).  This must be checked by any proposed
tag mark.  None of these statements repairs the scalar-unbalanced one-copy
short orbit.

### Lemma 3.1 (bounded-displacement pair profile)

Let
\[
 |S|=r,\qquad |S\setminus T|=a,
 \qquad |T\setminus S|=b.
 \tag{3.1}
\]
Uniformly in the protected band,
\[
   \boxed{
   {d(S,T)\over d(S)}
   \le {C_B(1+a+b)\over
          \binom ra\binom{2m-r}b}.}
   \tag{3.2}
\]

#### Proof

Condition on a template slot realizing \(S\).  The stabilizer of \(S\)
is transitive on the targets \(T\) having the fixed relation type
\((a,b)\), and this orbit has size
\[
   \binom ra\binom{2m-r}b.
   \tag{3.3}
\]
For a bounded-displacement interval/geodesic schedule, once the first slot
is fixed, the second slot can realize this relation at only
\(C_B(1+a+b)\) relative phase positions.  Indeed, comparison with the
ordinary interval schedule changes each boundary by at most \(B\), while
the exact interval overlap changes by one at each boundary step; the
eligible starts therefore lie in at most two intervals of total length
\(O_B(1+a+b)\).  Divide this slot count by (3.3).  \(\square\)

This proof is one joint orbit count; it does not multiply two marginal
probabilities.

### Corollary 3.2 (the two pair scales)

For distinct same-rank targets,
\[
   {d(S,T)\over d(S)}=O_B(m^{-2}).
   \tag{3.4}
\]
For an adjacent comparable pair \(S\subset T\), \(|T|=|S|+1\),
\[
   {d(S,T)\over d(S)}=O_B(m^{-1}).
   \tag{3.5}
\]
In the central claimed columns the reverse bound also holds, so
\[
   \boxed{{\Delta_2\over D}=\Theta_B(m^{-1}).}
   \tag{3.6}
\]
For the two-parent interval convention the exact leading value is
\((2+o(1))/m\); a one-parent convention gives \((1+o(1))/m\).

#### Proof

For (3.4), distinct same-rank targets have \(a=b\ge1\), so (3.2) starts
with denominator \((m+O(Q))^2\).  For (3.5), take \((a,b)=(0,1)\).

For the lower bound, use a central adjacent-depth pair for which both
claims occur on \((1-o(1))s\) phase columns.  Conditioned on its lower
target, the edge contains at least one intended upper cover target on
average.  There are \(m+O(Q)\) possible upper covers, and the target
stabilizer is transitive on them.  Hence each has relative codegree at
least \((1-o(1))/(m+O(Q))\).  The two-parent convention counts the two
aligned parent slots and gives the stated leading two.  \(\square\)

For an edge \(e\), write \(C(e)\) for its protected target set, omitting
the tag vertex, and put
\[
   \Xi_2(e)={1\over D}
      \sum_{f:\tau(f)\ne\tau(e)}
         \binom{|C(e)\cap C(f)|}{2}.
   \tag{3.7}
\]

### Theorem 3.3 (exact order of pair-overlap mass)

Uniformly over the fixed orbit,
\[
   \boxed{\Xi_2(e)=\Theta_B(K/m).}
   \tag{3.8}
\]

#### Proof

For the lower bound, a claimed vertical column of height \(h\) contains
\(h\) adjacent Boolean cover pairs.  Summed over all columns, the number
of such pairs is \(K-O(s)\).  A positive constant fraction lies in the
central Gaussian range, where Corollary 3.2 gives relative codegree at
least \(c_B/m\).  Same-tag occurrences form a vanishing fraction of a
central target degree, so deleting them does not change the order.  This
gives \(\Xi_2(e)\ge c_BK/m\).

For the upper bound on the short return-free template, group target pairs
in \(e\) by their grid span \(t\).  There are at most \(2K(t+1)\)
unordered pairs of span \(t\).  Lemma 3.1 and the ordered-boundary relation
give
\[
   \Xi_2(e)
   \le C_BK\sum_{t\ge1}
       {(t+1)^2\over\binom{m-g}{t}}.
   \tag{3.9}
\]
The ratio after the first summand is
\[
   O_B\left({(t+2)^2\over(t+1)(m-g-t)}\right)=o(1)
   \tag{3.10}
\]
through the permitted range \(t\le2g=o(m)\).  Thus the sum is
\(O_B(1/m)\), proving the upper bound in the short case.

The full \(M\)-phase bounded-displacement trajectory is not a return-free
\(g=o(m)\) grid, so (3.9) must not be used for it.  Instead, write \(h\)
for rank gap and \(d=|S\setminus T|\).  The exact near-interval slot count
is
\[
   L_B(h,d)\le |h|+2d+4B+1.
   \tag{3.10a}
\]
Conditioning on the first target and summing the stabilizer orbits gives
directly
\[
 \Xi_2(e)
 \le \sum_r k(r)
    \sum_{(h,d)\ne(0,0)}
    {L_B(h,d)^2\over
      \binom{m-Q}{d}\binom{m-Q}{d+|h|}}.
 \tag{3.10b}
\]
The inner sum is \(O_B(1/m)\), dominated by \((|h|,d)=(1,0)\), while
\(\sum_rk(r)=K-1\).  Hence the full trajectory also has
\(\Xi_2(e)=O_B(K/m)\).  Its same-phase adjacent flag pairs give the
matching lower bound exactly as above.  This proves (3.8) in both stated
cases.  \(\square\)

The same-tag deletion used above is legitimate for the actual carrier
fibres.  If a carrier tag has degree \(A\), a fixed target \(S\subset U\)
in a row with \(k_q\) slots occurs in exactly
\[
   A{k_q\over\binom{M}{m\pm q}}
   \tag{3.11}
\]
tag-fibre edges.  Since \(H-|q|\to\infty\) in the protected band, this is
an exponentially small fraction of the global calibrated target degree.

### Theorem 3.4 (the conflict graph has full local rank)

Let \(\Gamma_{\ne\tau}\) join two orbit edges on distinct tags when they
share a protected target.  Assume the exact floor/cap/deadline ledger
\[
   \sum_{v\in C(e)}\left(1-{d(v)\over D}\right)=o(K),
   \tag{3.12}
\]
which is the orbit form of the audited scalar calibration.  Then
\[
   \boxed{d_{\Gamma_{\ne\tau}}(e)=(1-o(1))KD.}
   \tag{3.13}
\]

#### Proof

For every distinct-tag edge \(f\), put
\[
   r_f=|C(e)\cap C(f)|.
\]
Double counting gives
\[
   S_1:=\sum_fr_f=(1-o(1))KD,
   \tag{3.14}
\]
by (3.11)--(3.12), and
\[
   S_2:=\sum_f\binom{r_f}{2}=D\Xi_2(e)=O(DK/m).
   \tag{3.15}
\]
For every integer \(r\ge1\),
\[
   r-\binom r2\le1\le r.
   \tag{3.16}
\]
Summing (3.16) over the conflicting edges gives
\[
   S_1-S_2\le d_{\Gamma_{\ne\tau}}(e)\le S_1.
   \tag{3.17}
\]
Since \(S_2/S_1=O(1/m)\), (3.13) follows.  \(\square\)

Thus a maximal-matching or local-ratio argument which merely charges every
blocked orbit edge to a selected edge sees essentially \(KD\) distinct
blockers.  Its automatic guarantee remains only order
\[
   {|E|\over KD}={T_*\over K},
   \tag{3.18}
\]
not \((1-o(1/Q))T_*\).

## 4. Fixed-anchor obstructions are too thin in the full orbit

The literal odd bundles constructed for adversarial rational subpoints do
not obstruct the uniform fixed-template orbit.

### Proposition 4.1 (exact anchor dilution)

Let a carrier tag \(U\) have orbit-fibre degree \(A\), and suppose one
template edge has \(k_0\) distinct middle owners.  For every prescribed
middle target \(S\subset U\),
\[
   \boxed{
   |\{e:\tau(e)=U,\ S\in e\}|
   =A{k_0\over\binom M m}.}
   \tag{4.1}
\]

#### Proof

The stabilizer of \(U\) is transitive on its \(m\)-subsets.  Double count
the \(Ak_0\) tag-edge--middle-target incidences.  \(\square\)

If \(k_0\le M\) and \(H\to\infty\), then
\[
   {k_0\over\binom M m}=o(1).
   \tag{4.2}
\]
Consequently an endpoint-fixed \((2r+1)\)-cycle of such bundles has
test-weight matching ratio at most
\[
   {2r+1\over r}A{k_0\over\binom M m}=o(A).
   \tag{4.3}
\]
It is far below the orbit denominator \(D=(1+o(1))A\).  Thus the known
finite-chart triangles and odd cycles obstruct arbitrary chosen retained
points, but not the uniform full orbit.  A real orbit obstruction would
have to be anchor-diffuse and carry \(\Theta(D)\) mass per participating
bundle.

More generally, if \(R\) is any \(G\)-orbit of \(j\)-tuples of augmented
vertices and one edge contains \(a_R\) such tuples, then their common
codegree is
\[
   d_R={|E|a_R\over |R|}\le D.
   \tag{4.4}
\]
The corresponding packing capacity is
\[
   {|R|\over a_R}={|E|\over d_R}\ge{|E|\over D}=T_*.
   \tag{4.5}
\]
Hence no missed invariant pair- or tuple-capacity inequality can lower the
singleton capacity \(T_*\).  Any positive orbit defect is necessarily a
nonlocal blossom or matching-polytope obstruction.

## 5. Exact growing-rank obstruction to standard nibbles

### Theorem 5.1 (the full-edge codegree scale tends to one)

Let \(\Delta_j\) be the maximum codegree of a \(j\)-set of vertices in the
simple augmented orbit, and define the standard full-codegree scale
\[
   B_*:=\min_{2\le j\le K}
       \left({D\over\Delta_j}\right)^{1/(j-1)}.
   \tag{5.1}
\]
Then
\[
   \boxed{
   1\le B_*\le D^{1/(K-1)}=1+o(1).}
   \tag{5.2}
\]

For the rigid target-support orbit (2.17), if
\(\log a_F=o(g\log m)\), the sharper value is
\[
   D^{1/(K-1)}
   =1+\left({2\over\sqrt\pi}+o(1)\right)
      {\log m\over\sqrt m}.
   \tag{5.3}
\]
For a full carrier trajectory with \(D\le M!\), the coefficient \(2\)
in (5.3) is replaced by at most \(1\).

#### Proof

Every \(j\)-codegree is at most the degree of any one of its vertices, so
\(\Delta_j\le D\) and \(B_*\ge1\).  The only simple orbit edge containing
all \(K\) vertices of a fixed edge is that edge itself, so
\(\Delta_K=1\).  The entropy estimates below give
\[
   {\log D\over K-1}=o(1).
   \tag{5.4}
\]
Indeed, for the balanced short template, (2.16) and (2.18) give
\[
 {\log D\over K}
 =O\left({(H+g)\log m\over g\sqrt m}\right)=o(1)
 \tag{5.5}
\]
at the current \(g=\sqrt{QH}\), \(Q=m^{1/2+o(1)}\) calibration.  For a
full trajectory, \(\log D\le(1+o(1))m\log m\) and
\(K=(\sqrt\pi+o(1))m^{3/2}\), again giving (5.4).  In the target-support
case, (2.17)--(2.18) give the displayed constant in (5.3).
Exponentiation proves the theorem.  \(\square\)

Thus a theorem whose leftover is of order \(B_*^{-1+o(1)}\) cannot produce
an \(o(1)\) residual here, much less \(o(1/Q)\).

The pair-codegree theorem used successfully for polylogarithmic strips has
the hypotheses
\[
   K\le\tfrac12\log D,
   \qquad
   e^{2K}{\Delta_2\log D\over D}=o(1),
   \tag{5.6}
\]
and leaves a factor containing
\[
   K\left(
      {\Delta_2\log(1+\Delta_2)\over D}
     \right)^{1/(K-1)}.
   \tag{5.7}
\]
Here (5.4) gives
\[
   {K\over\log D}\to\infty,
   \tag{5.8}
\]
so the first hypothesis fails.  The exponential condition fails even more
strongly.  Finally, using \(\Delta_2/D=\Theta(1/m)\), the logarithm of the
base in (5.7) has magnitude \(O(\log m+\log\log D)=o(K)\).  Thus, whenever
the base is below one, its \((K-1)\)-st root tends to one rather than zero;
when it is above one, the bound is already vacuous.
This is a quantitative failure, not merely a fixed-uniformity citation
gap.

### Theorem 5.2 (independent residuals annihilate the orbit)

Retain every one of the \(K-1\) distinct physical protected targets with
mutually independent probability \(z\), leaving tags available.  The
expected number of surviving orbit
edges is exactly
\[
   |E|z^{K-1}.
   \tag{5.9}
\]
For the carrier-tagged short orbit,
\[
   \log|E|=\log N+\log A
   =O\bigl(m+(H+g)\log m\bigr).
   \tag{5.10}
\]
For a full carrier trajectory, \(\log|E|=O(m\log m)\).
For the calibrated regime \(g\ge\sqrt m\) and every fixed \(c>0\), taking
\(z=m^{-c}\) gives
\[
   \log(|E|z^{K-1})\longrightarrow-\infty.
   \tag{5.11}
\]
For the full carrier trajectory the same conclusion follows from
\(K=(\sqrt\pi+o(1))m^{3/2}\) and \(\log|E|=O(m\log m)\).
The same holds at \(z=1/\log m\) whenever
\[
   g\sqrt m\,\log\log m
   \gg m+(H+g)\log m,
   \tag{5.11a}
\]
as in the current \(g=\sqrt{QH}\) calibration.  A transitive short-tag enlargement with
\(\exp(o(K\log\log m))\) extra marks has the same conclusion at
\(z=1/\log m\).  At \(z=m^{-c}\), the weaker bound
\(\exp(o(K\log m))\) is sufficient.  In particular, the required
polynomial number \(M/s\) of marks is harmless for this entropy estimate
if it is physically legitimate.

#### Proof

An edge survives exactly when all its \(K-1\) target vertices survive,
proving (5.9).  Equation (5.10) follows from (2.8)--(2.9) and
\(\log N=O(m)\).  By (2.18),
\[
   -(K-1)\log z
   =(c\sqrt\pi+o(1))g\sqrt m\log m
   \tag{5.12}
\]
for \(z=m^{-c}\), which dominates (5.10) for \(g\ge\sqrt m\).  For
\(z=1/\log m\), replace \(c\log m\) by \(\log\log m\).  \(\square\)

By Markov's inequality, with probability tending to one the independent
residual contains no orbit edge at all.  This does not prove that a
matching-generated residual is empty.  It proves that a successful proof
must maintain very strong, non-product correlations essentially from the
start; a fully product residual nibble cannot reach the required
\(o(1/Q)\) scale.  Independent marginals, independence only between ranks,
or bounded-wise independence do not justify the factor \(z^{K-1}\) and are
not ruled out by this theorem.

## 6. The owner orbit is genuinely pseudorandom

The preceding obstruction is not caused by the middle geodesic itself.
There is an exact all-orders bound for its owner projection.

Let
\[
   P=(X_0,\ldots,X_{s-1})
   \tag{6.1}
\]
be a monotone middle geodesic, and let \({\cal O}_{\rm own}\) be its full
coordinate orbit.  Let \(D_{\rm own}\) be the degree of one middle target.
For \(j\ge2\), put
\[
   \Psi_j(P)={1\over D_{\rm own}}
       \sum_{F\in{\cal O}_{\rm own}}
          \binom{|F\cap P|}{j}.
   \tag{6.2}
\]

### Theorem 6.1 (exact owner overlap generating function)

For every \(w\ge0\),
\[
   \boxed{
   \sum_{j\ge2}\Psi_j(P)w^{j-2}
   \le {2\over s}\sum_{h=1}^{s-1}
      {(s-h)^2(1+w)^{h-1}\over\binom mh^2}.}
   \tag{6.3}
\]
If
\[
   s=o\left({m\over\sqrt{\log m}}\right)
   \tag{6.4}
\]
and \(0\le w\le C\log m\), then uniformly in this range
\[
   \boxed{
   \sum_{j\ge2}\Psi_j(P)w^{j-2}
   =(2+o(1)){s\over m^2}.}
   \tag{6.5}
\]

#### Proof

Two positions at distance \(h\) in \(P\) are at Johnson distance \(h\).
Conditioned on a first middle target, its distance-\(h\) sphere has size
\(\binom mh^2\).  There are \(2(s-h)\) ordered pairs of template positions
at this distance.  Stabilizer transitivity therefore gives the exact pair
ratio
\[
   {d(A,B)\over D_{\rm own}}
   ={2(s-h)\over s\binom mh^2}.
   \tag{6.6}
\]

A \(j\)-subset of positions with extreme separation \(h\) can be chosen
in
\[
   (s-h)\binom{h-1}{j-2}
   \tag{6.7}
\]
ways.  Its codegree is no larger than that of its two extremes.  Sum
(6.6)--(6.7) over \(j\), using
\[
   \sum_{j=2}^{h+1}\binom{h-1}{j-2}w^{j-2}
   =(1+w)^{h-1},
   \tag{6.8}
\]
to get (6.3).

The ratio of the \((h+1)\)-st summand in (6.3) to the \(h\)-th is at most
\[
   (1+w)\left({h+1\over m-h}\right)^2
   \le(1+w)\left({s\over m-s}\right)^2=o(1)
   \tag{6.9}
\]
under (6.4).  Hence the \(h=1\) term dominates and equals
\[
   {2(s-1)^2\over sm^2}=(2+o(1)){s\over m^2}.
\]
This term is also an exact lower bound: it is the contribution of the
\(s-1\) adjacent owner pairs to \(\Psi_2(P)\), and (6.6) is an equality
for each such pair.  All other contributions are nonnegative.  Thus the
upper estimate is matched, proving the equality in (6.5).
\(\square\)

Thus the owner-only orbit has the exact low-overlap hierarchy one would
want.  This is a genuine positive input, but it is not an integral
matching theorem by itself.

## 7. Why vertical-column contraction is not an orbit quotient

### Theorem 7.1 (equivariant cover-pair contraction collapses two ranks)

Fix \(1\le r<2m-1\).  Let \(\sim\) be an \(S_{2m}\)-invariant
equivalence relation on
\[
   \binom{[2m]}r\ \mathbin{\dot\cup}\ 
   \binom{[2m]}{r+1}.
   \tag{7.1}
\]
If \(S\sim T\) for one Boolean cover pair \(S\subset T\), then every
vertex in the two displayed ranks lies in one equivalence class.

#### Proof

The group \(S_{2m}\) is transitive on Boolean cover pairs, so invariance
gives
\[
   A\sim B\qquad\text{for every }A\subset B,
   \quad |A|=r,\ |B|=r+1.
   \tag{7.2}
\]
The bipartite inclusion graph between the two ranks is connected.  Indeed,
for any exchange \(A'=A-a+b\),
\[
   A\subset A+b\supset A-a+b=A',
   \tag{7.3}
\]
and such exchanges connect the Johnson graph on rank \(r\).  Every
rank-\((r+1)\) vertex is adjacent to an \(r\)-set.  Transitivity of
\(\sim\) along this connected graph proves the claim.  \(\square\)

Iterating Theorem 7.1 through adjacent depths collapses the whole protected
band.  Therefore there is no nontrivial physical-target quotient that
contracts the intended vertical chains while retaining coordinate
symmetry.  An occurrence-labelled column system is not a workaround: one
physical target then has many formal column copies, and a matching of
formal columns may reuse that physical target.

This explains why the owner theorem in Section 6 does not lift by a simple
column contraction.  The same obstruction is visible geometrically in a
shared grid square: two distinct row/column realizations can share physical
targets while having no common occurrence-labelled column.

## 8. Exact proved and unproved boundary

### Proved

1. For one edge-transitive augmented orbit, arbitrary weighted residual
   cuts are exactly equivalent to its unweighted full-orbit matching
   ratio, with the original degree \(D\).
2. The carrier-tagged orbit size, tag degree, and tag/middle scalar split
   are (2.8)--(2.12).  In particular, one short carrier-tag orbit is
   rigorously too small at the middle row.  The calibrated augmented rank
   is (2.18).
3. The exact pair scales are \(m^{-2}\) in one rank and \(m^{-1}\) for
   adjacent nested ranks; the total pair-overlap mass is \(\Theta(K/m)\).
4. Distinct target-star blockers are essentially unclustered:
   the target-conflict degree is \((1-o(1))KD\).
5. Fixed-anchor odd bundles are \(o(D)\) inside the uniform orbit.
6. The full-edge codegree parameter is \(1+o(1)\); it is
   \(1+(2/\sqrt\pi+o(1))\log m/\sqrt m\) for the rigid target-support
   orbit.  Independent residuals at coefficient scale contain no orbit
   edge.
7. The owner projection has the summable hierarchy (6.3), but no
   nontrivial equivariant physical-target contraction lifts it to the
   flags.

### Unproved

For a balanced full-trajectory orbit, the single statement
\[
   \boxed{
   \nu(H_F)\ge(1-o(1/Q)){|E|\over D}}
   \tag{8.1}
\]
remains unproved.  No actual orbit obstruction to (8.1) is known.

For a short chunk there is an earlier unproved scalar gate: construct a
literal \(S_{2m}\)-transitive tag enlargement of size
\((1+o(1))W/s\).  Merely attaching \(M/s\) inert copy labels produces a
union of separate edge orbits and does not inherit Theorem 1.1.  Only
after this tag gate is solved does (8.1) become the sole matching gate.

There is one additional scope condition.  The frozen exact middle-wreath
factor applies only when the fixed template's middle projection is
literally the already factored wreath orbit.  A nontrivial
bounded-displacement switch changes the middle support, and its middle-only
orbit may itself require a new matching theorem.  Edge transitivity does
not supply that theorem.

Accordingly, the viable next route is not another pair-codegree estimate.
It is an orbit-specific global augmentation/design theorem which maintains
complete interval columns and creates a strongly correlated residual.  It
must either work directly in the augmented orbit or prove a capacity-safe
nonlocal replacement for the impossible equivariant column contraction.

## 9. Independent audit record

The decisive steps were rederived independently.

* The orbit averaging proof was checked both by averaging a fixed maximum
  matching and by convex symmetrization of \(w\mapsto\nu_w\).  Both give
  (1.2), and the residual-denominator triangle example verifies the exact
  scope.
* The orbit count was checked by orbit--stabilizer with the persistent
  core, carrier remainder, and outside-carrier stabilizers kept
  separately.  Reversal and phase symmetries belong in \(a_F\); merging
  the carrier remainder with the outside complement would incorrectly
  erase the tag.
* The constants in (0.3)--(0.8) were independently checked.  In
  particular, \(K=(\sqrt\pi+o(1))s\sqrt m\) is the calibrated profile,
  not the unthinned value \(s(2Q+1)\), and the leading adjacent-pair
  constant depends on the one-parent/two-parent convention while its
  order \(1/m\) does not.
* The short-grid pair sum (3.9) was explicitly barred from the full cyclic
  trajectory.  The latter uses the independent near-interval sum
  (3.10a)--(3.10b).
* The full-edge codegree audit must be performed in the simple orbit.
  Collapsing parallel presentations first is essential.
* The cover-pair contraction obstruction was checked directly from the
  connectivity of the two-rank Boolean inclusion graph.

No step in this report asserts the missing near-perfect matching.
