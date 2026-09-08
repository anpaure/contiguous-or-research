# Symmetrized balanced-flow/rotor double resolution

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result and precise scope

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad M=m+H,\qquad
 N_H=\binom{2m}{M}=\binom{2m}{m-H},\qquad
 T=MN_H,
\tag{0.1}
\]

Assume \(H=o(m)\) is the least integer for which

\[
 \frac{W}{N_H}\ge m+H=M.
\tag{0.1a}
\]

Then \(T\le W\) and \(T=W-o(W)\).  Indeed, writing
\(\lambda_h=W/N_h\), minimality gives \(\lambda_{H-1}<M-1\), while

\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{N_{H-1}}{N_H}
 =\frac{m+H}{m-H+1}.
\tag{0.1b}
\]

Consequently

\[
 1\le\frac{\lambda_H}{M}
 <\frac{M-1}{m-H+1}=1+o(1),
\qquad
 \frac{T}{W}=\frac{M}{\lambda_H}=1-o(1).
\tag{0.1c}
\]

Fix a truncated depth \(1\le Q<H\).  Let \(\mathcal B\) be any integral
balanced top-rooted full-flag resolution: it has exactly \(M\) indexed
columns over every top, and at every column rank \(s\) each ambient
rank-\(s\) target has its prescribed floor/ceiling load.  Resolve every
column to its radius-\(Q\) quotient state.

This note proves an exact positive statement and identifies its exact
desymmetrization gate.

1. Take every coordinate relabelling of \(\mathcal B\).  The resulting
   colored multiset has constant integral multiplicity on every exact
   quotient state.
2. That multiset has an integral legal rotor cycle factorization.  Thus,
   after full symmetrization, the exact balanced flag measure is the
   stationary measure of a deterministic legal rotor transport.
3. The balanced resolutions and the rotor cycles are two integral
   resolutions of the same occurrence multiset.  Aligning equal-state
   occurrences colors the rotor cycles by balanced resolutions.  If the
   total number of maximal constant-color runs is

   \[
    R=o\!\left(\frac{|S_{2m}|W}{Q}\right),
    \tag{0.2}
   \]

   then one color has reset cost \(o(W)\), giving an integral truncated
   path factorization of exact length \(T+o(W)\le W+o(W)\) for that
   balanced resolution.
4. Consecutive queue-cylinder discrepancy gives an exact lower bound on
   this run count.  Exact rank balance after color-forgetting, even
   together with exact local per-top rank balance in every color, does
   not control this discrepancy.  This obstruction is not asserted to
   supply an ambient floor/ceiling-balanced color.

The theorem removes every fractional-denominator issue at the orbit
scale.  It does not prove (0.2), and therefore does not prove coefficient
one.

## 1. State space and the balanced color resolution

For a top \(U\in\binom{[2m]}M\), a quotient state is

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=m-Q,\quad |R|=H-Q,
\tag{1.1}
\]

whose displayed parts partition \(U\).  Its state-space size is

\[
 F:=|\Omega(U)|
 =\frac{M!}{(m-Q)!(H-Q)!}.
\tag{1.2}
\]

The legal rotor update is

\[
 (L;z_1,\ldots,z_{2Q};R)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}),
\tag{1.3}
\]

where \(x\in L\) and \(y\in R\).  Thus every state has the same in- and
outdegree

\[
 D=(m-Q)(H-Q).
\tag{1.4}
\]

Let

\[
 \mathscr S=\{(U,\omega):U\in\tbinom{[2m]}M,
                         \ \omega\in\Omega(U)\}.
\tag{1.5}
\]

Then \(|\mathscr S|=N_HF\).  Every indexed full-flag column \(c\) of
\(\mathcal B\) has a resolved state \(\rho(c)\in\mathscr S\).  Repeated
resolved states are retained as distinct column occurrences.

Let \(G=S_{2m}\).  For each \(g\in G\), the relabelled family
\(g\mathcal B\) is one **balanced color**.  It still has exactly \(M\)
columns at every top.  At every rank it merely permutes the target loads
of \(\mathcal B\), so all its loads remain the prescribed floors or
ceilings.

## 2. Exact uniform occurrence multiplicity

### Theorem 2.1 (balanced orbit resolution)

In the colored multiset

\[
 \widehat{\mathcal B}
 :=\bigsqcup_{g\in G}g\mathcal B,
\tag{2.1}
\]

every exact quotient state \(s\in\mathscr S\) occurs exactly

\[
 \boxed{
 h=T(m-H)!(m-Q)!(H-Q)!}
\tag{2.2}
\]

times.  In particular \(\widehat{\mathcal B}\) is simultaneously:

* a disjoint union of \(|G|\) integral balanced color resolutions; and
* the uniform integral quotient-state multicover of multiplicity \(h\).

#### Proof

The group \(G\) acts transitively on \(\mathscr S\).  The stabilizer of
one state may permute independently the ambient complement of its top,
its unordered \(L\)-block, and its unordered \(R\)-block.  Hence

\[
 |\operatorname{Stab}_G(s)|
 =(m-H)!(m-Q)!(H-Q)!.
\tag{2.3}
\]

Fix one indexed column \(c\) of \(\mathcal B\).  The permutations
\(g\) satisfying \(g\rho(c)=s\) form a coset of this stabilizer, so there
are exactly (2.3) of them.  Summing over the \(T\) indexed columns gives
(2.2).  The two asserted resolutions follow respectively from the
definition of the colors and from the state-independent multiplicity.
\(\square\)

The count is consistent with orbit--stabilizer:

\[
 |G|=N_HF(m-H)!(m-Q)!(H-Q)!,
\tag{2.4}
\]

and therefore \(|G|T=|\mathscr S|h\).

## 3. Exact integral legal cycle factorization

### Theorem 3.1 (rotor resolution of the same multiset)

The occurrence multiset \(\widehat{\mathcal B}\) admits a deterministic
legal successor permutation.  Equivalently, all its occurrences factor
into directed legal rotor cycles, with every full-flag column occurrence
used exactly once.

#### Proof

Fix a top \(U\).  Split \(\Omega(U)\) into a left and a right copy and
join a left state to a right state exactly when (1.3) is a legal rotor
edge.  By (1.4) this bipartite graph is \(D\)-regular.  If \(A\) is a set
of left vertices, its \(D|A|\) incident edges end in \(N(A)\), each of
whose vertices receives at most \(D\) of them.  Thus

\[
 |N(A)|\ge |A|.
\tag{3.1}
\]

Hall's theorem gives a perfect matching, hence a legal successor
permutation \(\phi_U\) of all \(F\) exact states at \(U\).

Take \(h\) labelled copies of this permutation for every top.  The result
is a legal successor permutation of a multiset containing exactly \(h\)
copies of every state in \(\mathscr S\).  By Theorem 2.1 this is exactly
the resolved-state multiplicity of \(\widehat{\mathcal B}\).  For each
state type, biject its \(h\) dynamic copies with the \(h\) indexed
full-flag column occurrences of that type.  Transporting the successor
permutation through these typewise bijections gives the claimed
permutation of the actual column occurrences.  Every finite permutation
is a disjoint union of cycles. \(\square\)

Thus the fully symmetrized exact balanced flow has an integral stationary
rotor coupling.  No averaging or rational transition weight remains.
What remains is to respect one balanced color at a time.

## 4. The exact low-switch desymmetrization problem

Fix the typewise bijections in the last paragraph of the proof of
Theorem 3.1.  Every vertex of every rotor cycle now carries the color
\(g\) of its column occurrence in \(g\mathcal B\).  On each directed
cycle, split the cyclic color word into maximal constant-color runs; an
entirely monochromatic cycle counts as one run.  Put

\[
 R_g=\#\{\text{runs of color }g\},
 \qquad R=\sum_{g\in G}R_g.
\tag{4.1}
\]

Every run is a genuine legal rotor path.  For a fixed color \(g\), its
runs partition precisely the \(T\) columns of \(g\mathcal B\), hence
preserve all of that color's exact floor/ceiling loads.

### Proposition 4.1 (run ledger)

The radius-\(Q\) columns of color \(g\) compile in literal length

\[
 \boxed{T+(2Q+1)R_g.}
\tag{4.2}
\]

Consequently some balanced color compiles in length at most

\[
 T+(2Q+1)\frac{R}{|G|}.
\tag{4.3}
\]

In particular, (0.2) implies an \(o(W)\) reset toll.

#### Proof

A rotor path with \(a\) state endpoints is initialized by \(2Q+2\)
nonempty masks and then uses one new mask for each of its remaining
\(a-1\) endpoints.  Its exact length is \(a+2Q+1\).  Summing over the
\(R_g\) runs proves (4.2).  Since \(\sum_gR_g=R\), some color has
\(R_g\le R/|G|\), proving (4.3).  Finally

\[
 (2Q+1)\frac{R}{|G|}=o(W)
\]

under (0.2). \(\square\)

Together with \(T\le W\), this gives exact compiled length at most
\(W+o(W)\).

Theorem 3.1 alone gives no bound on \(R\): its cycles may change balanced
color at every vertex.  This is the precise distinction between an
integral stationary factorization after symmetrization and a usable
one-resolution factorization.

## 5. A fixed-top cylinder lower bound for the number of runs

Let \(\mathcal A\) be any multiset of \(s\) states at one top.  For an
injective word \(w\) of length \(2Q-1\), define

\[
 P_{\mathcal A}(w)
 =\#\{\omega\in\mathcal A:(z_1,\ldots,z_{2Q-1})=w\},
\tag{5.1}
\]

\[
 S_{\mathcal A}(w)
 =\#\{\omega\in\mathcal A:(z_2,\ldots,z_{2Q})=w\}.
\tag{5.2}
\]

### Proposition 5.1 (current-endpoint cylinder charge)

If \(\mathcal A\) is partitioned into \(p\) legal directed rotor paths,
then

\[
 \boxed{
 \|P_{\mathcal A}-S_{\mathcal A}\|_1\le2p.}
\tag{5.3}
\]

Hence every such path factor has

\[
 p\ge\frac12\|P_{\mathcal A}-S_{\mathcal A}\|_1.
\tag{5.4}
\]

#### Proof

On every internal rotor edge \(\omega\to\eta\), the queue shift gives

\[
 (z_1(\omega),\ldots,z_{2Q-1}(\omega))
 =(z_2(\eta),\ldots,z_{2Q}(\eta)).
\tag{5.5}
\]

Delete the \(p\) terminal vertices from the multiset counted by
\(P_{\mathcal A}\), and delete the \(p\) initial vertices from the
multiset counted by \(S_{\mathcal A}\).  Equation (5.5) pairs the two
remaining word multisets exactly.  Deleting one unit changes a histogram
by \(1\) in \(\ell^1\), so the original histograms differ by at most
\(p+p\). \(\square\)

Apply this proposition to the \(M\)-column table over every top of one
balanced color.  If \(\delta_{g,U}\) denotes its cylinder discrepancy,
then

\[
 R_g\ge\frac12\sum_U\delta_{g,U}.
\tag{5.6}
\]

Therefore a necessary condition for an \(o(W)\) reset ledger is

\[
 \sum_U\delta_{g,U}=o(W/Q)
\tag{5.7}
\]

for at least one balanced color.  Rank-set loads do not determine these
ordered fixed-top cylinder histograms.

Under the hypotheses of its construction
\(2\le Q\le H-2\) and \(H<m\), the explicit cyclic anticycle table in
`MATH_ATTACK_TRP_BALANCED_FLOW_HIDDEN_COLOR_OBSTRUCTION_20260725.md`
has \(\delta=2M\), while all of its one-position queue marginals and all
proper-rank per-top flag loads are exactly balanced.  Thus (5.4) gives
\(p\ge M\), which is sharp because that table has no legal edge at all.
Its full coordinate orbit is exactly ambient-rank-balanced only after
the color is forgotten; its individual global colors are not claimed to
have the ambient floor/ceiling loads imposed on \(\mathcal B\).

## 6. Proved boundary

The following statements are now exact.

* Full coordinate symmetrization turns every integral balanced flag
  resolution into a uniform integral quotient-state multicover.
* That multicover has a deterministic legal rotor cycle factorization.
* Desymmetrizing it with coefficient-one reset cost is exactly a charged
  low-color-run problem.  The sufficient scale is (0.2).
* Consecutive queue-cylinder discrepancy is a mandatory charge.  The
  anticycle construction shows that it can be maximal while local
  per-top rank balance and one-coordinate balance hold in every color and
  ambient rank balance holds after color-forgetting.  It does not provide
  a bad ambient-balanced color.

What is not proved is the existence of a single ambient floor/ceiling
balanced resolution whose fixed-top tables satisfy weighted successor
Hall and have total path count \(o(W/Q)\).  The exact positive target is
therefore a **conditional balanced-flow construction** controlling the
ordered queue cylinders (or the full Hall system) before symmetrization;
aggregate stationary balance cannot be desymmetrized by itself.

## 7. Exact occurrence-transport follow-up

`MATH_ATTACK_ROTOR_SCD_SYMMETRIZED_LOW_RUN_TRANSPORT_20260725.md`
optimizes the color runs after the legal successor permutation and the
equal-state occurrence alignment are both allowed to vary.  If
\(p_U^*(\mathcal B)\) is the minimum legal path-factor component count in
the \(M\)-column table of the base resolution at top \(U\), then the exact
orbit optimum is

\[
 R_{\rm orb}^*(\mathcal B)
 =|S_{2m}|\sum_U p_U^*(\mathcal B).
\]

The upper bound is an integral endpoint-transport construction: conjugate
optimal base path factors through the full coordinate orbit, observe that
their start and end multiplicities are exactly equal at every quotient
state, and splice them with copies of one perfect matching of the regular
rotor state graph.  The lower bound holds for every chronology because
each color/top run family is a path factor of its prescribed table.

Consequently the cycle-cylinder law with parameters \(\theta_U\) gives the
genuine low-run assignment

\[
 R_{\rm orb}^*(\mathcal B)
 \le |S_{2m}|H_M\sum_U\theta_U,
\]

while every orbit coloring obeys

\[
 R\ge |S_{2m}|\sum_U
 \max\{\Delta_U,\delta_U/2\}.
\]

This follow-up optimizes the rotor cycle resolution.  Recoloring one
arbitrarily frozen cycle factor remains a more restrictive problem.
