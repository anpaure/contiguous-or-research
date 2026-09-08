# PBBS saturation versus clustered seams: a non-equivariant no-escape theorem

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B=\operatorname {Cat}_m,\qquad W=NB,
 \qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed.  Work on the long-cycle Dyck quotient of the
normalized step-two PBBS permutation.  The exact reciprocal-height defect
identity is

\[
 b_h-(h+2)|\mathcal P_h|
 =U_h+\sum_{I\in\mathcal P_h}\bigl(k(I)-h-2\bigr),
\tag{0.2}
\]

where \(b_h\) is the number of retained height-\(h\) quotient edges,
\(U_h\) is the number of such edges uncovered by the packing, and
\(k(I)\) is the number of quotient edges in the residence trace.

This note gives the exact conclusion available from (0.2).

1. A genuinely trace-near-saturating packing is an approximate edge
   tiling by relatively minimum-gap returns:

   \[
    \sum_hU_h=o_A(B),\qquad
    \sum_I(k(I)-h(I)-2)=o_A(B).
   \tag{0.3}
   \]

   Apart from \(o_A(B/H)\) members, its additive height-gap excess is
   \(o_A(H)\).  Exact equality gives a literal cycle-by-cycle tiling by
   the leader--predecessor closure towers.  Asymptotic equality does
   **not** force a positive fraction of literal equality towers: excess
   one on every one of \(\Theta(B/H)\) traces costs only \(O(B/H)=o(B)\)
   in (0.3).

2. A merely positive critical packing need not be close to full
   reciprocal-height equality.  It does, however, contain a positive
   critical subpacking at Gaussian height and at positive exact-stratum
   utilization.  Its traces cover \(\Omega_A(B)\) quotient edges.  After
   the audited factor-two minimal-return reduction and chronology
   quarantine, the remaining possible counterfamily is precisely the
   positive-utilization, simple fixed-core, densely reframing class.

3. Cluster-span sharing cannot compile either kind of critical family at
   sublinear cost.  The following lower bound holds for an arbitrary
   physical cut system; no deck invariance is assumed.  If
   \(\mathcal P^{\ge a}\) is a quotient-edge-disjoint packing with
   \(h(I)\ge a\sqrt m\), and \(\mathfrak S_H^{\rm phys}\) is the cost of
   any established clustered chart hitting all physical residences, then

   \[
    \boxed{
    \mathfrak S_H^{\rm phys}
    \ge {3a\over2A}\,HN|\mathcal P^{\ge a}|.}
   \tag{0.4}
   \]

   Consequently, if

   \[
    |\mathcal P|\ge\varepsilon B/\sqrt m,
   \tag{0.5}
   \]

   then, after choosing \(a=a(A,\varepsilon)>0\),

   \[
    \boxed{\mathfrak S_H^{\rm phys}\ge c_{A,\varepsilon}W.}
   \tag{0.6}
   \]

Thus the present clustered-seam construction is not an alternative to
\((ST_A)\): a failure of \((ST_A)\) forces a linear physical seam bill.
Cluster sharing can improve the constant, but not the order.  The only
two surviving coefficient-one possibilities are:

* prove the strict little-oh packing theorem \((ST_A)\); or
* replace the additive \(7H+3S-3\) chart by a genuinely in-place
  compiler whose marginal cost is not bounded below by a positive
  combination of collar height and active span.

No such in-place replacement is constructed here.  The result is a
sharp obstruction to the proposed clustered-seam escape, not a proof of
\((ST_A)\).

## 1. Exact weighted saturation identity

Let \(V_H\) be the retained long-cycle quotient edge set and let

\[
 b_h=|\{D\in V_H:\operatorname {ht}(D)=h\}|.
\tag{1.1}
\]

Every eligible residence interval has invariant height \(h(I)\le H-1\)
and

\[
 k(I)\ge h(I)+2.
\tag{1.2}
\]

For a quotient-edge-disjoint family \(\mathcal P\), define

\[
 U_h=b_h-\sum_{I\in\mathcal P_h}k(I)\ge0.
\tag{1.3}
\]

Then finite double counting gives (0.2).  Equivalently, with

\[
 \mathcal T_{m,H}=\sum_{h\le H-1}{b_h\over h+2},
 \qquad
 \Delta(\mathcal P)=\mathcal T_{m,H}-|\mathcal P|,
\tag{1.4}
\]

one has the exact complementary-slackness formula

\[
 \boxed{
 \Delta(\mathcal P)
 =\sum_{h\le H-1}{U_h\over h+2}
  +\sum_{I\in\mathcal P}
       {k(I)-h(I)-2\over h(I)+2}.}
\tag{1.5}
\]

Every term is nonnegative.  In particular,

\[
 |\mathcal P|=\mathcal T_{m,H}
\tag{1.6}
\]

if and only if every retained eligible quotient edge is covered exactly
once and every selected trace has length \(h+2\).  On each quotient
cycle, the trace starts then form one residue class modulo \(h+2\), so
the cycle length is divisible by \(h+2\).  The exact PBBS equality
classification identifies each such trace with a complete recursive
leader--predecessor closure tower.

## 2. What asymptotic saturation does and does not force

### Proposition 2.1 (aggregate near-tiling)

If

\[
 \Delta(\mathcal P)=o_A(B/\sqrt m)=o_A(B/H),
\tag{2.1}
\]

then

\[
 \sum_hU_h=o_A(B),
 \qquad
 \sum_{I\in\mathcal P}\bigl(k(I)-h(I)-2\bigr)=o_A(B).
\tag{2.2}
\]

Moreover, for every packing sequence satisfying (2.1), there is a
sequence \(\rho_m\downarrow0\) such that

\[
 \#\{I\in\mathcal P:
       k(I)-h(I)-2\ge\rho_mH\}
 =o_A(B/H).
\tag{2.3}
\]

#### Proof

Every positive denominator in (1.5) is at most \(H+1\).  Hence

\[
 \sum_hU_h+
 \sum_I(k(I)-h(I)-2)
 \le(H+1)\Delta(\mathcal P)=o_A(B),
\tag{2.4}
\]

which proves (2.2).  Write the left side's second summand as
\(d_mB\), where \(d_m\to0\), and take

\[
 \rho_m=\sup_{n\ge m}\sqrt {d_n}+{1\over m}.
\]

Then \(\rho_m\downarrow0\) and \(\rho_m\ge\sqrt {d_m}\).  Markov's
inequality gives

\[
 \#\{I:k(I)-h(I)-2\ge\rho_mH\}
 \le {d_mB\over\rho_mH}
 \le{\sqrt {d_m}B\over H}=o_A(B/H).
\]

\(\square\)

The conclusion is deliberately relative.  If every selected Gaussian
trace has excess exactly one, then the total excess is
\(\Theta(B/H)=o(B)\).  Such a family is compatible with (2.1).  Thus
the saturation identity cannot by itself replace relative
\(o(H)\)-minimality by literal equality, nor can it prove \((ST_A)\).

### Proposition 2.2 (positive critical utilization)

Suppose

\[
 |\mathcal P|\ge\varepsilon {B\over\sqrt m}
\tag{2.5}
\]

along a subsequence.  Then there are constants
\(a=a(A,\varepsilon)>0\), \(\delta=\delta(A,\varepsilon)>0\), and a
subfamily \(\mathcal P^\star\subseteq\mathcal P\) such that

\[
 |\mathcal P^\star|\ge {\varepsilon\over2}{B\over\sqrt m},
\tag{2.6}
\]

after a harmless adjustment of \(\varepsilon/2\), and every height
stratum used by \(\mathcal P^\star\) satisfies

\[
 a\sqrt m\le h\le H-1,
 \qquad
 \theta_h:={(h+2)|\mathcal P_h|\over b_h}\ge\delta,
\tag{2.7}
\]

where \(\theta_h=0\) when \(b_h=0\).

In particular the union of the traces in \(\mathcal P^\star\) has size

\[
 \left|\bigcup_{I\in\mathcal P^\star}I\right|
 \ge a\sqrt m\,|\mathcal P^\star|
 \ge c_{A,\varepsilon}B.
\tag{2.8}
\]

#### Proof

The sub-Gaussian reciprocal-height tail supplies a function
\(\eta_A(a)\downarrow0\) such that

\[
 \sum_{h<a\sqrt m}{b_h\over h+2}
 \le\eta_A(a){B\over\sqrt m}+o_A(B/\sqrt m).
\tag{2.9}
\]

Choose \(a\) so that this is at most
\(\varepsilon B/(4\sqrt m)\).  Also

\[
 \mathcal T_{m,H}\le C_A{B\over\sqrt m}.
\tag{2.10}
\]

Choose \(\delta=\varepsilon/(4C_A)\).  The contribution of strata with
\(\theta_h<\delta\) is at most

\[
 \delta\mathcal T_{m,H}
 \le{\varepsilon\over4}{B\over\sqrt m}.
\tag{2.11}
\]

Deleting the two classes in (2.9) and (2.11) leaves at least
\(\varepsilon B/(2\sqrt m)\), proving (2.6)--(2.7).  Since the traces
are edge-disjoint and each has at least \(h+2\ge a\sqrt m\) edges,
(2.8) follows. \(\square\)

This is the exact distinction between two uses of the word
"near-saturator."  A family of order \(B/H\) is only a positive weighted
utilizer of reciprocal capacity.  Only a family within \(o(B/H)\) of
\(\mathcal T_{m,H}\) satisfies Proposition 2.1.

The factor-two minimal-return theorem may now be applied to
\(\mathcal P^\star\).  Repeating the elementary utilization truncation
after that reduction gives a positive critical family of simple
fixed-core sectors.  The established stable-window contraction then
removes, at arbitrarily small fixed loss, sectors with sublinear
reframing; the one-witness theorem removes the family containing a
canonical stable block longer than
\((1/2+\epsilon)\log_2m\).  Hence the still-unexcluded positive critical
class has simultaneously:

\[
 \begin{gathered}
 h=\Theta_A(\sqrt m),\qquad
 \theta_h\ge\delta,\qquad
 R(I)\ge\epsilon_0s(I),\\
 G(I)<(1/2+\epsilon)\log_2m+1,
 \end{gathered}
\tag{2.12}
\]

and its simple traces and their one-edge translates are each pairwise
edge-disjoint.  Statement (2.12) is a classification of the surviving
class, not a construction of it.

## 3. The exact collar-versus-span alternative

The established chart charges a cluster of physical cuts of active span
\(S\) by

\[
 c_H(S)=7H+3S-3.
\tag{3.1}
\]

The following lemma makes cluster sharing quantitative.

### Lemma 3.1 (many collars or linear span)

Let \(I_1,\ldots,I_M\) be pairwise edge-disjoint nonwrapping intervals
on a disjoint union of cycles, each of length at least \(L\).  Let a cut
transversal be partitioned, cycle by cycle, into \(K\) nonempty clusters.
Assign to each interval one transversal cut which it contains, and let
\(t_J\) be the number assigned to cluster \(J\).  Then

\[
 \sum_JS_J\ge L(M-2K)_+,
\tag{3.2}
\]

and therefore

\[
 \boxed{
 \sum_J(7H+3S_J-3)
 \ge (7H-3)K+3L(M-2K)_+.}
\tag{3.3}
\]

#### Proof

Lift one cycle just before the first cut of a cluster.  Apart from the
first and last assigned intervals, every assigned interval lies wholly
between the extreme cluster cuts.  Edge-disjointness gives

\[
 S_J\ge L(t_J-2)_+.
\tag{3.4}
\]

Summing and using

\[
 \sum_J(t_J-2)_+
 \ge\left(\sum_Jt_J-2K\right)_+=(M-2K)_+
\tag{3.5}
\]

proves (3.2), and (3.3) follows from the definition of the chart cost.
\(\square\)

Formula (3.3) is the exact clustering dichotomy.  If \(K\ge M/2\), the
base collars alone cost \(\Omega(HM)\).  If \(K<M/2\), reducing the
number of collars forces the extreme-cut spans to cross essentially all
of the middle intervals.

### Corollary 3.2 (uniform per-interval cost)

If \(L=\gamma H\) with \(0<\gamma\le1/2\), then, for \(H\ge1\),

\[
 \boxed{
 \sum_J(7H+3S_J-3)\ge3\gamma HM.}
\tag{3.6}
\]

#### Proof

If \(K\le M/2\), the right side of (3.3) is

\[
 3\gamma HM+K\bigl(7H-3-6\gamma H\bigr)
 \ge3\gamma HM,
\]

because \(\gamma\le1/2\).  If \(K>M/2\), then

\[
 (7H-3)K>{7H-3\over2}M\ge3\gamma HM.
\]

\(\square\)

Thus close packing is not a saving mechanism.  One huge cluster changes
the leading constant from the singleton-collar value toward the span
coefficient, but its span is the length of the tiled region.

## 4. Lifting the lower bound through all phases

Let \(\mathcal P^{\ge a}\) be a quotient-edge-disjoint packing with
\(h(I)\ge a\sqrt m\).  Lift every quotient interval through all \(N\)
cyclic label phases.  The lifted family has exactly

\[
 M=N|\mathcal P^{\ge a}|
\tag{4.1}
\]

members and is physical-edge-disjoint.  The cyclic translation action is
free on middle owners: if a nontrivial translation orbit had size
\(d>1\), then \(d\mid N\) and invariance would force \(d\mid m\),
contrary to \(\gcd(m,2m+1)=1\).  Hence every quotient edge has exactly
\(N\) physical preimages.  Equivariance and bijectivity of the PBBS map
make the \(N\) path lifts disjoint, while distinct quotient edges have
disjoint inverse images.

For all sufficiently large \(m\),

\[
 H\le2A\sqrt m,
\tag{4.2}
\]

so every lifted trace has length at least

\[
 h(I)+2\ge a\sqrt m\ge {a\over2A}H.
\tag{4.3}
\]

Take

\[
 \gamma={a\over2A}<\frac12.
\tag{4.4}
\]

Any physical cut system valid for all eligible residences hits, in
particular, every member of this lifted packing.  Corollary 3.2 and (4.1)
give

\[
 \mathfrak S_H^{\rm phys}
 \ge3\gamma HN|\mathcal P^{\ge a}|
 ={3a\over2A}HN|\mathcal P^{\ge a}|,
\tag{4.5}
\]

which is (0.4).  Notice that the physical cuts and their clusters were
never assumed to be rotation invariant.  The quotient is used only to
produce the edge-disjoint phase-lifted test family.

### Theorem 4.1 (critical clustered-seam no-escape)

If (0.5) holds, then every established clustered cut compiler for the
same residence family satisfies (0.6).

#### Proof

By Proposition 2.2, after choosing \(a>0\),

\[
 |\mathcal P^{\ge a}|
 \ge{\varepsilon\over2}{B\over\sqrt m}.
\tag{4.6}
\]

Substitution in (4.5), followed by \(H\ge A\sqrt m\), gives

\[
 \mathfrak S_H^{\rm phys}
 \ge {3a\over2A}HN\,{\varepsilon B\over2\sqrt m}
 \ge {3a\varepsilon\over4}NB
 ={3a\varepsilon\over4}W.
\tag{4.7}
\]

This proves (0.6) with \(c_{A,\varepsilon}=3a\varepsilon/4>0\).
\(\square\)

The same argument applies a fortiori to a trace-near-saturator, since
\(\mathcal T_{m,H}=\Theta_A(B/\sqrt m)\).  In fact the closer the traces
come to an edge tiling, the more literal the obstruction becomes: the
cut clusters must span a positive fraction of a physical deck unless
there are \(\Theta(W/H)\) separate collar payments.

## 5. Exact implication boundary

The theorem gives the following exhaustive alternative for the current
PBBS literal compiler, after the proved short-cycle and sub-Gaussian
tails.

### Alternative I: strict chronology

If

\[
 \overline\nu_H=o_A(B/\sqrt m)=o_A(B/H),
\tag{5.1}
\]

then a circular-interval transversal of size at most twice the packing
number, used as singleton clusters, has quotient cost \(o_A(B)\), hence
physical cost \(o_A(W)\).  This is \((ST_A)\), and the established PBBS
ledger gives coefficient one.

### Alternative II: critical saturation

If (5.1) fails, then along a subsequence there is an
\(\varepsilon>0\) and a packing satisfying (0.5).  Propositions 2.1--2.2
and the previous chronology reductions classify its two possible
strengths:

* at positive critical scale it is a positive-utilization Gaussian
  partial tiling, with a simple fixed-core, densely reframing,
  double-deck subfamily covering \(\Omega_A(B)\) quotient edges;
* if it approaches the full reciprocal trace, its uncovered edge mass
  and total relative height-gap slack are \(o_A(B)\), so it is an
  approximate minimum-gap tiling.

In both cases Theorem 4.1 gives

\[
 \mathfrak S_H^{\rm phys}=\Omega_{A,\varepsilon}(W).
\tag{5.2}
\]

Therefore cluster-span sharing of the established form cannot be the
replacement promised in Alternative II.  This remains true for
non-equivariant cut choices, arbitrary assignments of cuts to clusters,
and clusters containing an unbounded number of nearby returns.

The lower bound only uses that the marginal chart cost has a positive
collar term and a positive active-span term.  More generally, the proof
works for every cost

\[
 \alpha H+\beta S-O(1),\qquad \alpha,\beta>0,
\tag{5.3}
\]

with a changed positive constant.  Hence a genuine replacement must fall
outside the additive collar-plus-span model: for example, it would have
to overwrite or reuse already-counted baseline letters in place, rather
than append a chart whose length grows with either the number of clusters
or their total active span.

## 6. Status

Proved here:

1. the exact distinction between positive critical utilization and
   asymptotic reciprocal-height equality;
2. the quantitative collar-versus-span inequality (3.3);
3. the non-equivariant physical lower bound (0.4);
4. the linear-cost obstruction (0.6) for every failure of \((ST_A)\).

Not proved here:

1. \((ST_A)\);
2. existence of a genuine canonical PBBS critical saturator;
3. an in-place seam compiler outside the additive chart model.

Accordingly, the exact saturation identity does classify the only
surviving counterfamilies, but it does not itself yield the desired
little-oh.  More importantly, those counterfamilies cannot be rescued by
cluster-span chart sharing: under the established literal compiler their
total seam cost is necessarily \(\Omega(W)\).
