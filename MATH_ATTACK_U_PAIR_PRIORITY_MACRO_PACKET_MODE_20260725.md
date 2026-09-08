# Lane U: pair-priority cubes and equal-radius FIFO macro-packets

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, or solver is used.

## 0. Outcome

The adjacent-priority cube has a larger integral refinement than previously
recorded.  Under the natural pair-symmetric choice of local factors, every
affected lower target may choose its old or swapped token independently;
every corner remains lower-saturating and middle-simple.  This gives an
exact orbitwise minimizer for one complete \(\tau\)-odd upper-rank energy
mode.

At upper depth \(q=1\), the number of tokens on which that minimizer can
differ from an endpoint cube corner is at most \(4\operatorname{Cat}_{m-1}\).
Consequently the minimizing corner is still a literal union of tight FIFO
runs with total initialization cost \(o(W)\) throughout the Gaussian band.
This is an unconditional integral contraction of the **variable
\(\tau\)-odd part** of one rank mode to its exact lattice minimum.  The
\(\tau\)-even orbit totals are invariant and may still have linear defect.

At an arbitrary single Gaussian depth
\(q=\lfloor\gamma\sqrt m\rfloor\), exact lattice minimization can be
replaced by a stronger physical statement.  The nonfixed tokens split into
at most \(2\operatorname{Cat}_{m-1}\) cyclic collar components.  Subdivide
them into proportional equal-radius blocks of length \(a_q\) as defined in
Corollary 4.3, with one short remainder
per component.  There are only \(O(p)\) blocks.  Independent block signs
have exact variance at most \((q+1)\operatorname{Cat}_{m-1}=o(W)\), so a
deterministic integral corner attains the complete rank-\(q\) energy of the
half-swapped midpoint up to \(o(W)\), with literal Gaussian initialization
cost \(o(W)\).  The midpoint itself is not proved floor-balanced, and the
corner depends on \(q\); hence this is one full Gaussian-mode contraction,
not a simultaneous-band theorem.

For packet-constant choices across a whole radius-\(d\) class, the exact
remaining condition is a signed two-fibre graph.  A balanced signed graph
(in particular, a forest) has an explicit integral signing attaining the
parity-minimal \(\tau\)-odd energy simultaneously at every upper depth
\(1,\ldots,d+1\).  If the packet dictionary is target-simple under that
signing, one Gaussian radius class containing \(\Theta(W)\) flag incidences
is realized literally at cost \(o(W)\).  Existence of such a balanced
global dictionary is not proved here.

The physical bundling part can nevertheless be completed for one full
Gaussian radius.  Exactly \(p\) length-\(a_d\) packets can be placed in
\(\Theta_\gamma(R_m)=\Theta(W/m)\) terminal row blocks, one common cube
sign per block.  Their fresh-run overhead is \(O(R_md)=O(W/\sqrt m)\), and
they retain \(\Omega_\gamma(W)\) genuinely nonfixed flag incidences.  This
is an unconditional integral FIFO macro-packet theorem.  It does not force
the row collision graph to be bipartite.  Even before parity, q1 simplicity
requires at least

\[
 pa_d-3R_m
 =\left(2\gamma e^{-\gamma^2}+o(1)\right)W/\sqrt m
\]

distinct \(\tau\)-fixed canonical q1 targets; the local-factor axioms alone
only guarantee \(\Theta(W/m)\).  This is an exact fixed-support gate which
no signing can repair.

There is also a sharp FIFO splice theorem.  A carrier change after a
radius-\(d\) packet requires \(d+1\) undesignated starts in the worst case.
The one-spacer architecture from
`MATH_ATTACK_U_COLUMN_CORRELATED_NIBBLE_AUDIT_20260725.md` therefore lifts
the priority cube uniformly by this worst-case protected-splice mechanism
for radius \(0\).  Exactly

\[
 a_0=1
\]

for all sufficiently large \(m\), so this radius-zero/q1 special case is
literal and exact.  Repeating fresh starts or deep buffers independently
over all radius classes costs too much.  Thus constant one remains open.

## 1. Pair-symmetric adjacent swap

Put

\[
 n=2m+1,\qquad W=\binom nm.
\]

Let \(A,B\) be two disjoint coordinate pairs occupying adjacent positions
in a first-avoided priority order.  Put

\[
 R=[n]\setminus(A\cup B),
\]

and let \(\tau\) interchange \(A\) and \(B\) coordinatewise while fixing
\(R\) pointwise.  Choose an exact local row factor \(F_A\) on
\(Q_A=[n]\setminus A\), and choose

\[
 F_B=\tau F_A
\tag{1.1}
\]

on \(Q_B=[n]\setminus B\).

Let \(D\) be the lower targets affected by interchanging \(A,B\):

\[
 D=\left\{S\in\binom{[n]}{m-1}:
 S\cap A=S\cap B=\varnothing,
 \quad S\text{ meets every earlier priority pair}\right\}.
\tag{1.2}
\]

For \(S\in D\), let \(e_0(S)\) be its selected \(F_A\)-token and let
\(e_1(S)=\tau e_0(S)\) be its \(F_B\)-token.  Write their middle owners as

\[
 Y_0(S)=Y(S),\qquad Y_1(S)=\tau Y(S).
\tag{1.3}
\]

For every signed flag depth for which the token is defined,

\[
 \boxed{
 L_r(e_1(S))=L_r(e_0(S)),
 \qquad
 U_r(e_1(S))=\tau U_r(e_0(S)).}
\tag{1.4}
\]

Indeed every lower flag is a subset of \(S\subseteq R\), while the entire
new row is the \(\tau\)-image of the old row.

## 2. The cube refines to independent target bits

### Theorem 2.1 (independent-target priority cube)

For every function

\[
 \epsilon:D\longrightarrow\{0,1\},
\]

replace \(e_0(S)\) by \(e_{\epsilon(S)}(S)\), while retaining every token
outside \(D\).  The resulting token set \(M_\epsilon\) is an exact
lower-saturating, middle-simple matching.

Thus pair symmetry refines the one-bit adjacent-priority swap to a
\(2^{|D|}\)-corner integral cube.

#### Proof

Every lower target is unchanged and still has exactly one token.  The old
owner map \(Y:D\to\binom{[n]}m\) is injective, and so is \(\tau Y\).  It
remains to exclude a mixed collision.  Suppose

\[
 Y(S)=\tau Y(T).
\tag{2.1}
\]

The left side avoids \(A\), since it belongs to \(F_A\); the right side
avoids \(B\), since it belongs to \(F_B\).  Their common value therefore
avoids \(A\cup B\), hence is fixed by \(\tau\).  Applying \(\tau\) to
(2.1) gives

\[
 Y(T)=Y(S).
\]

Injectivity of the old owner map gives \(T=S\).  This is not a collision
between two selected tokens, because each lower target chooses only one of
its alternatives.

Finally, a token outside \(D\) is disjoint from every old alternative
because the all-old priority state is a matching, and from every new
alternative because the all-new priority state is a matching. \(\square\)

### Corollary 2.2 (exact mode support)

Every lower flag mode is pointwise invariant on the cube.  At upper depth
\(q\), the entire varying load lies in the \(\tau\)-odd subspace

\[
 P_-f=\frac12(f-\tau f).
\tag{2.2}
\]

The \(\tau\)-even projection and every \(\tau\)-orbit total are fixed.

## 3. Exact integral contraction of one upper-rank mode

Freeze a depth \(q\ge1\), and freeze the loads of all tokens outside
\(D\).  Let \(c_T\) denote that fixed load at an upper target \(T\).
The forced uniform mean \(\lambda_q\) is \(\tau\)-invariant.

For a nonfixed orbit

\[
 O=\{T,\tau T\},
\]

choose \(T\) to be the member which can occur as an old \(F_A\)-flag, and
let \(k_O\) be the number of variable tokens whose old upper flag is
\(T\).  If \(x\) of them choose state zero, the two final loads are

\[
 c_T+x,\qquad c_{\tau T}+k_O-x.
\tag{3.1}
\]

This representative is well defined: an old flag avoids \(A\).  If both
members of its \(\tau\)-orbit avoided \(A\), the old flag would avoid
\(A\cup B\) and the orbit would be fixed.

### Theorem 3.1 (orbitwise lattice minimizer)

There is an explicit integral cube corner which minimizes the complete
rank-\(q\) squared energy over the whole independent-target cube.  On each
nonfixed orbit choose

\[
 \boxed{
 x_O\in\operatorname*{argmin}_{0\le x\le k_O,\ x\in\mathbb Z}
 \left[(c_T+x-\lambda_q)^2+
 (c_{\tau T}+k_O-x-\lambda_q)^2\right].}
\tag{3.2}
\]

Equivalently, \(x_O\) is an integer in \([0,k_O]\) nearest

\[
 \frac{k_O+c_{\tau T}-c_T}{2}.
\tag{3.3}
\]

The residual odd discrepancy is exactly

\[
 \delta_O=\min_{0\le x\le k_O}
 |c_T-c_{\tau T}+2x-k_O|,
\tag{3.4}
\]

and obeys

\[
 \boxed{
 \delta_O\le
 1+\bigl(|c_T-c_{\tau T}|-k_O\bigr)_+.}
\tag{3.5}
\]

This minimizes the full varying \(\tau\)-odd mode, not merely one scalar
projection.

#### Proof

The sum of the two loads in (3.1) is fixed.  Hence their \(\tau\)-even
part is independent of \(x\), and the energy varies only with the square of
their difference

\[
 c_T-c_{\tau T}+2x-k_O.
\]

The allowable differences form the consecutive parity lattice from
\(c_T-c_{\tau T}-k_O\) to
\(c_T-c_{\tau T}+k_O\).  The nearest point to zero gives
(3.2)--(3.5).  Different target orbits use disjoint token variables, so the
orbit minimizers combine.  Theorem 2.1 makes the combined choice an
integral matching. \(\square\)

### Proposition 3.2 (exact target-simplicity criterion)

On the orbit \(O\), a choice with both final target loads at most one exists
if and only if

\[
 \boxed{
 c_T\le1,\qquad c_{\tau T}\le1,\qquad
 k_O\le2-c_T-c_{\tau T}.}
\tag{3.6}
\]

Thus an excessive invariant orbit total is an exact obstruction which no
cube signing can repair.

#### Proof

The two residual capacities are \(1-c_T\) and \(1-c_{\tau T}\).  The
\(k_O\) variable occurrences can be split between them exactly when both
capacities are nonnegative and their sum is at least \(k_O\). \(\square\)

### Proposition 3.3 (floor baselines are preserved exactly)

Let a rank contain \(N\) targets and total mass \(M\), and write

\[
 \frac MN=c+\theta,\qquad c=\left\lfloor\frac MN\right\rfloor,
 \qquad 0\le\theta<1.
\]

Then

\[
 \sum_T(\mu(T)-c)(\mu(T)-c-1)
 =\left\|\mu-\frac MN\mathbf1\right\|_2^2
  -N\theta(1-\theta).
\tag{3.7}
\]

The mean, the final term in (3.7), and the \(\tau\)-even projection are
constant across the cube.  Therefore Theorem 3.1 also minimizes the exact
floor-corrected energy in the varying \(\tau\)-odd mode.  No fractional or
floor term has been discarded.

## 4. Literal run cost of the one-mode minimizer

Let

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
     =\operatorname{Cat}_{m-1}
\tag{4.1}
\]

be the number of cyclic rows in one local factor.  In one \(F_A\)-row, an
affected target \(S_i\) avoids \(B\).  Its upper flag \(U_q(S_i)\) is
nonfixed under \(\tau\) only when one of the two coordinates of \(B\)
lies in the \((q+1)\)-position exterior collar of \(S_i\).  Each coordinate
lies in that collar for at most \(q+1\) starts.  Hence the number of
variable tokens which can affect the rank-\(q\) mode is at most

\[
 \boxed{K_q\le2(q+1)R_m.}
\tag{4.2}
\]

All other token bits may be left in state zero.

### Theorem 4.1 (literal one-mode contraction)

Let \(J_0\) be the run count of the all-old first-avoided matching.  The
orbitwise minimizing corner of Theorem 3.1 can be emitted as literal tight
FIFO runs with

\[
 \boxed{J\le J_0+2K_q
 \le J_0+4(q+1)R_m.}
\tag{4.3}

\]

In particular,

\[
 J_0=O\left(\frac{W\log^2m}{m}\right),
 \qquad
 \frac{R_m}{W}=\frac{m+1}{2(2m+1)(2m-1)}.
\tag{4.4}

If all runs are initialized through a Gaussian flag depth \(H\), their
extra literal cost is \(o(W)\) whenever

\[
 H=o(m/\log^2m),
 \qquad H(q+1)=o(m).
\tag{4.5}

For the proportional Gaussian choice

\[
 H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,
\]

the complete upper-\(q=1\), \(\tau\)-odd rank mode therefore has an exact
integral lattice-minimizing cube corner with literal \(o(W)\) FIFO cost.

#### Proof

Relative to the all-old state, switch only the at most \(K_q\) nonfixed
tokens used by (3.2).  Removing those positions from their \(F_A\) source
rows creates at most \(K_q\) new runs; adding their mates to the \(F_B\)
rows creates at most another \(K_q\).  This is also the rowwise XOR
boundary inequality.  Every resulting component is a literal tight-row
run, so initialization through depth \(H\) costs at most
\((2H+1)J+O(1)\).  Equations (4.2)--(4.5) make this \(o(W)\). \(\square\)

**Scope.**  The theorem minimizes the variable odd component exactly.  It
does not assert that the attained minimum is \(o(W)\): the invariant orbit
sums in Proposition 3.2, the \(\tau\)-even component, and all other depth
modes may retain linear defect.

### Theorem 4.2 (one complete Gaussian-mode packet contraction)

Specialize to the first adjacent pair \(A,B\), so there are no earlier
priority constraints in (1.2).  Fix one depth

\[
 1\le q\le H<m-1.
\]

Let \(D_q^{\mathrm{nf}}\subseteq D\) be the tokens whose old upper
depth-\(q\) flag is not fixed by \(\tau\), and put

\[
 k_q=|D_q^{\mathrm{nf}}|.
\tag{4.6}
\]

In each cyclic row of \(F_A\), take the maximal cyclic components of
\(D_q^{\mathrm{nf}}\).  Their total number \(c_q\) satisfies

\[
 \boxed{c_q\le2R_m,
 \qquad k_q\le(q+1)R_m.}
\tag{4.7}
\]

For an arbitrary integer \(\ell\ge1\), subdivide every component into
consecutive packets of length \(\ell\), followed by at most one shorter
packet.  Denote the packet family by \(\mathcal P_q\).  Then

\[
 \boxed{
 |\mathcal P_q|\le\frac{k_q}{\ell}+c_q.}
\tag{4.8}
\]

Require one common old/new bit on every packet, and leave every other token
old.  Let \(\mu_{q,\sigma}\) be the complete upper-rank load, including all
unchanged tokens, and let \(\bar\mu_q\) be its fractional midpoint over
the packet bits.  There is an explicit integral packet signing \(\sigma\)
such that

\[
 \boxed{
 \|\mu_{q,\sigma}-\lambda_q\mathbf1\|_2^2
 \le
 \|\bar\mu_q-\lambda_q\mathbf1\|_2^2
 +\frac{k_q}{2}
 \le
 \|\bar\mu_q-\lambda_q\mathbf1\|_2^2
 +\frac{q+1}{2}R_m.}
\tag{4.9}
\]

Every such signing is lower-saturating and middle-simple.  It is a literal
union of tight FIFO runs with

\[
 \boxed{
 J\le J_0+2|\mathcal P_q|
 \le J_0+\frac{2k_q}{\ell}+2c_q.}
\tag{4.10}
\]

The same statement holds after subtracting the exact integer-floor
baseline \(B_q\).  In particular, if

\[
 \|\bar\mu_q-\lambda_q\mathbf1\|_2^2\le B_q+o(W),
\tag{4.11}
\]

then the integral packet corner has floor-corrected rank-\(q\) energy
\(o(W)\).

#### Proof

In one \(F_A\)-row, the two coordinates of \(B\) cut the cycle into two
gaps consisting only of \(R\)-coordinates.  Their lengths sum to
\(2m-3\), so exactly one gap has length at least \(m-1\).  The
length-\((m-1)\) windows avoiding both coordinates of \(B\) are precisely
the windows contained in this unique long gap; their starts form one
cyclic interval.  Orient and index it as \(1,\ldots,\ell\).

In the predecessor-token convention, the upper depth-\(q\) window adds
one coordinate at the left end of the lower window and \(q\) coordinates
at its right end.  Hence its nonfixed starts in the displayed interval are
exactly

\[
 \{1\}\cup
 \{\max(1,\ell-q+1),\ldots,\ell\}.
\tag{4.7a}
\]

This has at most two cyclic components and at most \(q+1\) starts.  Summing
over the \(R_m\) rows proves (4.7).  Summing the elementary ceiling bound
over the components proves (4.8).

For a packet \(K\), write

\[
 \Delta_K=
 \sum_{S\in K}
 \bigl(\mathbf1_{\tau U_q(S)}-\mathbf1_{U_q(S)}\bigr).
\tag{4.12}
\]

The old upper flags in one physical row are distinct proper cyclic
windows, and their \(\tau\)-images are distinct.  There is no mixed
equality.  Indeed, if \(U_q(S)=\tau U_q(T)\), the common set avoids both
\(A\) and \(B\), hence is \(\tau\)-fixed; applying \(\tau\) then gives
\(U_q(S)=U_q(T)\), so \(S=T\), contradicting nonfixedness.  Consequently

\[
 \boxed{\|\Delta_K\|_2^2=2|K|.}
\tag{4.13}
\]

With independent uniform signs,

\[
 \mu_{q,\sigma}
 =\bar\mu_q+\frac12\sum_{K\in\mathcal P_q}\sigma_K\Delta_K.
\tag{4.14}
\]

Orthogonality of the random signs, not of different packets, gives

\[
 \mathbb E_\sigma
 \|\mu_{q,\sigma}-\lambda_q\mathbf1\|_2^2
 =\|\bar\mu_q-\lambda_q\mathbf1\|_2^2
 +\frac14\sum_K\|\Delta_K\|_2^2
 =\|\bar\mu_q-\lambda_q\mathbf1\|_2^2+\frac{k_q}{2}.
\tag{4.15}
\]

Expose the packet signs successively, always choosing a sign which does not
increase the remaining conditional expectation.  This constructs the
integral signing in (4.9).  Theorem 2.1 gives exact lower saturation and
middle simplicity.

Each packet is a contiguous interval in an \(F_A\)-row and its mate is the
corresponding interval in the paired \(F_B\)-row.  Removing one interval
from the old row and inserting its mate can create at most two additional
runs in total.  This proves (4.10).  The rank mass and its exact floor
baseline are independent of \(\sigma\), proving the final assertion.
\(\square\)

### Corollary 4.3 (literal Gaussian specialization)

Put

\[
 b=\lfloor m^{3/4}\rfloor,
 \qquad p=\left\lfloor\frac Wb\right\rfloor,
 \qquad N_r=\binom n{m+r},
\]

\[
 b_r=\left\lfloor\frac{N_r}{p}\right\rfloor,
 \qquad a_d=b_{-d}-b_{-(d+1)}.
\tag{4.16}
\]

Take

\[
 q=d=\lfloor\gamma\sqrt m\rfloor,
 \qquad \gamma>0\text{ fixed},
 \qquad \ell=a_d.
\tag{4.17}
\]

Then \(a_d>0\) for all sufficiently large \(m\), and

\[
 a_d=\left(2\gamma e^{-\gamma^2}+o(1)\right)\frac b{\sqrt m}.
\tag{4.18}
\]

Therefore

\[
 |\mathcal P_q|=O(W/b)=O(p),
 \qquad
 \frac{k_q}{2}\le\frac{q+1}{2}R_m
 =\left(\frac{\gamma}{16\sqrt m}+o(m^{-1/2})\right)W.
\tag{4.19}
\]

For

\[
 H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,
\]

initializing every resulting run through the whole depth \(H\) costs

\[
 (2H+1)J
 =O(HJ_0)+O(Hp)=o(W).
\tag{4.20}
\]

Thus (4.9) is a literal, integral contraction of one complete Gaussian
rank mode to within \(o(W)\) of its half-swapped midpoint.  The chosen
corner may depend on \(q\), and (4.11) remains a separate midpoint
condition; no simultaneous Gaussian-band conclusion follows.

#### Proof

Equation (4.18) is the adjacent-binomial estimate proved again in (6.6).
Using (4.7), (4.8), and \(R_m=\Theta(W/m)\) gives

\[
 \frac{k_q}{a_d}=O(W/b),
 \qquad c_q=O(W/m)=o(W/b),
\]

which proves the packet bound.  The exact ratio in (4.4) gives the constant
in (4.19).  Finally \(HJ_0=o(W)\) by (4.4), while

\[
 \frac{Hp}{W}\le\frac Hb=o(1).
\]

Apply Theorem 4.2. \(\square\)

## 5. Packet-constant signs and the exact two-fibre graph

Now partition a changed token family into contiguous physical packets
\(K\), all of one radius \(d\), and require every token of a packet to use
one common sign

\[
 \sigma_K\in\{+1,-1\}.
\]

State \(+1\) is the old packet and state \(-1\) its \(\tau\)-mate.  Fix a
set of upper depths, in particular \(1\le q\le d+1\), and suppose every
packet is internally target-simple at each selected depth.

This section concerns the packet system itself.  If other packets have
already been frozen, their occupied targets must be inserted as zero/one
residual-capacity or unary sign constraints; the unmodified graph below
does not silently account for such a background.

For a nonfixed orbit \(O=\{U,\tau U\}\), assign every state-\(+1\)
occurrence a base polarity \(\eta_{K,O}=+1\) if its target is \(U\) and
\(-1\) if its target is \(\tau U\).  Under packet sign \(\sigma_K\), its
chosen polarity is \(\eta_{K,O}\sigma_K\).

For every orbit having exactly two occurrences, in packets \(K,L\), form
a signed edge with constraint

\[
 \boxed{
 \sigma_K\sigma_L
 =\chi_e:=-\eta_{K,O}\eta_{L,O}.}
\tag{5.1}
\]

Parallel edges and loops are retained.  A loop coming from two internally
distinct targets of one packet is automatically labelled \(+1\).

### Theorem 5.1 (signed two-fibre packet theorem)

A packet-constant choice is target-simple at every selected upper depth if
and only if:

1. every fixed \(\tau\)-orbit has at most one occurrence;
2. every nonfixed orbit has at most two occurrences; and
3. the signed packet multigraph is balanced, meaning

   \[
   \boxed{\prod_{e\in C}\chi_e=1}
   \tag{5.2}
   \]

   for every graph cycle \(C\).

When these conditions hold, root every connected component and propagate
the signs using (5.1).  This gives an explicit integral signing.  In the
all-old representative convention all base polarities are \(+1\), so the
condition reduces to ordinary bipartiteness.

#### Proof

A fixed orbit cannot be changed.  A nonfixed orbit has only two target
positions, so more than two occurrences cannot be simple.  With two
occurrences, simplicity says their chosen polarities are opposite, which
is exactly (5.1).  A signed edge system has a vertex signing precisely when
the product of its edge labels on every cycle is \(+1\).  Root propagation
constructs the signing when the condition holds. \(\square\)

### Theorem 5.2 (exact odd-energy/frustration identity)

Assume the first two fibre-size conditions of Theorem 5.1.  Let \(s_q\)
be the number of singleton nonfixed orbits at depth \(q\), and give depth
\(q\) weight \(w_q\ge0\).  Then

\[
 \boxed{
 E_d^-(\sigma)
 =\frac12\sum_qw_qs_q
 +2\sum_{e\text{ violated}}w_{q(e)}.}
\tag{5.3}
\]

Consequently

\[
 \boxed{
 \min_\sigma E_d^-(\sigma)
 =\frac12\sum_qw_qs_q
 +2\operatorname{frust}_w(G,\chi),}
\tag{5.4}
\]

where \(\operatorname{frust}_w\) is the minimum total weight of violated
signed edges.  A balanced graph attains the exact parity minimum.

#### Proof

On a nonfixed orbit with load difference \(\delta\), the squared norm of
its odd projection is \(\delta^2/2\).  A singleton has \(|\delta|=1\) and
contributes \(1/2\).  A satisfied two-fibre edge puts one occurrence on
each target and contributes zero.  A violated edge puts both occurrences
on the same target, has \(|\delta|=2\), and contributes two.  Sum with the
depth weights. \(\square\)

The uniform means and integer-floor baselines are \(\tau\)-even, so
(5.3)--(5.4) are also the exact varying terms in the floor-corrected
energy for the packet load alone, or in the presence of a
\(\tau\)-invariant frozen background.  For an arbitrary frozen background
\(h\), one must additionally retain the external-field term

\[
 2\langle P_-h,P_-\mu_\sigma\rangle.
\tag{5.5}
\]

The resulting minimization is a signed Ising/frustration problem with
external fields; (5.4) alone is then not the complete energy.

## 6. A complete one-radius Gaussian special case

Return to the proportional parameters

\[
 b=\lfloor m^{3/4}\rfloor,\qquad
 p=\left\lfloor\frac Wb\right\rfloor,
\]

\[
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor,\qquad
 a_d=b_{-d}-b_{-(d+1)}\quad(d<H).
\tag{6.1}
\]

### Proposition 6.1 (physical packet supply at one radius)

For every \(d<H\) with \(a_d>0\), the first adjacent swap family
\(D_1\) contains at least \(p\) pairwise disjoint contiguous old-state
packets, each of length \(a_d\), for all sufficiently large \(m\).
Their lower targets and middle owners are pairwise distinct, and their
\(\tau\)-mates are physical packets of the same length.

#### Proof

Here

\[
 |D_1|=\binom{2m-3}{m-1}=\Theta(W).
\tag{6.2}
\]

Inside each row of \(F_A\), the \(D_1\)-starts form exactly one nonempty
cyclic interval; Proposition 6.3 below gives the exact gap proof.  Write
their lengths as \(\ell_1,\ldots,\ell_{R_m}\), where

\[
 C=R_m=O(W/m),
 \qquad \sum_i\ell_i=|D_1|.
\]

The number of disjoint length-\(a_d\) subintervals is at least

\[
 \sum_i\left\lfloor\frac{\ell_i}{a_d}\right\rfloor
 \ge\frac{|D_1|}{a_d}-C.
\tag{6.3}
\]

The exact adjacent-binomial ratio gives

\[
 a_d\le
 \frac{W}{p}\frac{2d+2}{m+d+2}+1
 =O(bH/m)+1=O(m^{1/4}\sqrt{\log m}),
\tag{6.4}
\]

uniformly for \(d\le H\).  Therefore the right side of (6.3) is
\(\Omega(W/m^{1/4}\sqrt{\log m})\), whereas

\[
 p=\Theta(W/m^{3/4}).
\]

It is larger than \(p\) for all sufficiently large \(m\).  Physicality
and lower/middle distinctness follow from the first-avoided matching;
applying \(\tau\) gives the mates. \(\square\)

The proposition supplies the physical packet carriers unconditionally.
It does not supply distinct deeper flags or the signed-graph condition.

### Theorem 6.2 (balanced-graph one-radius contraction)

Take \(p\) packets from Proposition 6.1, give every packet the complete
radius-\(d\) flag system, and form the signed two-fibre graph across upper
depths \(1,\ldots,d+1\).  Assume:

1. the unchanged lower flag dictionary is target-simple at every active
   lower depth;
2. the upper fibres satisfy the size conditions in Theorem 5.1; and
3. the signed graph is balanced.

Then root propagation gives an integral packet signing for which:

* all lower flags remain target-distinct;
* all middle owners remain distinct;
* all upper flags through depth \(d+1\) are target-distinct;
* every packet remains one literal FIFO run; and
* every active-rank count \(p a_d\), and hence every floor baseline already
  fixed before signing, is unchanged.

The total literal length needed for this one radius class is at most

\[
 \boxed{p(a_d+2d+3)=o(W).}
\tag{6.5}
\]

If the signed graph is a forest, the balance hypothesis is automatic.

For the natural all-old packets extracted in Proposition 6.1, every
nonfixed orbit has the same canonical old representative.  Hence all base
polarities are \(+1\), every edge has label \(-1\), and the balance
hypothesis here is exactly bipartiteness of the packet multigraph.  The
more general signed formulation applies after packetwise gauge reversal or
mixed base-state conventions.

#### Proof

Theorems 2.1 and 5.1 prove matching legality and target simplicity.  Start
each chosen packet as its own physical radius-\((d+1)\) run.  A packet of
\(a_d\) selected owners costs at most \(a_d+2d+3\) letters.  Moreover,

\[
 \frac{pa_d}{W}
 \le\frac{2d+2}{m+d+2}+\frac pW=o(1),
\]

where the final harmless term may be replaced directly by \(p/W\); and

\[
 \frac{p(2d+3)}W\le\frac{2H+3}{b}=o(1).
\]

This proves (6.5).  Packet signs change no count or floor. \(\square\)

For a genuine Gaussian radius

\[
 d=\lfloor\gamma\sqrt m\rfloor,
 \qquad \gamma>0\text{ fixed},
\]

local binomial asymptotics give

\[
 a_d=\left(2\gamma e^{-\gamma^2}+o(1)\right)\frac b{\sqrt m}.
\tag{6.6}
\]

Hence the number of designated flag incidences realized target-distinctly
in the complete symmetric radius class is

\[
 \boxed{
 (2d+2)pa_d
 =\left(4\gamma^2e^{-\gamma^2}+o(1)\right)W.}
\tag{6.7}
\]

Thus Theorem 6.2 is a genuinely linear-sized full Gaussian-mode special
case, not a bounded-depth toy.  Its signed-fibre and lower-dictionary
hypotheses are explicit and remain unproved for the global packet supply.
Only the middle/upper \(\tau\)-odd data vary under the cube.  The lower
flags are pointwise fixed; the total designated upper incidence count is

\[
 (d+1)pa_d
 =\left(2\gamma^2e^{-\gamma^2}+o(1)\right)W.
\tag{6.8}
\]

An arbitrary packet placement from Proposition 6.1 may have many
\(\tau\)-fixed upper flags.  The placement-dependent linear lower bound on
genuinely nonfixed incidences is (6.20) below.

Also, this isolated radius class does not by itself instantiate the full
proportional counts \(pb_q\) or the global residues \(N_q-pb_q\).

### Proposition 6.3 (exact first-pair row geometry and collar law)

In every cyclic row \(\pi\) of \(F_A\), the two coordinates of \(B\) cut
the remaining \(2m-3\) coordinates into two cyclic gaps.  There is a unique
gap of length \(G_\pi\ge m-1\), and the \(D_1\)-starts in that row form one
cyclic interval of exact length

\[
 \boxed{\ell_\pi=G_\pi-m+2\in[1,m-1].}
\tag{6.9}
\]

Moreover,

\[
 \boxed{
 \sum_\pi\ell_\pi=|D_1|,
 \qquad
 \frac{|D_1|}{R_m}=\frac m2.}
\tag{6.10}
\]

Orient the interval and index its starts by \(1,\ldots,\ell_\pi\).  At
upper depth \(q<m-1\), its nonfixed starts are exactly

\[
 \boxed{
 \{1\}\cup
 \{\max(1,\ell_\pi-q+1),\ldots,\ell_\pi\}.}
\tag{6.11}
\]

Consequently the starts which are nonfixed at some upper depth
\(1\le q\le d+1\) are exactly

\[
 \{1\}\cup
 \{\max(1,\ell_\pi-d),\ldots,\ell_\pi\}.
\tag{6.12}
\]

A direct old-to-\(\tau\) carrier change after start \(r\) first changes a
left upper flag at depth

\[
 q_0=\ell_\pi-r+1.
\tag{6.13}
\]

Thus it preserves all left upper flags through depth \(d+1\) exactly when

\[
 r\le\ell_\pi-d-1.
\tag{6.14}
\]

If \(s\) undesignated starts are inserted before the change, the sharp
worst-case requirement is

\[
 \boxed{
 s\ge s_{\min}:=
 \max\{0,d+1-(\ell_\pi-r)\}.}
\tag{6.15}
\]

#### Proof

The two gap lengths sum to \(2m-3\).  At least one is at least \(m-1\),
and they cannot both be.  A length-\((m-1)\) window avoids both coordinates
of \(B\) precisely when it lies in the unique long gap.  Sliding that
window inside a gap of length \(G_\pi\) gives (6.9).

Every affected target occurs in exactly one row, so the first identity in
(6.10) is a partition count.  Direct factorial cancellation gives

\[
 \frac{|D_1|}{R_m}
 =(2m-1)
 \frac{\binom{2m-3}{m-1}}{\binom{2m-1}{m-1}}
 =\frac m2.
\]

The predecessor-token upper window adds one coordinate at the left end and
\(q\) at the right end of the lower window.  It meets \(B\) exactly at the
first start or at one of the final \(q\) starts, proving (6.11)--(6.12).
For a change after \(r\), the right boundary coordinate first enters the
last left token after \(\ell_\pi-r+1\) upper extensions.  This proves
(6.13)--(6.14), and inserting \(s\) blank ages gives (6.15).  Sharpness
holds when the boundary coordinate belongs to \(B\). \(\square\)

### Theorem 6.4 (exact \(p\)-packet FIFO row bundling)

Fix \(\gamma>0\), let

\[
 d=\lfloor\gamma\sqrt m\rfloor,
 \qquad a=a_d,
 \qquad
 t_0=\left\lceil\frac{d+1}{a}\right\rceil,
\tag{6.16}
\]

and use the proportional parameters in (6.1).  There are, for all
sufficiently large \(m\), integers \(t_\pi\ge t_0\) on

\[
 s=\lfloor\eta_\gamma R_m\rfloor,
 \qquad
 \eta_\gamma:=\min\{1/4,4e^{-\gamma^2}\}>0,
\tag{6.17}
\]

physical rows, such that

\[
 t_\pi\le\left\lfloor\frac{\ell_\pi}{a}\right\rfloor,
 \qquad
 \boxed{\sum_\pi t_\pi=p.}
\tag{6.18}
\]

In each selected row take the terminal block of \(t_\pi a\) affected
starts and partition it into \(t_\pi\) consecutive length-\(a\) packets.
Then:

1. there are exactly \(p\) physical radius-\(d\) packets, grouped into
   only \(s=O(R_m)=O(W/m)\) row-contiguous macro-blocks;
2. assigning one old/new sign to each macro-block preserves exact lower
   saturation and middle simplicity in the ambient first-avoided matching
   when all outside tokens are retained; as an isolated dictionary, the
   selected packets have distinct lower targets and middle owners;
3. every macro-block is one canonical tight FIFO run through all depths
   \(-d,\ldots,d+1\); emitting the blocks as fresh runs has exact upper
   bound

   \[
   \boxed{pa+s(2d+3)=pa+O(R_md)=pa+o(W);}
   \tag{6.19}
   \]

4. the selected blocks contain at least

   \[
   \boxed{
   s\frac{(d+1)(d+2)}2
   =\left(\frac{\eta_\gamma\gamma^2}{16}+o(1)\right)W}
   \tag{6.20}
   \]

   nonfixed upper \((\text{start},\text{depth})\) incidences.

Thus a complete Gaussian radius class has an unconditional integral FIFO
bundling into \(O(W/m)\), rather than \(p=\Theta(W/m^{3/4})\), physical
macro-runs while retaining linear \(\tau\)-odd leverage.

#### Proof

From the exact mean (6.10) and \(1\le\ell_\pi\le m-1\), at least
\(R_m/3\) rows satisfy \(\ell_\pi\ge m/4\).  Indeed, otherwise their
average would be strictly smaller than

\[
 \frac13(m-1)+\frac23\frac m4<\frac m2.
\]

Choose any \(s\) such rows.  Distribute \(p\) packets among them as evenly
as possible, so every \(t_\pi\) is either \(\lfloor p/s\rfloor\) or
\(\lceil p/s\rceil\).  By (6.6),

\[
 \frac{p}{R_mt_0}=16e^{-\gamma^2}+o(1).
\tag{6.21}
\]

Hence \(t_\pi\ge t_0\) for all large \(m\), by the definition of
\(\eta_\gamma\).  Also

\[
 t_\pi=\left(\frac8{\eta_\gamma}+o(1)\right)m^{1/4},
\tag{6.21a}
\]

whereas every chosen row has packet capacity at least

\[
 \left\lfloor\frac{m}{4a}\right\rfloor
 =\Theta_\gamma(m^{3/4}).
\tag{6.22}
\]

Thus every \(t_\pi\) fits.  The floor/ceiling distribution proves (6.18)
without fractional allocation or clone capacities.  Equivalently,

\[
 t_\pi a
 =\left(\frac{16\gamma e^{-\gamma^2}}{\eta_\gamma}+o(1)\right)\sqrt m
 \ge(4\gamma+o(1))\sqrt m>d+1,
\tag{6.22a}
\]

which also verifies directly that every chosen terminal block contains the
complete active collar.

Theorem 2.1 proves the second assertion.  A block and its \(\tau\)-mate
are each one contiguous physical row interval, giving (6.19); if the whole
matching is initialized through a larger proportional depth \(H\), the
corresponding additional term is \(O(R_mH)=o(W)\).

Every selected block has length at least \(t_0a\ge d+1\), so it contains
the final \(d+1\) starts in its row interval.  Equation (6.11) shows that
at depth \(q\) its final \(q\) starts are nonfixed.  Summing
\(q=1,\ldots,d+1\) gives \((d+1)(d+2)/2\) incidences per block.  Finally,
\(R_m/W=(8m)^{-1}+o(m^{-1})\), proving (6.20). \(\square\)

The cost in (6.19) is a fresh-run/cut cost.  It is not a claim that one
blank start splices arbitrary neighboring blocks.  Equations
(6.13)--(6.15) show why the sign-effective terminal tail admits only one
uniform reset-free carrier sign per row unless extra ages are supplied.

### Corollary 6.5 (conditional row-graph completion)

Form a graph whose vertices are the macro-blocks in Theorem 6.4.  At every
upper depth \(1,\ldots,d+1\), put an edge between the two blocks whose old
flags occupy one nonfixed \(\tau\)-orbit twice.  Assume:

1. the selected lower dictionary is target-simple;
2. every fixed upper orbit has at most one selected occurrence;
3. every nonfixed upper orbit has at most two selected occurrences; and
4. the row-collision graph is bipartite.

Then a two-colouring of the row graph gives one integral old/new sign per
macro-block for which every selected upper flag through depth \(d+1\) is
target-distinct.  The complete radius class has the literal cost (6.19)
and the linear nonfixed support (6.20).

#### Proof

Proper cyclic windows are distinct inside one row block, so no graph loop
occurs.  In the natural all-old representative convention every edge has
label \(-1\).  Theorem 5.1 therefore reduces exactly to bipartiteness, and
Theorem 2.1 preserves the lower/middle matching. \(\square\)

The four displayed hypotheses are not proved by the row packing.  With a
frozen background they must be stated in residual-capacity form, including
the corresponding unary sign constraints.  In particular, (6.20) does not
imply that the actual row graph is bipartite.

### Proposition 6.6 (fixed-support gate before bipartiteness)

Let \(M\) affected starts be grouped into \(B_0\) contiguous physical row
blocks, and suppose their upper-q1 flags are required to be target-simple
after arbitrary old/\(\tau\) block signs and arbitrary fresh right collars.
Let

\[
 \mathcal F_1^{\mathrm{fix}}
 =\{U_1(S):S\in D_1,\ \tau U_1(S)=U_1(S)\}
\tag{6.23}
\]

be the distinct canonical fixed-target support of the whole \(F_A\)
factor.  Necessarily

\[
 \boxed{
 |\mathcal F_1^{\mathrm{fix}}|
 \ge M-B_0-2R_m.}
\tag{6.24}
\]

For the exact packing in Theorem 6.4, \(M=pa_d\) and \(B_0=s\le R_m\),
so

\[
 \boxed{
 |\mathcal F_1^{\mathrm{fix}}|
 \ge pa_d-3R_m
 =\left(2\gamma e^{-\gamma^2}+o(1)\right)
   \frac W{\sqrt m}.}
\tag{6.25}
\]

On the other hand, the local-factor axioms alone give only

\[
 |\mathcal F_1^{\mathrm{fix}}|
 \ge
 \frac{|D_1|-2R_m}{\lfloor(m+1)/2\rfloor}
 =\Theta(W/m).
\tag{6.26}
\]

Consequently any exact factor with support smaller than the right side of
(6.25) is a literal no-go for a target-simple \(p\)-packet Gaussian row
bundling, regardless of row-graph bipartiteness.

#### Proof

In a block of length \(L\), the first \(L-1\) q1 flags are forced by
consecutive middle owners; only the terminal flag can depend on a fresh
right collar.  Thus at least \(M-B_0\) q1 occurrences are canonical.
Equation (6.11) with \(q=1\) shows that at most two occurrences per row,
hence at most \(2R_m\) globally, are nonfixed.  Every remaining occurrence
must use a distinct member of \(\mathcal F_1^{\mathrm{fix}}\), proving
(6.24)--(6.25).

A fixed \((m+1)\)-target can occur at q1 at most
\(\lfloor(m+1)/2\rfloor\) times.  Every occurrence uses two consecutive
rank-\(m\) facets.  If two occurrences shared a facet, uniqueness of that
facet in the exact factor would put them at adjacent starts in the same
row, but distinct proper cyclic \((m+1)\)-windows in one row cannot be
equal.  Thus the facet pairs are disjoint among occurrences of the fixed
target.
There are at least \(|D_1|-2R_m\) fixed occurrences, which proves (6.26).
\(\square\)

More generally, put

\[
 \mathcal F_q^{\mathrm{fix}}
 =\{U_q(S):S\in D_1,\ \tau U_q(S)=U_q(S)\}.
\tag{6.26a}
\]

The same internal-witness count at depth \(q\) gives the necessary
condition

\[
 |\mathcal F_q^{\mathrm{fix}}|
 \ge M-qB_0-2(q+1)R_m.
\tag{6.27}
\]

This fixed-support gate is independent of the signed-cycle gate.

## 7. Exact FIFO protected-splice theorem

Let

\[
 \pi=(x_t),\qquad \tau\pi=(\tau x_t)
\]

be paired cyclic rows.  Use predecessor-token notation

\[
 Y_t=I_\pi(t-1,m),
\]

\[
 L_q(t)=I_\pi(t+q-1,m-q),
 \qquad
 U_q(t)=I_\pi(t-1,m+q).
\tag{7.1}
\]

Suppose

\[
 S_c=I_\pi(c,m-1)\subseteq R,
\tag{7.2}
\]

so \(\tau\) fixes the complete ordered overlap.  On a no-wrap linear
segment define the hybrid coordinate word

\[
 z_r=
 \begin{cases}
 x_r,&r\le c+m-2,\\
 \tau x_r,&r\ge c+m-1.
 \end{cases}
\tag{7.3}
\]

### Theorem 7.1 (sharp protected FIFO splice)

The hybrid word has middle owners

\[
 Y_t\quad(t\le c),
 \qquad
 \tau Y_t\quad(t\ge c+1).
\tag{7.4}
\]

If \(e_{c-s}\) is the final designated left token and

\[
 e_{c-s+1},\ldots,e_c
\]

are \(s\) undesignated starts, then:

1. every left lower flag is unchanged at every depth;
2. every left upper flag through depth \(q=s\) is unchanged;
3. every right lower and upper flag is exactly its canonical \(\tau\)-row
   flag at every depth.

At the last left token, \(U_{s+1}\) is the first flag which can change.  It
does change whenever

\[
 x_{c+m-1}\in B.
\tag{7.5}
\]

Thus the buffer length \(s\) is sharp in the worst case.

#### Proof

On the stipulated proportional no-wrap span there are fewer than
\(2m-1\) indices, so distinct indices of the \(Q_A\)-row \(\pi\) carry
distinct coordinates.  The old side contains only \(B\cup R\), the new
side only \(A\cup R\), and an \(R\)-coordinate cannot occur twice on this
span.  Hence the hybrid word is injective.

For \(t\le c\), the owner interval \([t-1,t+m-2]\) ends before the
switch in (7.3); for \(t\ge c+1\), every part before the switch lies inside
the fixed ordered core \(S_c\), so the owner is the \(\tau\)-image.  This
proves (7.4).

For a left token \(e_t\), its lower flag interval ends at \(t+m-2\),
independently of its depth, and hence stays on the old side when
\(t\le c-s\).  Its upper depth-\(q\) interval ends at
\(t+m+q-2\), which is at most \(c+m-2\) for \(q\le s\).  All right flag
intervals agree with the \(\tau\)-row because their overlap with the old
side lies inside \(S_c\), where \(x=\tau x\).  At \(t=c-s,q=s+1\), the
upper interval first contains \(x_{c+m-1}\), proving (7.5). \(\square\)

### Corollary 7.2 (radius-zero one-spacer lift)

A proportional radius-\(d\) packet is active through upper depth \(d+1\).
Therefore a worst-case reset-free carrier change immediately after it needs

\[
 \boxed{s\ge d+1.}
\tag{7.6}

Uniformly in the worst case, this protected-splice mechanism gives an exact
lift for \(d=0\).  A special deeper seam can need fewer blank starts if its
boundary coordinates are absent, or if a correlated predecessor already
supplies them with the required age.

Moreover, for all sufficiently large \(m\),

\[
 \boxed{a_0=b_0-b_{-1}=1.}
\tag{7.7}

#### Proof of (7.7)

Write \(W=pb+r\), \(0\le r<b\).  Since

\[
 N_{-1}=W\frac m{m+2},
\]

and \(b=o(m)\), \(p\sim W/b\), for all large \(m\)

\[
 p(b-1)<N_{-1}<pb.
\]

Indeed the right inequality is equivalent to
\(r<2W/(m+2)\), while the left follows from
\(2W/(m+2)<p+r\); both hold because \(r<b\ll W/m\) and
\(p\asymp W/b\gg W/m\).  Hence \(b_{-1}=b-1\), while \(b_0=b\).
\(\square\)

The radius-zero packet is one start, and the one blank start protects its
complete upper-q1 flag while changing from an old to a \(\tau\)-carrier.
This is an exact local reset-free FIFO splice template for one radius-zero
carrier bit of the same q1 type treated in Theorem 4.1.  The global
orbitwise minimizer
may use many scattered bits and is made literal there by regrouping them
into fresh runs; Corollary 7.2 does not sew all those bits into one row.
Nor does it align those bits with the \(p\) proportional radius-zero packet
slots or construct a global target-disjoint macro-packet dictionary.  It is
a local preservation/routing result and by itself has no leverage on a
genuinely deep defect.

## 8. Why the construction does not yet sum over the Gaussian band

There are five independent obstructions.

1. **Invariant orbit totals.**  The cube changes only the odd projection.
   Proposition 3.2 gives the exact capacity obstruction in the even
   projection.
2. **Fixed target support.**  Proposition 6.6 shows that standard fused
   Gaussian packets require \(\Theta(W/\sqrt m)\) distinct fixed q1
   targets.  Packet signs cannot change those targets, while the exact
   local-factor axioms presently guarantee only \(\Theta(W/m)\) support.
3. **Signed-cycle parity.**  Packet-constant simplicity across several
   depths is equivalent to the balance of the signed two-fibre graph.  An
   unbalanced cycle forces the positive frustration term (5.4).
4. **FIFO age.**  One blank start uniformly protects only radius zero.  A
   uniform worst-case radius-\(d\) carrier change needs \(d+1\) protected
   starts or a
   correlated predecessor already carrying every entering coordinate with
   the correct age.  Theorem 6.4 bypasses this for one radius by using one
   fresh terminal macro-run per selected row, but it does not give
   independently signable reset-free subblocks in the active tail.
5. **Aggregate initialization in the original \(p\)-copy architecture.**
   Starting all \(p\) packets separately at every radius, or giving each
   of those \(p\) copies its own deep buffer, is affordable for one radius
   class but not for all of them.  Proposition 5.3 of
   `MATH_ATTACK_U_COLUMN_CORRELATED_NIBBLE_AUDIT_20260725.md` proves that
   the proportional profile has \(K=\Omega(\sqrt m)\) nonempty radius
   classes.  Therefore

   \[
   \sum_{d:a_d>0}(d+1)\ge\frac{K(K+1)}2=\Omega(m).
   \tag{8.1}
   \]

   An ordering can omit a terminal buffer for at most one class.  Since
   \(H=O(\sqrt{m\log m})=o(m)\), with \(p\sim W/b\) this separately
   buffered \(p\)-copy cost is at least

   \[
   p\left(\sum_{d:a_d>0}(d+1)-O(H)\right)
   =\Omega(pm)=\Omega(Wm/b),
   \tag{8.2}
   \]

   which is not \(o(W)\) for \(b=m^{3/4}\).  This is not a lower bound for
   every radius-by-radius construction: Theorem 6.4 groups the \(p\) copies
   of one radius into only \(O(R_m)\) macro-runs.  Nor is it an obstruction
   to the open shared correlated-age construction.  Whether the row
   grouping can be shared across all radii at aggregate \(o(W)\) cost
   remains unproved.

A fixed token bit also controls every upper depth simultaneously.  The
orbitwise minimizers from Theorem 3.1 for different depths need not agree.
Thus neither the q1 theorem nor the balanced one-radius theorem can be
iterated independently into constant one.

The exact remaining positive theorem is now:

> **Correlated-age near-rainbow packet theorem (OPEN).**  Construct one
> global packet dictionary which meets the fixed-support inequalities
> (6.24)/(6.27), whose signed two-fibre graph is balanced after all Gaussian
> depths are combined, and route its packet signs through common FIFO
> predecessors carrying every entering coordinate with the required age,
> with total protected-start cost \(o(W)\).

This theorem would combine the integral priority cube with the spaced
macro-packet reduction.  It is not implied by the low-run bound, by the
\(O(m^{-2})\) inter-packet overlap, or by abstract SCD flow.

No constant-one conclusion is claimed.

## 9. Independent audits

Three independent audits checked the decisive statements.

1. The first independently proved the mixed-owner collision argument and
   the protected-splice identities, including the sharp \(d+1\) blank
   bound and the exact equality \(a_0=1\).
2. The second derived the signed two-fibre graph, its cycle-product
   criterion, the exact frustration energy (5.3), and the linear Gaussian
   incidence count (6.7).
3. The third checked the chronology obstruction and distinguished the
   unconditional q1 odd-mode minimizer from the conditional all-depth
   packet theorem.  It found no forced odd cycle in the actual packet
   graph; balancedness remains an existence condition, not a theorem about
   the global dictionary.
4. All three rechecked Theorem 4.2.  They verified the exact endpoint-collar
   geometry, \(\|\Delta_K\|_2^2=2|K|\), the conditional-expectation
   identity, the \(\gamma/16\) constant in (4.19), and the distinction
   between an unconditional rounding gap and the unproved midpoint bound
   (4.11).
5. Two independent audits rederived the exact mean
   \(R_m^{-1}\sum\ell_\pi=m/2\), the floor/ceiling allocation of exactly
   \(p\) packets to \(\Theta_\gamma(R_m)\) terminal blocks, the constant in
   (6.20), and the q1 fixed-support inequality (6.24).  Both confirmed that
   the construction proves physical FIFO bundling but neither fibre bounds
   nor bipartiteness.
