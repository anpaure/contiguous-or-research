# Augmented template orbits: one matching implies every weighted cut

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

Let one fixed augmented rotor/geodesic template be acted on by
\(G=S_{2m}\), retaining indexed copies if the template has a stabilizer.
Its edge orbit is edge-transitive.  There is an exact positive
symmetrization theorem:

> If the orbit hypergraph contains one matching occupying a
> \((1-\varepsilon)\)-fraction of its tag capacity, then every nonnegative
> weighted matching cut holds with loss \((1-\varepsilon)^{-1}\).

More precisely, if there are \(T\) tags, every edge contains one tag, and
the tag degree is \(D\), then a matching of size at least
\((1-\varepsilon)T\) implies

\[
 \boxed{
 \nu_y({\cal H})
 \ge {1-\varepsilon\over D}\,y(E({\cal H}))
 \qquad(y:E({\cal H})\to{\mathbb R}_{\ge0}).}
\tag{0.1}
\]

Equivalently,

\[
 \boxed{\chi_f'({\cal H})\le {D\over1-\varepsilon}.}
\tag{0.2}
\]

This conclusion is hereditary under arbitrary edge deletion or
reweighting: put weight zero on the deleted edges.  It is therefore
exactly the proposed route by which one unweighted full-orbit matching
would settle all weighted residual cuts.

For the calibrated multirank trajectory edge, a matching of size \(N-r\)
unpacks into one integral template-tiled partial SCD/rotor resolution.
Its exact total protected-band hole count is

\[
 \boxed{\delta_\Sigma+rK,}
\tag{0.3}
\]

where \(N=\binom{2m}{m+H}\) is the number of carrier tags,
\(\delta_\Sigma=o(W)\) is the floor ledger, and

\[
 K=M+2\sum_{q=1}^Q\kappa_q
\tag{0.4}
\]

is the number of protected mask targets in one augmented edge.  Hence
the direct coefficient-one requirement is

\[
 rK=o(W).
\tag{0.5}
\]

Writing \(\varepsilon=r/N\) and

\[
 \Lambda_Q={W+2\sum_{q=1}^QN_q\over W},
\]

condition (0.5) is

\[
 \varepsilon\Lambda_Q=o(1).
\tag{0.6}
\]

In a Gaussian-width band, \(\Lambda_Q=\Theta(\sqrt m)\), so the required
relative leave is \(\varepsilon=o(m^{-1/2})\).

The relation to SCDs is one-way and exact.  A matching is equivalent to a
partial band resolution whose chains are partitioned into coordinate
copies of the fixed augmented template.  It is not equivalent to an
arbitrary SCD/rotor resolution.  Even a tag-saturating matching generally
is not a full SCD, because the calibrated floor defects leave
\(\delta_0=W-MN\) middle owners and \(\delta_q\) masks in the other ranks.

Thus the orbit argument closes the weighted-cut implication completely.
It does not prove the unweighted matching.  Edge transitivity and the
uniform fractional point alone do not imply a near-perfect matching; the
actual multirank geometry is still needed.

## 1. Abstract edge-orbit theorem

Let a finite group \(G\) act transitively on the indexed edge set \(E\)
of a finite hypergraph \({\cal H}\).  Vertices need not form one orbit,
and the hypergraph may be multipartite.  For a matching \({\cal M}\),
write

\[
 s=|{\cal M}|.
\]

For \(g\in G\), the translate \(g{\cal M}\) is again a matching.

### Lemma 1.1 (uniform orbit multiplicity)

Every indexed edge of \({\cal H}\) occurs in exactly

\[
 \boxed{\lambda={|G|s\over|E|}}
\tag{1.1}
\]

of the indexed translates \(g{\cal M}\).

#### Proof

Fix \(e\in E\).  Count pairs

\[
 (g,f)\in G\times{\cal M}
 \quad\text{such that}\quad gf=e.
\]

For each \(f\in{\cal M}\), the set of such \(g\) is a coset of
\(\operatorname {Stab}_G(e)\), and therefore has size
\(|\operatorname {Stab}_G(e)|\).  Hence the count is

\[
 s|\operatorname {Stab}_G(e)|.
\]

Edge transitivity gives

\[
 |E|={|G|\over|\operatorname {Stab}_G(e)|},
\]

which proves (1.1).  In particular, the displayed rational number is an
integer. \(\square\)

### Theorem 1.2 (one matching gives all weighted cuts)

For every nonnegative edge weighting \(y=(y_e)\),

\[
 \boxed{
 \nu_y({\cal H})
 :=\max_{{\cal N}\text{ matching}}\sum_{e\in{\cal N}}y_e
 \ge {s\over|E|}\sum_{e\in E}y_e.}
\tag{1.2}
\]

Moreover, the \(|G|\) translates of \({\cal M}\) form a proper edge
coloring of the \(\lambda\)-fold edge multihypergraph.  Consequently

\[
 \boxed{
 \chi_f'({\cal H})\le {|E|\over s}.}
\tag{1.3}
\]

#### Proof

By Lemma 1.1,

\[
 \begin{aligned}
 {1\over|G|}\sum_{g\in G}y(g{\cal M})
 &={1\over|G|}\sum_{e\in E}\lambda y_e\\
 &={s\over|E|}\sum_{e\in E}y_e.
 \end{aligned}
\tag{1.4}
\]

Some translate has weight at least this average, proving (1.2).

The same incidence count says that the matchings \(g{\cal M}\), viewed as
colors, cover every indexed edge exactly \(\lambda\) times.  Giving each
color weight \(1/\lambda\) is a fractional edge coloring of total weight

\[
 {|G|\over\lambda}={|E|\over s}.
\]

Equivalently, without division, the translates properly color
\(\lambda\) labelled copies of every edge with \(|G|\) colors.  This
proves (1.3). \(\square\)

### Corollary 1.3 (tag normalization)

Suppose every edge contains exactly one tag, there are \(T\) tags, and
every tag has degree \(D\).  Then

\[
 |E|=DT.
\tag{1.5}
\]

If \(s\ge(1-\varepsilon)T\), Theorem 1.2 gives

\[
 \nu_y({\cal H})
 \ge {1-\varepsilon\over D}y(E),
\tag{1.6}
\]

and

\[
 \chi_f'({\cal H})
 \le {D\over1-\varepsilon}
 =D(1+\varepsilon+O(\varepsilon^2)).
\tag{1.7}
\]

If \(s=T\), then the tag star gives the reverse inequality
\(\chi_f'\ge D\), and hence

\[
 \boxed{\chi_f'({\cal H})=D.}
\tag{1.8}
\]

Taking \(y=\mathbf1_F\) for an arbitrary edge subset \(F\subseteq E\)
shows the hereditary form

\[
 \boxed{
 \nu({\cal H}[F])
 \ge {1-\varepsilon\over D}|F|.}
\tag{1.9}
\]

Thus later deletion of edges, including deletion caused by a residual
vertex set, creates no new weighted cut at the original \(D\)-scale.
This does not assert the stronger renormalized inequality
\(\nu({\cal H}[F])\ge(1-o(1))|F|/D_F\) when the residual maximum degree
\(D_F\) is much smaller than \(D\).  The renormalized statement is
unnecessary for the global fractional coloring furnished by the orbit
translates, but it would still be needed by an iterative proof which
discards those translates and restarts from the residual alone.

## 2. What edge transitivity does not prove

Theorem 1.2 begins with an integral matching.  It cannot be reversed from
edge transitivity or from the uniform fractional point.

A simple \(S_n\)-orbit example makes this exact.  Let the vertices be
the pairs \(\binom{[n]}2\).  For \(i\in[n]\), let

\[
 E_i=\{\{i,j\}:j\ne i\}.
\tag{2.1}
\]

The family \(\{E_i:i\in[n]\}\) is one edge orbit under \(S_n\).  Giving
every \(E_i\) weight \(1/2\) covers every pair vertex exactly once, so it
is an exact fractional perfect matching of value \(n/2\).  Nevertheless

\[
 E_i\cap E_j=\{\{i,j\}\}\ne\varnothing
\qquad(i\ne j),
\]

and therefore the integral matching number is one.

This example is not asserted to occur inside the rotor/geodesic
catalogue.  It proves that full symmetric-group edge transitivity,
regularity, and even an exact fractional perfect matching do not establish
the desired integral matching.  The fixed template's interval and
geodesic geometry must still be used.

The orbit hypothesis must also be kept literal.  A catalogue containing
several nonconjugate schedule or priority templates is a union of edge
orbits, not one edge-transitive hypergraph.  A matching in one orbit proves
the weighted cuts for that orbit and gives a direct construction from it;
it does not color arbitrary demand placed on the other orbits.

## 3. The fixed augmented trajectory orbit

Now specialize to the even-dimensional deterministic trajectory setup.
Put

\[
 W=\binom{2m}m,\qquad
 M=m+H,\qquad
 N=\binom{2m}M,
\tag{3.1}
\]

and let

\[
 N_q=\binom{2m}{m-q}.
\]

Fix one internally rainbow augmented trajectory template \(A\) on a
reference carrier \(U_0\).  It contains

* the carrier tag \(t_{U_0}\);
* all \(M\) middle-owner phase columns; and
* \(\kappa_q\) claimed lower targets and \(\kappa_q\) claimed upper
  targets at every \(1\le q\le Q\).

The common priority law gives

\[
 \kappa_0=M,\qquad
 \kappa_q=\min\left\{M,\left\lfloor{N_q\over N}\right\rfloor\right\}.
\tag{3.2}
\]

Take the indexed coordinate orbit

\[
 {\cal E}_A=\{gA:g\in S_{2m}\}.
\tag{3.3}
\]

If distinct group elements yield the same unindexed support, retain the
resulting labelled parallel edges.  The group is transitive on this
indexed edge set and on the carrier tags.

Let \({\cal H}_A\) be the augmented hypergraph whose vertices are the
carrier tags and all protected Boolean targets.  Put

\[
 K=M+2\sum_{q=1}^Q\kappa_q.
\tag{3.4}
\]

Every augmented edge contains one tag and exactly \(K\) protected
targets.

## 4. Exact hole ledger of an orbit matching

Define the floor defects

\[
 \delta_0=W-MN,
\qquad
 \delta_q=N_q-N\kappa_q
\quad(1\le q\le Q),
\tag{4.1}
\]

and

\[
 \delta_\Sigma=\delta_0+2\sum_{q=1}^Q\delta_q.
\tag{4.2}
\]

The calibrated trajectory calculation gives

\[
 \delta_\Sigma=o(W).
\tag{4.3}
\]

### Theorem 4.1 (matching equals a zero-collision extraction)

Let \({\cal M}\) be a matching in \({\cal H}_A\) of size

\[
 |{\cal M}|=N-r.
\tag{4.4}
\]

Then its selected templates leave exactly

\[
 \boxed{h_0=\delta_0+Mr}
\tag{4.5}
\]

middle masks and

\[
 \boxed{h_q^\pm=\delta_q+\kappa_qr}
\tag{4.6}
\]

masks in each signed depth-\(q\) row.  Hence the total protected-band
hole count is

\[
 \boxed{
 h_{\rm band}
 =\delta_\Sigma+rK.}
\tag{4.7}
\]

#### Proof

The matching uses distinct carrier tags, so it selects \(N-r\)
templates.  Internal rainbowness and target-disjointness of different
matching edges show that their \(M(N-r)\) middle claims are all distinct.
Subtracting from \(W\) proves (4.5).

At signed depth \(q\), the selected edges similarly make exactly
\(\kappa_q(N-r)\) distinct claims.  Subtracting this from \(N_q\) and
using (4.1) proves (4.6).  Summation gives (4.7).
\(\square\)

There is also an exact useful normalization.  Put

\[
 V_Q=W+2\sum_{q=1}^QN_q.
\tag{4.8}
\]

Then

\[
 \boxed{NK=V_Q-\delta_\Sigma.}
\tag{4.9}
\]

Consequently, for \(r=\varepsilon N\),

\[
 h_{\rm band}
 =\delta_\Sigma+\varepsilon(V_Q-\delta_\Sigma).
\tag{4.10}
\]

Thus a matching with

\[
 \boxed{
 \varepsilon{V_Q\over W}=o(1)}
\tag{4.11}
\]

leaves only \(o(W)\) protected masks.  In a fixed Gaussian window
\(Q=A\sqrt m\),

\[
 {V_Q\over W}=\Theta_A(\sqrt m),
\tag{4.12}
\]

while if \(Q/\sqrt m\to\infty\) through the calibrated range, the ratio is
\((\sqrt\pi+o(1))\sqrt m\).  Hence (4.11) becomes

\[
 \boxed{\varepsilon=o(m^{-1/2}).}
\tag{4.13}
\]

This is the precise meaning of “near-perfect” for the full augmented
edge.  An unspecified \(o(1)\) tag leave is insufficient.

### Corollary 4.2 (direct literal consequence)

Assume the audited reset and outer-tail hypotheses

\[
 QN=o(W),\qquad
 \text{outer-tail size}=o(W).
\tag{4.14}
\]

If (4.11) holds, the selected templates give a nonzero contiguous-OR word
of length \(W+o(W)\).

#### Proof

Cut and emit every selected trajectory.  Their total primary length is at
most

\[
 (N-r)(M+2Q+1)
 \le MN+(2Q+1)N
 =W-\delta_0+o(W).
\]

By (4.3), (4.10), and (4.11), the protected holes have total size
\(o(W)\); append them literally.  Append the \(o(W)\) outer masks.  The
total is \(W+o(W)\). \(\square\)

## 5. Relation to an SCD/rotor resolution

Every phase column of \(A\) is a nested symmetric-chain segment

\[
 L_{d(t)}(t)\subset\cdots\subset X_t
 \subset\cdots\subset U_{d(t)}(t),
\tag{5.1}
\]

and the \(M\) columns of one template are internally disjoint at every
claimed rank.  They are also arranged in one literal rotor/geodesic
chronology.

### Proposition 5.1 (exact template-tiling equivalence)

A matching of \(s\) edges in \({\cal H}_A\) is equivalent to a family of
pairwise target-disjoint symmetric-chain columns which

1. is partitioned into \(s\) blocks;
2. has every block equal, after one coordinate permutation, to the fixed
   augmented template \(A\); and
3. inherits the literal rotor/geodesic chronology inside every block.

#### Proof

Unpack every matching edge into its phase columns.  Internal rainbowness
gives disjointness inside a block, and the hypergraph matching condition
gives disjointness between blocks.  All remaining properties are part of
the augmented-edge definition.

Conversely, replace every template block in such a column family by its
corresponding orbit edge.  Pairwise target disjointness and distinct
carrier tags say exactly that these edges form a matching.
\(\square\)

Thus a tag-saturating matching is one **template-tiled partial band
SCD/rotor resolution**.  It is not generally a full SCD.  Indeed, even
when \(r=0\), it contains only

\[
 MN=W-\delta_0
\tag{5.2}
\]

middle columns and leaves the floor defects (4.5)--(4.6).  Unless all
these defects vanish, it cannot be an exact SCD resolution.

In the exceptional exact-calibration case

\[
 MN=W,\qquad N\kappa_q=N_q\quad(1\le q\le Q),
\tag{5.3}
\]

a tag-saturating matching covers every protected mask exactly once.
Its unpacked columns are then a saturated symmetric-chain decomposition
of the band, tiled by copies of \(A\).  The audited band-extension theorem
extends it to a full SCD while retaining every internal band adjacency.
Thus an exact SCD is recovered precisely in this zero-floor special case.

Conversely, an arbitrary full SCD or an arbitrary low-run rotor resolution
does not imply a matching in \({\cal H}_A\).  It would have to admit the
extra partition in Proposition 5.1 into blocks all lying in the single
coordinate orbit of \(A\).  The fixed gap schedule, priority pattern,
carrier grouping, and within-block intersection table are invariants of
that orbit and are not consequences of the SCD rank equations.

If an exact band SCD happens to possess this template tiling, then its
blocks give a matching.  This is the precise, and only automatic,
connection with one SCD/rotor resolution.

## 6. Consequences of a near-perfect orbit matching

Let \(D\) be the tag degree of \({\cal H}_A\).  Since there are \(N\)
tags,

\[
 |{\cal E}_A|=DN.
\tag{6.1}
\]

If a matching has size \(N-r=(1-\varepsilon)N\), Corollary 1.3 gives,
for every nonnegative edge weight \(y\),

\[
 \boxed{
 \nu_y({\cal H}_A)
 \ge {1-\varepsilon\over D}y({\cal E}_A),}
\tag{6.2}
\]

and

\[
 \boxed{
 \chi_f'({\cal H}_A)
 \le {D\over1-\varepsilon}.}
\tag{6.3}
\]

After a common integral blow-up, the coordinate translates of the one
matching are themselves the colors achieving (6.3).  No additional
weighted matching, Berge-cycle, or residual-cut theorem is needed.
By Proposition 5.1, every such color is a coordinate copy of the same
template-tiled partial SCD/rotor resolution.  Thus orbiting one matching
does give an exact multicover resolution into geometric colors; the only
qualification is that each color has the common floor and matching leave,
rather than being a full SCD.

There are two different accuracy requirements.

1. For direct use of the one matching and literal repair, (4.11) is
   enough; in the Gaussian band this is
   \(\varepsilon=o(m^{-1/2})\).
2. To obtain a no-reserve edge-coloring with
   \(D(1+o(1/Q))\) colors, one needs the stronger
   \(\varepsilon=o(1/Q)\).

The first route is cheaper because it uses the large matching itself.
The second decomposes every orbit edge demand into matchings.

## 7. What remains open

The orbit argument has therefore reduced the weighted problem to one
unweighted statement:

> **Augmented orbit matching gate.**  For one fixed internally rainbow
> multirank trajectory template \(A\), prove that its full
> \(S_{2m}\)-orbit hypergraph has a matching of size
> \[
> N-o(N/\sqrt m).
> \]

Such a matching directly gives \(o(W)\) aggregate band holes and, by
Theorem 1.2, every weighted residual cut.

This gate is not proved by the current orbit census.  The uniform orbit
weights give the already known joint fractional matching.  Adjacent
nested rows have relative codegree \(\Theta(1/m)\), while one augmented
edge has \(K=\Theta(M\sqrt m)\) protected targets in a Gaussian band.
Thus the ordinary growing-rank pair-codegree parameter does not vanish.

The exact positive content is nevertheless substantial: one need not
prove a hereditary weighted theorem separately.  A single sufficiently
large unweighted matching in the genuine multirank augmented edge orbit
would supply it automatically.
