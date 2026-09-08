# Cross-audit of the cyclic boundary-moment obstruction and its PBBS interface

Date: 2026-07-25

Method: pure hand mathematics only.  No web search, finite search, solver,
random experiment, or long-running computation was used.

Audited source:

`MATH_ATTACK_W_SPC_CYCLIC_BOUNDARY_MOMENT_OBSTRUCTION_20260725.md`.

PBBS comparison source:

`MATH_ATTACK_R_PBBS_DEPENDENT_BALANCED_REBUNDLING_20260725.md`.

## 0. Audit verdict

The decisive quota-uniform cyclic identity and PSD packet obstruction are
valid.  The two-block negative-mode theorem, its `t/sqrt(m)` scale, edit
robustness, and the private exact-component cube barrier are also valid.

Five corrections or scope refinements are necessary.

1. The sharp quota-prescribed uniform packet-size bound at depth `q` is

   \[
   R_q^*=c_q+1+\mathbf1_{\rho_q>0},
   \tag{0.1}
   \]

   not always `c_q+2`.  The printed choice `c_q+2` remains a valid upper
   bound, so none of the printed lower bounds is false; it is merely
   nonsharp at an integral-ratio depth `rho_q=0`.

2. The general support theorem proves

   \[
   s=\Omega(q),
   \]

   not `s=Theta(q)`.  The latter is valid only after a separate
   `s=O(q)` hypothesis, as in the mesoscopic two-block class.

3. The entropy theorem is a theorem for one fixed **labelled** support
   `U`.  A placement type must record the full labelled embedding of `U`
   into the cycle modulo rotation and reversal.  Architectures in which
   `U` varies are not covered unless the choices of `U` are included in
   the type catalogue.  Hence Sections 6.1 and 6.2 do not compose into the
   unrestricted architecture no-go claimed in the source; they compose
   only for an independently bounded `s=O(q)`, fixed-support or
   support-counted class.

4. The private `C8` components live in the canonical MSW/`(2 3)`
   interaction overlay.  It is imprecise to say that the alternating
   components are contained in one factor alone.  The resulting cube
   vertices are genuine exact factors, and the packet lower bound on every
   vertex is valid.

5. “Collision-free” in the local Hall relaxation means injective centres
   and targets.  It does not assert that the two neighbouring middle
   vertices of different wedges are disjoint.

The PBBS investigation gives a new exact conditional no-evasion theorem.
If an exact reference factor already has the report's mesoscopic negative
mode at `q=Theta(sqrt(m))`, then `O(Cat_m)` exact-factor-realizable PBBS
packets of uniformly bounded depth-`q` `l1` mass cannot remove it, no matter
how their selectors are dependent.  Removing the mode requires total
histogram mass `Omega(q Cat_m)`, so with only Catalan-many packets their
average mass is `Omega(q)`.  This is exactly the mass regime that the Lane
R Gaussian collision example identifies as critical.

This theorem is conditional because the raw PBBS cycle factor is not an
exact wreath factor, and no current theorem puts any exact PBBS-derived
reference factor in the negative spectral class.  With only Catalan-many
bounded-mass packets, PBBS can evade the class only by starting outside it;
it cannot repair a factor that is already inside it.  An `omega(t)` packet
family is a separate alternative.

## 1. Notation

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m.
\tag{1.1}
\]

At depth `q`, put

\[
r=m-q,\qquad
N_q=\binom nr,\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,
\qquad
\rho_q=W-c_qN_q.
\tag{1.2}
\]

For an exact factor `F`, let `mu_q^F(S)` be the number of cyclic
rank-`r` owners of `S`.  For distinct coordinates `i,j`, let

\[
H_q(F;i,j)
=\sum_{C\in F}(d_C(i,j)-r)_+,
\qquad H_q(F;i,i)=0,
\tag{1.3}
\]

where `d_C(i,j)` is their shorter distance in the row `C`.

For a PSD test `Q` with `Q 1=0`, define

\[
M_q(Q)
=\max_{|S|=r}\mathbf1_S^{\mathsf T}Q\mathbf1_S.
\tag{1.4}
\]

## 2. Quota elimination and the sharp threshold

### Verdict on Lemma 1.1

The quota order-statistic elimination is valid exactly as written.
For a target with owner set `O`, covering every `j`-owner packet is
equivalent to

\[
\operatorname{bot}_j(x;O)\ge1.
\]

A low target has packet size `c_q+1`; a high target has packet size
`c_q+2`.  Therefore all targets must satisfy the high condition, while
every failure of the low condition must be assigned one of the `rho_q`
high quotas.  The high-quota locations may be chosen independently at
different ranks, while the row weights remain common.

The convention `bot_j=+infinity` for `|O|<j` is correct: in that case
there is no `j`-owner survival packet to cover.

### Correction 2.1 — sharp quota-uniform packet-size bound

For a fixed depth, the sharp bound determined uniformly by the quota
prescription is

\[
\boxed{
R_q^*=c_q+1+\mathbf1_{\rho_q>0}.}
\tag{2.1}
\]

#### Proof

If `rho_q=0`, every quota equals `c_q`, so every survival packet has size
`c_q+1`.  If `rho_q>0`, at least one high quota equals `c_q+1`, whose
survival packets have size `c_q+2`; no larger packet occurs.  ∎

For a particular factor and quota placement, the exact largest **nonempty**
packet can be smaller if every high target has too few owners to contain a
`c_q+2` packet.  Thus the statement in the source that `c_q+2` is always
sharp should be corrected.  Using `c_q+2` uniformly is valid and loses only
a constant at resonant depths.

## 3. The cyclic boundary identity

### Verdict on Theorem 2.1

Every displayed identity and constant in Theorem 2.1 is valid:

\[
K_q(F)
:=\sum_{|S|=r}(\mu_q^F(S)-c_q)
 \mathbf1_S\mathbf1_S^{\mathsf T}
=a_qJ+b_qI+H_q(F),
\tag{3.1}
\]

where

\[
a_q=\binom{n-2}{m-2}-qt-c_q\binom{n-2}{r-2}
\tag{3.2}
\]

and

\[
b_q
=\frac{m+1}{2}t-c_q\binom{2m-1}{m-q-1}
=\frac{m+1}{2}t(1-c_qp_q),
\qquad
p_q=\prod_{j=1}^q\frac{m-j}{m+j}.
\tag{3.3}
\]

The off-diagonal count has no missing ordered-pair factor.  In one row,
the number of rank-`r` cyclic intervals containing a pair at shorter
distance `d` is `(r-d)_+`.  Exact middle ownership gives

\[
\sum_{C\in F}(m-d_C(i,j))
=\binom{n-2}{m-2}
=\frac{m-1}{2}t.
\tag{3.4}
\]

The identity

\[
(m-q-d)_+=(m-d)-q+(q-m+d)_+
\]

then proves the off-diagonal part of (3.1).  The diagonal count `rt`
proves the stated `b_q`.

The row sum and entry bounds are also exact:

\[
H_q\mathbf1=q(q+1)t\mathbf1,
\qquad
0\le H_q(i,j)\le\frac{qt}{2}.
\tag{3.5}
\]

For the second inequality, write `s_C=m-d_C(i,j)`.  The chord bound

\[
(q-s)_+\le q\left(1-\frac{s}{m-1}\right)
\]

and (3.4) give `qt/2` exactly.

Finally,

\[
\lambda_qp_q
=1-\frac{q(q+1)}{m(m+1)}
\tag{3.6}
\]

and hence

\[
\frac{b_q}{t}
=\frac{q(q+1)}{2m}
 +\frac{m+1}{2}p_q(\lambda_q-c_q).
\tag{3.7}
\]

No sign or floor correction is missing.

### Verdict on the compressed trace

For `P=I-J/n`,

\[
\operatorname{Tr}P(b_qI+H_q)
=m(m+1)t p_q(\lambda_q-c_q)\ge0.
\tag{3.8}
\]

This is valid and shows that a negative mode is not forced by trace.  At
an integral ratio `lambda_q`, the compressed trace is zero, but this alone
does not produce either a negative mode or a balanced factor.

## 4. Packet cover to quota-safe core

### Verdict on Lemma 3.1

The truncation argument is valid.  With

\[
y_C=(1-Rx_C)_+,
\qquad
D=\sum_C(1-y_C),
\]

one has

\[
D\le R\sum_Cx_C.
\]

If `k=beta_q(S)+1<=R` owners had positive `y`-weight, each would satisfy
`x_C<1/R<=1/k`, so that packet would have total weight strictly below
one.  Therefore at most `beta_q(S)` owners survive positively and

\[
\mu_q^y(S)\le\beta_q(S).
\]

The strict inequality is essential and is present in the source proof.
One may use the sharp `R_q^*` from (2.1).

## 5. Quota-uniform PSD obstruction

### Theorem 5.1 — sharpened audited form

For every exact factor `F`, every depth `q`, every placement of the
balanced high quotas, and every

\[
Q\succeq0,\qquad Q\mathbf1=0,
\]

with `M_q(Q)>0`,

\[
\boxed{
\vartheta(F,\beta)
\ge
\frac{[-\operatorname{Tr}Q(b_qI+H_q(F))]_+}
 {nR_q^*M_q(Q)}.}
\tag{5.1}
\]

#### Audit proof

For a packet cover `x`, use the truncated core `y` and put

\[
\delta=\mu_q^F-\mu_q^y,
\qquad
h=\beta_q-c_q,
\qquad
\gamma=\beta_q-\mu_q^y.
\]

Then

\[
K_q(F)=\mathcal G(\delta)+\mathcal G(h)-\mathcal G(\gamma),
\tag{5.2}
\]

where every Gram matrix is PSD, and

\[
\sum_S\gamma(S)=nD.
\tag{5.3}
\]

The sign in (5.2) is correct.  Testing against PSD `Q` drops the first two
terms and bounds the last by `nDM_q(Q)`.  Since `Q1=0` kills `a_qJ`, and
`D<=R_q^* sum x_C`, minimization proves (5.1).  Thus the theorem is truly
uniform over the mobile quota locations.

PSD is indispensable.  The condition `Q1=0` alone does not make the two
positive Gram terms discardable.

### Corollary 5.2 — sharpened negative spectral-mass bound

Let

\[
\mathcal N_q(F)
=\sum_{\xi<0}|\xi|
\]

be the negative spectral mass of the compression of `b_qI+H_q(F)` to
`1^perp`.  Then

\[
\boxed{
\vartheta(F,\beta)
\ge
\frac{\mathcal N_q(F)}
 {R_q^*r(n-r)}.}
\tag{5.4}
\]

#### Proof

Let `Q` be the projector onto the negative eigenspace.  Since
`Q<=P=I-J/n`,

\[
M_q(Q)
\le\mathbf1_S^{\mathsf T}P\mathbf1_S
=r-\frac{r^2}{n}
=\frac{r(n-r)}n.
\]

Insert this in (5.1).  ∎

The source bound with denominator `n(c_q+2)r` is valid but weaker by an
asymptotic factor of about two and also misses the resonant threshold
improvement.

### Exact spectral scale

For `q<=A sqrt(m)`, `R_q^*=O_A(1)` and `r(n-r)=Theta(m^2)`.  Therefore:

- `vartheta=O_A(t/m)` only forces

  \[
  \mathcal N_q(F)=O_A(mt);
  \tag{5.5}
  \]

- `vartheta=o(t/m)` forces

  \[
  \mathcal N_q(F)=o_A(mt);
  \tag{5.6}
  \]

- generic negative spectral mass `Omega_A(m^{3/2}t)` forces

  \[
  \vartheta=\Omega_A(t/\sqrt m).
  \tag{5.7}
  \]

A localized rank-one test can be stronger than (5.4), because its exact
`M_q(Q)` can be much smaller than the universal projector bound.

### Multidepth direct sums

The source Corollary 4.3 is valid.  Applying the one-depth proof to the
same packet cover and summing gives a ratio of sums, which cannot exceed
the best one-depth ratio after negative numerators are replaced by their
positive parts.  Direct sums of block-diagonal pair moments therefore do
not create cross-depth amplification.

## 6. Mesoscopic negative modes

### Verdict on Theorem 5.1 of the source

Let `P,N` be disjoint with `|P|=|N|=s/2`, and put

\[
u=\mathbf1_P-\mathbf1_N,
\qquad Q=uu^{\mathsf T}.
\]

The exact score is

\[
-u^{\mathsf T}(b_qI+H_q)u
=2[w_q(P,N)-w_q(P)-w_q(N)]-b_qs.
\tag{6.1}
\]

Under the two rank-feasibility hypotheses in the source,

\[
M_q(Q)=\frac{s^2}{4}.
\tag{6.2}
\]

Thus the aggregate bias hypothesis

\[
2[w_q(P,N)-w_q(P)-w_q(N)]
\ge[b_q+\gamma q(q+1)t]s
\tag{6.3}
\]

implies

\[
\boxed{
\vartheta(F,\beta)
\ge
\frac{4\gamma q(q+1)t}{nR_q^*s}.}
\tag{6.4}
\]

The source denominator `c_q+2` is valid; `R_q^*` is the sharp version.
If

\[
q/\sqrt m\to a>0,
\qquad s\le Cq,
\]

then (6.4) is

\[
\left(\frac{2\gamma a}{CR_q^*}+o(1)\right)
\frac t{\sqrt m}.
\tag{6.5}
\]

The size assumptions used to obtain (6.2) are necessary.  The source
correctly states them and correctly refuses to infer (6.3) from a biased
subfamily of rows alone.

### Edit robustness

The source Proposition 5.2 is valid.  A one-row tail matrix is symmetric,
nonnegative, and `q(q+1)`-regular, hence has operator norm at most
`q(q+1)`.  Replacing `k` old rows by `k` new rows changes a PSD trace by at
most

\[
2kq(q+1)\operatorname{Tr}Q.
\]

Thus `k<=gamma t/4` preserves half the stated negative margin.

## 7. Support scale and entropy

### Theorem 7.1 — corrected support conclusion

If `Q` is supported on `s` coordinates, then the source inequality

\[
\operatorname{Tr}Q(b_qI+H_q)
\ge
\left(b_q-\frac{(s-1)qt}{2}\right)
\operatorname{Tr}Q
\tag{7.1}
\]

is valid.  Hence a negative certificate requires

\[
s>1+\frac{2b_q}{qt}.
\tag{7.2}
\]

If `q/sqrt(m)->a>0`, `c_q=c` along the sequence, and

\[
1-ce^{-a^2}>0,
\]

then

\[
\frac{s}{q}
\ge
\frac{1-ce^{-a^2}}{a^2}-o(1).
\tag{7.3}
\]

The correct conclusion is

\[
\boxed{s=\Omega(q),}
\]

not `s=Theta(q)`.  No upper bound on `s` follows from (7.1).  At a
resonance `ce^{-a^2}=1`, only the exact floor expression (3.7) is valid.

### Theorem 7.2 — exact scope of the type-entropy bound

For one fixed labelled set `U`, `|U|=s`, and a trace family
`T subseteq 2^U`, the source bound is exact:

\[
\frac{|\mathcal C|}{t}
\le
\sum_{R\in\mathcal T}
\frac{\binom{n-s}{m-|R|}}{\binom nm}
\le
|\mathcal T|
\left(\frac{m+1}{n-s+1}\right)^s.
\tag{7.4}
\]

If a placement type records the full labelled embedding
`U -> Z_n` modulo the dihedral action, it produces at most `n` traces.
For a catalogue of `L` such types occupying density `alpha`,

\[
\boxed{
L\ge
\frac\alpha n
\left(\frac{n-s+1}{m+1}\right)^s.}
\tag{7.5}
\]

For `s=Theta(sqrt(m))`, this is

\[
L\ge\frac1n\exp((\log2-o(1))s)
\]

for fixed positive `alpha`.

The qualifier “labelled” is essential.  An unlabeled gap type can acquire
up to label-permutation factors and need not have only `n` traces.  The
support `U` is also fixed.  If atoms use varying supports, each support
family must first be partitioned or assigned to fixed-`U` subfamilies.
The resulting pairs `(U,type)` can then be counted and their bounds summed.
Merely counting possible supports without such a row decomposition does
not invoke (7.5).

Consequently the source's claimed general composition of its Theorems 6.1
and 6.2 is unsupported.  The composition is valid for a class with both

\[
s=O(q)
\]

and a fixed or explicitly counted support catalogue.  In that class,
(7.3) gives `s=Theta(q)` and (7.5) gives the advertised exponential type
requirement.

## 8. Depth-one Hall and equivariant lift

### Verdict

The depth-one Gram identity, including

\[
a_1=\frac{m-4}{m+2}t,
\qquad b_1=t,
\qquad \rho_1=\frac{2W}{m+2},
\]

is valid.  If a full exact factor is itself quota-safe at depth one, then

\[
tI+H_1\succeq0
\quad\hbox{on }\mathbf1^\perp.
\]

The two Hall arguments in the local centre-target graph are also valid.
“Collision-free local angle core” means only that the centres and assigned
targets are distinct.  The two neighbouring middle vertices used by the
corresponding local wedges may repeat, so this is not a vertex-disjoint
partial wreath packing.

The prime congruence calculation in Proposition 7.3 is correct for the
equivariant, wedge-respecting lift.  There are at most

\[
(p-1)/2=m
\]

fixed arithmetic cyclic supports, and the quotient row count violates the
residue condition exactly when

\[
p\equiv1,11\pmod {12}.
\]

This does not exclude an arbitrary non-equivariant re-decomposition of the
same invariant centre set.  It closes the equivariant lift, not the
unrestricted local Hall relaxation.

## 9. Private exact-component cube

### Imported input scope

The audited theorem from
`MATH_ATTACK_P5_AFR_BRIDGE_SELECTION_20260725.md` says that the canonical
MSW/`(2 3)` interaction overlay contains

\[
L=\operatorname{Cat}_{m-4}
\]

independent alternating `C8` components.  Switching any subset yields a
genuine exact factor.  Their depth-one four-cell supports are disjoint and
each switch has profile

\[
(3,1,1,1)\longmapsto(2,2,0,2).
\tag{9.1}
\]

This is the exact imported hypothesis used in the source.  No larger
overlay component is included in the resulting `L`-coordinate subcube.

### Verdict on the mobile overload identity

For every nonnegative integral depth-one histogram of total `W`,

\[
O_1(h)=\max\{H_0(h),E_2(h)\}
\tag{9.2}
\]

is exact.  It follows by writing

\[
r_2+E_2=H_0+\rho_1
\]

and optimizing the `rho_1` upper quotas.

### Theorem 9.1 — sharpened private-cube barrier

At a cube vertex obtained by switching `k` of the `L` components, let
`H_0^0,E_2^0` be the canonical values.  Then

\[
H_0=H_0^0+k,
\qquad
E_2=E_2^0-k,
\tag{9.3}
\]

and, for every balanced common multidepth quota system,

\[
\boxed{
\vartheta(F_I,\beta)
\ge
\frac{\max\{H_0^0+k,E_2^0-k\}}{3n}
\ge
\frac{\max\{k,L-k\}}{3n}
\ge
\frac{\lceil L/2\rceil}{3n}.}
\tag{9.4}
\]

In particular,

\[
\vartheta(F_I,\beta)
\ge\frac{L}{6n}
=\left(\frac1{3072}+o(1)\right)\frac tm.
\tag{9.5}
\]

#### Audit proof

Every switched rectangle creates one hole and removes one unit of
load-above-two, proving (9.3).  The `L` old load-three cells are distinct,
so `E_2^0>=L`, giving the second inequality of (9.4).

For a target with `h` owners and packet size

\[
j=\beta_1(S)+1\le3,
\]

averaging all `j`-owner packet inequalities gives

\[
\sum_{C\in O_{1,S}}x_C\ge\frac hj.
\]

For a violating target,

\[
h-\beta_1(S)\le h\le3\frac hj.
\]

After summing over targets, every row is counted at most `n` times, so

\[
O_{\beta_1}(F_I)\le3n\sum_Cx_C.
\]

Use (9.2) and minimize.  Finally

\[
\frac{\operatorname{Cat}_{m-4}}t\to\frac1{256},
\qquad \frac m{6n}\to\frac1{12},
\]

which gives `1/3072`.

“Arbitrary dependence” is valid only inside this fixed overlay subcube.
It does not cover trades using the omitted larger overlay components or
external PBBS packets whose shadow supports meet the private rectangles.

## 10. Exact bridge from PBBS load mass to the cyclic spectrum

The following theorem is the main new comparison.

### Theorem 10.1 — spectral Lipschitz transport

Let `F_0,F_1` be exact factors on the same coordinates.  Fix a depth
`1<=q<=m-2` and put

\[
\delta_q(S)=\mu_q^{F_1}(S)-\mu_q^{F_0}(S),
\qquad
E_q=\|\delta_q\|_1.
\tag{10.1}
\]

Then

\[
\boxed{
H_q(F_1)-H_q(F_0)
=\sum_{S\in\Omega_q}\delta_q(S)
 \mathbf1_S\mathbf1_S^{\mathsf T}.}
\tag{10.2}
\]

For every `Q\succeq0` with `Q1=0`,

\[
\boxed{
\left|
\operatorname{Tr}Q(H_q(F_1)-H_q(F_0))
\right|
\le M_q(Q)E_q.}
\tag{10.3}
\]

If

\[
D_0:=-\operatorname{Tr}Q(b_qI+H_q(F_0))>0,
\tag{10.4}
\]

then every balanced quota placement for `F_1` satisfies

\[
\boxed{
\vartheta(F_1,\beta)
\ge
\frac{[D_0-M_q(Q)E_q]_+}
 {nR_q^*M_q(Q)}.}
\tag{10.5}
\]

#### Proof

The constants `a_q,b_q` in (3.1) are independent of the exact factor.
Subtracting the two boundary identities gives (10.2).  Since `Q` is PSD,

\[
0\le\mathbf1_S^{\mathsf T}Q\mathbf1_S\le M_q(Q).
\]

The triangle inequality proves (10.3).  Thus the negative score at `F_1`
is at least `D_0-M_q(Q)E_q`; apply (5.1).  ∎

This theorem is completely insensitive to independence or product signs.
It uses only the two actual integral exact factors and their exact
histogram distance.

### Corollary 10.2 — additive packet leverage

Suppose the actual exact-factor change decomposes as

\[
\delta_q=\sum_{i=1}^P\delta_{i,q}
\]

and

\[
\|\delta_{i,q}\|_1\le R
\qquad(1\le i\le P).
\]

Then

\[
E_q\le PR.
\tag{10.6}
\]

No independence hypothesis is used.  If switches interact nonlinearly,
the `delta_{i,q}` must be increments of actual exact-factor-valid clusters
or of a telescoping sequence of exact factors; isolated formal switch
increments cannot be substituted for the actual change.

## 11. Catalan bounded-mass PBBS cannot repair a mesoscopic mode

### Theorem 11.1 — exact conditional no-evasion theorem

Assume an exact reference factor `F_0` has the two-block score

\[
D_0
\ge\gamma q(q+1)t s,
\tag{11.1}
\]

where `Q=uu^T` is as in Section 6 and therefore

\[
M_q(Q)=s^2/4.
\]

Let `F_1` be any exact factor with

\[
E_q=\|\mu_q^{F_1}-\mu_q^{F_0}\|_1.
\]

Then every balanced quota system satisfies

\[
\boxed{
\vartheta(F_1,\beta)
\ge
\left[
\frac{4\gamma q(q+1)t}{nR_q^*s}
 -\frac{E_q}{nR_q^*}
\right]_+.}
\tag{11.2}
\]

In particular, making the same trace nonnegative requires

\[
\boxed{
E_q\ge\frac{4\gamma q(q+1)t}{s}.}
\tag{11.3}
\]

If `s<=Cq`, then

\[
E_q\ge\frac{4\gamma}{C}(q+1)t.
\tag{11.4}
\]

Suppose now that

\[
q/\sqrt m\to a>0,
\qquad s\le Cq,
\qquad P\le C_0t.
\tag{11.5}
\]

If `F_0 -> F_1` is realized by `P` packets of mass at most a constant
`R_0`, then

\[
E_q\le C_0R_0t,
\]

and (11.2) retains an

\[
\Omega_A(t/\sqrt m)
\]

lower bound; the bounded-mass correction is only `O_A(t/m)`.

Conversely, with only `C_0t` packets, removing the mode forces average
packet mass at least

\[
\frac{4\gamma(q+1)}{CC_0}=\Omega(q).
\tag{11.6}
\]

Reducing the lower bound in (11.2) merely to `O_A(t/m)`, rather than all
the way to zero, still requires

\[
E_q
\ge
\frac{4\gamma q(q+1)t}{s}-O_A(t),
\tag{11.7}
\]

which is a `1-O_A(1/q)` fraction of the full spectral leverage in
(11.3).

#### Proof

Insert `M_q(Q)=s^2/4` and (11.1) into (10.5), giving (11.2).
Equation (11.3) is the necessary condition `D_0-ME_q<=0`, and (11.4)
uses `s<=Cq`.  The remaining statements follow from (10.6),
`n=Theta(m)`, and `q=Theta(sqrt(m))`.  ∎

### Interpretation for the Lane R reservoir

The verified clean-reservoir theorem supplies a subfamily of `Theta(t)`
algebraic four-core packets after harmless truncation.  Therefore, under
the still-unproved hypotheses that a `P=O(t)` selection of these packets is
exact-factor realizable and has uniformly bounded actual depth-`q` mass,
Theorem 11.1 says it cannot move an already obstructed exact factor out of
the W mesoscopic spectral class.  This does not rule out an
`omega(t)`-packet architecture if a larger usable family can be built.

The alternatives are exact:

1. the exact PBBS-derived base factor already has no such negative mode;
2. the construction uses `omega(t)` packets;
3. the average packet mass is `Omega(q)`;
4. the final factor is not obtained as a bounded-mass perturbation of the
   obstructed exact reference.

Alternative 3 meets the independent Lane R barrier.  A common balanced
fractional slab, constant target congestion, and packet mass `Theta(q)`
can still have `Theta(W)` Gaussian weighted collision.  Thus an already
W-bad base creates a genuine dilemma:

- bounded mass has too little spectral leverage;
- `Theta(q)` mass has enough leverage but is at the critical collision
  scale and needs additional signed cancellation.

This is not a global impossibility theorem, because no current result puts
the PBBS object in the W-negative class.

## 12. Can the concrete PBBS dependencies lie outside the class?

### 12.1 Full rotation packets do not give a bounded-mass escape

For a separated load-one core `K`, let `delta_{K,1}` be the individual
clean `C8` first-shadow increment.  The proved rotation orthogonality is

\[
\left\|\sum_j a_j\tau^j\delta_{K,1}\right\|_2^2
=\|\delta_{K,1}\|_2^2\sum_ja_j^2,
\tag{12.1}
\]

and translated supports are disjoint.  Hence

\[
\left\|\sum_j a_j\tau^j\delta_{K,1}\right\|_1
=\|\delta_{K,1}\|_1\sum_j|a_j|.
\tag{12.2}
\]

If the seed increment is nonzero, a positive centered selection in the
gcd-one case uses all `n` rotations and has first-shadow mass

\[
n\|\delta_{K,1}\|_1,
\]

not bounded mass.  In the exceptional gcd-three design, a positive
selection of `n/3` rotations still gives mass
`(n/3)||delta_{K,1}||_1`.  Therefore averaging positive switch
subfamilies cannot simultaneously provide centered balance and an `O(1)`
packet mass, unless the seed is already first-shadow invisible.  When `n`
is prime, the signed Fourier theorem gives the same all-constant
classification.  For composite `n`, additional bounded signed
Fourier-kernel relations are not excluded.

Seed nonvanishing is unproved, and the statement is packet-local; different
core orbits may overlap and cancel.

### 12.2 Four-core dependencies are outside the rotation no-go but remain
conditional

The algebraic relation

\[
\zeta_A+\zeta_B=\zeta_C+\zeta_D
\]

uses only four cores and therefore escapes the `n`-rotation
**switch-count** obstruction.  It is not a cyclic average and is not ruled
out by (12.1)-(12.2).  Four switches can nevertheless have actual
depth-`q` shadow mass `Theta(q)`; `O(1)` shadow mass is not implied by the
four-core ownership identity.

However, the relation concerns centered residual-path ownership.  It does
not imply any of the following:

- endpoint-compatible exact-factor sewing;
- an affine four-sparse shadow increment;
- overlap of the four shadow supports with the signs needed for
  cancellation;
- a common fractional floor slab;
- absence of a W negative mode in the completed exact factor.

Thus the four-core packets can lie outside the **formal hypotheses** of the
rotation and private-cube no-go classes, but no actual bounded-mass spectral
evasion has been constructed.

### 12.3 The raw PBBS factor has no W spectrum yet

The matrix identity (3.1) uses exact middle ownership by literal
`n`-wreath rows.  The canonical PBBS cycle factor can have components of
length `hn`, `h>1`.  It is therefore invalid to compute its long-component
tail matrix and insert it into Theorem 11.1 as though it were an exact
factor.

The spectral question becomes meaningful only after an integral PBBS
rebundling has produced literal exact wreaths.  No such positive-density
rebundling is currently proved.

## 13. Relation to the private-cube barrier

The private cube requires only first-shadow, not Gaussian-depth, leverage.
This makes its scale different from the mesoscopic spectral mode.

### Proposition 13.1 — external histogram mass needed to leave the private
debt

Let `h_I` be the depth-one histogram of a private-cube vertex and let `h'`
be any nonnegative integral histogram of total `W`.  Put

\[
E_1=\|h'-h_I\|_1.
\]

Then

\[
\max\{H_0(h'),E_2(h')\}
\ge
\left\lceil\frac L2\right\rceil-\frac{E_1}{2}.
\tag{13.1}
\]

If `h'` is the depth-one histogram of an exact factor `F'`, then every
balanced quota system satisfies

\[
\boxed{
\vartheta(F',\beta)
\ge
\frac{[\lceil L/2\rceil-E_1/2]_+}{3n}.}
\tag{13.2}
\]

#### Proof

Because the two histograms have the same total mass, their total positive
and negative variations are both `E_1/2`.  Filling a hole uses at least one
unit of positive variation, while removing one unit of `E_2` uses at least
one unit of negative variation.  Therefore

\[
H_0(h')\ge H_0(h_I)-E_1/2,
\qquad
E_2(h')\ge E_2(h_I)-E_1/2.
\]

Take their maximum and use
`max{H_0(h_I),E_2(h_I)}>=ceil(L/2)`.  The same packet-averaging argument
used in Section 9 gives `vartheta>=O_1/(3n)`, proving (13.2).  ∎

To reduce the private debt to `o(t)`, and hence evade its `t/m` lower
scale, one needs `E_1>=L-o(t)=Theta(t)`.  Catalan-many bounded-mass
packets can have total first-shadow mass `Theta(t)`, so the private-cube
barrier does **not** give the `Omega(qt)` no-evasion conclusion of
Theorem 11.1.  PBBS cross-core packets have enough aggregate magnitude in
principle, but their required signs, support overlaps, exact topology, and
common multidepth behavior remain unproved.

## 14. Precise final boundary

### Valid without correction

1. The boundary-moment identity, including every floor coefficient, tail
   row sum, and entry bound.
2. The packet-to-PSD argument and its uniformity over mobile quota
   positions.
3. The two-block negative-mode theorem and `t/sqrt(m)` scale.
4. Positive-radius row-edit stability of an exhibited negative mode.
5. The exact lower support inequality and nonresonant `Omega(q)` bound.
6. The fixed-labelled-support entropy theorem.
7. The depth-one Gram identity and local Hall relaxations, with the stated
   cyclicity caveat.
8. The equivariant prime residue obstruction, within its equivariant
   wedge-respecting scope.
9. The private exact-component cube barrier and constant `1/3072`.

### Corrections

1. Replace the claimed sharp `c_q+2` by `R_q^*` in (2.1) when
   `rho_q=0` matters.
2. Replace every unrestricted `Theta(q)` support conclusion by
   `Omega(q)`.
3. Restrict the composition with entropy to `s=O(q)` and a fixed or
   support-counted labelled catalogue.
4. Describe the private alternating components as components of the
   interaction overlay, not of one factor in isolation.
5. Interpret “collision-free local Hall core” as centre-target injectivity,
   not vertex-disjoint wedge packing.

### PBBS conclusion

Catalan-many uniformly bounded-mass PBBS packets cannot repair an
already-present W mesoscopic negative mode.  This is an exact theorem and
does not depend on independent signs.  With only `O(t)` bounded-mass
packets, the only escape is to construct an exact PBBS-derived factor that
is spectrally benign from the outset.  An `omega(t)` packet family is not
excluded.  The present PBBS package neither constructs such a factor nor
proves it impossible.

Full positive cyclic PBBS packets fail bounded mass whenever their seed
shadow increment is nonzero.  Four-core cross-orbit dependencies are the
bounded-size candidates constructed in the audited Lane R package, but
their exact-factor topology and multidepth shadow cancellation remain open;
this is not a classification of every possible PBBS trade.  The
private-cube barrier can in principle be crossed with `Theta(t)` total
first-shadow mass, so it is not by itself a no-go for Catalan-many bounded
packets.

No constant-one theorem, literal contiguous-OR word, or global SPC
counterexample follows from this audit.
