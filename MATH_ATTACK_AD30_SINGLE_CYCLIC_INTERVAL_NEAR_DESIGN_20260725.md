# AD30: the single cyclic-interval near-design gate

## 0. Scope and outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 R_q=\binom{2m}{m-q}\quad(0\le q<m).
\]

This report analyzes the exact $2m$-cycle lift of the global rotor
circulation and the common-arrival cone.  It proves the following.

1.  A single, purely integral cyclic-interval near-design statement is
    sufficient for a literal band word of length $W+o(W)$.  The exact
    compiler length is

    \[
      t(2m+2Q)+2\sum_{q=0}^Q h_q,
    \]

    where $t$ cyclic packets are selected and $h_q$ is the number of
    uncovered complementary atoms at depth $q$.

2.  The full permutation circulation gives the exact optimal fractional
    solution of this near-design problem.  It does not give an integral
    solution by division or independent thinning.  Every diffuse independent
    thinning at the optimal packet mass leaves $(e^{-1}-o(1))W/2$ owner
    atoms, hence $(e^{-1}-o(1))W$ owner masks, uncovered with high
    probability.

3.  The complete band packet hypergraph has exact degrees and codegrees.
    Although adjacent nested atoms have relative codegree of order $1/m$,
    its normalized outside-edge link mass is less than

    \[
       \frac{90}{m-Q}
    \]

    for $Q\le m/8$ and all sufficiently large $m$.  Thus the ordinary
    projective-plane/link-overlap obstruction is absent.  A growing-rank
    integral rounding theorem with absolute leftover $o(W)$ is still
    unproved.

4.  The frozen exact odd wreath factor supplies a stronger integral partial
    thinning.  Choosing one inclusive semicircle in every projected row gives
    exactly $W$ middle-state occurrences in $W/(m+1)$ literal rotor paths.
    Its full band defect is an explicit two-chart functional $D_Q(S)$ of a
    row-switch set $S$.  If $D_Q(S)=o(W)$, the resulting word has exact length

    \[
       W+2Q\frac{W}{m+1}+D_Q(S)=W+o(W).
    \]

The decisive boundary is therefore integral vertical incidence, not literal
chronology.  No constant-one theorem is claimed here.

Throughout, all selections and words are integral.  A displayed mask used as
one word letter is a literal subset of $[2m]$.

## 1. Cyclic packets and complementary atoms

Let $\Omega^+$ be the directed cyclic orders on $[2m]$, modulo rotation but
not reversal.  Thus

\[
 |\Omega^+|=(2m-1)!.
\]

For $\pi\in\Omega^+$, $j\in\mathbb Z_{2m}$, and $1\le r<2m$, write

\[
 I_\pi(j,r)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}.
\]

At depth zero let

\[
 \mathcal V_0=
 \bigl\{[A]=\{A,A^c\}: |A|=m\bigr\};
 \qquad |\mathcal V_0|=\frac W2.
\]

For $q\ge1$, let

\[
 \mathcal V_q=
 \bigl\{[A]=\{A,A^c\}: |A|=m-q\bigr\};
 \qquad |\mathcal V_q|=R_q.
\]

The lower representative of a positive-depth atom is unique.  Define the
radius-$Q$ packet

\[
 e_Q(\pi)=
 \bigl\{[I_\pi(j,m-q)]:0\le q\le Q,
                         j\in\mathbb Z_{2m}\bigr\}.
\]

At depth zero, starts $j$ and $j+m$ give the same atom.  At every positive
depth all $2m$ atoms are distinct.  Hence

\[
 |e_Q(\pi)|=m+2mQ=m(2Q+1).                 \tag{1.1}
\]

For a family $\Pi\subseteq\Omega^+$, let

\[
 h_q(\Pi)=
 \bigl|\mathcal V_q\setminus\textstyle\bigcup_{\pi\in\Pi}e_Q(\pi)\bigr|.
                                                        \tag{1.2}
\]

Thus $2h_q$ is exactly the number of uncovered masks in the paired ranks
$m-q,m+q$; at $q=0$, it is the number of uncovered middle masks.

## 2. The exact common-arrival compiler

The following lemma separates literal chronology from incidence coverage.

### Lemma 2.1 (hard-started rotor paths)

Fix $1\le Q<m$.  Suppose $T$ saturated radius-$Q$ state occurrences are
partitioned into $p$ directed rotor paths.  For signed depth
$-Q\le d\le Q$, let $\mathcal U_d$ be the support of the displayed
rank-$(m+d)$ masks, and put

\[
 H_d=\binom{2m}{m+d}-|\mathcal U_d|.
\]

Let

\[
 c_0=T-|\mathcal U_0|=T-(W-H_0).
\]

Then there is a literal word covering the entire controlled band with
length

\[
 \boxed{
 L_{\rm band}\le
 W+c_0+\sum_{\substack{-Q\le d\le Q\\d\ne0}}H_d+2Qp.}
                                                        \tag{2.1}
\]

### Proof

Write a state as

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),\qquad |L|=m-Q,
\]

with saturated flags

\[
 C_{-Q+h}(\omega)=L\cup\{z_1,\ldots,z_h\},
 \qquad 0\le h\le2Q.
\]

Hard-start a path at $\omega_0$ by the literal letters

\[
 \{z_{0,2Q}\},\ldots,\{z_{0,1}\},L_0.       \tag{2.2}
\]

The suffix of $h+1$ letters ending at $L_0$ has OR
$C_{-Q+h}(\omega_0)$.

The exact one-letter common-arrival cone is

\[
 C'_{-Q}=C_{-Q}-x+y,
 \qquad
 C'_d=C_{d-1}+y\quad(-Q<d\le Q),             \tag{2.3}
\]

where $x\in C_{-Q}$ and $y\notin C_Q$.  Put
$L'=C'_{-Q}=L-x+y$ and append $L'$ as one new letter.  The one-letter
suffix gives $C'_{-Q}$ itself.  For $1\le h\le2Q$, inductively the suffix
of $h$ old letters has OR $C_{-Q+h-1}$.  Therefore the suffix of $h+1$
letters ending at $L'$ has OR

\[
 L'\cup C_{-Q+h-1}
 =(L-x+y)\cup C_{-Q+h-1}
 =C_{-Q+h-1}+y=C'_{-Q+h}.
\]

Thus every successor state costs one new letter.  A path with $a$ states
costs exactly

\[
 (2Q+1)+(a-1)=a+2Q                         \tag{2.4}
\]

letters.  The total path cost is $T+2Qp$.  Append every missing band mask
as one literal letter.  Since $T+H_0=W+c_0$, (2.1) follows.  Intervals
crossing concatenation seams can only add witnesses.  $\square$

### Audit of the reset constant

The reset toll is $2Q$, not $2Q+1$.  The lower core $L_0$ in (2.2) is
already the first state occurrence.  This is the only endpoint convention
used below.

## 3. One packet is a literal cyclic erosion block

For one cyclic order $\pi$, put

\[
 E_j=I_\pi(j,m-Q).
\]

Consider the linear word

\[
 \mathcal E_Q(\pi)=
 E_0,E_1,\ldots,E_{2m-1},E_0,E_1,\ldots,E_{2Q-1}.
                                                        \tag{3.1}
\]

It has exact length $2m+2Q$.  For $0\le s\le2Q$,

\[
 E_j\cup E_{j+1}\cup\cdots\cup E_{j+s}
   =I_\pi(j,m-Q+s).                         \tag{3.2}
\]

The repeated prefix in (3.1) makes (3.2) an ordinary, noncircular
contiguous interval for every start $j$.  Thus (3.1) literally exposes both
members of every atom in $e_Q(\pi)$.  It is the direct erosion form of
Lemma 2.1 after cutting the $2m$-state rotor cycle once.

## 4. The single cyclic-interval near-design theorem

### Theorem 4.1 (exact sufficient lemma)

Let $Q=Q(m)<m$, and put

\[
 t=\left\lceil\frac{W}{2m}\right\rceil.
\]

Suppose there is a family $\Pi_m$ of $t$ directed cyclic orders satisfying

\[
 \boxed{
 \sum_{q=0}^{Q}h_q(\Pi_m)=o(W).}             \tag{SCIND}
\]

Then there is a literal word covering every mask of ranks
$m-Q,\ldots,m+Q$ and having length

\[
 \boxed{
 L_{\rm band}\le
 t(2m+2Q)+2\sum_{q=0}^{Q}h_q(\Pi_m).}         \tag{4.1}
\]

In particular, if $Q=o(m)$, then $L_{\rm band}=W+o(W)$.

If, in addition, the masks outside the controlled band admit a literal word
of length $o(W)$, then concatenation gives

\[
 \nu(2m)\le W+o(W).
\]

### Proof

Concatenate the $t$ erosion blocks (3.1).  Their total length is
$t(2m+2Q)$, and every atom met by a selected packet has both of its masks
covered literally.  For every missing atom append its two masks as two
one-letter repairs.  This proves (4.1).

Write $2mt=W+\delta_m$, where

\[
 0\le\delta_m<2m.
\]

Then

\[
 t(2m+2Q)
 =W+\delta_m+\frac Qm(W+\delta_m).
\]

For $Q=o(m)$, both $\delta_m=o(W)$ and
$Q(W+\delta_m)/m=o(W)$.  Condition (SCIND) finishes the band estimate.
The outer word can be concatenated because all of its witnesses remain
literal intervals inside that word.  $\square$

### Minimal path form

Full packets are convenient but not logically necessary.  For arbitrary
selected phase sets, Lemma 2.1 shows that the exact sufficient condition is

\[
 \boxed{
 c_0+\sum_{d\ne0}H_d+2Qp=o(W).}             \tag{4.2}
\]

This is the common-arrival version of (SCIND).  It already forces
$T\le W+o(W)$ because $c_0\ge T-W$.  Splicing can reduce $p$, but it
cannot change $T$, $c_0$, or any support $\mathcal U_d$.

For the full-cycle theorem, $p=t=O(W/m)$, so

\[
 2Qp=O(QW/m)=o(W).                            \tag{4.3}
\]

Consequently even perfect cross-packet synchronization could save only
$o(W)$ beyond (4.1).  The common-arrival cone solves chronology; it cannot
round the fractional incidence system.

## 5. Full multiplicity is the exact optimal fractional solution

### Proposition 5.1 (degrees and fractional optimum)

A fixed $r$-set is a cyclic interval in exactly

\[
 D_r=r!(2m-r)!                               \tag{5.1}
\]

directed cyclic orders modulo rotation.  Hence a depth-$q$ atom has degree

\[
 D_q=(m-q)!(m+q)!.                           \tag{5.2}
\]

Assign every packet the uniform weight

\[
 x_\pi=\frac1{(m!)^2}.                       \tag{5.3}
\]

Then the total packet mass is exactly

\[
 \sum_{\pi\in\Omega^+}x_\pi
 =\frac{(2m-1)!}{(m!)^2}
 =\frac W{2m}.                               \tag{5.4}
\]

Every owner atom has load one.  Every depth-$q$ atom has load

\[
 \lambda_q=\frac{D_q}{D_0}
 =\frac{(m-q)!(m+q)!}{(m!)^2}
 =\frac W{R_q}\ge1.                         \tag{5.5}
\]

Moreover, $W/(2m)$ is the minimum possible total mass of any fractional
packet cover of the owner atoms.

### Proof

Contract a prescribed $r$-set to one cyclic block.  Its internal order can
be chosen in $r!$ ways and the cyclic order of that block together with the
$2m-r$ outside labels in $(2m-r)!$ ways, proving (5.1).

Equations (5.2)--(5.5) follow by direct substitution and

\[
 W=\frac{(2m)!}{(m!)^2},\qquad
 R_q=\frac{(2m)!}{(m-q)!(m+q)!}.
\]

Finally, every packet contains exactly $m$ owner atoms.  Covering the
$W/2$ owner atoms fractionally therefore requires packet mass at least

\[
 \frac{W/2}{m}=\frac W{2m}.
\]

The uniform circulation attains equality.  $\square$

Passing from directed orders to static orders modulo reversal divides
$|\Omega^+|$, every degree, and every codegree by two.  It leaves the packet
itself, all normalized formulas, the total fractional mass, and every
literal compiler unchanged.  Thus no later factor of two depends on this
orientation convention.

The permutation-orbit circulation is therefore not merely approximately
balanced: after division by $(m!)^2$ it is the exact optimal fractional
solution.  The unresolved operation is an integral rounding to $t$ packets
with absolute aggregate hole count $o(W)$.

## 6. An exact quota formulation of the rounding gate

Let $t=\lceil W/(2m)\rceil$.  A selected family has total atom-occurrence
counts

\[
 s_0=mt,qquad s_q=2mt\quad(1\le q\le Q).     \tag{6.1}
\]

For every depth choose integer balanced quotas

\[
 b_q(v)\in
 \left\{
  \left\lfloor\frac{s_q}{|\mathcal V_q|}\right\rfloor,
  \left\lceil\frac{s_q}{|\mathcal V_q|}\right\rceil
 \right\},
 \qquad
 \sum_{v\in\mathcal V_q}b_q(v)=s_q.          \tag{6.2}
\]

Let $a_q(v)$ be the selected packet load of $v$ and put

\[
 V_q=\sum_{v\in\mathcal V_q}(a_q(v)-b_q(v))_+.
                                                        \tag{6.3}
\]

### Lemma 6.1 (quota rounding is sufficient)

For every $q$,

\[
 h_q\le V_q.                                  \tag{6.4}
\]

Consequently

\[
 \boxed{\sum_{q=0}^Q V_q=o(W)}                \tag{6.5}
\]

is a concrete integral sufficient condition for (SCIND).

### Proof

The selected loads and quotas have the same total, so

\[
 \sum_v(a_q(v)-b_q(v))_+
 =\sum_v(b_q(v)-a_q(v))_+.                    \tag{6.6}
\]

At depth zero, $mt\ge W/2=|\mathcal V_0|$.  At positive depth,
$2mt\ge W\ge R_q=|\mathcal V_q|$.  Thus every quota is at least one.
A hole $a_q(v)=0$ contributes at least one to the right side of (6.6),
proving (6.4).  $\square$

This condition is much stronger than correct rank marginals.  Since both
$2mt$ and $W$ are even, $\delta_m$ is even.  At owner depth, all but
$\delta_m/2$ atoms have quota one and $\delta_m/2$ have quota two.  At
depth one (for all sufficiently large $m$), all but

\[
 2mt-R_1=\frac W{m+1}+\delta_m                 \tag{6.7}
\]

atoms have quota one, and the displayed number have quota two.  Thus almost
every first-shadow atom must be hit exactly once.

There is also a floor-energy certificate.  Put

\[
 \alpha_q=\left\lfloor\frac{s_q}{|\mathcal V_q|}\right\rfloor,
 \qquad
 \Phi_q=\frac12\sum_{v\in\mathcal V_q}
 (a_q(v)-\alpha_q)(a_q(v)-\alpha_q-1).         \tag{6.8}
\]

Every summand is a nonnegative integer.  A hole contributes
$\binom{\alpha_q+1}{2}$, whence

\[
 h_q\le
 \frac{\Phi_q}{\binom{\alpha_q+1}{2}}.        \tag{6.9}
\]

Thus the explicit weighted aggregate condition

\[
 \boxed{
 \sum_{q=0}^Q
 \frac{\Phi_q}{\binom{\alpha_q+1}{2}}=o(W)}
                                                        \tag{6.10}
\]

would also prove (SCIND).  No such bound is proved here.

### Absolute versus relative leftover

The absolute scale in (SCIND) is essential.  If
$Q\ge\lfloor\sqrt m\rfloor$, then

\[
 |\mathcal V_0|+\sum_{q=1}^Q|\mathcal V_q|
 =\Theta(W\sqrt m).                           \tag{6.11}
\]

For the upper bound, use

\[
 \sum_{q=0}^{m}R_q=2^{2m-1}+\frac W2
 =\Theta(W\sqrt m).
\]

For the lower bound, when
$q\le\sqrt m/4$,

\[
 \frac{R_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
 =\prod_{i=0}^{q-1}
 \left(1-\frac{2i+1}{m+i+1}\right)
 \ge e^{-1/8}
\]

for all sufficiently large $m$, using
$\log(1-x)\ge-2x$ for $0\le x\le1/2$.
There are $\Theta(\sqrt m)$ such depths.  Therefore an ordinary
$o(1)$-fraction matching leftover is insufficient: the required leftover
fraction across the band is

\[
 o(W)/\Theta(W\sqrt m)=o(m^{-1/2}).           \tag{6.12}
\]

## 7. Independent normalization fails sharply

The exact fractional solution cannot be rounded by diffuse independent
packet choices.

### Theorem 7.1 (diffuse independent-thinning obstruction)

Choose each directed packet $\pi$ independently with probability $p_\pi$.
Assume

\[
 p_*:=\max_\pi p_\pi=o(1),
 \qquad
 \sum_\pi p_\pi\le(1+o(1))\frac W{2m}.        \tag{7.1}
\]

Let $H_0$ be the number of uncovered owner atoms.  Then

\[
 \mathbb E H_0\ge(e^{-1}-o(1))\frac W2,       \tag{7.2}
\]

\[
 \operatorname {Var}H_0=O(mW)=o(W^2),        \tag{7.3}
\]

and hence, with probability tending to one,

\[
 H_0=\Omega(W).                               \tag{7.4}
\]

In particular, this independent selection fails the packet-support
condition (SCIND), and the direct singleton repair used in Theorem 4.1 has
linear length.  This is not a lower bound against accidental cross-seam
coverage or against arbitrary literal words.

### Proof

For an owner atom $v$, let

\[
 \ell_v=\sum_{\pi\ni v}p_\pi.
\]

Since each packet contains $m$ owner atoms,

\[
 \frac2W\sum_{v\in\mathcal V_0}\ell_v
 =\frac{2m}{W}\sum_\pi p_\pi\le1+o(1).      \tag{7.5}
\]

For $0\le x\le p_*$,

\[
 \log(1-x)\ge-\frac{x}{1-p_*}.
\]

Therefore

\[
 \Pr(v\text{ is uncovered})
 =\prod_{\pi\ni v}(1-p_\pi)
 \ge\exp\!\left(-\frac{\ell_v}{1-p_*}\right).
\]

The exponential is convex.  Jensen's inequality and (7.5) prove (7.2).

Changing one Bernoulli packet coordinate can change $H_0$ by at most $m$.
Efron--Stein therefore gives

\[
 \operatorname {Var}H_0
 \le m^2\sum_\pi p_\pi(1-p_\pi)
 =O(mW),
\]

which is $o(W^2)$.  Chebyshev's inequality proves (7.4).  Every missing
atom consists of two packet-support holes, so the singleton repair in
Theorem 4.1 uses $2H_0$ letters.  $\square$

For exactly $t$ independent uniform packets chosen with replacement, the
same calculation is explicit:

\[
 \Pr(v\text{ is missed})
 =\left(1-\frac{2m}{W}\right)^t=e^{-1}+o(1).
                                                        \tag{7.6}
\]

Thus dependence is not a technical refinement; it is indispensable.

## 8. Exact packet codegrees

The incidence geometry is nevertheless favorable after complementary
quotienting.

### Lemma 8.1 (two-mask interval count)

Let $A,B\subset[2m]$ have sizes $1\le k,l\le2m-1$, and put
$a=|A\cap B|$,

\[
 h=\max(0,k+l-2m),\qquad u=\min(k,l).
\]

For distinct, noncomplementary masks, the number of directed cyclic orders
in which both are intervals is

\[
 N_{k,l}(a)\,a!(k-a)!(l-a)!(2m-k-l+a)!,       \tag{8.1}
\]

where

\[
 N_{k,l}(a)=
 \begin{cases}
  |2m-k-l|+1,&a=h,\\
  2,&h<a<u,\\
  |k-l|+1,&a=u,\\
  0,&\text{otherwise}.
 \end{cases}                                  \tag{8.2}
\]

### Proof

Anchor the unique start of $A$ in positions $1,\ldots,k$.  The possible
starts of an $l$-interval meeting those positions in exactly $a$ places are
counted by (8.2): two in a proper crossing, and the indicated number of
internal placements in a containment or disjoint endpoint case.  For each
start, the four Venn atoms can be ordered independently, giving the
factorials in (8.1).  $\square$

### Corollary 8.2 (band codegrees)

Let $q\ge r$, and let the lower representatives of two atoms have sizes
$m-q,m-r$ and intersection size $a$.  Normalizing their codegree by the
degree $D_r$ gives

\[
 \frac{\lambda_{q,r}(a)}{D_r}=
 \begin{cases}
  \dfrac{q+r+1}{\binom{m+r}{q+r}},&a=0,\\[7pt]
  \dfrac{2}{
     \binom{m-r}{a}\binom{m+r}{m-q-a}},
       &0<a<m-q,\\[9pt]
  \dfrac{q-r+1}{\binom{m-r}{q-r}},&a=m-q.
 \end{cases}                                  \tag{8.3}
\]

The exact maximum normalized codegree over distinct band atoms is

\[
 \boxed{\frac{2}{m-Q+1},}                     \tag{8.4}
\]

attained by a saturated nested pair at depths $Q,Q-1$.

At owner depth, distinct complementary atoms satisfy

\[
 \frac{\lambda_a}{D_0}
 =\frac{2}{\binom ma^2}\le\frac2{m^2}.       \tag{8.5}
\]

A prescribed saturated nested flag

\[
 A_0\subset A_1\subset\cdots\subset A_s
\]

with

\[
 0\le s\le2m-|A_0|-1
\]

has relative codegree

\[
 \frac{2^s}{(2m-|A_0|)_s}.                   \tag{8.6}
\]

Here $(x)_s=x(x-1)\cdots(x-s+1)$ is the falling factorial.  In a
radius-$Q$ band, $s\le2Q$ automatically lies in the displayed range because
$Q<m$.

### Proof

Equation (8.3) is (8.1) divided by $D_r$.  In either endpoint case the
ratio has the form

\[
 \frac{d+1}{\binom Kd},
 \qquad
 K-d+1=m-q+1\ge m-Q+1.
\]

For $1\le d\le K-1$,

\[
 \binom Kd\ge\frac{(d+1)(K-d+1)}2,
\]

so every endpoint ratio is at most $2/(m-Q+1)$.  In the proper-crossing
case both binomial factors are nontrivial; their product is at least
$m(m-Q)\ge m-Q+1$.  The owner-only value (8.5) is smaller.  Adjacent
containment with $q=Q,r=Q-1$ gives equality in (8.4).

At depth zero, the two orientations inside a complementary atom give
(8.5).  For (8.6), condition on $A_0$ being an interval.  Each prescribed
new label must be the next left or right endpoint; the $2^s$ choices are
disjoint.  $\square$

The relatively large value in (8.4) lies on one-dimensional nested spines,
and every additional prescribed spine step introduces another factor of
order $1/m$.

## 9. A full-band outside-edge link theorem

For a packet $e=e_Q(\pi)$ and an atom $v=[A]\notin e$ at depth $q$, choose
its lower representative and put

\[
 k=|A|=m-q,
 \qquad
 \Lambda_Q(e,v)=\frac1{D_q}\sum_{u\in e}\lambda(v,u).
                                                        \tag{9.1}
\]

This is a union-bound upper estimate for the probability that a uniformly
random packet through $v$ meets the fixed packet $e$ somewhere else.

### Theorem 9.1 (no $Q$ loss in outside-link spread)

If $Q\le m/8$ and $m$ is sufficiently large, then

\[
 \boxed{
 \Lambda_Q(e,v)
 \le \frac5k+\frac{10}{2m-k}
      +\frac{64m}{k(2m-k)}
 <\frac{90}{m-Q}.}                            \tag{9.2}
\]

### Proof

Enumerate the lower representatives of packet atoms as all intervals

\[
 B=I_\pi(j,m-r),\qquad 0\le r\le Q.
\]

At $r=0$ this counts each owner atom twice, so it can only enlarge the sum.
Condition on $A$ being an interval in a uniformly random packet through
$v$.  Since $v\notin e$, neither $A$ nor $A^c$ occurs in the enumeration.

If $B\subsetneq A$ and $d=k-|B|\ge1$, at most $d+1$ intervals of the fixed
order $\pi$ can occur: decompose $A$ into cyclic runs.  Each specified $B$
has conditional probability

\[
 \frac{d+1}{\binom{k}{d}}.
\]

This class contributes at most

\[
 \sum_{d=1}^{Q}\frac{(d+1)^2}{\binom{k}{d}}.  \tag{9.3}
\]

If $A\subsetneq B$, complementing reduces the same count to a subinterval
of $A^c$.  If $A\cap B=\varnothing$, write
$d=2m-k-|B|\ge1$.  These two classes together contribute at most

\[
 \sum_{d=1}^{Q}\frac{(d+1)^2}{\binom{2m-k}{d}}
 +\sum_{d=1}^{2Q}\frac{(d+1)^2}{\binom{2m-k}{d}}.       \tag{9.4}
\]

In every proper crossing put

\[
 a=|A\cap B|\in[1,k-1],
 \qquad b=|B\setminus A|\in[1,2m-k-1].
\]

Its exact conditional probability is

\[
 \frac{2}{\binom{k}{a}\binom{2m-k}{b}}.
\]

For fixed $(a,b)$, the order $\pi$ has at most $2m$ intervals of length
$a+b$.  Hence all crossings contribute at most

\[
 4m
 \left(\sum_{a=1}^{k-1}\binom{k}{a}^{-1}\right)
 \left(\sum_{b=1}^{2m-k-1}\binom{2m-k}{b}^{-1}\right)
 \le\frac{64m}{k(2m-k)},                     \tag{9.5}
\]

using

\[
 \sum_{i=1}^{K-1}\binom Ki^{-1}<\frac4K.
\]

For $K$ sufficiently large and $D\le K/4$,

\[
 \sum_{d=1}^{D}\frac{(d+1)^2}{\binom Kd}\le\frac5K.  \tag{9.6}
\]

Indeed, the $d=1$ term is $4/K$.  For
$t_d=(d+1)^2/\binom Kd$,

\[
 \frac{t_{d+1}}{t_d}
 =\frac{(d+2)^2}{(d+1)(K-d)}\le\frac12
\]

for $2\le d\le K/4$ and $K\ge27$, while
$2t_2=18/\binom K2\le1/K$ for sufficiently large $K$.

Here $Q\le m/8$ gives

\[
 Q\le k/4,\qquad 2Q\le(2m-k)/4.
\]

Apply (9.6) to (9.3)--(9.4), then add (9.5).  Since
$k,2m-k\ge m-Q$ and $m/(m-Q)\le8/7$, the resulting expression is less
than $90/(m-Q)$.  $\square$

The theorem is compatible with huge edge-edge overlap.  Swapping two
adjacent labels in a cyclic order changes exactly one owner atom and two
atoms at each positive depth.  The two packets therefore overlap in

\[
 m+2mQ-(2Q+1)                              \tag{9.7}
\]

atoms.  A useful rounding theorem must exploit the outside-edge spread
(9.2), not a bounded edge-intersection hypothesis.

## 10. The exact odd-factor semicircle thinning

The full-cycle near-design remains open, but the frozen exact odd wreath
factor gives a genuine one-$W$-scale partial-cycle selection.

Let $\mathcal F$ be an exact wreath factor on
$[2m]\cup\{\infty\}$.  Its number of rows is

\[
 B_o=\frac{\binom{2m+1}{m}}{2m+1}
    =\frac W{m+1}.                              \tag{10.1}
\]

For each row $v$, take its associated cyclic-interval order
$\widehat\pi_v$, namely the order whose length-$m$ cyclic windows are the
middle vertices of that wreath.  (If the row is presented by its
omitted-edge word, this is the audited doubled-index order.)  Rotate it so
that it is

\[
 (\infty,a_0,\ldots,a_{2m-1}),
\]

and let $\pi_v=(a_0,\ldots,a_{2m-1})$ be the order obtained by deleting
$\infty$.  Choose
the phase origin so that

\[
 J_v^0=\{0,1,\ldots,m\}                       \tag{10.2}
\]

is exactly the inclusive semicircle whose odd $m$-windows avoid
$\infty$.  Put

\[
 J_v^1=J_v^0+m\pmod {2m}.                     \tag{10.3}
\]

The two semicircles have $m+1$ starts and share their two antipodal
endpoints.

### Lemma 10.1 (the complement-pair row graph)

For every even middle mask $X$, let $f_X$ be the unique factor row whose
canonical semicircle $J^0$ contains $X$.  For every complementary atom
$[X]=\{X,X^c\}$, either

1. $f_X=f_{X^c}$, in which case $[X]$ is the unique private endpoint pair
   of that row; or
2. $f_X\ne f_{X^c}$, in which case $[X]$ gives an edge between those two
   rows.

The nonprivate atoms form an $(m-1)$-regular multigraph $G$ on
$\mathcal F$.

### Proof

The odd factor partitions all middle masks not containing $\infty$, so
$f_X$ is unique.  Within one projected row, $J^0$ and $J^1$ share exactly
the two masks of one complementary endpoint atom.  The remaining $m-1$
canonical masks have their complements in the opposite semicircle and in
the canonical semicircle of their unique other rows.  Thus every row has
one private atom and $m-1$ nonprivate incidences.  $\square$

For $S\subseteq\mathcal F$, select $J_v^1$ on rows $v\in S$ and $J_v^0$
on rows $v\notin S$.

### Lemma 10.2 (exact middle switching ledger)

The selection consists of exactly $W$ state occurrences in $B_o$ phase
paths, and

\[
 \boxed{H_0(S)=c_0(S)=|\delta_G(S)|.}          \tag{10.4}
\]

Here $H_0(S)$ counts missing middle masks, not atoms.

### Proof

There are $(m+1)B_o=W$ selected occurrences.  At $S=\varnothing$, the
factor property says that the canonical semicircles partition all $W$ even
middle masks.

A private pair lies at both endpoints and is unchanged by a switch.  On a
nonloop edge, the two canonical endpoint rows select opposite masks of its
complementary pair.  Switching exactly one endpoint makes both rows select
the same mask: the other mask is missing and the selected mask has one
extra occurrence.  Switching neither or both preserves one occurrence of
each.  Hence each cut edge contributes exactly one hole and exactly one
excess occurrence, with no factor two.  $\square$

## 11. The direct and shifted-dual vertical charts

For $-Q\le d\le Q$, define the saturated column

\[
 C_{v,t}(d)=I_{\pi_v}(t,m+d).                  \tag{11.1}
\]

Traverse each selected semicircle in decreasing $t$.  If
$y=a_{t-1}$ and $x=a_{t+m-Q-1}$, then

\[
 C_{v,t-1}(-Q)=C_{v,t}(-Q)-x+y,
\]

and, for $d>-Q$,

\[
 C_{v,t-1}(d)=C_{v,t}(d-1)+y.                 \tag{11.2}
\]

Thus every semicircle is an exact common-arrival rotor path.

For $1\le q\le Q$, define the direct lower support

\[
\begin{aligned}
 A_q(S)={}&
 \bigcup_{v\notin S}
  \{I_{\pi_v}(t,m-q):t\in J_v^0\}\\
 &\cup
 \bigcup_{v\in S}
  \{I_{\pi_v}(t,m-q):t\in J_v^1\},
\end{aligned}                                      \tag{11.3}
\]

and the shifted-dual lower support

\[
\begin{aligned}
 B_q(S)={}&
 \bigcup_{v\notin S}
  \{I_{\pi_v}(t+q,m-q):t\in J_v^1\}\\
 &\cup
 \bigcup_{v\in S}
  \{I_{\pi_v}(t+q,m-q):t\in J_v^0\}.
\end{aligned}                                      \tag{11.4}
\]

The identity

\[
 [2m]\setminus I_{\pi_v}(t,m+q)
 =I_{\pi_v}(t+m+q,m-q)                       \tag{11.5}
\]

and $J_v^0+m=J_v^1$ show that $A_q(S)$ is exactly the selected lower
support, while $B_q(S)$ is the complement-image of the selected upper
support.

Define the exact chart defect

\[
\boxed{
 D_Q(S)=|\delta_G(S)|
 +\sum_{q=1}^{Q}
 \left[(R_q-|A_q(S)|)+(R_q-|B_q(S)|)\right].} \tag{11.6}
\]

### Theorem 11.1 (semicircle near-design compiler)

If, for some $S\subseteq\mathcal F$,

\[
 D_Q(S)=o(W),                                  \tag{11.7}
\]

then the selected semicircles and literal hole repairs give a band word of
exact safe length

\[
 \boxed{
 L_{\rm band}\le
 W+2Q\frac W{m+1}+D_Q(S).}                    \tag{11.8}
\]

In particular, (11.7) and $Q=o(m)$ imply $L_{\rm band}=W+o(W)$.

### Proof

Lemma 10.2 gives $T=W$, $p=B_o$, and middle excess
$c_0=|\delta_G(S)|$.  Equations (11.3)--(11.5) give the exact lower and
upper hole counts.  Substitute them in Lemma 2.1.  The path reset cost is
$2QB_o$, proving (11.8).  $\square$

For the canonical choice $S=\varnothing$, write the selected middle states
of one row in path order as $X_0,\ldots,X_m$.  Its $m$ internal upper flags
include

\[
 Y_i=X_i\cup X_{i+1}\qquad(0\le i<m).
\]

The complementary odd vertices in that factor row are
$([2m]\setminus Y_i)\cup\{\infty\}$.  Since the odd factor partitions all
vertices containing $\infty$, the sets $Y_i$ over all rows partition
$\binom{[2m]}{m+1}$.  The one additional boundary upper occurrence in
each selected semicircle may duplicate this support, but creates no hole.
Consequently

\[
 B_1(\varnothing)=\binom{[2m]}{m-1}.           \tag{11.9}
\]

Thus the middle row is an exact occurrence partition, while the selected
upper depth-one support is hole-free (not an occurrence partition).  The
direct lower chart and the deeper paired charts are the remaining incidence
problem.

## 12. A sharp conditional obstruction to row switching

Put

\[
 d_q(S)=2R_q-|A_q(S)|-|B_q(S)|.               \tag{12.1}
\]

### Lemma 12.1 (switch Lipschitz bound)

For all $S,T\subseteq\mathcal F$,

\[
 \boxed{
 |d_q(S)-d_q(T)|
 \le2(m-1)|S\triangle T|.}                    \tag{12.2}
\]

### Proof

Switching one row retains the two endpoint phases and replaces exactly
$m-1$ interior occurrences in each of the two charts.  Replacing $m-1$
occurrences can change the support size of one chart by at most $m-1$.
Sum the two chart changes and telescope over $S\triangle T$.  $\square$

### Corollary 12.2 (expanding-row obstruction)

Suppose that, for some fixed $c,\kappa>0$ and some depth $q$,

\[
 d_q(\varnothing)\ge cW,
 \qquad d_q(\mathcal F)\ge cW,                \tag{12.3}
\]

and the row multigraph obeys

\[
 |\delta_G(S)|
 \ge\kappa(m-1)
 \min\{|S|,|\mathcal F\setminus S|\}         \tag{12.4}
\]

for every $S$.  Then no $S$ satisfies $D_Q(S)=o(W)$.

### Proof

If $d_q(S)=o(W)$, (12.2), (12.3), and
$W=(m+1)|\mathcal F|$ imply, for all sufficiently large $m$,

\[
 |S|\ge\frac c3|\mathcal F|,
 \qquad
 |\mathcal F\setminus S|\ge\frac c3|\mathcal F|.
\]

Equation (12.4) then gives

\[
 |\delta_G(S)|
 \ge\frac{\kappa c}{3}(m-1)|\mathcal F|
 =\Omega(W).
\]

This term is part of $D_Q(S)$, a contradiction.  $\square$

This is conditional: no expansion assertion for the particular frozen
factor graph is imported.  It proves that, on an expanding row graph, a
linear defect in both constant semicircle charts cannot be repaired by
local row switches without creating a linear middle defect.

## 13. Precise proved and unproved boundary

The following statements are proved.

1.  Every selected $2m$-cycle is a literal radius-$Q$ rotor cycle, and one
    cut costs exactly $2Q$ letters.
2.  (SCIND) is sufficient, with the exact length (4.1).
3.  The full multiplicity circulation is the exact optimal fractional
    solution.
4.  Diffuse independent thinning at optimal mass has a linear owner-hole
    defect with high probability.
5.  The quotient packet hypergraph has exact codegrees (8.3)--(8.6) and
    the full-band outside-link bound (9.2), with no factor $Q$.
6.  The exact odd factor has an integral $W$-state semicircle thinning with
    the exact two-chart defect (11.6) and word length (11.8).

The following lemma is **unproved**:

> **Single cyclic-interval near-design lemma.**  For some growing
> $Q=o(m)$ compatible with an $o(W)$ outer-tail compiler, there are
> $\lceil W/(2m)\rceil$ cyclic packets with
> $\sum_{q=0}^Q h_q=o(W)$.

The following alternative odd-factor chart statement is also **unproved**:

> There is a switch set $S\subseteq\mathcal F$ for which
> $D_Q(S)=o(W)$.

No standard fractional-to-integral division has been supplied.  The exact
fractional optimum, favorable owner codegrees, and the outside-edge spread
do not by themselves imply the required absolute $o(W)$ leftover in this
growing-uniformity regime.  Conversely, no invariant or unconditional
obstruction to (SCIND) is proved here.  The lane ends at a genuine integral
near-design/absorption theorem.

## 14. Independent audit checklist

The decisive constants and scopes were checked independently.

1.  The erosion block repeats exactly $2Q$ lower cores, so its length is
    $2m+2Q$.
2.  A hard-started path with $a$ states costs $a+2Q$, not $a+2Q+1$.
3.  At positive depth, one missing complementary atom requires two literal
    masks; the same is true at depth zero.  This gives the factor two in
    (4.1).
4.  In the semicircle switch ledger a cut edge creates one missing middle
    mask and one duplicate middle occurrence, not two.  Hence
    $H_0=c_0=|\delta_G(S)|$.
5.  Cross-packet common-arrival splicing affects only $p$.  Since the
    unspliced full-cycle toll is already $O(QW/m)=o(W)$, it cannot repair
    vertical support.
6.  The outside-link crossing term is
    $64m/[k(2m-k)]$, and the three endpoint classes contribute
    $5/k+10/(2m-k)$.  Under $Q\le m/8$ their sum is strictly less than
    $90/(m-Q)$ for sufficiently large $m$.
7.  The expansion obstruction in Corollary 12.2 is conditional; expansion
    of the actual row graph is not asserted.
