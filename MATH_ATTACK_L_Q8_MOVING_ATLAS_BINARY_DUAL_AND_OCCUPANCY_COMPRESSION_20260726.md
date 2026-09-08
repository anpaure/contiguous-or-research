# Pure-shore Q8 moving frames: exact binary Hall dual, valid compression, and an occupancy obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent option sampling is used.

## 0. Verdict

Use the simultaneous-depth component dual in
`MATH_THEOREM_MOVING_ATLAS_OUTER_PACKET_HALL_DUAL_20260726.md` with the
binary coefficients displayed in its primal:

\[
 a_{r,o}=\mathbf1_{\{\text{whole option }o\text{ hits target row }r\}}.
                                                               \tag{0.1}
\]

Here a row is \(r=(q,\epsilon,T)\), with one common option used at every
depth and sign.  Under this exact uncovered-target normalization, uniform
component expansion is false for the concrete **pure-shore status-option
catalogue** defined below.  Its whole options first choose one global
perfect matching and then factor all of its status cells.  Adjacent
matchings are the two pure shores of a four-coordinate recoupling, and the
bounded common-owner \(Q_8\) associator certifies that adjacency on its
24-owner support.  The theorem does not identify this catalogue with the
larger, presently uncompiled class of phase-changing or mosaic \(Q_8\)
columns.

Take all perfect matchings obtainable from a reference matching by local
four-coordinate recouplings

\[
 ab\mid cd\longleftrightarrow ac\mid bd
 \quad\text{or}\quad ad\mid bc,                    \tag{0.2}
\]

The recoupling graph generates all perfect matchings of \([2m]\).  Their
coordinate union graph is \(K_{2m}\), so the exact exclusion-process
quotient has one owner component, the whole middle layer.  In the
pure-shore catalogue, a legal column is **defined** to choose one whole
global matching-status option; it does not choose shores or status cells
independently.  Connected overlap alone would not justify that definition
for a larger hybrid catalogue.

Let \(\mathcal Q\) be any protected depth set and let \(\mathcal R_{\mathcal
Q}\) contain both signs at those depths.  If \(I_o\subseteq\mathcal
R_{\mathcal Q}\) is the distinct literal target support of option \(o\),
then the exact simultaneous binary LP value for this one-simplex catalogue
is

\[
 \boxed{
 \eta_{\mathcal Q}^{\mathrm{bin}}
 =|\mathcal R_{\mathcal Q}|-
   \max_o|I_o|.}                                   \tag{0.3}
\]

Equivalently, an optimal dual weight is

\[
 \boxed{y_r\equiv1.}                               \tag{0.4}
\]

Thus arbitrary weights need no speculative shifting: in the connected
one-component quotient they compress rigorously to the all-ones weight,
simultaneously across depths and signs.

Every option subordinate to one physical perfect matching obeys an exact
full/empty-pair occupancy support cap.  Put \(W=\binom{2m}{m}\),
\(N_q=\binom{2m}{m-q}\), and

\[
\begin{aligned}
 V_f&=\frac{m!\,2^{m-2f}}{f!^2(m-2f)!},\\
 T_{f,q}&=\frac{m!\,2^{m-2f-q}}
               {f!(f+q)!(m-2f-q)!},\\
 D_{m,q}&=\sum_f(T_{f,q}-V_f)_+ .                  \tag{0.5}
\end{aligned}
\]

Here \(V_f=0\) outside \(0\le f\le\lfloor m/2\rfloor\), and
\(T_{f,q}=0\) outside
\(0\le f\le\lfloor(m-q)/2\rfloor\); equivalently, every factorial with a
negative argument makes that term zero.

Then

\[
 \boxed{
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge2\sum_{q\in\mathcal Q}D_{m,q}.}               \tag{0.6}
\]

This is the no-exception lower bound.  If at depth \(q\) at most \(L_q^-\) lower
and \(L_q^+\) upper distinct hits per option come from phases not certified
to use \(q\) distinct directions of one fixed matching, the exact robust
form is (5.4) below.

For a sequence of protected sets \(\mathcal Q=\mathcal Q_m\), suppose
\(q_m=\lfloor A\sqrt m\rfloor\in\mathcal Q_m\), where \(A>0\) is fixed.
Assume every nonexceptional certified \(q_m\)-window uses \(q_m\) distinct
directions inside its chosen fixed-\(M\) status cell and
\(L_{q_m}^-+L_{q_m}^+=o(W)\).  Then

\[
 \boxed{
 \frac{D_{m,q_m}}W\longrightarrow
 \delta_A^{\mathrm{pair}}
 :=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}              \tag{0.7}
\]

Hence one Gaussian depth already gives

\[
 \boxed{
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge(2\delta_A^{\mathrm{pair}}-o(1))W,}           \tag{0.8}
\]

refuting \(o(W)\) two-sign component expansion.

There are two necessary qualifications.

1. Averaging coordinate conjugates does close the **occurrence-multiplicity**
   relaxation, because its mean load is \(W/N_q\).  It does not close the
   binary-support LP (0.1).  These are different fractional programmes.
2. The theorem treats the explicitly restricted pure-shore
   moving-perfect-matching/status-cell column model: a whole option has one
   underlying matching.  A cycle whose protected window changes its
   physical matching by phase, or a hybrid exact tiling assembled from
   several shores, is a larger column model and is not refuted here.

## 1. Exact binary versus multiplicity normalization

For a whole option \(o\), let

\[
 m_{r,o}=\#\{\text{literal phase occurrences of target row }r\}.            \tag{1.1}
\]

The target is hit integrally if and only if \(m_{r,o}>0\).  Therefore the
multiple-choice set-cover coefficient is the binary support

\[
 a_{r,o}=\mathbf1_{\{m_{r,o}>0\}},                 \tag{1.2}
\]

not \(m_{r,o}\).  For an integral choice the two coefficients give the same
zero/nonzero decision, but their fractional relaxations differ: if one
option hits a target ten times and has fractional weight \(1/2\), its binary
cover load is \(1/2\), not five.

The displayed primal in the cited report uses (1.2).  Its exact joint dual
is

\[
 \boxed{
 \mathfrak D_{\mathcal Q}(y)
 =\sum_{r\in\mathcal R_{\mathcal Q}}y_r
  -\sum_\kappa\max_{o\in\Theta_\kappa}
    \sum_{r\in\mathcal R_{\mathcal Q}}a_{\kappa,o}(r)y_r,
 \qquad0\le y_r\le1.}                             \tag{1.3}
\]

Writing an image as a multiset and summing \(y_r\) with multiplicity instead
replaces \(a\) by \(m\) and defines a weaker occurrence-flow relaxation.  It
must not be called the exact binary uncovered-target LP.

This distinction is unavoidable in a connected atlas.  Every whole factor
has \(W\) phase occurrences at depth \(q>0\), while the target layer has

\[
 N_q=\binom{2m}{m-q}<W                              \tag{1.4}
\]

members.  Global trace injection is impossible, so repeated occurrences
must exist even if every local packet map is injective.

There is a second LP which must not be conflated with (1.3).  Suppose
overlapping packet columns \(a\) have owner sets \(P(a)\) and binary target
supports \(S(a)\).  Its primal is

\[
\begin{aligned}
 \min\quad&\sum_tz_t,\\
 z_t+\sum_{a:t\in S(a)}x_a&\ge1 &&(t),\\
 \sum_{a:X\in P(a)}x_a&=1 &&(X),\\
 x_a,z_t&\ge0.                                      \tag{1.5}
\end{aligned}
\]

The exact uncovered-target dual of that packet-master LP is

\[
 \boxed{
 \max_{\substack{0\le y_t\le1\\ \pi_X\in\mathbb R}}
 \left(\sum_ty_t-\sum_X\pi_X\right)}              \tag{1.6}
\]

subject to

\[
 \boxed{
 \sum_{t\in S(a)}y_t
 \le\sum_{X\in P(a)}\pi_X\qquad(a).}              \tag{1.7}
\]

Indeed, dualize the target inequalities with \(y_t\ge0\), the unit repair
columns impose \(y_t\le1\), and dualize the owner equalities with free
variables \(-\pi_X\).  The zero cost of \(x_a\) gives exactly (1.7).

The free owner prices \(\pi_X\) are absent from the disjoint-component
simplex dual (1.3).  A symmetric fractional cover by overlapping conjugate
packets may therefore be valid for (1.5)--(1.7) without proving the
one-component inequality studied here.

## 2. The pure-shore recoupling catalogue has one selector component

Assume \(m\ge4\).  Let \(M_0\) be a reference perfect matching on
\([2m]\), and let the atlas
contain all matchings reached by recouplings (0.2).  For each matching, the
legal pure-shore options are exact factors assembled wholly from that
matching's status cells.  The certified bounded \(Q_8\) associator realizes
an adjacent two-shore trade on its 24-owner occupancy support.  We do not
assume that arbitrary sequences of those bounded trades already compile a
new hybrid whole-column factor.

As in the cited outer-dual reduction, existence of the declared protected-
depth status-cell compilers is a hypothesis.  The support inequalities below
hold for every such compiler; where a cell is not certified through depth
\(q\), its phases are entered explicitly in the exceptional ledger
\(L_q^\pm\).

### Lemma 2.1 (four-switch generation)

The graph of perfect matchings, joined when two matchings differ by one
switch (0.2), is connected.

#### Proof

Fix a target matching \(M_*\).  Suppose \(ab\in M_*\) but the current
matching contains \(ac\) and \(bd\).  Switching on \(\{a,b,c,d\}\) creates
\(ab\) and \(cd\).  If all already corrected edges are removed before this
step, the switch changes none of them.  Induction fixes every edge of
\(M_*\). \(\square\)

Therefore the atlas contains every perfect matching.  The union of their
coordinate edges is \(K_{2m}\), which is connected.  By the exact
exclusion-component theorem, the common owner quotient consists of the
single set

\[
 \mathcal U=\binom{[2m]}m.                         \tag{2.1}
\]

Connected overlap is restrictive for the status-selector architecture: it
provides one independent component variable on \(\mathcal U\).  In the
declared pure-shore menu, that variable chooses one whole global matching
resolution.  The six cycles of one local 24-owner associator shore are not
independent owner supplies.  This statement does not classify every
conceivable exact hybrid tiling of \(\mathcal U\).

The option catalogue is closed under \(S_{2m}\), but this symmetry will not
be needed for the exact dual compression below.

## 3. Exact simultaneous-depth compression of all target weights

In the one-component quotient, write simply \(I_o\subseteq\mathcal
R_{\mathcal Q}\) for the binary support of option \(o\).  The joint primal is

\[
\begin{aligned}
 \min\quad&\sum_{r\in\mathcal R_{\mathcal Q}}z_r,\\
 z_r+\sum_o a_{r,o}x_o&\ge1 &&(r),\\
 \sum_ox_o&=1,\\
 x_o,z_r&\ge0.
\end{aligned}                                      \tag{3.1}
\]

### Theorem 3.1 (one-component binary collapse)

The value of (3.1) is (0.3), and the all-ones dual (0.4) is optimal.

#### Primal proof

For every row,

\[
 c_r:=\sum_oa_{r,o}x_o\le\sum_ox_o=1.              \tag{3.2}
\]

Thus the optimal repair variable is \(z_r=1-c_r\), and

\[
 \sum_rz_r
 =|\mathcal R_{\mathcal Q}|-
   \sum_ox_o|I_o|.                                 \tag{3.3}
\]

Minimizing a linear average over the simplex chooses an option of maximum
support, proving (0.3).

#### Dual proof and compression

Choose \(o_*\) with maximum \(|I_o|\).  For every \(0\le y\le1\),

\[
\begin{aligned}
 \mathfrak D_{\mathcal Q}(y)
 &\le\sum_ry_r-\sum_{r\in I_{o_*}}y_r\\
 &=\sum_{r\notin I_{o_*}}y_r\\
 &\le|\mathcal R_{\mathcal Q}|-|I_{o_*}|\\
 &=\mathfrak D_{\mathcal Q}(\mathbf1).
                                                               \tag{3.4}
\end{aligned}
\]

This proves the exact compression of *all* simultaneous-depth weights to
\(y\equiv1\).  It is stronger than a conjectural reduction to occupancy
thresholds, and it does not use independent choices, asymptotic symmetry, or
depthwise optimization.

For comparison, Reynolds averaging over a genuine option-system symmetry is
also valid.  The functional in (1.3) is concave and invariant, so group
averaging cannot lower it.  In a transitive target layer this again makes
\(y\) constant.  The direct proof (3.4) shows that connected-component
simplex normalization, not symmetry, is the decisive fact.

## 4. Why arbitrary occupancy averaging is not a valid shifting theorem

Outside the one-component collapse, a proposed linear compression \(P\) must
respect the component option polytope.  At one sign/depth put

\[
 K_\kappa=\operatorname{conv}\{a_{\kappa,o}:o\in\Theta_\kappa\},
 \qquad K=\sum_\kappa K_\kappa.                    \tag{4.1}
\]

Then the option term in the dual is the support function \(h_K(y)\), and

\[
 \mathfrak D(y)=\mathbf1^Ty-h_K(y).                \tag{4.2}
\]

If \(P\) preserves total weight, then the full-space criterion is

\[
 \mathfrak D(Py)\ge\mathfrak D(y)\quad\text{for every real }y
 \quad\Longleftrightarrow\quad
 P^TK\subseteq K.                                  \tag{4.3}
\]

Indeed, \(h_K(Py)=h_{P^TK}(y)\), and support-function domination on all real
directions is equivalent to convex-set inclusion.  For the actual dual
domain \(0\le y\le1\), assume also that \(P\) maps the unit cube into
itself.  Positive homogeneity reduces the test to all \(y\ge0\), and the
exact weaker criterion is

\[
 P^TK\subseteq K-\mathbb R_+^{\mathcal R}.         \tag{4.3a}
\]

This follows because the lower closure \(K-\mathbb R_+^{\mathcal R}\) has
support function \(h_K\) on nonnegative directions, and a point outside
that closed convex lower set is separated from it by a nonnegative normal.

Thus (4.3) is sufficient but need not be necessary on the positive cube.
Averaging over a group which genuinely permutes all component options
satisfies the stronger inclusion.  A coarse occupancy conditional
expectation need not even satisfy (4.3a), as the positive-weight example
below shows.

### Certified 24-owner Q8 failure of rank-only compression

Let \(A=\{a,b,c,d\}\), \(R=\{u,v,w,x\}\), and

\[
 \mathcal Y=\{uw,ux,vw,vx\},\qquad
 \mathcal V=\binom A2\times\mathcal Y.             \tag{4.4}
\]

The three shores use the three perfect matchings

\[
 M_0=\{ab,cd\},\quad M_1=\{ac,bd\},\quad
 M_2=\{ad,bc\}                                    \tag{4.5}
\]

on \(A\), together with the common reservoir matching
\(\{uv,wx\}\).  Each shore is the certified exact six-square factor on the
same 24 middle owners \(\mathcal V\).

At lower depth one, the distinct targets of shore \(j\) are

\[
 C^-\ \dot\cup\ R_j^-,                             \tag{4.6}
\]

where

\[
\begin{aligned}
 C^-&=\{\{a_0\}\cup Y:a_0\in A,\ Y\in\mathcal Y\},
      &|C^-|&=16,\\
 R_j^-&=\{Z\cup\{r_0\}:Z\in M_j,\ r_0\in R\},
      &|R_j^-|&=8.
\end{aligned}                                      \tag{4.7}
\]

The three \(R_j^-\) are disjoint and partition the 24 two-from-\(A\),
one-from-\(R\) targets.  At upper depth one the corresponding decomposition
is

\[
\begin{aligned}
 C^+&=\{(A\setminus\{a_0\})\cup Y:
          a_0\in A,\ Y\in\mathcal Y\},
      &|C^+|&=16,\\
 R_j^+&=\{Z\cup(R\setminus\{r_0\}):
          Z\in M_j,\ r_0\in R\},
      &|R_j^+|&=8.                                 \tag{4.8}
\end{aligned}
\]

These formulae are literal set formulae, so no occurrence-to-support
inference is being made.  On the 40-target candidate union
\(C^-\dot\cup R_0^-\dot\cup R_1^-\dot\cup R_2^-\), the all-ones dual has
value

\[
 40-\max_j(16+8)=16.                               \tag{4.9}
\]

The upper sign gives the same value, and the jointly tagged candidate
universe gives \(32\).  On the full local rank-three target layer there are
additional targets hit by no shore, so (4.9) is only the deliberately
restricted witness, not an undercount disguised as equality for the full
layer.

This also gives a certified failure of compression which forgets the shore
orbit data.  Give weight one to the 24 selective lower targets and zero to
all other \(\binom83-24=32\) rank-three targets.  Its dual value is
\(24-8=16\).  Genuine rank-only averaging makes the weight constant
\(24/56=3/7\) on the full rank-three layer.  It preserves total weight but
changes the option score from \(8\) to \((3/7)24=72/7\), and hence lowers
the dual value to \(96/7\).  Thus this compression loses exactly \(16/7\).
At minimum, the common/selective shore orbit must be retained.  The example
warns against unsupported shifting; the asymptotic obstruction below
instead uses a genuine exact occupancy threshold.

## 5. Exact fixed-matching occupancy threshold

Fix one global perfect matching \(M\) of the \(2m\) coordinates.  A middle
owner has, relative to \(M\), some number \(f\) of full pairs, the same
number \(f\) of empty pairs, and \(m-2f\) split pairs.  Hence the source
count is \(V_f\) in (0.5).

A lower rank-\((m-q)\) target of type \(f\) has \(f\) full pairs,
\(f+q\) empty pairs, and \(m-2f-q\) split pairs.  Its count is \(T_{f,q}\)
in (0.5).

Every \(M\)-status cell varies only orientations of split \(M\)-pairs.  An
isometric \(q\)-window uses \(q\) distinct split-pair directions.  In its
lower intersection those \(q\) pairs become empty, while the full-pair count
\(f\) is unchanged.  Therefore at most \(V_f\) distinct type-\(f\) lower
targets can be hit.  Consequently every option subordinate to \(M\) obeys

\[
\begin{aligned}
 |I_{o,q}^-|
 &\le\sum_f\min(V_f,T_{f,q})\\
 &=N_q-D_{m,q}.                                    \tag{5.1}
\end{aligned}
\]

For an upper target, stratify instead by its number \(f\) of empty
\(M\)-pairs.  It then has \(f+q\) full pairs and
\(m-2f-q\) split pairs, so its target count is again \(T_{f,q}\).  The
upper union of a \(q\)-window preserves the owner's \(f\) empty pairs and
turns exactly \(q\) split pairs full.  The same source-capacity argument
therefore gives directly

\[
 |I_{o,q}^+|\le N_q-D_{m,q}.                       \tag{5.2}
\]

The bound is independent of the particular matching \(M\), cyclic order,
cell factor, or coordinate conjugate.  Hence it holds uniformly over the
whole pure-shore matching catalogue.

If a more permissive compiler quarantines exceptional occurrences, let
\(L_q^-\) and \(L_q^+\) bound, uniformly over whole options, the numbers of
distinct protected targets at depth \(q\) which need not obey the fixed-
\(M\) status rule.  Then the robust form is

\[
\begin{aligned}
 |I_{o,q}^-|&\le N_q-D_{m,q}+L_q^-,\\
 |I_{o,q}^+|&\le N_q-D_{m,q}+L_q^+.                \tag{5.3}
\end{aligned}
\]

Together with the trivial support cap \(|I_{o,q}^\pm|\le N_q\), these
inequalities say
\(|I_{o,q}^\pm|\le N_q-(D_{m,q}-L_q^\pm)_+\).  Theorem 3.1 therefore gives

\[
 \eta_{\mathcal Q}^{\mathrm{bin}}
 \ge\sum_{q\in\mathcal Q}
 \bigl[(D_{m,q}-L_q^-)_++(D_{m,q}-L_q^+)_+\bigr]. \tag{5.4}
\]

Equation (0.6) is the no-exception specialization of this lower bound; it
need not equal the actual deficit.

For the usual fixed-\(M\) status partition, the number \(s_M(X)\) of split
pairs of a uniform middle owner satisfies

\[
 \mathbb E s_M(X)=\frac{m^2}{2m-1}=\frac m2+O(1),
 \qquad \operatorname {Var}(s_M(X))=O(m).          \tag{5.4a}
\]

Thus, for fixed \(A\), only \(o(W)\) owners lie in cells with
\(s_M(X)<\lfloor A\sqrt m\rfloor\); Chebyshev already gives \(O(W/m)\).
If the granted local compiler is \(q\)-isometric on every remaining cell,
these low-dimensional cells may be put into \(L_q^\pm=o(W)\).  Hence the
robust bound (5.4), not an implicit assertion that every status cell is
large, yields the asymptotic conclusion (0.8).

The occupancy cut is an exact threshold.  Its likelihood ratio is

\[
 \boxed{
 \frac{T_{f,q}}{V_f}
 =\prod_{i=0}^{q-1}
   \frac{m-2f-i}{2(f+1+i)}.}                      \tag{5.5}
\]

Every factor in (5.5) decreases with \(f\), so the set
\(\{f:T_{f,q}>V_f\}\) is an initial interval.  Thus the positive part in
\(D_{m,q}\) is literally one occupancy-threshold family; no unproved
shifting assertion is used.

Combining (3.3), (5.1), and (5.2) at all protected depths proves (0.6),
and the exceptional version proves (5.4).

## 6. Gaussian evaluation of the occupancy threshold

Take

\[
 q=\lfloor A\sqrt m\rfloor,
 \qquad A>0\text{ fixed},                          \tag{6.1}
\]

and write

\[
 f=\frac m4+x\sqrt m.                              \tag{6.2}
\]

Uniformly for bounded \(x\), expansion of (5.5) gives

\[
 \log\frac{T_{f,q}}{V_f}
 =-8Ax-3A^2+o(1).                                  \tag{6.3}
\]

Hence, with the exact discrete convention
\(f_*(m,q)=\max\{f:T_{f,q}>V_f\}\), the occupancy crossing is

\[
 f_*(m,q)
 =\frac m4-\frac{3A}{8}\sqrt m+o(\sqrt m).        \tag{6.4}
\]

For completeness, the exact consecutive ratios are

\[
 \frac{V_{f+1}}{V_f}
 =\frac{(m-2f)(m-2f-1)}{4(f+1)^2},                \tag{6.5}
\]

and

\[
 \frac{T_{f+1,q}}{T_{f,q}}
 =\frac{(m-2f-q)(m-2f-q-1)}
        {4(f+1)(f+q+1)}.                           \tag{6.6}
\]

Writing \(\varphi\) for the standard normal density, uniform Stirling
expansion on \(|x|\le K\), for each fixed \(K\), gives

\[
 \frac{V_f}{W}
 =\frac1{\sqrt m}\,4\varphi(4x)(1+o_K(1)),        \tag{6.7}
\]

and

\[
 \frac{T_{f,q}}{N_q}
 =\frac1{\sqrt m}\,4\varphi(4x+2A)(1+o_K(1)).    \tag{6.8}
\]

These local estimates control the tails.  Under \(V_f/W\), \(f\) is the
number of full pairs in a uniform middle subset; under \(T_{f,q}/N_q\), it
is the number of full pairs in a uniform rank-\((m-q)\) subset.  One- and
two-pair hypergeometric counting gives, uniformly for \(q=O(\sqrt m)\),

\[
\begin{aligned}
 \mathbb E_Vf&=\frac m4+O(1),
 &\operatorname {Var}_V(f)&=O(m),\\
 \mathbb E_Tf&=\frac m4-\frac q2+O(1),
 &\operatorname {Var}_T(f)&=O(m).                 \tag{6.9}
\end{aligned}
\]

Chebyshev supplies tightness after scaling by \(\sqrt m\); (6.7)--(6.8)
then give

\[
 x\Longrightarrow N(0,1/16)
 \quad\text{under }V_f/W,                          \tag{6.10}
\]

and

\[
 x\Longrightarrow N(-A/2,1/16)
 \quad\text{under }T_{f,q}/N_q.                   \tag{6.11}
\]

The central-binomial ratio gives

\[
 \frac{N_q}{W}\longrightarrow e^{-A^2}.           \tag{6.12}
\]

Let \(\mathbb P_V\) and \(\mathbb P_T\) denote the two laws above.  Since
the deficient types form the exact initial interval \(f\le f_*\),

\[
 \frac{D_{m,q}}W
 =\frac{N_q}{W}\,\mathbb P_T\{f\le f_*\}
  -\mathbb P_V\{f\le f_*\}.                       \tag{6.13}
\]

Equations (6.4) and (6.10)--(6.13) yield

\[
\begin{aligned}
 \frac{D_{m,q}}W
 &\longrightarrow
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2)\\
 &=\delta_A^{\mathrm{pair}}.                       \tag{6.14}
\end{aligned}
\]

The constant is strictly positive, since

\[
 \delta_A^{\mathrm{pair}}
 =e^{-A^2}\int_{-\infty}^{A/2}
  \left(1-e^{2At-A^2}\right)\varphi(t)\,dt>0,      \tag{6.15}
\]

because \(2At-A^2<0\) on the integration range except at its endpoint.

Equations (5.1)--(6.15) prove (0.7)--(0.8).

## 7. Reconciliation with symmetric conjugacy averaging

For occurrence multiplicities, every whole exact factor has total mass \(W\)
at a signed depth.  Averaging all coordinate conjugates therefore gives
uniform multiplicity load

\[
 \frac W{N_q}\ge1                                 \tag{7.1}
\]

on each target, simultaneously at all depths.  Thus the multiplicity
relaxation has no weighted Hall cut.

For binary support, the same conjugacy average gives only

\[
 \frac{|I_{o,q}^\epsilon|}{N_q}
 \le1-\frac{D_{m,q}}{N_q}<1                       \tag{7.2}
\]

per target when averaged over an orbit of equally sized supports.  It cannot
meet unit demand under the one-component simplex normalization.  This is why
the symmetric occurrence-flow theorem and the binary component Hall no-go
are consistent.

The distinction also explains why independent packet columns can have a
useful symmetric fractional owner cover while one connected common-owner
component cannot: the former LP has many independently weighted source
columns; the latter has one simplex of mutually exclusive whole options.

## 8. Exact boundary

The following are proved for the declared pure-shore
moving-perfect-matching/status-cell catalogue.

1. Its status-selector owner quotient is connected, so its one component
   simplex selects one whole option globally.
2. In that binary simultaneous-depth simplex dual, \(y\equiv1\) is optimal;
   arbitrary labelled weights compress to it without loss.
3. The certified 24-owner associator has the literal common/selective cut
   (4.6)--(4.9), and a rank-only average is not a valid compression.  More
   generally, a compression must satisfy (4.3a).
4. Every fixed-matching option has occupancy support deficit at least
   \(D_{m,q}\), whose Gaussian limit is (0.7); the actual deficit may be
   larger.
5. Hence uniform component expansion and aggregate \(o(W)\) binary holes are
   false for the pure-shore catalogue.

The proof does **not** show that the full exact associator-switch fibre is
pure-shore.  Connected exclusion overlap classifies independent
status-selector supports; it does not exclude a new hybrid or mosaic exact
factor.  The two-sided phase-changing \(Q_8\) primitive already proves its
successor and predecessor frame identities, but it has not yet supplied a
literal physical-shadow map at every protected depth assembled into one
whole exact owner column.  If that larger compiler is constructed, its
binary image sets must be inserted into (1.3) and audited afresh; Theorem
3.1 will still make \(y\equiv1\) optimal if the enlarged atlas remains one
component, but the fixed-\(M\) support cap (5.1)--(5.2) will no longer follow.

No claim is made against a master LP with independently weighted overlapping
packets or against the occurrence-multiplicity relaxation; those are
different optimization problems.
