# Blind-context flat resolutions: exact degrees and the sparse-quotient capacity cut

Date: 2026-07-26

## 0. Verdict

The blind-context flats of the recursive diverse compiler are genuine
all-depth realizable bundles, but quotienting by them does not turn the
packet problem into an ordinary flat matching problem.

Let

\[
 R=2n,\qquad n=4\cdot2^s,\qquad K=2^R,
\]

and fix the largest protected depth \(H=o(n)\).  For physical phase
\(\rho\in\{0,1\}\), put

\[
 d_\rho=d_\rho(H)
   =\left\lfloor{\rho+H-1\over2}\right\rfloor+1,
 \quad v_\rho=4d_\rho,
 \quad u_\rho=n-v_\rho.                              \tag{0.1}
\]

Every compiler option partitions its phase-\(\rho\) starts into exactly

\[
 J_\rho=2^{n+v_\rho}                                  \tag{0.2}
\]

blind flats, each of size

\[
 B_\rho=2^{u_\rho-1},
 \qquad J_\rho B_\rho=K/2.                           \tag{0.3}
\]

Every flat is simultaneously target-rainbow at both signs and every
\(q\le H\), and the same affine label realizes all those bundles.

The exact affine degree of a prescribed abstract depth-\(H\) flat of
phase type \(\rho\) is

\[
 \boxed{
 D_\rho^{\rm flat}
 =|\Gamma_R|\,{J_\rho\over
  \binom RH\binom{R-H}{u_\rho}
  2^{R-H-u_\rho+1}}.}                               \tag{0.4}
\]

For an ordered all-depth flag use the count in (3.2) below; shorter
prefixes retain the initial bits of the future directions.
The complete intersections of several flats are coefficients of the
exact stacked \(k\)-target recursion in
`MATH_THEOREM_RECURSIVE_COMPILER_HIGHER_ORDER_BLIND_FLATS_AND_K_ENUMERATOR_20260726.md`.

There is, however, a sharp uniform Hall cut.  If a proposed quotient
construction uses at most \(s_P\) blind flats as home bundles in packet
\(P\), then at any one typed depth

\[
 \boxed{
 \left|\bigcup_P\text{assigned homes from }P\right|
 \le B_{\max}\sum_Ps_P,
 \qquad B_{\max}=\max_\rho B_\rho.}                 \tag{0.5}
\]

There are \(G/K\) packets and \(B_{\max}/K=2^{-n+O(H)}=o(1)\).
Consequently one representative flat per packet covers only

\[
                         2^{-n+O(H)}G=o(N_q)          \tag{0.6}
\]

targets.  More generally, an \(o(1)\)-fraction of the flat slots cannot
cover a positive fraction of a central layer.  A near-cover must use
\(1-o(1)\) of the entire flat **row mass**, hence exponentially many
flat classes per packet.

Thus the blind flats are not a sparse absorber or a smaller matching
instance.  They form parallel classes: one legal option selects one
whole resolution consisting of exponentially many flats.  Choosing the
flats independently is illegal, while enforcing that they come from one
resolution recovers the original whole-option problem.

This is an explicit Hall cut against the naive positive quotient.  A
structured near-resolution remains possible only if one proves a global
matching of almost complete flat resolutions, with all flats of one
packet sharing one option label.  The current local enumerator supplies
the degrees of that two-level hypergraph but no cross-parent resolution
theorem.

## 1. Exact flat partition inside one option

Use the unique physical start representation

\[
                         (p,x,\rho),qquad
 p\in E_n, x\in Q_n, \rho\in\{0,1\}.              \tag{1.1}
\]

For fixed \((x,\rho)\), the length-\(H\) window visits
\(d_\rho\) distinct bottom \(Q_4\)-leaves.  Let
\(V(x,\rho)\subset[n]\) be their context coordinates and let

\[
                         U(x,\rho)=[n]\setminus V(x,\rho).
\]

Then \(|V|=v_\rho\) and \(|U|=u_\rho\).  Two even contexts belong to
the same blind flat when their difference is an even vector supported on
\(U\):

\[
 p\sim_{x,\rho}p'
 \quad\Longleftrightarrow\quad
 p-p'\in E(U(x,\rho)).                              \tag{1.2}
\]

The subgroup in (1.2) has size \(2^{u_\rho-1}\).  Since the even context
shore has size \(2^{n-1}\), it has \(2^{v_\rho}\) cosets for each fixed
\((x,\rho)\).  There are \(2^n\) choices of \(x\).  This proves
(0.2)--(0.3).

If \(p'\sim p\), every visited leaf sees the same local context and the
same recursive direction sequence.  The physical starts differ only on
fixed \(b_i\)-coordinates outside every prefix support.  Hence, for each
\(q\le H\), the starts of one flat produce \(B_\rho\) distinct lower
targets and \(B_\rho\) distinct upper targets.  The one option label
realizes all of them simultaneously.

An affine compiler conjugate carries the whole partition (1.2) to
another partition of its image.  It cannot select or move one flat
without moving the other flats in the same resolution.

## 2. The flat-incidence resolution hypergraph

For a physical packet \(P\), option \(g\), phase \(\rho\), and flat
index \(\lambda\in[J_\rho]\), define the typed configuration bundle

\[
 \mathbf F_{P,g,\rho,\lambda}
 =\bigdotcup_{q\le H,\epsilon=\pm}
       F_{P,g,\rho,\lambda}^{q,\epsilon}.            \tag{2.1}
\]

Every projection in (2.1) has size \(B_\rho\).  For fixed \((P,g)\),
the bundles over \(\rho,\lambda\) partition every option image
\(I_{P,g,q}^{\epsilon}\).

There are two levels.

* A **flat edge** is one bundle (2.1).
* A **resolution edge** is the complete collection

  \[
       \mathscr R_{P,g}
       =\{\mathbf F_{P,g,\rho,\lambda}:
                    \rho\in\{0,1\},\lambda\in[J_\rho]\}.       \tag{2.2}
  \]

A legal state chooses exactly one resolution edge \(\mathscr R_{P,g_P}\)
for each packet color \(P\).  It may then assign any covered target to
one of the selected flat edges containing it.  Selecting flat edges from
different resolutions of one color is not legal.

Eliminating the flat indices in this two-level incidence system gives
exactly

\[
                         \sum_gx_{P,g}=1,
 \qquad
 h_t+\sum_{P,g}{\bf1}_{\{t\in I_{P,g}\}}x_{P,g}\ge1,           \tag{2.3}
\]

the original one-sided packet LP.  Thus the flat system is an exact
extended formulation, not a stronger relaxation.

## 3. Exact affine flat degrees

At one depth \(H\), an abstract blind flat of phase type \(\rho\) is
specified by:

1. a support \(J\in\binom{[R]}H\);
2. a set \(U\in\binom{[R]\setminus J}{u_\rho}\);
3. fixed outside symbols on the remaining \(R-H-u_\rho\) coordinates;
4. one of the two parity cosets on \(U\).

Therefore the ambient number of such flats is

\[
 {\cal N}_\rho^{\rm flat}
 =\binom RH\binom{R-H}{u_\rho}
    2^{R-H-u_\rho+1}.                               \tag{3.1}
\]

The affine cube group is transitive on this family.  Every base compiler
image contains exactly \(J_\rho\) of them.  Double counting an affine
label together with one of its flat blocks proves (0.4).

For the all-depth chain attached to one start, the ordered list of its
first \(H\) directions is remembered.  Its depth-one face retains the
initial bits on every coordinate except the first moved direction, so
the future \(H-1\) direction bits must also be retained.  The
corresponding ambient flat count is

\[
 \widetilde{\cal N}_\rho^{\rm flat}
 =(R)_H\binom{R-H}{u_\rho}
    2^{R-u_\rho},                                   \tag{3.2}
\]

and the same double count gives

\[
 \widetilde D_\rho^{\rm flat}
 ={|\Gamma_R|J_\rho\over\widetilde{\cal N}_\rho^{\rm flat}}.  \tag{3.3}
\]

The ambient number of individual ordered chains is
\((R)_H2^{R-1}\), so the conditional ratio below is unchanged from the
single-depth calculation.  If \(m_\rho\) phases have the same value of
\(u\), combine their
numerators.  Conditional on one compatible depth-\(H\) face lying in a
uniform affine option, the probability that its prescribed type-\(u\)
flat is the blind flat selected by the resolution is exactly

\[
                         {m_u\over2\binom{R-H}u}.    \tag{3.4}
\]

Indeed the face degree is
\(|\Gamma_R|K/[\binom RH2^{R-H}]\); divide (0.4), summed over the
\(m_u\) phases, by that degree.

For two or more prescribed flats, their common resolution degree is not
the product of (3.4).  It is the coefficient of their joint stacked
column histogram in the exact higher enumerator.  This is precisely the
point at which the blind-flat quotient retains the original higher-order
compiler dependence.

## 4. Uniform capacity cut

### Theorem 4.1 (sparse flat home assignments cannot near-cover)

Fix one typed layer \((q,\epsilon)\).  Suppose a legal construction
chooses one option per packet, but declares target homes in at most
\(s_P\) blind flats of packet \(P\).  Then

\[
 M_q^\epsilon
 \ge N_q-B_{\max}\sum_Ps_P.                         \tag{4.1}
\]

In particular, if one flat is used per packet,

\[
 M_q^\epsilon
 \ge N_q-{G\over K}B_{\max}
 =(1-o(1))N_q.                                      \tag{4.2}
\]

#### Proof

At the fixed typed layer, one declared flat contains at most
\(B_{\max}\) distinct targets.  The union of all declared home sets is
therefore at most \(B_{\max}\sum_Ps_P\), independently of overlaps.
Subtract from \(N_q\) to obtain (4.1).

Now

\[
 {B_{\max}\over K}
 =2^{-n-v_{\min}-1}=2^{-n+O(H)}=o(1),               \tag{4.3}
\]

and the packet count is \(G/K\).  Since \(N_q=\Theta(G)\) in every
fixed Gaussian window, (4.2) follows. \(\square\)

Equivalently, the constant target weight \(y\equiv1\) is a Farkas/Hall
witness against the flat hypergraph in which one is allowed only
\(s_P\) flat slots of color \(P\): its total support function is at most
\(B_{\max}\sum_Ps_P\).

The sharp necessary utilization statement is

\[
 \sum_{P}\sum_{\substack{F\text{ declared}\\F\subset\mathscr R_{P,g_P}}}
 |F|
 \ge N_q-o(W).                                      \tag{4.4}
\]

Because the total flat row mass over all packets is \(G\), (4.4) uses a
\(1-o(1)\) fraction of that mass whenever \(G/N_q=1+o(1)\), as at the
shallow depths.  The quotient therefore cannot discard most flat classes.

## 5. Exact surviving structured target

The blind-flat structure can still be positive, but only at the level of
whole parallel classes.  A sufficient theorem would be:

> Choose one resolution \(\mathscr R_{P,g_P}\) in every packet so that,
> at every signed protected depth, all but \(o(W)\) targets can be assigned
> to selected flat blocks, using a \(1-o(1)\) fraction of their total row
> mass.

This is equivalent to making the product-hole minimum \(o(W)\); the flat
partition supplies a structured certificate but does not weaken the
optimization.  Its exact local resolution degrees are (0.4), (3.3), and
the higher-enumerator coefficients.  The missing information is their
quenched alignment between different parent cells.

Nonconjugate compilers or cross-parent schedules could improve the
situation only by providing additional **whole resolutions**.  Adding
isolated flat edges without an owner factor would violate the one-option
constraint.  A useful new template must either:

1. align most of one resolution's flats with undercovered physical target
   regions; or
2. make the currently blind context influence the schedule, thereby
   replacing the large parity flats by a finer all-depth resolution.

No such global resolution is constructed here.  What is proved is the
exact two-level hypergraph, its affine flat degrees, and the capacity cut
showing that a sparse blind-flat quotient cannot be the missing
near-cover theorem.
