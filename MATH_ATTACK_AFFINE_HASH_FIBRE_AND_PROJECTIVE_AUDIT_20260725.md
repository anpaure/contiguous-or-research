# Affine all-row hash: entropy survives; fibre regularity and singleton cuts do not follow automatically

## 0. Verdict

The affine subset-sum hash is substantially stronger than an iid
target-color hash.

* It makes every protected row hash-rainbow using only \(O(p+Q)=O(g)\)
  coordinate-label equations.
* Its entropy cost is
  \[
    p^{\,3-2(p+2Q)}\exp(m^{o(1)})
    =\exp[-\Theta(g\log g)],
  \]
  not \(g^{-K}\).
* The original coordinate-labelling entropy absorbs this cost, leaving
  degree \(\exp(\Theta(g\log m))\).
* For a balanced global hash, every rank--hash part has
  \((1/p+e^{-\Omega(m)})\) of its Boolean rank.

These are genuine positive results.

Two gaps remain.

1. For one fixed global hash, the affine subcatalogue degree of a tag or
   target is a buffered arithmetic-progression partition function of its
   full hash histogram.  Its coefficient-accurate regularity is not a
   consequence of the entropy count; the exact partition function is
   displayed in (4.4).
2. Hash-rainbow rows are physically \(p\)-partite, but truncated
   projective planes are already partite.  At the palette-incidence level
   the affine progression adds no obstruction: any transversal can be
   ordered by its part labels as one full arithmetic progression.

Thus the affine hash evades the fatal iid-target entropy loss and is worth
retaining, but it does not yet prove the weighted matching cut.

---

## 1. Setup

Let \(p\) be prime, with

\[
 Q=o(p),\qquad p=m^{1/2+o(1)},
 \tag{1.1}
\]

and put

\[
 L=p+2Q.
 \tag{1.2}
\]

Take a balanced coordinate labelling

\[
 h:[2m]\to\mathbb F_p,
 \tag{1.3}
\]

so every label class has size \(2m/p+O(1)\).  A buffered grid is affine
when, for some \(A,B\in\mathbb F_p\) and
\(\alpha\in\mathbb F_p^\times\),

\[
 h(a_i)=A+\alpha i,\qquad
 h(b_i)=B+\alpha i\qquad(1\le i\le L),
 \tag{1.4}
\]

and

\[
 (B-A)/\alpha\notin[-Q,Q].
 \tag{1.5}
\]

For \(\chi(S)=\sum_{x\in S}h(x)\), the exact grid calculation gives

\[
 \chi(L_q(t+1))-\chi(L_q(t))=(B-A)-\alpha q,
 \tag{1.6}
\]

\[
 \chi(U_q(t+1))-\chi(U_q(t))=(B-A)+\alpha q.
 \tag{1.7}
\]

Thus every signed row through the \(p\) physical phases is a permutation
of \(\mathbb F_p\).

---

## 2. Exact entropy cost

Fix \(2L\) distinct physical coordinates
\(a_1,\ldots,a_L,b_1,\ldots,b_L\).  If their labels are iid uniform, then
for fixed \((A,B,\alpha)\), (1.4) has probability \(p^{-2L}\).
The number of admissible triples is

\[
 p^2(p-1)\left(1-\frac{2Q+1}{p}\right)
 =p^3(1-o(1)).
 \tag{2.1}
\]

Distinct triples give distinct label patterns once \(L\ge2\).  Hence

\[
 \boxed{
 \theta_{\rm aff}
 =p^{3-2L}(1-o(1))}
 \tag{2.2}
\]

under iid labels.

For a balanced labelling, prescribed labels are sampled without
replacement from classes of size \(2m/p+O(1)\).  Every residue is requested
at most three times because \(L=p+2Q<2p\) eventually.  The falling
factorial correction gives

\[
 \boxed{
 \theta_{\rm aff}^{\rm bal}
 =
 p^{3-2L}
 \exp\!\left[
 O\!\left(\frac{L^2}{m}+\frac{Qp}{m}\right)
 \right]
 =
 p^{3-2L}\exp(m^{o(1)}).}
 \tag{2.3}
\]

Indeed, the denominator correction is \(O(L^2/m)\), while repeated
residue requests contribute \(O(Q/(2m/p))=O(Qp/m)\).

A tag catalogue contains, before priorities and schedules are counted,
at least two independent ordered coordinate strings chosen from reservoirs
of size \(m-O(L)\).  Consequently

\[
\begin{aligned}
 \log D_{\rm aff}
 &\ge
 2L\log(m-O(L))-(2L-3)\log p-O(m^{o(1)})\\
 &=
 2L\log(m/p)+O(L+\log p+m^{o(1)})\\
 &=
 \Theta(p\log m).
\end{aligned}
 \tag{2.4}
\]

Thus

\[
 \boxed{D_{\rm aff}=\exp(\Theta(g\log m)).}
 \tag{2.5}
\]

The affine restriction therefore preserves exponentially more than enough
local choices.  It escapes the iid physical-target bound
\(g!\,g^{-K}\).

---

## 3. The global hash parts are balanced

Assume first that every residue occurs exactly
\(n=2m/p\) times.  Let

\[
 N_{r,c}=\#\{S\subseteq[2m]:|S|=r,\ \chi(S)=c\}.
\]

With \(\omega=e^{2\pi i/p}\), Fourier inversion gives

\[
 N_{r,c}
 =
 \frac1p\sum_{a\in\mathbb F_p}
 \omega^{-ac}
 [z^r]\prod_{s\in\mathbb F_p}(1+z\omega^{as})^n.
 \tag{3.1}
\]

The \(a=0\) term is \(\binom{2m}{r}/p\).  For \(a\ne0\),

\[
 \prod_{s\in\mathbb F_p}(1+z\omega^{as})^n
 =
 \bigl(1-(-z)^p\bigr)^n.
 \tag{3.2}
\]

Hence the nontrivial Fourier coefficient is zero unless \(p\mid r\);
when \(r=kp\), its magnitude is \(\binom nk\).  Uniformly for
\(r=m+O(H)\),

\[
 \frac{\binom n{r/p}}{\binom{pn}r}
 =e^{-\Omega(m)}.
 \tag{3.3}
\]

Therefore

\[
 \boxed{
 N_{r,c}
 =
 \left(\frac1p+e^{-\Omega(m)}\right)\binom{2m}r.}
 \tag{3.4}
\]

If the class sizes differ by at most one, (3.2) acquires at most \(p\)
extra linear factors.  Their total coefficient mass is \(e^{O(p)}\), which
is absorbed by the \(e^{-\Omega(m)}\) ratio.  Thus (3.4) remains valid with
an \(e^{-\Omega(m)+O(p)}\) error.

So the physical rank--hash capacities are essentially perfectly balanced.
This does **not** yet say that the affine path degrees into them are
balanced.

---

## 4. Exact tag-fibre partition function

The remaining regularity issue can be written explicitly.

Fix a carrier/tag \(U\).  Put

\[
 u_s=|U\cap h^{-1}(s)|,\qquad
 v_s=|U^c\cap h^{-1}(s)|.
 \tag{4.1}
\]

For fixed \(A,\alpha\), the label sequence
\(A+\alpha,\ldots,A+\alpha L\) uses every residue once and repeats the
affine interval

\[
 I_{A,\alpha}
 =\{A+\alpha,\ldots,A+2Q\alpha\}.
 \tag{4.2}
\]

Hence the exact number of departure strings in \(U\) with those labels is

\[
 \boxed{
 \prod_{s\in\mathbb F_p}u_s
 \prod_{s\in I_{A,\alpha}}(u_s-1).}
 \tag{4.3}
\]

The corresponding arrival factor is obtained by replacing \(u\) by \(v\)
and \(A\) by \(B\).  Up to schedule/priority factors independent of the
histogram, the affine degree is therefore

\[
\boxed{
\begin{aligned}
 D_{\rm aff}(U;h)
 \propto&
 \left(\prod_su_sv_s\right)
 \sum_{\alpha\ne0}
 \sum_{\substack{A,B\\(B-A)/\alpha\notin[-Q,Q]}}
 \left[\prod_{s\in I_{A,\alpha}}(u_s-1)\right]
 \left[\prod_{s\in I_{B,\alpha}}(v_s-1)\right].
\end{aligned}}
 \tag{4.4}
\]

This identity is useful for two reasons.

First, the unbuffered factor \(\prod_su_sv_s\) is unusually stable.
Write
\(\mu_+=|U|/p\), \(\mu_-=(2m-|U|)/p\),
\(u_s=\mu_++x_s\), and \(v_s=\mu_--x_s+O(1)\).
Since \(\sum_sx_s=0\), its total linear fluctuation cancels:

\[
 \sum_s\log(u_sv_s)
 =
 p\log(\mu_+\mu_-)
 -\frac12\left(\mu_+^{-2}+\mu_-^{-2}\right)\sum_sx_s^2
 +O\!\left(
 (\mu_+^{-3}+\mu_-^{-3})\sum_s|x_s|^3+1
 \right).
 \tag{4.5}
\]

For a random carrier, the fluctuation of the sum of the quadratic terms is
\(O(p^{3/2}/m)=o(1)\).  Thus the main \(p\)-phase factor is
coefficient-regular on all but \(o(1)\) tag weight.

Second, the buffer is the genuine remaining term.  It is the affine
interval partition function in the second line of (4.4).  A single
interval product has logarithmic variance on the scale

\[
 \frac{Qp}{m}=m^{o(1)},
 \tag{4.6}
\]

so pointwise class-count concentration is not enough.  Averaging over all
\((A,B,\alpha)\) introduces signed departure/arrival cancellation, but a
coefficient-accurate bound for (4.4), and its target-fibre analogue, is not
currently proved.

The exact fibre theorem needed is

\[
\boxed{
\begin{gathered}
\text{for one balanced }h,\text{ outside weighted }o(W)\text{ fibres,}\\
D_{\rm aff}(F;h)=(1+o(1/Q))\,\overline D_{\operatorname{stratum}(F)}.
\end{gathered}}
 \tag{AFR}
\]

The \(o(1/Q)\) accuracy is sufficient for literal row repair.  An \(o(1)\)
version would still be useful together with the flagged chain/braid
reserve, but does not by itself finish coefficient one.

Thus the entropy calculation proves that (AFR) is not locally impossible;
it does not prove (AFR).

---

## 5. Affine row order does not eliminate the truncated projective plane

For each signed rank, the affine hash turns a path row into a transversal
of the \(p\) physical parts

\[
 V_c=\{S:|S|=m\pm q,\ \chi(S)=c\}.
 \tag{5.1}
\]

At the level of one row, the assertion that its colors form a nonconstant
arithmetic progression adds no set-system restriction beyond
transversality.  Given any transversal \(e\), order its unique member of
\(V_c\) by

\[
 c=c_0+t d,\qquad t\in\mathbb F_p,
 \tag{5.2}
\]

for any \(d\ne0\).  Its color order is then an affine progression.

Now take a truncated projective plane.  Its points are partitioned into
the lines through a deleted point, and every remaining line meets every
part exactly once.  Thus every edge is already a transversal.  Order each
edge by its part labels as in (5.2).  Pad every other signed row with
private targets carrying the same phase colors.  Then:

* every row of every edge is hash-rainbow in affine order;
* tag and target capacities can be made exact by parallel repetition;
* every two obstructing edges retain their singleton physical
  intersection;
* the projective matching cut is unchanged.

Therefore

\[
\boxed{
\text{partiteness plus affine phase order does not imply the required
 matching-dispersal inequality.}}
 \tag{5.3}
\]

This is an abstract logical obstruction, not a claim that the truncated
plane embeds into the Boolean geodesic catalogue.  It proves that any
positive use of the affine hash must exploit the actual cross-row
coordinate incidence, not merely its parallel classes.

There is one modest local gain.  A fixed physical target \(S\) and a fixed
path's affine parameters determine its unique phase in that row.  Two
shared targets determine a slope relation and therefore reduce nonlinear
two-target codegrees.  But the dangerous projective construction uses one
different singleton intersection for every edge pair, so this gain is
orthogonal to the unresolved first-order cut.

---

## 6. Updated affine-hash gate

The affine hash successfully replaces the fatal target-level probability
\(e^{-\Theta(K\log g)}\) by the affordable cost
\(e^{-\Theta(g\log g)}\).  It also gives globally balanced physical
rank--hash capacities.

To affect coefficient one it still needs both:

1. the affine fibre-regularity theorem (AFR), controlling (4.4) and its
   target-fibre version for one fixed \(h\);
2. a geodesic-specific weighted matching theorem inside the resulting
   transversal catalogue, stronger than abstract partiteness/affine row
   order.

Neither statement follows from the present entropy calculation.  In
particular, the affine hash does not by itself bound

\[
 \sum_t\left(
 \frac{\mathscr E_t}{\eta_t^2}
g\alpha^2\mathscr B_t
 \right),
\]

although it supplies an exponentially large structured subcatalogue on
which that gate can now be attacked.

---

## 7. Trim the physical block: the buffer partition function disappears

There is a simple improvement to the formulation above.

Instead of taking \(p\) physical phases and adding \(Q\) certificate
coordinates at both ends, take **exactly \(p\) affine-labelled coordinates
in each of the \(a\)- and \(b\)-strings**, reserve the first and last \(Q\)
positions as certificates, and emit only the central

\[
 \ell=p-2Q
 \tag{7.1}
\]

physical phases.  Since \(Q=o(p)\),

\[
 \ell=(1-o(1))p,\qquad Q/\ell=o(1).
 \tag{7.2}
\]

Every protected \(q\)-flag of a central phase still lies inside the
length-\(p\) affine strings.  Equations (1.6)--(1.7) remain valid, and each
row is hash-injective on the \(\ell<p\) emitted phases.

The reset/certificate cost is

\[
 O(Q)\frac{W}{\ell}
 =O(Q/p)W
 =o(W).
 \tag{7.3}
\]

The gain is algebraic: the label sequence

\[
 A+\alpha,\ldots,A+\alpha p
\]

uses every residue of \(\mathbb F_p\) exactly once.  There are no repeated
buffer residues.  Hence, for a tag histogram \(u,v\), the exact affine
string count for **every** admissible \((A,B,\alpha)\) is simply

\[
 \prod_su_s\prod_sv_s.
 \tag{7.4}
\]

Consequently the complete tag degree is

\[
 \boxed{
 D_{\rm trim}(U;h)
 =
 C_{\rm sched,pr}\,
 p(p-1)(p-2Q-1)
 \prod_{s\in\mathbb F_p}u_sv_s,}
 \tag{7.5}
\]

where \(C_{\rm sched,pr}\) is independent of the hash histogram.  The
buffer partition function in (4.4) has vanished.

The entropy fraction also improves to

\[
 \theta_{\rm trim}
 =
 p^{3-2p}\exp[O(p^2/m)],
 \tag{7.6}
\]

and still leaves

\[
 D_{\rm trim}=\exp(\Theta(p\log m)).
 \tag{7.7}
\]

### Proposition 7.1 (typical tag regularity)

For a uniformly random carrier of the prescribed size, with balanced
global \(h\),

\[
 \log\prod_su_sv_s
 =
 \gamma_{m,p}+o_{\Pr}(1)
 \tag{7.8}
\]

for a deterministic \(\gamma_{m,p}\).  Therefore all but \(o(1)\) of the
tag weight has degree

\[
 (1+o(1))\overline D_{\rm trim}.
 \tag{7.9}
\]

#### Proof

Use the expansion (4.5).  For the multivariate hypergeometric vector,
\[
 \operatorname{Var}\!\left(\sum_sx_s^2\right)=O(p\mu^2),
 \qquad \mu\asymp m/p.
\]
After multiplication by the quadratic coefficient
\(\Theta(\mu^{-2})\), the standard deviation is
\[
 O(\sqrt p/\mu)=O(p^{3/2}/m)=o(1).
\]
The summed cubic remainder is
\[
 O_{\Pr}(p/\mu^{3/2})
 =O_{\Pr}(p^{5/2}/m^{3/2})=o(1)
\]
in the present \(p=m^{1/2+o(1)}\) range.  The complement of the
coordinatewise central event has probability \(o(1)\) by hypergeometric
tails.  This proves (7.8)--(7.9). \(\square\)

This proves \(1+o(1)\) tag regularity for the trimmed affine catalogue; it
is compatible with the tagged chain/braid reserve.  Literal independent
repair would require the stronger \(o(1/Q)\) tag-defect scale, which is not
claimed here.  It was the buffer, not the \(p\)-phase core, that prevented
even this \(1+o(1)\) conclusion in the earlier formulation.

The target-fibre theorem remains.  Conditioning on one physical target
fixes a membership-atom profile across the hash classes, and the analogue
of (7.5) must be averaged over its possible affine phase and signed depth.
The rank--hash capacities are already balanced by (3.4), but the required
statement is still

\[
 \boxed{
 \sum_U
 \frac{D_{\rm trim}(U,S)}{D_{\rm trim}(U)}
 \le 1+o(1/Q)
 }
 \tag{7.10}
\]

outside \(o(W)\) target weight (or the corresponding weighted-cut form).
Unlike (AFR), equation (7.10) no longer contains the buffered affine
interval partition function.  It is now a pure membership-atom
equidistribution problem for one full residue transversal.

Thus trimming strictly advances the affine lane:

* entropy survives;
* all rows remain simultaneously physically hash-rainbow;
* reset cost is \(o(W)\);
* tag degrees are asymptotically regular;
* only the target-load/matching cut, including singleton dispersal,
  remains.

---

## 8. Exact hash-color mean drift

The trimmed construction also removes the degree-one **hash-color**
imbalance mode.

Parameterize \(B=A+\delta\).  Since the full \(a\)-string uses every
residue once,

\[
 \chi(C)=\chi(U).
 \tag{8.1}
\]

For an owner phase \(t\),

\[
 \boxed{\chi(X_t)=\chi(U)+t\delta.}
 \tag{8.2}
\]

For signed depth \(d\in[-Q,Q]\), the same calculation gives

\[
 \boxed{
 \chi(F_d(t))
 =
 \chi(U)+\beta_d(A,\alpha,\delta)
 +t(\delta+\alpha d),}
 \tag{8.3}
\]

where, for \(d\ne0\), the coefficient of \(A\) in \(\beta_d\) is \(d\).
Every step \(\delta+\alpha d\) is nonzero by the affine admissibility
condition.

For fixed \((\alpha,\delta,t)\) and \(d\ne0\), varying the free offset
\(A\) translates (8.3) bijectively through all of \(\mathbb F_p\).
Equation (7.5) shows that every \(A\) has exactly the same tag degree.
Consequently the uniform affine catalogue has **exactly equal incidence
in every hash color at every noncentral signed row**, before and after any
priority thinning which is independent of \(A\).

At \(d=0\), the offset \(A\) cancels and (8.2) applies.  The tag colors
\(\chi(U)\) themselves are balanced:

\[
 \#\{U:|U|=M,\ \chi(U)=c\}
 =
 \left(\frac1p+e^{-\Omega(m)+O(p)}\right)\binom{2m}M
 \tag{8.4}
\]

by the Fourier calculation of Section 3.  Activate the same number of
live tags in every tag-color class (discarding the exponentially tiny
rounding discrepancy).  Averaging also over the allowed nonzero
\(\delta\)'s makes the omitted \(2Q\) owner colors equidistributed.
Thus the owner-row hash-color losses are equal as well.

We have proved:

### Proposition 8.1 (color-stratified mean preservation)

For the trimmed affine catalogue, there is a tag-color-stratified bite
whose conditional first moment removes the same fraction of every
rank--hash part, simultaneously at all protected signed depths.

This statement concerns hash parts, not individual physical targets.
It kills the degree-one/color-imbalance harmonic exactly.  The remaining
nontrivial covariance is between distinct hash parts and is measured by
the residual pair-square/four-walk profile

\[
 \sum_{y\in V_{r+h}}K_z(x,y)^2.
 \tag{8.5}
\]

Thus the affine hash and the block-Schur theorem fit cleanly:

\[
 \boxed{
 \text{affine color stratification closes mean drift;}
 \quad
 \text{hereditary cross-color pair squares remain.}}
 \tag{8.6}
\]

Partiteness still does not prove the latter, as Section 5's truncated
projective-plane warning shows.

---

## 9. The single affine propagation theorem

Let \(z\ge1/\log m\) be the current common density of every rank--hash
part under the color-stratified bite.  Let

\[
 K_z(x,y)=\frac{d_z(x,y)}{\sqrt{d_z(x)d_z(y)}}.
\]

After the time-zero target-load condition (7.10) is supplied, the remaining
stochastic assertion can be stated without palettes:

> **Affine pair-square propagation (APSQ).**  Outside target fibres of
> total weight \(o(W)\), uniformly for every protected \(x\) and every
> rank gap \(h\),
> \[
> \sum_{|y|=|x|+h}K_z(x,y)^2
> \le Cz^{-2}
> \begin{cases}
> m^{-2},&h=0,\\
> (|h|+1)^2|h|!(C/m)^{|h|},&h\ne0.
> \end{cases}
> \tag{APSQ}
> \]

Proposition 8.1 supplies the exact **hash-color** degree-one part.  The
within-color target identity loads still require (7.10).  Given that
initial condition, the block-Schur theorem turns (APSQ) into

\[
 \mathfrak T_z(x)\le Cg/(mz^2),
\]

which is summable through \(z=1/\log m\).  Dynamic four-antichain
quarantine removes the large-intersection terms at raw cost \(o(W)\).

Thus, within the affine lane, the exact remaining pair is:

1. the time-zero within-color target-load theorem (7.10);
2. APSQ, a cross-color weighted four-walk propagation theorem.

Entropy, hash-part balance, tag regularity, and raw covariance are no
longer open.
