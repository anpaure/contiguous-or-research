# Edge-transitive symmetrization and augmented geodesic orbit packing

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Fix one legal geodesic schedule, one priority template, one labelled
carrier, and all of its protected claims.  Regard the carrier tag, every
middle owner, and every protected lower and upper target as vertices of one
augmented edge.  Take its full \(S_{2m}\)-coordinate orbit.

The symmetrization insight is exact:

\[
 \boxed{
 \sup_{y\ge0}
 {\sum_{e\in\mathcal O}y_e
  \over\max_{M\text{ matching}}\sum_{e\in M}y_e}
 ={ |\mathcal O|\over\nu(\mathcal O)}.}
 \tag{0.1}
\]

The weights may be supported on an arbitrary residual subfamily.  Thus all
residual weighted matching cuts of this orbit reduce exactly to its
ordinary unweighted matching number.

If \(T\) is the number of tags and \(d_{\rm tag}=|\mathcal O|/T\), the
uniform orbit point has weight \(1/d_{\rm tag}\) on every edge.  Its exact
weighted cut value is

\[
 \boxed{{T\over\nu(\mathcal O)}.}
 \tag{0.2}
\]

Consequently the no-reserve coefficient-one gate for this one orbit is
precisely

\[
 \boxed{
 \nu(\mathcal O)=T-o(T/Q).}
 \tag{OP_Q}
\]

No complete color-resolution theorem is needed once \((OP_Q)\) is proved.

The exact orbit codegrees can also be computed.  Target-pair codegrees have
the factorial rank-gap decay and pair-square estimates already found for
the symmetrized catalogue.  They do not yet prove \((OP_Q)\):

* the largest relative pair codegree is \(\Theta(1/m)\), while one
  augmented edge has \(m^{3/2+o(1)}\) protected targets;
* claimed crossing squares of side \(s\asymp\log m\) make the standard
  full-codegree root parameter bounded, not divergent; and
* orbit-invariance is lost after conditioning on a partial matching, so
  the raw pair-square bounds still require a hereditary
  survival-conditioned recurrence.

Thus edge transitivity closes the **weighted** part of the problem
completely.  The remaining theorem is the unweighted augmented orbit
packing \((OP_Q)\).  The exact middle-only wreath packing is the matching
number of a projection obtained by deleting the protected targets; it says
nothing about \((OP_Q)\) and is not used below.

## 1. The augmented coordinate orbit

Put

\[
 n=2m,
 \qquad M=m+H,
 \qquad G=S_n,
 \qquad \mathcal U=\binom{[n]}M,
 \qquad T=|\mathcal U|.
 \tag{1.1}
\]

Fix one carrier \(U_0\), one schedule and priority template on it, and one
legal augmented edge

\[
 e_0=\{\tau_{U_0}\}\cup C_0.
 \tag{1.2}
\]

Here \(\tau_{U_0}\) is the carrier tag and \(C_0\) contains all claimed
protected targets.  For each protected rank \(r\), put

\[
 k_r=|C_0\cap\tbinom{[n]}r|,
 \qquad
 K=|C_0|=\sum_rk_r.
 \tag{1.3}
\]

For the full carrier trajectory,

\[
 k_m=M,
 \qquad
 k_{m-q}=k_{m+q}=c_q
 \quad(1\le q\le Q),
 \tag{1.4}
\]

where the priority template fixes the actual claimed phase sets of these
sizes.  Every target in \(C_0\) is a subset of \(U_0\).

Let

\[
 \mathcal O=G e_0
 \tag{1.5}
\]

be the simple orbit of augmented supports.  Equivalently one may retain
the labelled orbit indexed by \(G\); every argument below is unchanged,
because left multiplication acts transitively on the labelled copies.
The vertex set is the disjoint union of

\[
 \{\tau_U:U\in\mathcal U\}
 \quad\text{and}\quad
 \binom{[n]}r
 \quad(r\text{ protected}).
 \tag{1.6}
\]

The action of \(G\) is transitive on \(E(\mathcal O)\), on the tag
stratum, and separately on every protected target rank.

The calibration is

\[
 Tk_r\le R_r:=\binom nr
 \quad(r\text{ protected}),
 \tag{1.7}
\]

and its total scalar deficit is \(o(W)\).  Thus the uniform orbit measure
is already a genuine fractional matching in the augmented hypergraph.

## 2. Exact residual weighted reduction

### Theorem 2.1 (edge-transitive weighted matching identity)

Let \(\mathcal H\) be any finite edge-transitive multi-hypergraph, and let
\(\nu=\nu(\mathcal H)\).  For every nonnegative edge weighting \(y\),

\[
 \boxed{
 \max_{M\text{ matching}}\sum_{e\in M}y_e
 \ge {\nu\over|E(\mathcal H)|}
       \sum_{e\in E(\mathcal H)}y_e.}
 \tag{2.1}
\]

Moreover the coefficient is exact:

\[
 \boxed{
 \sup_{y\ge0}
 {\sum_e y_e\over\max_M\sum_{e\in M}y_e}
 ={ |E(\mathcal H)|\over\nu}.}
 \tag{2.2}
\]

#### Proof

Fix a maximum unweighted matching \(M_0\), \(|M_0|=\nu\), and choose a
uniform group element \(g\) from an edge-transitive automorphism group.
For every edge \(e\), transitivity makes

\[
 \Pr(e\in gM_0)=p
\]

independent of \(e\).  Summing these probabilities over all edges gives

\[
 p|E(\mathcal H)|=\mathbb E|gM_0|=\nu,
\]

so \(p=\nu/|E(\mathcal H)|\).  Therefore

\[
 \mathbb E\sum_{e\in gM_0}y_e
 ={\nu\over|E(\mathcal H)|}\sum_e y_e.
\]

Some translate attains at least its expectation, proving (2.1).  Taking
\(y_e=1\) for every edge gives equality in the ratio, proving (2.2).
\(\square\)

### Residual interpretation

The weighting \(y\) may vanish outside any prescribed residual family
\(\mathcal R\subseteq E(\mathcal H)\).  Delete the zero-weight edges from
the translated matching in (2.1).  Hence

\[
 \max_{M\subseteq\mathcal R}\sum_{e\in M}y_e
 \ge {\nu(\mathcal H)\over|E(\mathcal H)|}
       \sum_{e\in\mathcal R}y_e.
 \tag{2.3}
\]

This is the exact residual weighted reduction.  The residual family need
not be invariant under the group.

The scope is important.  Equation (2.3) treats an arbitrary matching
objective \(y\), including a residual support encoded by zero weights.  It
does not replace a genuinely nonuniform edge-demand vector \((m_e)\) by
its average: in a fractional-coloring dual the numerator would contain
\(m_ey_e\) while the matching denominator still contains \(y_e\).  The
present reduction applies exactly because the fixed coordinate orbit point
has one common demand on every orbit edge.

### Corollary 2.2 (uniform orbit cut)

For the augmented orbit \(\mathcal O\), let

\[
 d_{\rm tag}={|\mathcal O|\over T}.
 \tag{2.4}
\]

Give every orbit edge weight \(x_e=1/d_{\rm tag}\).  Then

\[
 \boxed{
 \sup_{y\ge0}
 {\sum_ex_ey_e\over\max_M\sum_{e\in M}y_e}
 ={T\over\nu(\mathcal O)}.}
 \tag{2.5}
\]

#### Proof

Divide (2.2) by \(d_{\rm tag}\) and use
\(|\mathcal O|=Td_{\rm tag}\). \(\square\)

Thus the weighted cut is \(1+o(1/Q)\) if and only if \((OP_Q)\) holds.
If it holds, rational LP denominator clearing gives an integral color
blow-up at the same normalized scale, and the two-ledger extraction theorem
selects one coefficient-safe color.  More economically, the matching in
\((OP_Q)\) itself is already the required one-column selection.

## 3. Exact augmented degrees and codegrees

All formulas in this section include the tag and every protected target.

### Proposition 3.1 (one-vertex degrees)

Every tag has degree

\[
 d_{\rm tag}={|\mathcal O|\over T},
 \tag{3.1}
\]

and every rank-\(r\) target has degree

\[
 \boxed{
 d_r={|\mathcal O|k_r\over R_r}.}
 \tag{3.2}
\]

Consequently

\[
 {d_r\over d_{\rm tag}}={Tk_r\over R_r}\le1.
 \tag{3.3}
\]

#### Proof

Every orbit edge contains one tag and \(k_r\) rank-\(r\) targets.  Double
count incidences and use transitivity on each vertex stratum. \(\square\)

### Proposition 3.2 (tag-target codegrees)

For a tag \(\tau_U\) and a rank-\(r\) target \(S\),

\[
 d(\tau_U,S)=0\quad\text{if }S\not\subseteq U.
 \tag{3.4}
\]

If \(S\subseteq U\), then

\[
 \boxed{
 {d(\tau_U,S)\over d_{\rm tag}}
 ={k_r\over\binom Mr},}
 \tag{3.5}
\]

and

\[
 \boxed{
 {d(\tau_U,S)\over d_r}
 ={1\over\binom{n-r}{M-r}}.}
 \tag{3.6}
\]

Distinct tags have codegree zero.

#### Proof

The stabilizer of \(U\) is transitive on its rank-\(r\) subsets.  A path
over \(U\) has \(k_r\) such targets, proving (3.5).  Equation (3.6)
follows from

\[
 T\binom Mr=R_r\binom{n-r}{M-r}.
\]

No augmented edge contains two tags. \(\square\)

### Proposition 3.3 (exact target-pair codegrees)

Fix protected ranks \(r,s\).  For \(0\le t\le\min(r,s)\), let

\[
 a_{r,s,t}
 =\#\{(A,B)\in C_0^2:
       A\ne B,\ |A|=r,\ |B|=s,\ |A\cap B|=t\}.
 \tag{3.7}
\]

For a fixed rank-\(r\) target \(S\), the number of rank-\(s\) targets
\(Z\) with \(|S\cap Z|=t\) is

\[
 b_{r,s,t}=\binom rt\binom{n-r}{s-t}.
 \tag{3.8}
\]

Every such ordered pair \((S,Z)\) has codegree

\[
 \boxed{
 d(S,Z)={|\mathcal O|a_{r,s,t}\over R_rb_{r,s,t}},}
 \tag{3.9}
\]

and hence

\[
 \boxed{
 {d(S,Z)\over d_r}
 ={a_{r,s,t}\over k_rb_{r,s,t}}.}
 \tag{3.10}
\]

#### Proof

Every orbit edge has exactly \(a_{r,s,t}\) ordered target pairs of this
type.  There are \(R_rb_{r,s,t}\) ambient ordered pairs of the type, and
the coordinate group is transitive on them.  Double counting proves
(3.9); divide by (3.2) to obtain (3.10). \(\square\)

The symmetrically normalized row square also has the exact expression

\[
 \boxed{
 \sum_{Z\ne S}{d(S,Z)^2\over d_rd_{|Z|}}
 =\sum_{s,t}
 {a_{r,s,t}^2R_s
  \over k_rk_sR_rb_{r,s,t}}.}
 \tag{3.11}
\]

This is obtained by multiplying the square of (3.9) by the
\(b_{r,s,t}\) targets of each type and substituting (3.2).

### Higher patterns

More generally, let \(\mathfrak a\) be a feasible membership-atom type of
an ordered target tuple.  If \(a_{\mathfrak a}\) is the number of ordered
occurrences of that type inside \(C_0\), and \(N_{\mathfrak a}\) is the
number of ambient ordered tuples of that type, then

\[
 \boxed{
 d(\mathbf S)={|\mathcal O|a_{\mathfrak a}
                  \over N_{\mathfrak a}}.}
 \tag{3.12}
\]

This is the exact multiple-codegree formula for the fixed-template orbit.
It is simply orbit transitivity plus the membership atoms; no independence
assumption is present.

## 4. What the exact pair codegrees give

For two protected targets put

\[
 \alpha=|S\setminus Z|,
 \qquad
 \beta=|Z\setminus S|.
 \tag{4.1}
\]

The geodesic pair formula applied to (3.10) gives

\[
 {d(S,Z)\over d(S)}
 \le
 {C(1+\alpha+\beta)
  \over\binom{|S|}{\alpha}
          \binom{n-|S|}{\beta}}.
 \tag{4.2}
\]

For same-rank distinct targets, the squared normalized row is

\[
 O(m^{-2}),
 \tag{4.3}
\]

and for rank gap \(h\ne0\),

\[
 \sum_{|Z|=|S|+h}
 {d(S,Z)^2\over d(S)d(Z)}
 \le C(|h|+1)^2|h|!(C/m)^{|h|}.
 \tag{4.4}
\]

The tag-target block (3.5)--(3.6) is exponentially smaller.  These are
the actual augmented pair-square estimates; the tag causes no loss.

There are also adjacent nested target pairs occurring at the same physical
phase.  For the central protected depths, their occurrence counts in
\(C_0\) are a \((1-o(1))\) fraction of the relevant \(k_r\).  Since
\(b_{r,r+1,r}=n-r=m+O(Q)\), (3.10) gives

\[
 \boxed{
 \max_{S\ne Z}{d(S,Z)\over d(S)}=\Theta(1/m).}
 \tag{4.5}
\]

Thus the maximum pair codegree is small relative to degree, but not small
relative to the growing edge rank.  Gaussian summation of (1.4) gives

\[
 K=M+2\sum_{q=1}^Qc_q
 =\Theta(M\sqrt m)=m^{3/2+o(1)}.
 \tag{4.6}
\]

Consequently

\[
 K{\Delta_2\over D_{\max}}=m^{1/2+o(1)},
 \qquad
 K^2{\Delta_2\over D_{\max}}=m^{2+o(1)}.
 \tag{4.7}
\]

No pair-codegree-only growing-rank nibble follows from (4.5).

## 5. Exact crossing squares obstruct a full-codegree black box

The complete codegree sequence contains a second, sharper warning.
For \(s\le Q\), an interior geodesic grid has the Boolean square

\[
 \mathcal R_s(t)
 =\{G_{t+p,t+q}:0\le p,q\le s\},
 \tag{5.1}
\]

of size

\[
 j_s=(s+1)^2.
 \tag{5.2}
\]

The number of oriented ambient \(s\)-squares is exactly

\[
 \boxed{
 \mathscr R_s=W(m)_s^2.}
 \tag{5.3}
\]

For the priority template, put \(d_s=M-c_s\).  The calibrated priority
count satisfies

\[
 d_s=O(s^2+s+1)
 \tag{5.4}
\]

for \(s=o(m^{2/3})\).  The \(d_s\) unclaimed phases cut the physical cycle
into at most \(d_s+1\) claimed runs.  Hence one run has length at least

\[
 {M-d_s\over d_s+1}.
 \tag{5.5}
\]

For

\[
 s=\lceil\log m\rceil,
 \tag{5.6}
\]

the right side of (5.5) is much larger than \(s+1\).  Therefore the fixed
template edge \(e_0\) contains at least one complete claimed
\(\mathcal R_s(t)\).

Let \(J\) be the resulting \(j_s\)-target set.  By (3.12) and (5.3),

\[
 d(J)\ge {|\mathcal O|\over W(m)_s^2}.
 \tag{5.7}
\]

The maximum augmented vertex degree is

\[
 D_{\max}=d_{\rm tag}
 ={ |\mathcal O|\over T}
 =(1+o(1)){|\mathcal O|M\over W},
 \tag{5.8}
\]

because \(W/T=(1+o(1))M\) and (3.3) bounds every target degree by the tag
degree.  Consequently

\[
 \boxed{
 {\Delta_{j_s}\over D_{\max}}
 \ge {1-o(1)\over M(m)_s^2}.}
 \tag{5.9}
\]

For the usual full-codegree root parameter this implies

\[
 \boxed{
 \left({D_{\max}\over\Delta_{j_s}}
 \right)^{1/(j_s-1)}
 \le
 \bigl((1+o(1))M(m)_s^2\bigr)^{1/(s^2+2s)}
 =e^{2+o(1)}.}
 \tag{5.10}
\]

Thus even the exact full-codegree roots do not tend to infinity.  The
crossing squares are genuine members of the protected augmented edge, not
middle-only artifacts.  A generic growing full-codegree nibble cannot be
invoked.

## 6. The unweighted packing attack and its present limit

The orbit has an exact fractional matching of total mass \(T\): give every
edge weight \(1/d_{\rm tag}\).  Therefore

\[
 \nu^*(\mathcal O)=T.
 \tag{6.1}
\]

The rank bound alone gives only the standard greedy/integrality estimate

\[
 \nu(\mathcal O)\ge {T\over K+1},
 \tag{6.2}
\]

which is useless for \((OP_Q)\).  Equations (4.3)--(4.5) improve the local
pair geometry but, by Section 5, not in a form covered by a verified
growing-uniformity theorem.

One may run a random greedy matching in the full orbit.  Its law remains
coordinate-invariant, so expected degrees are constant inside every rank.
That observation does not make a conditioned residual instance
edge-transitive.  After exposing a partial matching, individual target
links are tilted by the used physical labels.  The exact variance term is
the survival-conditioned common-link/four-walk kernel, not the raw
codegree (3.10).  Presently proved pair-square estimates control time zero
and one unconditioned bite; they do not give the hereditary recurrence
through residual tag density \(o(1/Q)\).

The square calculation has a second interpretation here.  Large
high-codegree patterns are highly structured within one grid and need not
prevent an orbit packing, but they invalidate the only available generic
route from exact codegrees to a near-perfect matching.  Exploiting them
positively would require an orbit-specific switch/absorber which preserves
the whole protected square profile.

The middle-only projection deletes precisely the target constraints which
cause (4.2)--(5.10).  Its exact wreath packing therefore supplies no bound
on \(\nu(\mathcal O)\) and is intentionally absent from the argument.

## 7. Exact remaining theorem

For one fixed schedule/priority template, the coefficient-one problem has
now been reduced without loss to:

> **Augmented geodesic orbit packing theorem.**  The full coordinate orbit
> \(\mathcal O\), whose edges contain one carrier tag and every protected
> lower, middle, and upper target, has
> \[
>   \nu(\mathcal O)=T-o(T/Q).
> \]

If this theorem holds, Theorem 2.1 automatically proves every residual
weighted matching cut at the \(1+o(1/Q)\) scale.  The scalar calibration
then turns the matching into a cyclic-interval near-design with \(o(W)\)
holes.

The exact degrees (3.1)--(3.12), factorial pair-square profile
(4.2)--(4.4), and crossing-square codegrees (5.7)--(5.10) are the complete
currently audited orbit inputs.  They neither reveal a capacity
obstruction nor prove the packing.  The remaining work is an
orbit-specific unweighted matching/absorption theorem which survives the
crossing-square clusters and the survival-conditioned physical-label
kernel.
