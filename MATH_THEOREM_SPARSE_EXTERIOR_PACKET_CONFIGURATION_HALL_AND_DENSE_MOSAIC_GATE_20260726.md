# Sparse exterior packets: an exact configuration-Hall cut and the dense-mosaic gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\longrightarrow\infty,\qquad H=o(m).
\tag{0.1}
\]

This note works only with literal Johnson owner chronologies.  No packet is
assumed to be a status cell.  The main theorem closes the architecture in
which genuinely exterior-moving finite routers are localized in a bounded
number of seam intervals on each long component.

Fix \(A>0\) and an integer

\[
                         q=A\sqrt m+O(1),\qquad q\le H.
\tag{0.2}
\]

Relative to any fixed coordinate pairing \(R\), define

\[
 \delta_A
   =e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0,
\tag{0.3}
\]

where \(\Phi\) is the standard normal distribution function.

### Sparse exterior-surgery obstruction

Let a literal owner factor have \(L\) exceptional rooted occurrences,
each supplying at most one depth-\(q\) target, and suppose its
non-\(R\) transitions lie, on component \(i\), in \(a_i\) cyclic seam
intervals of total length \(\ell_i\).  Then its actual lower target deficit
satisfies

\[
 \boxed{
 M_q^-\ge
 (\delta_A-o(1))W-L-
 \sum_i\bigl(\ell_i+(q-1)a_i\bigr).}
\tag{0.4}
\]

This is a literal \(0/1\)-weight configuration-Hall cut, not an average
degree estimate.  In particular, if

\[
 L=o(W/H),\qquad K=o(W/H),\qquad
 a_i=O(1),\qquad \ell_i=O(H)
\tag{0.5}
\]

uniformly over the \(K\) components, then

\[
                         M_q^-\ge(\delta_A-o(1))W.
\tag{0.6}
\]

Hence

\[
                         \sum_{s\le H}M_s^-\ne o(W).
\tag{0.7}
\]

The result applies to bounded \(C_6\), \(C_8\), or other finite
exterior-moving routers inserted only at \(O(1)\) localized seams per
backbone.  It does not assume that those routers use a fixed carrier or a
status-cell frame.

There is a second exact form.  If \(P_0\) is a background owner
permutation, \(P\) is the switched permutation, and

\[
                         D=\{X:P(X)\ne P_0(X)\},
\tag{0.8}
\]

then

\[
 \boxed{M_q^-(P)\ge M_q^-(P_0)-q|D|-L.}
\tag{0.9}
\]

Thus repairing a fixed-pair Gaussian deficit requires

\[
 |D|\ge
 \left({\delta_A\over A}+o(1)\right){W\over\sqrt m}
 =
 \left({\delta_A\over A}+o(1)\right)
       \omega\,{W\over H}.
\tag{0.10}
\]

An \(o(W/H)\)-component construction therefore needs an unbounded number
of genuinely support-changing exterior transitions per component on
average (or an even denser concentration on a smaller set of components).
Merely joining components with a bounded number of routers per backbone
cannot work.

### Exact boundary

The presently proved inverse-paired one-petal exterior routers satisfy a
stronger no-go: every strand-blind inverse-tube completion satisfying the
common phase template of Section 5 has exactly the same cyclic lower-
intersection and upper-union histograms in its two settings, at every
window length.  Arbitrarily correlated choices in a fixed owner-disjoint
bank leave every \(M_q^\pm\) unchanged.

The rank-\(10\) row-reencoding moving-exterior \(C_6\) packet is not
neutral and escapes that local theorem: its audited complete cyclic
carrier has \(\ell^1\)-changes \(6\) and \(30\) at depths one and two.
Even granting a disjoint
near-tiling by standalone copies, its three \(21\)-cycles per \(63\)
owners give \(K=(W-L)/21\), which fails
\(K=o(W/H)\).  It needs a dense embedding in long backbones, precisely the
case not supplied by the known packet theorem.

Finally, there is no universal nonnegative configuration-Hall obstruction
against the unrestricted full coordinate orbit of trace-injective
exterior packets.  That orbit has an exact simultaneous owner-and-target
fractional perfect home matching, with fractional packet count \(W/B\)
for packet size \(B\).  Consequently the obstruction above is sharp in
scope: it closes localized surgery, while the potentially payload-dense
prime-quotient class or a growing row-reencoding mosaic remains a genuine
integral factor--target problem.

## 1. Rooted trace dilation under successor surgery

Let \(\mathcal O=\binom{[2m]}m\).  For a permutation
\(P:\mathcal O\to\mathcal O\), define the rooted lower depth-\(q\) trace

\[
                         L_q^P(X)=\bigcap_{j=0}^{q}P^jX.
\tag{1.1}
\]

Only traces of rank \(m-q\) are accepted as literal protected targets.
Unsafe traces can only decrease support and will never be counted as
helpful.

Let \(P_0,P\) be two owner permutations and put \(D\) as in (0.8).

### Theorem 1.1 (exact predecessor-dilation lemma)

The set of roots whose depth-\(q\) state sequence can change is contained
in

\[
                         \bigcup_{j=0}^{q-1}P_0^{-j}D.
\tag{1.2}
\]

Consequently at most \(q|D|\) rooted depth-\(q\) traces change, and

\[
 \left|\operatorname{supp}_q^-(P)
          \setminus\operatorname{supp}_q^-(P_0)\right|
 \le q|D|.
\tag{1.3}
\]

If \(L\) owner slots are handled exceptionally, all successor changes on
the retained slots are included in \(D\), and each exceptional slot emits
at most one additional depth-\(q\) target, then

\[
 M_q^-(P)\ge M_q^-(P_0)-q|D|-L.
\tag{1.4}
\]

#### Proof

Suppose

\[
 P_0^jX\notin D\qquad(0\le j<q).
\tag{1.5}
\]

Inductively, \(P^0X=P_0^0X\).  If \(P^jX=P_0^jX\) for some \(j<q\),
then the common state is outside \(D\), so

\[
 P^{j+1}X=P(P_0^jX)=P_0(P_0^jX)=P_0^{j+1}X.
\tag{1.6}
\]

Thus the complete state strings through time \(q\), and therefore their
intersections, are identical.  This proves (1.2).

Every \(P_0^{-j}\) is a bijection, so the union in (1.2) has size at most
\(q|D|\).  One changed rooted trace can introduce at most one new literal
target, proving (1.3).  Exceptional slots can introduce at most one
additional depth-\(q\) target each, which proves (1.4). \(\square\)

### Corollary 1.2 (cyclic seam dilation)

Suppose \(D\), on the cycles of \(P_0\), is contained in a union of \(a\)
cyclic intervals having total length \(\ell\).  Then

\[
 \left|\bigcup_{j=0}^{q-1}P_0^{-j}D\right|
 \le \ell+(q-1)a.
\tag{1.7}
\]

Hence

\[
 M_q^-(P)\ge
 M_q^-(P_0)-\ell-(q-1)a-L.
\tag{1.8}
\]

#### Proof

The \(q\)-step predecessor dilation of one cyclic interval of length
\(\ell_s\) is a cyclic interval of size at most \(\ell_s+q-1\).
Sum over the \(a\) intervals.  Overlap only decreases the union size.
\(\square\)

This lemma is architecture-free.  The changed tails may be produced by
moving-exterior \(C_6\)'s, multipetal routers, or arbitrary literal
incidence trades.

## 2. The fixed-pair profile separator

Fix a perfect matching \(R\) of the \(2m\) coordinates.  For a set \(S\),
write

\[
                         F_R(S)=\#\{e\in R:e\subseteq S\}.
\tag{2.1}
\]

The number of middle owners of full-pair type \(k\) is

\[
 \boxed{
 S_k=
 {m!\,2^{m-2k}\over k!^2(m-2k)!}.}
\tag{2.2}
\]

The number of rank-\((m-q)\) targets of type \(k\) is

\[
 \boxed{
 T_{q,k}=
 {m!\,2^{m-2k-q}\over
       k!(k+q)!(m-2k-q)!}.}
\tag{2.3}
\]

The convention is that a factorial with negative argument makes the
corresponding count zero.

#### Proof of the counts

A middle owner with \(k\) full pairs has \(k\) empty pairs and
\(m-2k\) split pairs.  Choose the three pair classes and one endpoint in
every split pair, giving (2.2).

A rank-\((m-q)\) target with \(k\) full pairs has \(k+q\) empty pairs and
\(m-2k-q\) split pairs.  The same multinomial count gives (2.3).
\(\square\)

Their exact ratio is

\[
 \boxed{
 {T_{q,k}\over S_k}
 ={(m-2k)_{\underline q}\over
       2^q(k+1)^{\overline q}}.}
\tag{2.4}
\]

Let

\[
 \mathcal K_q=\{k:T_{q,k}>S_k\},\qquad
 \Delta_{m,q}=\sum_{k\in\mathcal K_q}(T_{q,k}-S_k).
\tag{2.5}
\]

Call a Johnson transition \(R\)-internal when it exchanges the two
endpoints of one edge of \(R\).  Let \(B_q^\times(P)\) be the number of
based depth-\(q\) windows of \(P\) which contain a transition that is not
\(R\)-internal.

### Theorem 2.1 (literal profile configuration cut)

For every literal owner factor \(P\), with \(L\) exceptional owners,

\[
 \boxed{
 B_q^\times(P)+M_q^-(P)+L\ge\Delta_{m,q}.}
\tag{2.6}
\]

#### Proof

Consider a correct-rank depth-\(q\) window all of whose transitions are
\(R\)-internal.  Its \(q\) used pairs are distinct.  They are split at
the starting owner, and their lower intersection makes them empty.  Every
full pair remains full.  Therefore

\[
                         F_R(L_q^P(X))=F_R(X).
\tag{2.7}
\]

There are exactly \(S_k\) possible starting owners of type \(k\).
Consequently the pair-internal windows can cover at most \(S_k\) distinct
targets of type \(k\).  A cross-\(R\) window can add at most one target,
and an exceptional owner can add at most one.  Thus the total number of
covered targets in the union of the deficient profiles
\(\mathcal K_q\) is at most

\[
                         \sum_{k\in\mathcal K_q}S_k
                         +B_q^\times(P)+L.
\tag{2.8}
\]

The demand in those profiles is
\(\sum_{k\in\mathcal K_q}T_{q,k}\).  Subtract (2.8), obtaining (2.6).
Unsafe windows supply no correct-rank target and only strengthen the
inequality. \(\square\)

### Configuration-Hall form

Suppose fixed owner regions are divided into choice groups \(g\), and one
complete legal option \(\omega\in\Omega_g\) is chosen in each group.
Let \(J_g^\omega\) be its literal depth-\(q\) lower target support.  Put

\[
 y_T=\mathbf1_{\{F_R(T)\in\mathcal K_q\}}.
\tag{2.9}
\]

Let \(C_g\) be the number of owner roots in group \(g\) whose full-pair
type belongs to \(\mathcal K_q\), and let

\[
 b_g=\max_{\omega\in\Omega_g}
 \#\{\text{cross-\(R\) based \(q\)-windows in option }\omega\}.
\tag{2.10}
\]

Then

\[
 \max_{\omega\in\Omega_g}
       \sum_{T\in J_g^\omega}y_T
 \le C_g+b_g.
\tag{2.11}
\]

Since

\[
 \sum_gC_g\le\sum_{k\in\mathcal K_q}S_k,
\tag{2.12}
\]

the exact reserve-\(E\) configuration-Hall inequality forces

\[
 \boxed{
 E\ge\Delta_{m,q}-\sum_gb_g-L.}
\tag{2.13}
\]

Thus (2.9) is a literal \(0/1\) separating weight.  Arbitrary correlations
between packet signs or local choices do not help: all variables shared
between options are first fused into the groups \(g\), and the maximum in
(2.11) is already over each whole legal fused option.

## 3. Sharp Gaussian evaluation

Assume (0.2).  The ratio in (2.4) is strictly decreasing in \(k\), so
\(\mathcal K_q\) is an initial interval.  Its boundary is

\[
 k_*={m\over4}-{3A\over8}\sqrt m+O(1).
\tag{3.1}
\]

The middle full-pair statistic has

\[
 {K-m/4\over\sqrt m/4}\Longrightarrow N(0,1),
\tag{3.2}
\]

while the rank-\((m-q)\) target statistic has mean

\[
 {m\over4}-{q\over2}+O(1)
\tag{3.3}
\]

and the same asymptotic standard deviation \(\sqrt m/4\).  The local
central limit theorem applied to (2.2)--(2.3) therefore gives

\[
 {1\over W}\sum_{k\in\mathcal K_q}S_k
 \longrightarrow \Phi(-3A/2),
\tag{3.4}
\]

\[
 {1\over N_q}\sum_{k\in\mathcal K_q}T_{q,k}
 \longrightarrow \Phi(A/2),
\qquad
 {N_q\over W}\longrightarrow e^{-A^2}.
\tag{3.5}
\]

Consequently

\[
 \boxed{
 {\Delta_{m,q}\over W}
 \longrightarrow
 \delta_A
 =e^{-A^2}\Phi(A/2)-\Phi(-3A/2).}
\tag{3.6}
\]

The constant is strictly positive.  Indeed, after shifting the second
normal integral by \(2A\),

\[
\begin{aligned}
 \delta_A
 &=\int_{-\infty}^{A/2}
     \left(e^{-A^2}\phi(x)-\phi(x-2A)\right)\,dx,\\
 {\phi(x-2A)\over\phi(x)}
 &=e^{2Ax-2A^2}\le e^{-A^2}
       \qquad(x\le A/2),
\end{aligned}
\tag{3.7}
\]

with strict inequality on a set of positive measure.

For completeness, (3.1) follows directly by taking logarithms in (2.4):
for every fixed \(B\), uniformly when
\(|k-m/4|\le B\sqrt m\),

\[
 \log {T_{q,k}\over S_k}
 =-\,{8q\over m}\left(k-{m\over4}\right)
   -{3q^2\over m}+O_{A,B}(m^{-1/2}).
\tag{3.8}
\]

The exact ratio is monotone with logarithmic step
\(-8A/\sqrt m+O_A(m^{-1})\), so the displayed error places its integer
crossing within \(O_A(1)\) of (3.1).  Stirling's formula, uniform on this
window, gives (3.2)--(3.5).  Outside a window of radius \(B\sqrt m\), the
tails are \(O(e^{-cB^2})\) uniformly in \(m\); letting first \(m\to\infty\)
and then \(B\to\infty\) proves (3.6).  The conclusion is unaffected by
the floor choices in \(q\) or \(k_*\).

Combining (2.6) and (3.6) proves

\[
 M_q^-\ge
 (\delta_A-o(1))W-B_q^\times(P)-L.
\tag{3.9}
\]

If all non-\(R\) transition positions lie in cyclic seam intervals as in
(0.4), then

\[
 B_q^\times(P)\le
 \sum_i\bigl(\ell_i+(q-1)a_i\bigr),
\tag{3.10}
\]

and (0.4) follows.

## 4. Consequences for finite exterior-router mosaics

### Corollary 4.1 (bounded seams per long component are impossible)

Suppose \(K=o(W/H)\), \(L=o(W/H)\), and for an absolute constant \(C\),

\[
                         a_i\le C,\qquad \ell_i\le CH
\tag{4.1}
\]

on every component.  Then, at every fixed \(A>0\),

\[
                         M_{\lfloor A\sqrt m\rfloor}^-
                         \ge(\delta_A-o(1))W.
\tag{4.2}
\]

#### Proof

Since \(q=O(\sqrt m)=o(H)\),

\[
 \sum_i(\ell_i+(q-1)a_i)
 \le C(H+q)K=o(W).
\tag{4.3}
\]

Also \(L=o(W)\).  Apply (0.4). \(\square\)

### Corollary 4.2 (support-changing tail density)

If \(P_0\) has

\[
                         M_q^-(P_0)\ge(\delta_A-o(1))W
\tag{4.4}
\]

and \(M_q^-(P)=o(W)\), with either no exceptional slots or an exceptional
allowance \(L=o(W)\) satisfying the hypotheses of (1.4), then

\[
 |D|\ge
 \left({\delta_A\over A}+o(1)\right){W\over\sqrt m}.
\tag{4.5}
\]

#### Proof

Equation (1.4) gives

\[
 q|D|\ge M_q^-(P_0)-M_q^-(P)-L
       =(\delta_A-o(1))W.
\]

Use \(q=A\sqrt m+O(1)\). \(\square\)

In particular, when \(H=\sqrt m\,\omega\),

\[
 { |D|\over W/H}
 \ge\left({\delta_A\over A}+o(1)\right)\omega
 \longrightarrow\infty.
\tag{4.6}
\]

If the mosaic has \(K=o(W/H)\) components, the average number of
support-changing successor tails on a component tends to infinity.

This is the exact sense in which successful exterior motion must be
payload-dense.  The theorem does not demand that a positive fraction of
all \(W\) tails change: the sharp necessary scale at one Gaussian depth
is \(W/\sqrt m\).  It does demand much more than one bounded router per
allowed component.

## 5. Exact neutrality of the certified inverse one-petal library

The preceding obstruction is quantitative.  The currently proved
one-petal exterior-router library has a stronger algebraic obstruction.

Let the strand set be \(I\), let \(\tau\) be a permutation of \(I\), and
let \(a_i\) be the exposed petal on strand \(i\).  Consider a closed tube
made from

1. a router transporting \(a_i\) to \(a_{\tau(i)}\);
2. a strand-independent payload;
3. the inverse router; and
4. a second strand-independent payload returning the common core.

The required strand-blindness hypothesis is phasewise, not merely a
support bound.  Assume that the two settings admit one common cyclic phase
index \(t\), common nonpetal sets \(C_t\), and masks
\(\alpha_t,\beta_t\in\{0,1\}\), all independent of \(i\), such that their
states have the forms

\[
\begin{aligned}
 X_{i,t}^{\tau}
   &=C_t\cup\bigl(\alpha_t\{a_i\}\bigr)
          \cup\bigl(\beta_t\{a_{\tau(i)}\}\bigr),\\
 X_{i,t}^{\tau^{-1}}
   &=C_t\cup\bigl(\alpha_t\{a_i\}\bigr)
          \cup\bigl(\beta_t\{a_{\tau^{-1}(i)}\}\bigr).
\end{aligned}
\tag{5.1}
\]

Here \(0\{a\}=\varnothing\) and \(1\{a\}=\{a\}\).  The same template is
assumed on the upper states.  The literal paired-\(C_6\) inverse tube and
its strand-independent cooldown payload satisfy (5.1).

### Theorem 5.1 (inverse one-petal trace neutrality)

Replacing \(\tau\) by \(\tau^{-1}\) preserves the complete literal cyclic
lower-intersection and upper-union histograms at every window length.

#### Proof

Fix one cyclic interval and take either its intersection or its union.
Applying the same Boolean operation to the common masks in (5.1) gives
another pair of masks independent of \(i\).  Its nonpetal part is likewise
independent of the strand and of the sign.  On row \(i\), its petal part
is therefore one of

\[
 \varnothing,\qquad
 \{a_i\},\qquad
 \{a_{\tau(i)}\},\qquad
 \{a_i,a_{\tau(i)}\}.
\tag{5.2}
\]

After summing over all strands, the singleton cases enumerate the same
petal set in either orientation.  The two-petal cases depend only on the
undirected multiset

\[
                         \{\{i,\tau(i)\}:i\in I\}.
\tag{5.3}
\]

This multiset is unchanged when \(\tau\) is replaced by
\(\tau^{-1}\).  Empty cases are trivial.  Adjoining the common nonpetal
context preserves equality of the literal sets with multiplicity.
\(\square\)

For the paired moving-exterior \(C_6\), \(I=\mathbb Z_3\) and
\(\tau\) is a \(3\)-cycle.  If either cyclic separation between the two
routers, counted from the insertion transition through the later removal
transition inclusively, has at most \(H\) Johnson transitions, one
\(H\)-window toggles that petal twice.  If both inclusive separations
exceed \(H\), this particular petal-repetition obstruction disappears;
regardless of any remaining payload-safety conditions, Theorem 5.1 says
that the tube still has no target action.

### Corollary 5.2 (correlation does not help a neutral bank)

Fix a bank which remains a disjoint union of the same whole closed tubes
in every option.  Allow arbitrary correlations among all tube signs.  At
every depth and both signs, the complete literal target histogram, its
support, and every missing-target number are independent of the chosen
signs.

#### Proof

Theorem 5.1 gives zero histogram derivative for each whole tube.
Histograms add over owner-disjoint complete components.  Correlation
changes the joint law of the signs but cannot change a pointwise zero
sum. \(\square\)

If \(\mathcal Z\) is a background hole family, then
\(y=\mathbf1_{\mathcal Z}\) is an exact configuration-Hall witness:
every option contributes zero on \(\mathcal Z\), so any reserve must have
size at least \(|\mathcal Z|\).

This covers the proved aligned and inverse-tube completions built from the
smallest moving-exterior \(C_6\), including arbitrary strand-blind cooldown
payloads satisfying the common phase template (5.1).  The open one-way
router by itself is not a closed tube.  The theorem does not cover the
rank-\(10\) row-dependent exterior
reencoding packet, a multipetal atom exposing at least three row-dependent
coordinates, cross-tube splicing, relocation of packet supports, or a
nonadditive overlapping collar system.  For the explicit aligned
\(\Phi/\Psi\) completion, the stronger equality of coordinate-word cyclic
interval histograms follows from its separate displayed-word theorem; it
is not inferred from (5.1).

## 6. Why no unrestricted fractional Hall cut exists

The sparse-surgery separator must not be promoted to an obstruction
against every exterior-moving packet.

Let \(P\) be one legal packet with \(B\) middle owners.  For every typed
protected depth \(a=(q,\varepsilon)\), suppose it has an injective literal
trace map

\[
                         \tau_a:P\longrightarrow\mathcal T_a,
\qquad |\mathcal T_a|=N_a.
\tag{6.1}
\]

Take the complete \(S_{2m}\)-orbit \(\mathcal E\) of the packet, with
parallel indexed copies retained.  Let \(d_0\) be the common orbit degree
of a middle owner and \(d_a\) the common degree of a typed target.
Double counting gives

\[
                         |\mathcal E|B=Wd_0=N_ad_a,
\tag{6.2}
\]

and hence

\[
                         {d_a\over d_0}={W\over N_a}.
\tag{6.3}
\]

A home bundle for an orbit packet \(e\) consists of all its owner
vertices together with an arbitrary subset of each typed target support.

### Theorem 6.1 (exact fractional owner--target home matching)

The complete orbit home-bundle hypergraph has a simultaneous fractional
perfect matching on every owner and every typed target.  Its total
fractional packet count is \(W/B\).

#### Proof

Give every orbit packet initial weight \(1/d_0\).  Independently for each
typed target occurrence of type \(a\), retain it in the home bundle with
probability

\[
                         p_a={N_a\over W}.
\tag{6.4}
\]

Distribute the weight \(1/d_0\) over the resulting finite bundle law.
All probabilities are rational, so denominators may be cleared if an
explicit finite multiset is desired.

Every owner is present in every bundle of each incident packet, and has
fractional degree \(d_0/d_0=1\).  A fixed typed target has fractional
degree

\[
                         {d_a\over d_0}p_a
 = {W\over N_a}{N_a\over W}=1.
\tag{6.5}
\]

Finally, summing owner degrees in two ways gives

\[
 \sum_e{1\over d_0}
 ={|\mathcal E|\over d_0}={W\over B}.
\tag{6.6}
\]

This proves the theorem. \(\square\)

If \(B/H\to\infty\), then \(W/B=o(W/H)\).  Therefore no nonnegative
configuration-Hall or Farkas weight can separate the unrestricted orbit
home-bundle relaxation.  Any global negative theorem must either

1. use a genuinely integral joint factor--target inequality;
2. restrict the allowed packet catalogue, as Sections 2--5 do; or
3. prove a semigroup/blossom-type obstruction invisible to nonnegative
linear target weights.

On the odd ground set where an exact middle-wreath factor is available,
the analogous uniform owner vector also lies in the convex hull of
integral owner factors: average the coordinate orbit of that exact factor.
Thus, in that setting, owner-only blossom cuts and target-only Farkas cuts
cannot separately close the unrestricted exterior-packet route.

## 7. The surviving non-status-cell construction

The strongest current owner-exact noncubical architecture is the
prime-quotient long-cycle lift on \(p=2m+1\) prime coordinates.  A
quotient perfect matching lifts to an exact translation-equivariant
odd-graph cycle cover with zero owner leave.  In this paragraph write

\[
                         W_p=\binom{p}{m},\qquad T_p={W_p\over p}.
\tag{7.0}
\]

If a quotient cycle \(C\) has voltage \(v(C)\), then its squared Johnson
component contribution is

\[
 \begin{cases}
 p\gcd(|C|,2),&v(C)=0,\\
 \gcd(|C|,2),&v(C)\ne0.
 \end{cases}
\tag{7.1}
\]

Its component condition for \(H=o(p)\) is exactly

\[
 \sum_{C:v(C)=0}\gcd(|C|,2)=o(T_p/H).
\tag{7.2}
\]

Opposite-parity trace duality gives

\[
                         M_q^+=M_q^-.
\tag{7.3}
\]

Thus one-sided support is enough.  A safe quotient lift proves constant
one if

\[
\boxed{
\begin{gathered}
 \text{cyclic \((H+1)\)-safety},\\
 \sum_{C:v(C)=0}\gcd(|C|,2)=o(T_p/H),\\
 \sum_{q=1}^{H}M_q^-=o(W_p).
\end{gathered}}
\tag{7.4}
\]

With unsafe windows, the exact replacement is the safe-cut/component
ledger

\[
 \kappa_H=o(W_p/H),\qquad
 c_H=o(W_p/H),\qquad
 z_0=o(T_p/H),\qquad
 d_H=o(W_p).
\tag{7.5}
\]

This architecture permits payload-dense motion and is not generated by
status cells; no selected quotient matching is yet proved to have the
required density or support.  Sections 1--4 do not obstruct the class.
Ordinary quotient edge-colouring controls none of (7.4); the remaining
object is a root-transversal, voltage-biased, target-balanced
\(H\)-memory perfect matching.  A solution of (7.4) proves the prime
subsequence; the separately established dense-subsequence transfer is
still needed for the all-\(k\) theorem.

## 8. Audited boundary

Proved here:

1. the exact trace predecessor-dilation law (1.2)--(1.4);
2. the literal full-pair configuration-Hall separator (2.6), (2.13);
3. the floor-safe Gaussian constant \(\delta_A\) in (3.6);
4. the localized-seam obstruction (0.4);
5. the necessary support-changing tail scale
   \(\Omega_A(W/\sqrt m)=\omega(W/H)\);
6. exact all-depth lower/upper trace neutrality for inverse-paired
   strand-blind one-petal tubes satisfying the common phase template; and
7. exact absence of a nonnegative fractional Hall cut for the
   unrestricted full-orbit home-bundle relaxation.

Not proved here:

1. a positive-density contextual packing of the productive rank-\(10\)
   row-reencoding packet;
2. a dense fusion of those atoms into \(o(W/H)\) long components;
3. the prime-quotient constrained matching in (7.4); or
4. a universal integral obstruction to every payload-dense
   exterior-moving packet mosaic.

The precise surviving positive requirement is therefore not “one moving
seam per long component.”  It is a payload-dense owner-exact chronology
whose number of non-\(R\) Gaussian windows is \(\Omega_A(W)\) for every
fixed reference pairing \(R\), together with one common integral
all-depth target assignment.  The prime-quotient formulation is the
cleanest current exact form of that requirement.
