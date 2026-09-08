# Literal parent-aligned `D_4` packets: exact supply constants and the root-density gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(C_t=\operatorname {Cat}_t\), put

\[
                         C_r=\theta p,qquad4\le\theta<16,
\tag{0.1}
\]

and write the certified fatal demand in one aligned size-\(r\) context as

\[
 \boxed{
 D_r(\theta)=C_r\left({1\over2}-{1\over\theta}\right)
                  =C_r{\theta-2\over2\theta}.}
\tag{0.2}
\]

Without an operadically dense suspension, a literal size-four packet can
meet the left boundary in at most \(C_{r-4}\) common contexts and the right
boundary in at most another \(C_{r-4}\).  The two banks overlap.  For every
middle filling \(R\in\mathcal D_{r-8}\), the fourteen left packets and
fourteen right packets form a \(K_{14,14}\) row-conflict component.  Hence
the maximum number of pairwise row-disjoint literal boundary packets is

\[
 \boxed{N_r=2C_{r-4}-14C_{r-8}.}
\tag{0.3}
\]

If one packet could contribute \(B\) perfectly signed useful units at the
serviced depth, its absolute best supply/demand ratio would be

\[
 \boxed{
 \mathcal R_B(r,\theta)
 ={B(2C_{r-4}-14C_{r-8})
       \over C_r(1/2-1/\theta)}.}
\tag{0.4}
\]

Since

\[
 {C_{r-4}\over C_r}\longrightarrow{1\over256},
 \qquad
 {C_{r-8}\over C_r}\longrightarrow{1\over65536},
\tag{0.5}
\]

one has

\[
 \boxed{
 \mathcal R_B(r,\theta)\longrightarrow
       {249B\theta\over16384(\theta-2)}.}
\tag{0.6}
\]

The limiting endpoint values are

\[
\begin{array}{c|c|c}
B&\theta=4&\theta\uparrow16\\ \hline
6&1494/8192=0.1824&1494/14336=0.1042\\
19&4731/8192=0.5775&4731/14336=0.3300\\
22&5478/8192=0.6687&5478/14336=0.3821\\
60&14940/8192=1.8237&14940/14336=1.0421.
\end{array}
\tag{0.7}
\]

Therefore:

1. the marked six-unit bridge is short by factors between \(5.48\) and
   \(9.59\);
2. even the complete uniform-carrier aggregate profiles of positive mass
   \(19\) or \(22\) are short at every \(4\le\theta<16\), under perfect
   signs and with no background loss;
3. only the start-resolved triangle-inequality envelope \(B=60\) exceeds
   the fatal demand.  Near \(\theta=16\) its margin is only \(4.21\%\).

The lower/upper profiles cannot be added.  Lengths \(2,7\) are
complementary copies of the same nineteen-unit packet profile, and lengths
\(3,6\) are complementary copies of the same twenty-two-unit profile.  A
single factor state and a single serviced depth choose one member of this
coupled family.  Likewise \(60\) is a start-resolved envelope at one local
length, not an additional budget on top of \(19\) or \(22\), and not a
separate lower-plus-upper supply.

Thus the constants prove a genuine no-go for every argument based on the
marked or aggregate carrier profiles.  They do **not**, by themselves,
prove that root-dense suspension is logically necessary: with completely
separated start carriers, perfectly favourable residual capacities, nearly
disjoint left/right banks, and almost lossless simultaneous signs, the
sixty-unit envelope is numerically large enough.  At the hardest overshoot,
it must retain at least

\[
                         {14336\over14940}=0.9596
\tag{0.8}
\]

of its formal value after every carrier collision, background saturation,
left/right incompatibility, and lower/upper sign conflict.  No theorem in
the current library supplies that \(95.96\%\) efficiency.

Accordingly the rigorous decision is:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
Root-dense suspension is mathematically necessary for the certified
six-unit and aggregate-profile routes.  It is not forced by scalar constants
alone if all sixty start-resolved units are allowed to be perfectly useful.
Closing the latter loophole requires a new inequality showing usable descent
per literal packet is below the critical value in (6.2), or an unavoidable
loss exceeding (4.21\%\) near \(\theta=16\).
\end{minipage}}
\tag{0.9}
\]

Full physical backgrounds can only decrease these optimistic ratios.

## 1. Exact left/right packet overlap

A literal left-boundary packet is indexed by a suffix
\(B\in\mathcal D_{r-4}\) and has the fourteen roots

\[
                         \{TB:T\in\mathcal D_4\}.
\tag{1.1}
\]

A literal right-boundary packet is indexed by a prefix
\(A\in\mathcal D_{r-4}\) and has roots

\[
                         \{AT:T\in\mathcal D_4\}.
\tag{1.2}
\]

The two packets meet precisely on a root

\[
                              T_iRT_j,
\tag{1.3}
\]

where \(T_i,T_j\in\mathcal D_4\) and
\(R\in\mathcal D_{r-8}\).  For a fixed \(R\), the overlapping left
packets are indexed by \(RT_j\), \(1\le j\le14\), and the overlapping
right packets by \(T_iR\), \(1\le i\le14\).  Every left packet meets every
right packet in the unique row (1.3).  Thus the row-conflict graph on this
sector is \(K_{14,14}\).

Different middle fillings \(R\) give disjoint conflict components.  A
row-disjoint choice takes at most fourteen vertices from each \(K_{14,14}\),
and this is attained by taking either complete shore.  Starting from the
formal \(2C_{r-4}\) packets, one therefore loses exactly fourteen packets
for every \(R\), proving (0.3).

This is the optimistic independent-packet count.  If overlapping left and
right substitutions can be combined into a separately proved joint atom,
its effect must be recomputed and cannot be credited as two independent
copies of the old budget.

## 2. Exact Catalan normalization

Repeated use of

\[
                         {C_{t-1}\over C_t}
                         ={t+1\over2(2t-1)}
\tag{2.1}
\]

gives

\[
 \boxed{
 {C_{r-4}\over C_r}
 ={(r+1)r(r-1)(r-2)
 \over16(2r-1)(2r-3)(2r-5)(2r-7)}.}
\tag{2.2}
\]

Likewise

\[
 \boxed{
 {C_{r-8}\over C_r}
 ={(r+1)r(r-1)(r-2)(r-3)(r-4)(r-5)(r-6)
 \over256\prod_{j=0}^{7}(2r-(2j+1))}.}
\tag{2.3}
\]

Equations (2.2)--(2.3) imply (0.5).  Dividing the optimistic supply
\(BN_r\) by (0.2) proves (0.4), and taking the limit gives

\[
\begin{aligned}
 \lim_{r\to\infty}{N_r\over C_r}
 &=2\cdot{1\over256}-14\cdot{1\over65536}\\
 &={249\over32768}.
\end{aligned}
\tag{2.4}
\]

Multiplication by \(2\theta/(\theta-2)\) proves (0.6).

## 3. The three packet budgets

For the certified canonical/new \(D_4\) factor pair, three different
numbers occur and must not be conflated.

### 3.1 Marked boundary budget

The six open-parent singleton starts have signed profile

\[
                         d=2e_2-3e_3-3e_6+4e_7,
\tag{3.1}
\]

whose positive and negative masses are six.  Thus no residual-capacity
state can extract more than six units of descent from this marked profile.
Taking \(B=6\) in (0.4) gives the first row of (0.7).

### 3.2 Uniform-carrier aggregate budgets

For all nine starts with one common carrier, the first nonzero lower target
profiles have masses

\[
                  {1\over2}\|\Delta_2\|_1=19,
 \qquad           {1\over2}\|\Delta_3\|_1=22.
\tag{3.2}
\]

Their complements have the same masses at lengths seven and six.  The
hinge is one-Lipschitz in positive mass, so even a perfectly placed profile
can lower cap overload by at most nineteen or twenty-two.  The middle rows
of (0.7) show that neither budget reaches the fatal demand.

### 3.3 Start-resolved envelope

Before equal physical targets at different cyclic starts are aggregated,
the largest sum of startwise positive masses at one local length is

\[
                              60.
\tag{3.3}
\]

This is only an envelope.  It becomes usable descent only if the negative
start arms lie on overloaded physical targets, the positive arms lie in
residual capacity, and carrier collisions do not restore the cancellations
which reduce sixty to nineteen or twenty-two.  Nevertheless, granting all
of those properties gives the last row of (0.7), so constants alone do not
eliminate this extreme scenario.

## 4. Lower and upper shadows are coupled

For the local nine-cycle, complementation gives

\[
 \Delta_{9-\ell,j+\ell}(J\setminus S)
                              =\Delta_{\ell,j}(S).
\tag{4.1}
\]

Hence \((\ell,9-\ell)=(2,7)\) and \((3,6)\) are not four independent
profiles.  They are two complementary pairs generated by the same factor
choice.  At one protected depth the local intersection size fixes \(\ell\),
so only the corresponding profile is available.  If lower and upper shadow
constraints are imposed simultaneously, the same packet orientation must
serve both; multiplying their marginal capacities is forbidden without a
joint residual-background theorem.

In particular neither

\[
                         19+22,qquad2(19+22),
\tag{4.2}
\]

nor \(2\cdot60\) is a valid per-depth packet budget.  The factor two for
the two physical boundaries has already been included in \(N_r\).

## 5. Background and carrier losses

For a physical old profile \(u\), signed packet direction \(D\), and true
residual capacity \(c=(p-\beta)_+\), the exact descent is

\[
 \mathscr D_c(D;u)
 =\sum_S\left[(u(S)-c(S))_+
              -(u(S)+D(S)-c(S))_+\right].
\tag{5.1}
\]

The universal bound

\[
                         |\mathscr D_c(D;u)|
                         \le\sum_S(D(S))_+
\tag{5.2}
\]

is the only input used in (0.4).  Equality requires every negative unit to
remove existing overflow and every positive unit to fit in spare residual
capacity.  Any pre-existing background at a destination, collision between
contexts, or incompatible sign forced by another protected depth lowers the
effective \(B\).

If only a fraction \(\eta\) of the formal packet budget is useful, the
asymptotic closure condition is

\[
 \boxed{
 \eta B\ge B_{\rm crit}(\theta)
 :={16384(\theta-2)\over249\theta}.}
\tag{5.3}
\]

The critical value increases from

\[
                  B_{\rm crit}(4)={8192\over249}=32.90
\quad\hbox{to}\quad
                  B_{\rm crit}(16)={14336\over249}=57.57.
\tag{5.4}
\]

Thus \(B\le22\) fails even with \(\eta=1\).  For \(B=60\), the required
efficiency tends to

\[
                         {14336\over14940}=0.9596
\tag{5.5}
\]

at the hard end of the overshoot interval.

## 6. Root-density decision

The constant audit separates a proved no-go from an open loophole.

### Theorem 6.1 (certified-profile no-go)

No literal parent-aligned \(D_4\) architecture with at most
\(C_{r-4}\) packets per boundary can meet the fatal demand using only

1. the six-unit marked profile, or
2. either uniform-carrier aggregate profile of mass nineteen or twenty-two,

even if all packets have perfect signs, the residual destinations are
empty, and every allowable left/right packet is row-disjoint.

#### Proof

The corresponding ratios in (0.7) are strictly below one throughout
\(4\le\theta<16\). \(\square\)

This proves that an operadically root-dense suspension, or a new atom with a
larger useful profile, is necessary for every presently certified routing
argument.

### Exact unresolved inequality

To prove root-dense suspension mathematically necessary without
qualification, it remains to show that every legal literal packet family
satisfies, at some protected depth or complementary lower/upper pair,

\[
 \boxed{
 \sum_{\text{selected packets}}
       \mathscr D_{c_q}(D_{C,q};u_{C,q})
 <D_r(\theta),}
\tag{6.1}
\]

or, sufficient at the one-packet level, that its uniformly usable descent
obeys

\[
 \boxed{
                         B_{\rm usable}
        <{16384(\theta-2)\over249\theta}.}
\tag{6.2}
\]

Near \(\theta=16\), it is enough to prove
\(B_{\rm usable}<57.57\), or any unavoidable loss of more than \(4.04\%\)
from the formal sixty-unit start-resolved envelope.  The current
carrier/background theorems do not yet prove this.  Therefore the strongest
rigorous conclusion is the qualified one in (0.9), rather than an
unconditional root-density no-go.
