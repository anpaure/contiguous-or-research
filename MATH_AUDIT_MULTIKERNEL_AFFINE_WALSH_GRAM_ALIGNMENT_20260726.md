# Multikernel directions plus affine phases: the exact Walsh--Gram audit

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Verdict

Let \(d=2r\) be the active cube dimension in one tensor cell.  Combine the
two newest inputs as strongly as their proved statements allow:

* the context-dependent multikernel factor supplies an exact isometric
  cycle factor \(F_R\) of \(Q_d\) whose cycle direction sets are balanced
  at every Gaussian depth, apart from an
  \(O((\log d)^6/d)\) fraction of direction sets; and
* the affine phase theorem supplies an owner-preserving array of affine
  conjugates over the \(2^d\) all-main cells of one fixed associator shore.

The combined construction does **not** presently supply the required
negative cross-packet covariance.  There are four exact reasons.

1. **The two certified factors are not yet composable.**  The multikernel
   theorem does not prove that

   \[
       x\longmapsto\tau_q^{F_R}(x)
   \tag{0.1}
   \]

   is injective.  The affine array's Bernoulli and physical-separation
   arguments use precisely this injectivity for its different base factor,
   the recursive half-depth rainbow factor.  Affine conjugacy preserves
   every pre-existing trace collision.  Thus replacing the affine base
   factor by \(F_R\) reopens the same-packet diagonal which had just been
   removed.

2. **What can be combined is only a first-moment trace array.**  Use every
   translation once on \(2^d\) copies of \(F_R\).  Then the multikernel
   direction census and the exact affine formula give an
   \(o(2^{2d})\) aggregate trace-discrepancy, except for the preceding
   possible within-cell repetitions.  This is a deterministic statement,
   proved below.  It is a marginal statement and has no negative sign.

3. **The affine theorem balances after forgetting a persistent physical
   tag.**  Its physical targets have the form

   \[
                         (a;t),
   \tag{0.2}
   \]

   where \(a\in Q_d\) is the reservoir tag and \(t\) is the quotient face
   trace.  Distinct values of \(a\) are physically disjoint.  The theorem
   balances \(\sum_a z_a(t)\), while cross-packet covariance depends on the
   complete row assignment \(z_a(t)\).  The signed \(2\times2\) rectangles

   \[
     e_{(a,t)}+e_{(b,u)}-e_{(a,u)}-e_{(b,t)}
   \tag{0.3}
   \]

   are invisible to every proved R/G marginal and visible to the physical
   Gram form.  This is an exact statewise quotient obstruction, not a
   probabilistic objection.

4. **The proved phase array lives on vanishing owner mass.**  The all-main
   cells contain

   \[
                         16^r=(2/3)^r24^r
   \tag{0.4}
   \]

   owners per packet.  Across the canonical packet atlas their total mass
   is \(W(2/3)^r+o(W)=o(W)\).  All local pair-type shore drift at a touched
   block is carried by the two reservoir-active cells, not the four main
   cells.  Hence the certified affine phase array is supported on the
   shore-neutral side of the local signed-drift table.  The full-mass mixed
   activity patterns have the R direction ledger but no proved affine phase
   array.

There is an additional definitional obstruction.  R and G construct arrays
for one fixed shore at a time.  A Walsh coefficient

\[
 \widehat Z_{P,q,I}
 =2^{-r}\sum_{\varepsilon\in\{0,1\}^r}
       \chi_I(\varepsilon)Z_{P,q}^{\varepsilon}
\tag{0.5}
\]

requires one common, owner-resolved coupling of the arrays on all \(2^r\)
shores.  No such equivariant coupling is part of either theorem.  The
separate marginal conclusions leave the physical row coupling unspecified,
so their "combined Walsh--Gram matrix" is not determined by the present
constructions.

The exact remaining object is the physical tagged overlap kernel in
Section 6.  A future positive theorem must simultaneously prove:

1. trace injectivity for the multikernel base factor;
2. an affine array on all \(6^r\) activity cells, not only the \(4^r\)
   main cells;
3. a common coupling of those arrays across all associator shores; and
4. a negative singular alignment of order \(W\) against the physical
   overlap kernel.

The present R/G results prove none of item 4, and their certified quotient
modes contribute zero in the exact-balance ideal.  A specially correlated
full physical construction is not ruled out; it is simply a new theorem.

## 1. The two actual inputs

### 1.1 The multikernel direction factor

Let \(F_R\) be the deterministic outcome of the multikernel rainbow-tiling
theorem on \(Q_d\), where \(d\) is a sufficiently large power of two.  It
has

\[
                         N_d={2^{d-1}\over d}
\tag{1.1}
\]

isometric \(2d\)-cycles.  For \(D\in\binom{[d]}q\), let \(A_q(D)\) be the
number of cycles whose cyclic direction order contains \(D\) as a
consecutive set.  For every fixed Gaussian window \(q\le A\sqrt d\), all
but a proportion

\[
 \xi_{d,q}=O_A\!\left({(\log d)^6\over d}\right)
\tag{1.2}
\]

of the direction sets satisfy

\[
 A_q(D)=(1\pm\epsilon_d){2^{d-1}\over\binom dq},
 \qquad \epsilon_d=\exp\{-\Omega((\log d)^3)\}.
\tag{1.3}
\]

For \(q<d\), every compatible cycle supplies exactly two starts having
direction set \(D\).  Hence the owner-start direction multiplicity is

\[
 n_q^{F_R}(D):=
  |\{x:D_q^{F_R}(x)=D\}|=2A_q(D).
\tag{1.4}
\]

The exact total is

\[
 \sum_DA_q(D)=dN_d=2^{d-1},\qquad
 \sum_Dn_q^{F_R}(D)=2^d.
\tag{1.5}
\]

Equations (1.2)--(1.5) imply that the exceptional direction sets carry at
most

\[
 \sum_{D\text{ exceptional}}n_q^{F_R}(D)
 =O((\xi_{d,q}+\epsilon_d)2^d)
\tag{1.6}
\]

starts.  Indeed, the good sets already account for
\((1-O(\xi_{d,q}+\epsilon_d))2^d\) starts.

What is not present in this theorem is any bound on

\[
 m_q^{F_R}(D,\eta)
 :=|\{x:\tau_q^{F_R}(x)=(D,\eta)\}|.
\tag{1.7}
\]

Only its direction sum is known:

\[
                         \sum_\eta m_q^{F_R}(D,\eta)
                         =n_q^{F_R}(D).
\tag{1.8}
\]

### 1.2 The affine phase array

For every factor \(F\), every \(\sigma\in S_d\), every translation
\(a\in Q_d\), and \(y=\sigma x+a\), the owner-resolved trace formula is

\[
 \boxed{
 \tau_q^{F^{\sigma,a}}(y)
 =\left(\sigma D_q^F(x),
        (\sigma x+a)|_{[d]\setminus\sigma D_q^F(x)}\right).}
\tag{1.9}
\]

Using every translation with one fixed \(\sigma\) gives, for each trace
\((D,\eta)\), the exact occurrence load

\[
 \sum_{a\in Q_d}m_q^{F^{\sigma,a}}(D,\eta)
 =2^q n_q^F(\sigma^{-1}D).
\tag{1.10}
\]

For the recursive injective factor, the affine phase theorem chooses one
permutation \(\sigma_a\) for every translation and obtains simultaneous
near-uniform trace load.  Its proof uses that each cell variable

\[
 \mathbf1_{\{(D,\eta)\in\operatorname {Im}\tau_q^{F^{\sigma_a,a}}\}}
\tag{1.11}
\]

is Bernoulli.  Formula (1.11) is no longer an incidence indicator if the
base trace map has repetitions.

## 2. The strongest literal combination currently justified

Even without injectivity, (1.3) and (1.10) combine into a deterministic
occurrence-balancing statement.

### Theorem 2.1 (translation-complete R/G occurrence array)

Use one affine translate \(F_R^{1,a}\) for every \(a\in Q_d\).  Let

\[
 L_q(D,\eta)=
 \sum_{a\in Q_d}m_q^{F_R^{1,a}}(D,\eta),
 \qquad
 \lambda_{d,q}={2^{d+q}\over\binom dq}.
\tag{2.1}
\]

Then every good direction set in (1.3) satisfies

\[
                         L_q(D,\eta)
 =(1\pm\epsilon_d)\lambda_{d,q}
\tag{2.2}
\]

for every outside orientation \(\eta\).  Moreover

\[
 \boxed{
 \sum_{D,\eta}|L_q(D,\eta)-\lambda_{d,q}|
 =O((\xi_{d,q}+\epsilon_d)2^{2d}).}
\tag{2.3}
\]

The same statement holds for reverse/upper traces.

#### Proof

Equation (1.10), followed by (1.3)--(1.4), gives (2.2).  For good
directions, summing their relative error over all traces costs at most
\(\epsilon_d2^{2d}\), because the total trace occurrence mass in all
\(2^d\) cells is \(2^{2d}\).

For exceptional directions, (1.6) and (1.10) show that their actual mass
over all translations and orientations is

\[
 2^d\sum_{D\text{ exceptional}}n_q^{F_R}(D)
 =O((\xi_{d,q}+\epsilon_d)2^{2d}).
\]

Their share of the constant comparison vector is at most
\(\xi_{d,q}2^{2d}\).  Adding the good and exceptional estimates proves
(2.3).  Reverse traces have the same cyclic direction census. \(\square\)

This is the exact positive combination of R and G.  It balances
**occurrences**, not distinct physical targets, and it is confined to a
translation-complete common-frame array.

## 3. The invariant same-cell diagonal

For a factor \(F\), define its depth-\(q\) trace collision defect by

\[
 \kappa_q(F)
 =\sum_{D,\eta}(m_q^F(D,\eta)-1)_+
 =2^d-|\operatorname {Im}\tau_q^F|.
\tag{3.1}
\]

### Proposition 3.1 (affine conjugacy cannot repair the diagonal)

For every affine cube automorphism \(g\),

\[
                         \kappa_q(gFg^{-1})=\kappa_q(F).
\tag{3.2}
\]

Consequently an array of \(M\) affine conjugates has at least

\[
                         M\kappa_q(F)
\tag{3.3}
\]

same-cell duplicate occurrences before any cross-cell collision is counted.

#### Proof

The affine trace formula is a bijective relabelling of owners and trace
resources.  It preserves every fibre cardinality of \(\tau_q^F\), proving
(3.2).  Cells are owner-disjoint, so their internal duplicate ledgers add,
proving (3.3). \(\square\)

For the R/G array of Theorem 2.1, the diagonal is therefore

\[
                         2^d\kappa_q(F_R).
\tag{3.4}
\]

To retain the previously proved packet-wide injectivity one needs the new
condition

\[
                         \boxed{\kappa_q(F_R)=0
                         \quad(q\le Q).}
\tag{RI}
\]

No estimate toward (RI) occurs in the multikernel direction theorem.
Direction balance does not imply it: (1.8) fixes only the row sums of the
orientation table, while (3.1) depends on its occupied cells.

Conversely, retaining the recursive injective base factor makes
\(\kappa_q=0\), but then the multikernel cycle-direction theorem is not a
property of that factor.  The two results are alternative cell-factor
certificates until (RI) or a common refinement is proved.

## 4. Tensor activity patterns and the local drift carrier

Fix one associator shore.  In each eight-block, four local cells are
special-active (main) and two are reservoir-active.  Thus the all-main
product sector has

\[
                         4^r=2^d
\tag{4.1}
\]

cells and

\[
                         4^r2^d=16^r
\tag{4.2}
\]

owners.  The complete packet has \(6^r\) cells and \(24^r\) owners.  Hence

\[
 {\text{all-main owners}\over\text{all packet owners}}
 ={16^r\over24^r}=\left({2\over3}\right)^r=o(1).
\tag{4.3}
\]

For the canonical global atlas, which covers \(W-o(W)\) owners, the total
owner mass on which the proved affine array acts is

\[
                         W_{\rm main}
 =\left({2\over3}\right)^rW+o(W)=o(W).
\tag{4.4}
\]

At any fixed depth, even perfect injectivity lets these starts cover at most
\(W_{\rm main}=o(W)\) distinct physical targets.  A Gaussian target layer
has \(N_q=\Theta(W)\).  Thus the certified main array cannot itself cover a
positive fraction of that layer; essentially all coverage must come from
the mixed activity cells for which no affine array is proved.

There is an exact alignment mismatch with the associator drift.  At local
depth one, the four main cells have the same sixteen lower target resources
on the two shores, and the same sixteen upper resources.  The old/new
literal difference is

\[
\begin{aligned}
 O_0^-&=\{abz,cdz:z\in\{u,v,w,x\}\},\\
 O_1^-&=\{acz,bdz:z\in\{u,v,w,x\}\},
\end{aligned}
\tag{4.5}
\]

and its upper analogue; these come from the two reservoir-active cells.
In the original-frame type quotient the half-drifts are

\[
 D^{\rm type,-}=4(e_F-e_{F+1}),\qquad
 D^{\rm type,+}=4(e_{F+1}-e_{F+2}).
\tag{4.6}
\]

Thus every nonzero entry in (4.6) is carried by reservoir-active cell
occurrences.  Changing direction orders does not alter this local support
statement.  The R construction balances which blocks are touched, but the
G phase theorem is proved only when every local cell is main.  It therefore
does not phase-balance the occurrences carrying (4.6).

The same statement holds when both directions of a local square are touched:
the main cells have common lower trace \(Y\) and common upper trace
\(abcd\cup Y\), while the reservoir cells retain the old fixed pair
\(ab,cd\) or the new fixed pair \(ac,bd\).  Thus, under the common
owner/phase coupling required for a local associator drift calculation, all
nonzero touched-block drift remains reservoir-carried.

This is a statewise support obstruction to the proposed use of the **proved**
arrays: the array with controlled phases is disjoint from the local carrier
whose signed alignment was supposed to create the covariance.  Mixed
activity patterns contain \(W-o(W)\) owners and remain without a certified
phase array.

## 5. The persistent-tag quotient obstruction

The physical interpretation of the affine theorem is not an untagged trace
design.  A main cell is indexed by its reservoir orientation
\(a\in Q_d\), and its physical trace is

\[
                         (a;t),
 \qquad t=(D,\eta)\in\mathcal T_{d,q}.
\tag{5.1}
\]

Different tags have disjoint physical target images.  Define the quotient
map

\[
 Q:\mathbb R^{Q_d\times\mathcal T_{d,q}}
       \longrightarrow\mathbb R^{\mathcal T_{d,q}},
 \qquad
 (Qz)(t)=\sum_{a\in Q_d}z(a,t).
\tag{5.2}
\]

The R/G occurrence conclusion is a statement about \(Qz\).  The physical
collision form is a statement about \(z\).

### Theorem 5.1 (tag-quotient statewise no-go)

The quotient data \(Qz\), even when exactly constant, determine neither the
sign nor the magnitude of a physical cross-array Gram product.  More
precisely, \(\ker Q\) contains the rectangle vectors

\[
 R_{a,b;t,u}
 =e_{(a,t)}+e_{(b,u)}-e_{(a,u)}-e_{(b,t)},
\tag{5.3}
\]

and these vectors change physical inner products while preserving every
R/G marginal.

#### Proof

Every trace coordinate occurs once with sign \(+1\) and once with sign
\(-1\) in (5.3), so \(QR_{a,b;t,u}=0\).  Put

\[
 x=e_{(a,t)}+e_{(b,u)},\qquad
 y=e_{(a,u)}+e_{(b,t)}.
\]

Then \(Qx=Qy=e_t+e_u\), but

\[
                         \langle x,x\rangle=2,
 \qquad                   \langle x,y\rangle=0.
\]

Adding disjoint copies gives an extensive difference with identical
quotient histograms. \(\square\)

The rectangle is an information-theoretic witness in the actual tagged
resource space; it is not asserted that every individual rectangle is a
legal factor trade.  Its conclusion is exactly that the quotient theorem,
without an additional legal row-coupling statement, cannot imply a physical
Gram estimate.

### Corollary 5.2 (balanced quotient modes have zero Walsh drift)

Suppose arrays on all shores have one common coupling and satisfy the exact
quotient identity

\[
                         Qz^\varepsilon=b
 \qquad(\varepsilon\in\{0,1\}^r).
\tag{5.4}
\]

Then, for every nonempty \(I\subseteq[r]\),

\[
                         Q\widehat z_I=0.
\tag{5.5}
\]

#### Proof

Apply \(Q\) to the Walsh definition and use
\(\sum_\varepsilon\chi_I(\varepsilon)=0\). \(\square\)

With the near-balanced R/G arrays, the right side of (5.5) is only the
Walsh transform of their error vectors.  Hence the certified constant mode
does not produce negative covariance: every potentially useful nonconstant
mode lies in the persistent-tag kernel left uncontrolled by the theorems.

This obstruction is present in the actual construction because the first
coordinate in (5.1) is a genuine spectator orientation, not an artificial
proof label.  The affine theorem explicitly forgets it when forming its
balanced quotient load.

The multikernel construction has the same logical shape one level lower:
its direction count sums over right-cycle fibres, merge phases, and cycle
basepoints.  Those context labels survive in the owner-resolved target but
are absent from \(A_q(D)\).  Combining the two marginal arrays therefore
does not restore the discarded joint table.

## 6. Exact physical overlap kernel and Walsh expansion

For a packet \(P\), shore \(\varepsilon\), product cell \(c\), and local
trace \(t\), let

\[
 \Phi_{P,c,q}^{\varepsilon,\pm}(t)
\tag{6.1}
\]

be the physical rank-\((m\pm q)\) target obtained by inserting that trace
into the cell's fixed core, active coordinate frame, and spectator tags.
Let

\[
 z_{P,c,q}^{\varepsilon,\pm}(t)
\tag{6.2}
\]

be its selected multiplicity.  Under packet-wide injectivity these are
zero-one and their physical images are disjoint for fixed \(P,\varepsilon\).

For two cells in different packets define the exact physical overlap kernel

\[
 K_{P,c;P',c',q}^{\varepsilon,\delta,\pm}(t,u)
 =\mathbf1\{\Phi_{P,c,q}^{\varepsilon,\pm}(t)
             =\Phi_{P',c',q}^{\delta,\pm}(u)\}.
\tag{6.3}
\]

Then the cross-packet collision count is identically

\[
\boxed{
 \langle Z_{P,q}^{\varepsilon,\pm},
         Z_{P',q}^{\delta,\pm}\rangle
 =\sum_{c,c'}\sum_{t,u}
    z_{P,c,q}^{\varepsilon,\pm}(t)
    K_{P,c;P',c',q}^{\varepsilon,\delta,\pm}(t,u)
    z_{P',c',q}^{\delta,\pm}(u).}
\tag{6.4}
\]

This formula uses the actual physical cores and frames.  Neither the R
direction census nor the G quotient trace census contains the kernel
(6.3).

Now suppose, in addition to the proved results, that arrays have been
chosen on every shore with one common owner coupling.  Their simultaneous
weighted Walsh--Gram coefficient is

\[
\begin{aligned}
 G_{P,I;P',J}
 ={}&2^{-2r}\sum_{\varepsilon,\delta}
        \chi_I(\varepsilon)\chi_J(\delta)\\
 &\quad\cdot\sum_{q,\pm}w_q
   \sum_{c,c',t,u}
    z_{P,c,q}^{\varepsilon,\pm}(t)
    K_{P,c;P',c',q}^{\varepsilon,\delta,\pm}(t,u)
    z_{P',c',q}^{\delta,\pm}(u).
\end{aligned}
\tag{6.5}
\]

At a Gaussian depth with balanced mean and diffuse packet incidences, the
exact second-moment ledger requires

\[
 2\sum_{P<P'}C_{P,P',q}
 =-W+N_q\theta_q(1-\theta_q)+o(W).
\tag{6.5a}
\]

Thus a negative term of fixed \(W\)-scale is required; making the one-point
trace histogram constant is not enough.

The coefficient-one gate is

\[
 \boxed{
 \min_\sigma
  \sum_{P<P'}\sum_{(I,J)\ne(\varnothing,\varnothing)}
       G_{P,I;P',J}\chi_I(\sigma_P)\chi_J(\sigma_{P'})
 \le-cW+o(W).}
\tag{6.6}
\]

Equations (1.3) and (2.3) control sums of the \(z\)'s after summing out
indices of (6.5).  The tag rectangles (5.3) show that those sums do not
control (6.5).  Thus the structured arrays do not verify (6.6).

## 7. The absent cross-shore coupling

There is a final exact logical gap before (6.5) can even be evaluated from
R and G.

### Proposition 7.1 (marginal shore arrays do not determine Walsh modes)

Suppose that, for every shore \(\varepsilon\), an array
\(Z^\varepsilon\) satisfies the same direction and affine trace marginal
bounds.  These separate statements do not determine any nonempty Walsh
coefficient

\[
                         \widehat Z_I
 =2^{-r}\sum_\varepsilon\chi_I(\varepsilon)Z^\varepsilon.
\tag{7.1}
\]

#### Proof

Both hypotheses specify only separate per-shore marginal constraints.  The
linear map from the complete shore table to those constraints has the tag
rectangle kernel (5.3).  Hence the constraints do not determine the signed
sum (7.1).  A common coupling could remove this ambiguity, but neither R nor
G supplies one. \(\square\)

The local associator's phase-compatible colouring gives a common owner
coupling for the basic six-square trade.  It does not couple the exterior-
dependent multikernel recursion or the independently chosen affine row
arrays.  A positive continuation needs an equivariant-array theorem:

\[
 \boxed{
 \text{one array on the ownership overlap of all }2^r\text{ shores,
 with common owner phases and controlled physical kernels.}}
\tag{EAC}
\]

Without (EAC), choosing the R/G array separately on every shore merely
chooses the unknown Walsh coefficients rather than estimating them.

## 8. Exact boundary

Proved in this audit:

1. the exact translation-complete occurrence balance obtained by genuinely
   composing the R direction count with the G affine formula;
2. the invariant same-cell defect \(2^d\kappa_q(F_R)\), and the missing
   injectivity condition (RI);
3. the vanishing \((2/3)^r\) owner mass of the certified all-main phase
   array;
4. the fact that the useful local signed type drift is carried by the
   reservoir-active cells excluded from that array;
5. the persistent-tag rectangle obstruction showing that balanced quotient
   traces do not determine physical Gram products;
6. the exact physical overlap-kernel formula (6.4)--(6.5); and
7. the missing common cross-shore coupling (EAC).

Therefore the actual deterministic arrays do not supply the negative
cross-packet covariance of order \(W\).  Their common certified content is a
near-constant first moment after two context labels have been summed out.
The desired negative covariance lives in precisely those discarded context
indices.

Not ruled out is a new full mixed-cell construction satisfying (RI), (EAC),
and (6.6).  Such a theorem would no longer be a consequence of the present
R/G arrays; it would be the missing physical joint-design theorem.
