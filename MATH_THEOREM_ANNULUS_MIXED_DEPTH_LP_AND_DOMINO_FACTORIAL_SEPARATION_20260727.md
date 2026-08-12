# Annulus synchronization: the mixed-depth LP, exact fractional ordinary cover, and domino-factorial separation

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, web
input, or independent depthwise nibble is used.

## 0. Outcome

Put

\[
 n=2m,\qquad q_0=a\sqrt m+O(1),\qquad
 H=b\sqrt m+O(1),\qquad0<a<b,
\]

\[
 R=m-q_0,\qquad
 N_q=\binom{2m}{m-q},\qquad
 W=\binom{2m}{m}.
\tag{0.1}
\]

For a cyclic packet \(\pi\), let \(P_q(\pi)\) be its \(n\) cyclic
intervals of length \(m-q\).  Let \(\mathcal M\) be one entrance matching
of \(s\) packets and put

\[
                         M=ns.
\tag{0.2}
\]

At depth \(q\), let \(B_q\) be the number of distinct targets hit and
\(H_q=N_q-B_q\) the number of holes.  The exact floor-correct repeat
excess is

\[
 \boxed{
 \widetilde E_q=\min\{M,N_q\}-B_q,\qquad
 H_q=(N_q-M)_++\widetilde E_q.}
\tag{0.3}
\]

The conclusions of this note are:

1. There is one exact mixed-depth configuration program whose integral
   solutions are precisely the entrance matchings in question.  Its
   objective deficit is \(\sum_q\widetilde E_q\), not a sum of
   independently chosen depthwise defects.

2. The full ordinary cyclic-packet catalogue has **zero fractional
   mixed-depth defect**.  One uniform packet weighting simultaneously
   attains
   \(\sum_Tz_{q,T}=\min\{M,N_q\}\) at every annular depth.  Hence no
   state-independent linear Hall cut obstructs the ordinary catalogue.

3. Fix any section which chooses one complementary component
   decomposition of every simple, correctly quotiented domino-twin
   entrance atom.  On this lifted catalogue the same fractional program
   has a linear deficit already at depth \(q_0+1\).  Every lifted atom has
   \(2n\) entrance targets but only \(3n/2\) distinct first descendants.
   Consequently

   \[
   \boxed{
   \operatorname {Def}^{\rm frac}_{q_0+1}
   \ge\min\{M,N_{q_0+1}\}-{3M\over4}.}
   \tag{0.4}
   \]

   At critical entrance mass
   \(M=N_{q_0}-O(N_{q_0}/\sqrt m)\), this is

   \[
                         (1/4-o(1))N_{q_0}=\Theta(W).
   \tag{0.5}
   \]

4. The audited factorial-overlap hierarchy through
   \(p=O(\log m)\) remains valid after passage to the simple twin
   quotient.  Thus exact entrance regularity, an exact entrance
   fractional factor, and all those factorial overlap bounds coexist
   with the linear fractional descendant deficit (0.5).  Those
   entrance-overlap hypotheses alone cannot imply the desired
   synchronized repeat estimate; an ordinary-packet theorem may still
   use additional chronology.

5. The labelled “near-parallel twin” interpretation needs correction.
   Flipping one internal domino does not produce a new simple column:

   \[
                            Q(P\circ s_i)=Q(P).
   \tag{0.6}
   \]

   The \(n2^m\) such anchored presentations form one representation
   fibre.  The stopped factorial generator identities remain valid, but
   the purported physical \(K-4\)-overlap cloud from those flips does
   not survive quotienting.

6. A genuine deterministic anti-twin charge does survive.  If an
   ordinary entrance matching contains \(t\) vertex-disjoint exact
   domino-twin pairs, then at every odd relative depth \(d=q-q_0\),

   \[
   \boxed{
   \widetilde E_q
   \ge {nt\over2}-(M-N_q)_+.}
   \tag{0.7}
   \]

   Therefore a critical matching with
   \(\sum_q\widetilde E_q=o(W)\) must have
   \(t=o(W/n)\).

7. This exact obstruction can be quarantined without changing the
   fractional optimum: attach the two simple-twin fibre labels carried
   by each ordinary packet as capacity-one resources.  This adds only
   two labels per packet, forbids exactly the two complementary twin
   traces which were otherwise entrance-compatible, and has
   \(o(1)\) uniform fractional load at every new label.

The requested integral ordinary matching is not constructed here.  The
smallest remaining statement is an \(o(W)\)-integrality-gap theorem for
the mixed-depth ordinary-packet program.  The stopped fresh-target
inequality in Section 7 is one sufficient trajectory-level formulation.
Static domino factorial overlap does not provide it.

## 1. Exact support and the correlated fresh-target identity

Let

\[
 \mu_q(T)=|\{\pi\in\mathcal M:T\in P_q(\pi)\}|.
\]

Every selected packet contributes \(n\) distinct targets, so
\(\sum_T\mu_q(T)=M\).  Therefore

\[
 \sum_T(\mu_q(T)-1)_+=M-B_q.
\]

Subtracting the scalar floor \((M-N_q)_+\) proves (0.3).

Order the selected packets as
\(\pi_1,\ldots,\pi_s\).  After \(t\) choices put

\[
 M_t=nt,\qquad
 \mathcal O_{q,t}=\bigcup_{j\le t}P_q(\pi_j).
\]

For a legal next packet \(\pi\), define its aggregate fresh count at
depth \(q\) by

\[
 Z_{q,t}(\pi)=|P_q(\pi)\setminus\mathcal O_{q,t}|,
\tag{1.1}
\]

and put

\[
 c_{q,t}
 =(N_q-M_t)_+-(N_q-M_t-n)_+
 =\min\{n,(N_q-M_t)_+\}.
\tag{1.2}
\]

### Theorem 1.1 (one-matching fresh-target telescope)

For every ordered entrance matching,

\[
 \boxed{
 \sum_{q=q_0}^{H}\widetilde E_{q,s}
 =
 \sum_{t=0}^{s-1}
 \left(
   \sum_{q=q_0}^{H}c_{q,t}
   -
   \sum_{q=q_0}^{H}Z_{q,t}(\pi_{t+1})
 \right).}
\tag{1.3}
\]

#### Proof

At time \(t\), equation (0.3) is

\[
 \widetilde E_{q,t}
 =\min\{M_t,N_q\}-|\mathcal O_{q,t}|.
\]

The first term increases by \(c_{q,t}\), while the second increases by
exactly \(Z_{q,t}(\pi_{t+1})\).  Subtract consecutive times and sum over
\(t,q\).  The time-zero value is zero. \(\square\)

Thus the exact deterministic target is cumulative aggregate fresh-score
deficit \(o(W)\).  Formula (1.3) permits compensation between depths and
between times; no separate depthwise matching occurs.

## 2. The exact mixed-depth configuration program

Let \(\mathscr P\) be the directed cyclic-packet catalogue.  Use binary
variables \(x_\pi\) and \(z_{q,T}\).  The program is

\[
 \sum_{\pi:A\in P_{q_0}(\pi)}x_\pi\le1
 \qquad
 \left(A\in\binom{[n]}R\right),
\tag{2.1}
\]

\[
                         \sum_{\pi\in\mathscr P}x_\pi=s,
\tag{2.2}
\]

\[
 z_{q,T}\le
 \sum_{\pi:T\in P_q(\pi)}x_\pi,\qquad
 0\le z_{q,T}\le1.
\tag{2.3}
\]

Maximize

\[
                         \sum_{q=q_0}^{H}\sum_Tz_{q,T}.
\tag{2.4}
\]

### Theorem 2.1 (integer objective is the synchronized repeat objective)

For integral variables, (2.1)--(2.3) choose exactly one size-\(s\)
entrance matching, and

\[
 \boxed{
 \min_{\mathcal M}\sum_q\widetilde E_q
 =
 \sum_q\min\{M,N_q\}
 -
 \max_{(2.1)-(2.3)}\sum_{q,T}z_{q,T}.}
\tag{2.5}
\]

#### Proof

Constraint (2.1) is precisely entrance disjointness and (2.2) fixes the
number of packets.  For a fixed integral \(x\), maximizing (2.4) sets
\(z_{q,T}=1\) exactly on the support of the selected depth-\(q\) load.
Thus (2.4) equals \(\sum_qB_q\).  Apply (0.3). \(\square\)

There is a useful explicit dual form.

### Theorem 2.2 (mixed-depth support dual)

Choose \(0\le\lambda_{q,T}\le1\), \(\alpha_A\ge0\), and
\(\beta\in\mathbb R\) such that every packet satisfies

\[
 \sum_{q=q_0}^{H}\sum_{T\in P_q(\pi)}\lambda_{q,T}
 \le
 \beta+\sum_{A\in P_{q_0}(\pi)}\alpha_A.
\tag{2.6}
\]

Then every size-\(s\) entrance matching satisfies

\[
 \boxed{
 \sum_q\widetilde E_q
 \ge
 \sum_{q,T}\lambda_{q,T}
 -\sum_A\alpha_A-s\beta
 -\sum_q(N_q-M)_+.}
\tag{2.7}
\]

Optimizing (2.7) is exactly the defect of the fractional relaxation of
(2.1)--(2.3).

#### Proof

For an integer load \(\mu\) and \(0\le\lambda\le1\),

\[
 \mathbf1_{\{\mu>0\}}\le1-\lambda+\lambda\mu.
\]

Sum this inequality over all targets and depths.  The selected packet
contribution is bounded using (2.6); entrance disjointness bounds the
\(\alpha\)-term by \(\sum_A\alpha_A\), and (2.2) gives \(s\beta\).
Subtract the resulting support upper bound from
\(\sum_q\min\{M,N_q\}\), obtaining (2.7).

For the converse, dualize (2.1), (2.2), the first inequality in (2.3),
and \(z\le1\).  The corresponding variables are
\(\alpha,\beta,\lambda,1-\lambda\), respectively.  The cover dual
variable may be truncated to \([0,1]\): replacing a value above one by
one only relaxes the packet constraint and does not increase the dual
objective.  This gives exactly (2.6)--(2.7), so finite-dimensional LP
duality proves the last assertion. \(\square\)

## 3. The ordinary catalogue has zero fractional defect

A rank-\((m-q)\) target belongs to exactly

\[
                         D_q=(m-q)!(m+q)!
\tag{3.1}
\]

directed cyclic packets modulo rotation.  Incidence counting gives

\[
 |\mathscr P|\,n=N_qD_q,
\qquad
 {D_q\over D_{q_0}}={N_{q_0}\over N_q}.
\tag{3.2}
\]

### Theorem 3.1 (simultaneous uniform fractional cover)

For every \(s\le N_{q_0}/n\), the fractional relaxation of
(2.1)--(2.3) has value

\[
                         \sum_{q=q_0}^{H}\min\{M,N_q\}.
\tag{3.3}
\]

Equivalently,

\[
 \boxed{\operatorname {Def}^{\rm frac}_{\rm ordinary}=0.}
\tag{3.4}
\]

#### Proof

Put

\[
 \theta={M\over N_{q_0}},\qquad
 x_\pi={\theta\over D_{q_0}}
 \quad(\pi\in\mathscr P).
\tag{3.5}
\]

Every entrance target has load \(\theta\le1\), while

\[
 \sum_\pi x_\pi
 ={|\mathscr P|\theta\over D_{q_0}}
 ={N_{q_0}\theta\over n}=s.
\]

At depth \(q\), every target has fractional load

\[
 D_qx_\pi={\theta D_q\over D_{q_0}}={M\over N_q}.
\]

Set

\[
                         z_{q,T}=\min\{1,M/N_q\}.
\]

This is feasible and its depth-\(q\) sum is \(\min\{M,N_q\}\), proving
(3.3).  No feasible solution can exceed that value, since
\(\sum_Tz_{q,T}\le N_q\) and also
\(\sum_Tz_{q,T}\le n\sum_\pi x_\pi=M\). \(\square\)

Thus the exact support LP for the ordinary problem has no mixed-depth
fractional or linear-dual obstruction.  Its entire difficulty is
integral correlated rounding.

## 4. The simple domino quotient and its component geometry

Assume \(R=2r+1\) is odd.  A simple domino necklace consists of unordered
blocks

\[
 B_i=\{b_i^0,b_i^1\}\qquad(i\in\mathbb Z_m)
\]

in one unoriented cyclic order.  Put

\[
                         C_i=B_i\cup\cdots\cup B_{i+r-1}.
\]

Its simple entrance atom is

\[
 \boxed{
 Q=\{C_i\cup\{z\}:
       i\in\mathbb Z_m,\ z\in B_{i-1}\cup B_{i+r}\}.}
\tag{4.1}
\]

It has \(4m=2n\) targets.

Choose an internal orientation
\(v=(v_i)\in\{0,1\}^m\), let
\(f_i(v)=b_i^{v_i}\) be the first member and
\(s_i(v)=b_i^{1-v_i}\) the second member, and let \(P_v\) be the
resulting ordinary cyclic packet.

### Lemma 4.1 (exact component intersection)

\[
 \boxed{
 |P_{q_0}(P_v)\cap P_{q_0}(P_w)|
 =2|\{i:v_i=w_i\}|.}
\tag{4.2}
\]

Hence two components of one simple \(Q\) are entrance-compatible if and
only if \(w=\bar v\), and their two decks then partition \(Q\).

#### Proof

Over the core \(C_i\), the component \(P_v\) has exactly the two targets

\[
 C_i\cup\{f_{i+r}(v)\},
 \qquad
 C_i\cup\{s_{i-1}(v)\}.
\tag{4.3}
\]

Every member of \(Q\) has a unique core \(C_i\), so targets with
different core indices cannot coincide.  At core \(i\), the two
components agree in the first target precisely when
\(v_{i+r}=w_{i+r}\), and in the second precisely when
\(v_{i-1}=w_{i-1}\).  Summing over \(i\) proves (4.2).
The intersection is empty exactly when every bit differs. \(\square\)

In particular, internal domino flips do not create new simple atoms:
all \(v\) give the same set (4.1).  Including cyclic anchoring and
dihedral presentation, every simple atom has the common fibre
multiplicity \(n2^m\).  This proves (0.6) and corrects the interpretation
of the one-domino flips as distinct physical columns.

The simple entrance set \(Q\) has \(2^{m-1}\) complementary component
decompositions and does not, by itself, determine a descendant deck.
For a chosen complementary pair define the lifted atom

\[
                         \widehat Q_v=(Q,\{P_v,P_{\bar v}\}).
\]

At depth \(q_0+1\), each chosen component has \(n\) targets and the two
components share exactly the \(m=n/2\) whole-domino cores \(C_i\).
Hence every lift satisfies

\[
 \boxed{
 |\operatorname {supp}(\widehat Q_v)_{q_0+1}|
 =2n-{n\over2}={3n\over2}.}
\tag{4.4}
\]

The same geometry gives the exact overlap at every odd relative depth.

### Lemma 4.2 (odd-depth twin intersection)

Let \(P_v,P_{\bar v}\) be complementary components of one simple
domino atom.  If \(q_0\le q\le H=o(m)\) and
\(d=q-q_0\) is odd, then, for all sufficiently large \(m\),

\[
 \boxed{
 |P_q(P_v)\cap P_q(P_{\bar v})|=m={n\over2}.}
\tag{4.5}
\]

#### Proof

Write \(R-d=2k\).  In the cyclic word

\[
 f_0(v),s_0(v),f_1(v),s_1(v),\ldots,
 f_{m-1}(v),s_{m-1}(v),
\]

the \(m\) length-\(2k\) intervals beginning at \(f_i(v)\) are exactly

\[
                         B_i\cup\cdots\cup B_{i+k-1}.
\tag{4.6}
\]

They are unchanged when \(v\) is replaced by \(\bar v\), so they are
common targets.  Every other length-\(2k\) interval in \(P_v\) has the
form

\[
 \{s_i(v)\}\cup B_{i+1}\cup\cdots\cup B_{i+k-1}
                 \cup\{f_{i+k}(v)\}.
\tag{4.7}
\]

Here \(2\le k\le m-2\) for all sufficiently large \(m\).  Hence the
set of wholly contained dominoes in (4.7)
determines its two boundary dominoes and its index \(i\).  The
corresponding non-whole interval for \(P_{\bar v}\) contains the
opposite member of each boundary domino, and hence is a different set.
It also cannot equal (4.6), since it contains exactly one member of each
of two boundary dominoes.  Thus (4.6) lists all common targets, proving
(4.5). \(\square\)

## 5. Linear fractional defect despite factorial overlap

Fix an arbitrary section \(Q\mapsto\widehat Q\) choosing one
complementary decomposition of every simple entrance atom.  Adapt
(2.1)--(2.3) to these lifted atoms, imposing entrance capacity through
their underlying simple supports \(Q\).  One lifted atom represents two
ordinary packets, so if \(\sum_{\widehat Q}x_{\widehat Q}=s_\square\),
put

\[
                         M=2ns_\square.
\tag{5.1}
\]

This fractional entrance system is nonempty at every \(M\le N_{q_0}\).
Indeed, if \(D\) is the underlying simple entrance degree, then
\(|\mathcal Q|\,2n=N_{q_0}D\), and the uniform value

\[
                         x_{\widehat Q}={M\over N_{q_0}D}
\]

has entrance load \(M/N_{q_0}\le1\) and total mass
\(M/(2n)=s_\square\).

For a fractional solution define its depth-\(q\) support deficit by

\[
 \operatorname {Def}^{\rm frac}_q
 =\min\{M,N_q\}-\sum_Tz_{q,T}.
\]

For an integral lifted selection with optimal \(z\), this is the ordinary
floor-correct repeat excess of its \(2s_\square\) component packets.

### Theorem 5.1 (lifted-twin fractional support cut)

Every fractional or integral selection of the lifted twin atoms satisfies

\[
 \boxed{
 \sum_Tz_{q_0+1,T}\le{3M\over4},\qquad
 \operatorname {Def}^{\rm frac}_{q_0+1}
 \ge\min\{M,N_{q_0+1}\}-{3M\over4}.}
\tag{5.2}
\]

#### Proof

Sum the covering constraint over all depth-one targets and use (4.4):

\[
 \sum_Tz_{q_0+1,T}
 \le\sum_{\widehat Q}x_{\widehat Q}
       |\operatorname {supp}(\widehat Q)_{q_0+1}|
 ={3n\over2}s_\square={3M\over4}.
\]

Subtract this from the scalar maximum
\(\min\{M,N_{q_0+1}\}\). \(\square\)

This is also the explicit dual obtained by applying Theorem 2.2 to the
one-depth restriction \(q=q_0+1\): take
\(\lambda_{q_0+1,T}=1\), every other \(\lambda=0\),
\(\alpha=0\), and \(\beta=3n/2\).

At critical mass,

\[
 M=N_{q_0}-O(N_{q_0}/\sqrt m),
\]

while

\[
 N_{q_0}-N_{q_0+1}
 =N_{q_0}{2q_0+1\over m+q_0+1}
 =O_a(N_{q_0}/\sqrt m).
\]

Substitution in (5.2) proves (0.5).  No integral lifted-twin near-factor
is needed: the descendant-support failure is already fractional.

### Theorem 5.2 (factorial-overlap separation)

For every fixed \(C_0\), the correctly quotiented simple twin catalogue
still satisfies, uniformly for \(p\le C_0\log m\),

\[
 {1\over D}\sum_{\substack{F'\ni X\\F'\ne F}}
 (|F\cap F'|-1)_p
 \le(Cp)^{Cp}m^{-2}.
\tag{5.3}
\]

Thus the entrance supports of the lifted catalogue satisfy (5.3) while
their linear fractional descendant defect (0.5) holds simultaneously.

#### Proof

The labelled factorial theorem counts anchored representations.  Every
simple atom has exactly the same \(\mu=n2^m\) anchored preimages.  Fix a
simple \(F\) and discard from the labelled sum the entire parallel fibre
lying over \(F\).  The remaining labelled sum is exactly \(\mu\) times
the simple sum over \(F'\ne F\), while the labelled degree is
\(\mu D\).  Division preserves the normalized ratio, and discarding the
nonnegative parallel-fibre terms can only decrease it.  Apply the proved
labelled bound. \(\square\)

The factorial hierarchy controls overlap between entrance atoms through
one entrance target.  It contains no term for the unary descendant
support loss (4.4) inside one lifted atom.  Theorem 5.1 proves that these
entrance-overlap hypotheses alone do not control descendant support, even
before integral rounding or stopped residuals enter.  It does not rule
out an ordinary-packet theorem using additional chronology.

## 6. A genuine deterministic anti-twin charge for ordinary packets

In an ordinary entrance matching \(\mathcal M\), call two selected
packets an exact twin pair when they are the complementary components
of one simple atom \(Q\).  Let \(t\) be the maximum number of
vertex-disjoint exact twin pairs contained in \(\mathcal M\).

### Theorem 6.1 (all-depth anti-twin charge)

At every odd relative depth \(d=q-q_0\),

\[
 \boxed{
 \widetilde E_q
 \ge {nt\over2}-(M-N_q)_+.}
\tag{6.1}
\]

Consequently, at critical mass, the condition
\(\sum_q\widetilde E_q=o(W)\) forces

\[
                              t=o(W/n).
\tag{6.2}
\]

#### Proof

At every odd relative depth, the two packets in one twin pair have
\(n/2\) common targets.  For a target \(T\), let \(k_T\) be the number
of the chosen vertex-disjoint twin pairs whose two members both contain
\(T\).  The selected packet occurrences used by different chosen pairs
are distinct, so

\[
                         \mu_q(T)\ge2k_T.
\]

If \(k_T>0\), then

\[
                         (\mu_q(T)-1)_+\ge2k_T-1\ge k_T.
\]

Summing over targets gives

\[
 \sum_T(\mu_q(T)-1)_+
 \ge\sum_Tk_T={nt\over2}.
\]

Subtract the forced floor \((M-N_q)_+\), proving (6.1).

At \(q=q_0+1\), critical entrance mass gives
\((M-N_q)_+=O_a(W/\sqrt m)=o(W)\).  If \(t\) were not \(o(W/n)\), the
right side of (6.1) would be \(\Omega(W)\), contradicting the assumed
aggregate \(o(W)\) bound. \(\square\)

Thus a positive trajectory needs a macroscopic anti-twin quarantine.
The static factorial estimate (5.3) does not imply (6.2): it is a
statement about overlaps of simple entrance atoms, whereas (6.2) concerns
simultaneous selection of both ordinary components inside one atom.

There is an equivalent fibre-occupancy form.  Let \(c_Q\) be the number
of selected component traces belonging to a simple atom \(Q\).  Lemma
4.1 gives \(c_Q\le2\).  Join two selected packets when they are the two
components of a double-occupied \(Q\), and put

\[
                         t_\square=\sum_Q(c_Q-1)_+.
\]

Every ordinary packet trace belongs to exactly two simple domino atoms,
so this twin graph has maximum degree at most two.  At an odd relative
depth, let \(e_T\) be the number of its edges whose two endpoint packets
both realize \(T\).  Then \(e_T\le\mu_q(T)\), and for
\(\mu_q(T)\ge2\),

\[
 (\mu_q(T)-1)_+\ge{\mu_q(T)\over2}\ge{e_T\over2}.
\]

Every twin edge has \(n/2\) common targets.  Summing first over targets
and then over twin edges gives the robust form

\[
 \boxed{
 \widetilde E_q
 \ge {nt_\square\over4}-(M-N_q)_+
 \qquad(d\ {\rm odd}).}
\tag{6.3}
\]

It follows at \(d=1\) that every critical matching with joint excess
\(o(W)\) satisfies

\[
                         t_\square=o(W/n)
\tag{6.4}
\]

as well.

There is a concrete way to remove this exact obstruction before any
slow bite begins.

### Proposition 6.2 (capacity-one twin-fibre augmentation)

Attach to each ordinary packet trace \(P\) the two simple domino atoms
\(Q^{(0)}(P),Q^{(1)}(P)\) obtained from the two perfect matchings of
adjacent positions on its even coordinate cycle.  Augment the entrance
edge of \(P\) by these two fibre labels, each of capacity one.

Then:

1. every matching in the augmented hypergraph is an ordinary entrance
   matching with \(c_Q\le1\) for every simple twin fibre;
2. for a fixed packet trace \(P\), the new labels forbid exactly its two
   complementary domino-twin traces among traces which were otherwise
   entrance-compatible with \(P\); every other component trace in the
   same \(Q\) already meets \(P\) at the entrance (in the directed
   presentation these are four columns, two orientations of each
   complementary trace); and
3. the uniform ordinary fractional point retains slack at every new
   label: in the directed catalogue used here a simple \(Q\) has
   \(2^{m+1}\) component presentations, so its new-label load is
   \(2^{m+1}\theta/D_{q_0}=o(1)\).

#### Proof

Every ordinary component trace belongs to exactly the two simple fibres
coming from the two alternating position matchings.  Capacity one is
therefore equivalent to \(c_Q\le1\).  Inside one fibre, Lemma 4.1 says
that the only component entrance-disjoint from \(P_v\) is
\(P_{\bar v}\).  Hence the new label adds only that formerly legal
conflict, once for each of the two fibres.  Finally

\[
 \log D_{q_0}=\Theta(m\log m),\qquad \log 2^m=\Theta(m),
\]

so the displayed fractional label load tends to zero. \(\square\)

This augmentation removes the exact domino-twin obstruction at constant
added edge size and negligible fractional load.  It does not control
nonexact common-descendant correlations and therefore does not prove the
mixed-depth rounding theorem.

## 7. Exact remaining theorem

The ordinary fractional point in Theorem 3.1 is already perfectly
synchronized.  The missing theorem is solely its integral rounding:

> **Mixed-depth ordinary-packet rounding (unproved).**  At critical
> \(s=N_{q_0}/n-O(N_{q_0}/(n\sqrt m))\), the program
> (2.1)--(2.3) has an integral solution whose objective is within
> \(o(W)\) of its fractional optimum.

A sufficient, trajectory-level formulation from Theorem 1.1 is to
construct a decision tree on legal extendible ordinary packets such that
at every visited state there is a distribution \(\Pi_t\) satisfying

\[
 \mathbb E_{\pi\sim\Pi_t}
 \sum_{q=q_0}^{H}Z_{q,t}(\pi)
 \ge
 \sum_{q=q_0}^{H}c_{q,t}-\varepsilon_t,
\qquad
 \sum_t\varepsilon_t=o(W).
\tag{7.1}
\]

This is a stopped descendant-hole incidence statement.  It is not a
consequence of time-zero entrance factorial overlap, and Theorem 5.1
shows that no theorem using only those factorial hypotheses can supply
it for locally similar catalogues.

## 8. Proved boundary

Proved:

1. the exact correlated fresh-target identity for one entrance matching;
2. the exact mixed-depth integer program and its support dual;
3. zero fractional defect for the full ordinary catalogue at every depth
   simultaneously;
4. the exact simple-domino component intersection formula;
5. the correction of internal domino flips from distinct columns to one
   representation fibre;
6. a linear fractional descendant-support deficit for every
   complementary-decomposition lift of the simple twin entrance
   catalogue;
7. coexistence of that deficit with the full logarithmic factorial
   overlap hierarchy; and
8. the deterministic anti-twin charge (6.1).

Not proved:

1. an integral critical ordinary-packet matching satisfying
   \(\sum_q\widetilde E_q=o(W)\);
2. a stopped fresh-target distribution satisfying (7.1);
3. an \(o(W)\) integrality-gap bound for (2.1)--(2.3); or
4. coefficient one.

The domino factorial theorem is therefore a valid static entrance
estimate but not an annulus synchronization theorem.  The first new
input must either control the stopped descendant hole array or use
additional ordinary-packet structure which excludes the lifted-twin
failure.  In either case, along the selected trajectory it must at least
force the quantitative anti-twin condition
\(t_\square=o(W/n)\); capacity-one exclusion is sufficient but is not
claimed necessary.
