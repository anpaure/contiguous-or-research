# Deterministic carrier-rotor trajectories: gap permutations, exact rainbows, and the common-path gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, random search, or
web input is used.

## 0. Outcome

This note gives a positive deterministic trajectory theorem and two sharp
architecture obstructions.  It does not yet prove coefficient one.

At the truncated carrier scale, let

\[
 n=2m,\qquad M=m+H,\qquad
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

where \(H\) is the calibrated crossing height, and let

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil,
 \qquad \gamma\to\infty,\quad \gamma=o(\log\log m).
\tag{0.2}
\]

Thus

\[
 Q=o(H),\qquad H=(1+o(1))\sqrt{m\log m},qquad
 T:=MN=W-o(W).
\tag{0.3}
\]

The proved advances are as follows.

1. A permutation \(\rho\) of the \(M\) cyclic time phases, whose forward
   gaps have total winding \(HM\), determines an exact cyclic owner path.
   If every gap lies strictly between \(Q\) and \(M/2-Q\), the owner path
   has a unique radius-\(Q\) carrier-rotor lift and is **exactly rainbow at
   every lower and upper rank through depth \(Q\)**.
2. Zero-winding bounded-displacement perturbations of the ordinary cyclic
   schedule give a large explicit non-AP subfamily.  Already the commuting
   adjacent-switch cube supplies \(2^{\lfloor M/2\rfloor}\) exactly
   rainbow trajectories for every labelled carrier.
3. After symmetrizing over carrier labellings and one common priority order,
   this deterministic catalogue gives an exact tag-saturating fractional
   matching with every calibrated target load at most one and total scalar
   leave \(o(W)\).  Every separate-rank Hall inequality also holds
   integrally.
4. The remaining assertion is only the simultaneous common-trajectory
   matching.  A matching missing
   \(e=o(W/m^{3/2})\) carriers would prove the truncated path theorem and
   hence coefficient one.
5. A polynomial affine/translation **departure atlas** cannot work, even
   if every departure order is equipped with all exponentially many
   admissible arrival switches.  Such a family covers only \(o(1)\) of the
   middle row.  More generally, a polynomial ambient atlas needs
   \(\Omega(H/\log m)\) run complexity in every exposed target.
6. At prime carrier size, a genuinely affine time permutation satisfying
   the rainbow gap conditions collapses to the ordinary cyclic schedule.
   The non-AP freedom is necessarily nonaffine and top-intrinsic.  No fully
   equivariant exact factor is asserted, so the known prime equivariance
   obstruction is respected.

## 1. Gap-permutation owner cycles

Fix one carrier \(U\), \(|U|=M\), and a cyclic labelling

\[
 U=\{u_c:c\in\mathbb Z_M\}.
\tag{1.1}
\]

The coordinate \(u_c\) will depart from the owner at transition \(c\).
Let \(\rho\in S(\mathbb Z_M)\), and let

\[
 \Delta_c=[\rho(c)-c]_M\in\{1,\ldots,M-1\}
\tag{1.2}
\]

be its positive forward cyclic gap.  The coordinate \(u_c\) returns to the
owner at transition \(\rho(c)\).

For a cyclic interval, \((a,b]\) means the time phases strictly after
\(a\) through and including \(b\).  Define the hole set and owner at state
time \(s\) by

\[
 B_s=\{u_c:s\in(c,\rho(c)]\},
 \qquad X_s=U\setminus B_s.
\tag{1.3}
\]

### Theorem 1.1 (exact winding construction)

Assume

\[
 \boxed{\sum_{c\in\mathbb Z_M}\Delta_c=HM.}
\tag{1.4}
\]

Then every \(B_s\) has size \(H\), every \(X_s\) has size \(m\), and

\[
 \boxed{
 X_{s+1}=X_s-u_s+u_{\rho^{-1}(s)}.}
\tag{1.5}
\]

The nonresidence and residence runs of \(u_c\) have exact lengths

\[
 \Delta_c,qquad M-\Delta_c.
\tag{1.6}
\]

#### Proof

Passing from state \(s\) to \(s+1\), exactly the interval beginning at
\(s\) becomes active and exactly the interval ending at \(s\) ceases to be
active.  Therefore

\[
 B_{s+1}=B_s+u_s-u_{\rho^{-1}(s)}.
\tag{1.7}
\]

The two coordinates are distinct because every gap in (1.2) is nonzero.
Thus \(|B_s|\) is independent of \(s\).  On the other hand, double
counting pairs \((c,s)\) with \(s\in(c,\rho(c)]\) gives

\[
 \sum_s|B_s|=\sum_c\Delta_c=HM.
\]

Hence \(|B_s|=H\).  Taking complements in (1.7) proves (1.5), and the
definition (1.3) gives (1.6). \(\square\)

### Theorem 1.2 (exact radius-\(Q\) rotor lift)

If

\[
 \Delta_c\ge Q+1,qquad M-\Delta_c\ge Q+1
 \quad\text{for every }c,
\tag{1.8}
\]

then the owner cycle in Theorem 1.1 has a unique quotient
carrier-rotor lift of radius \(Q\).

At time \(t\), its state is

\[
 z_{t,i}=u_{t+Q-i}\quad(1\le i\le2Q),
\tag{1.9}
\]

\[
 L_t=X_t\setminus\{u_t,u_{t+1},\ldots,u_{t+Q-1}\},
\tag{1.10}
\]

\[
 R_t=(U\setminus X_t)
 \setminus\{u_{t-1},u_{t-2},\ldots,u_{t-Q}\}.
\tag{1.11}
\]

The transition choices are

\[
 x_t=u_{t+Q},
 \qquad y_t=u_{\rho^{-1}(t)}.
\tag{1.12}
\]

#### Proof

The residence bounds show that the \(Q+1\) future departures
\(u_t,\ldots,u_{t+Q}\) are distinct members of \(X_t\).  The
nonresidence bounds show that the preceding departures
\(u_{t-1},\ldots,u_{t-Q}\) and the current arrival \(y_t\) lie in the
carrier tail, with \(y_t\) distinct from those preceding departures.
Thus (1.9)--(1.12) have the required block sizes and legal choices.

Substitution into the quotient rotor recurrence gives

\[
 (L_t;z_{t,1},\ldots,z_{t,2Q};R_t)
 \longmapsto
 (L_t-x_t+y_t;x_t,z_{t,1},\ldots,z_{t,2Q-1};
  R_t-y_t+z_{t,2Q}),
\]

which is precisely the state at \(t+1\).  Conversely, the queue delay
forces (1.9), and then (1.10)--(1.11) are forced by the owner and the state
partition. \(\square\)

The exposed flags have the path formulas

\[
 L_q(t)=\bigcap_{i=0}^qX_{t+i}
 =X_t\setminus\{u_t,\ldots,u_{t+q-1}\},
\tag{1.13}
\]

\[
 U_q(t)=\bigcup_{i=0}^qX_{t-i}
 =X_t\cup\{u_{t-1},\ldots,u_{t-q}\},
\tag{1.14}
\]

for \(0\le q\le Q\).

## 2. A simultaneous exact-rainbow theorem

We first isolate the elementary circular-order fact which controls all
depths at once.

For a permutation \(\theta\) of \(\mathbb Z_M\), put

\[
 C_s(\theta)=\{c:s\in(c,\theta(c)]\}.
\tag{2.1}
\]

### Lemma 2.1 (interval invariance criterion)

For distinct times \(s,t\),

\[
 C_s(\theta)=C_t(\theta)
\tag{2.2}
\]

if and only if the proper cyclic interval \(I=[s,t)\) is invariant under
\(\theta\).

#### Proof

For a coordinate \(c\), the indicators of
\(s\in(c,\theta(c)]\) and \(t\in(c,\theta(c)]\) differ exactly when one of
\(c,\theta(c)\) lies in \(I\) and the other does not.  Equality for every
\(c\) is therefore equivalent to

\[
 c\in I\iff\theta(c)\in I,
\]

which is \(\theta(I)=I\). \(\square\)

### Lemma 2.2 (short-forward permutations preserve no interval)

If every forward gap of \(\theta\) lies strictly between \(0\) and
\(M/2\), then \(\theta\) preserves no nonempty proper cyclic interval.

#### Proof

If \(I\) were invariant, so would its complement.  Choose the shorter of
the two, call it \(J\), so \(|J|\le M/2\), and rotate it to a linear
interval.  The restriction of \(\theta\) to \(J\) is a permutation.
Every cycle in this restriction contains a descending edge in the linear
order unless it is a fixed point.  A fixed point has forward gap zero,
while a descending edge has forward cyclic gap at least

\[
 M-(|J|-1)>M/2.
\]

Both alternatives contradict the hypothesis. \(\square\)

### Theorem 2.3 (gap-permutation simultaneous rainbow)

In addition to (1.4), assume the exact gap bounds

\[
 \boxed{
 Q<\Delta_c<M/2-Q
 \quad\text{for every }c.}
\tag{2.3}
\]

Then the unique carrier-rotor trajectory of Theorem 1.2 is internally
injective at every controlled rank:

\[
 t\longmapsto L_q(t),qquad
 t\longmapsto U_q(t)
\tag{2.4}
\]

are injective for every \(0\le q\le Q\).

#### Proof

For the lower flag, (1.13) and complements give

\[
 U\setminus L_q(t)
 =\bigcup_{i=0}^qB_{t+i}
 =\{u_c:t\in(c-q,\rho(c)]\}.
\tag{2.5}
\]

Relabel \(d=c-q\) and put

\[
 \theta_q^-(d)=\rho(d+q).
\tag{2.6}
\]

Its forward gap is \(\Delta_{d+q}+q\), which by (2.3) lies strictly in
\((0,M/2)\).  Equality of lower flags at two distinct times would, by
Lemma 2.1 after this relabelling, force \(\theta_q^-\) to preserve a proper
cyclic interval.  Lemma 2.2 forbids this.

For the upper flag,

\[
 U\setminus U_q(t)
 =\bigcap_{i=0}^qB_{t-i}
 =\{u_c:t\in(c+q,\rho(c)]\}.
\tag{2.7}
\]

Relabel \(d=c+q\) and put

\[
 \theta_q^+(d)=\rho(d-q).
\tag{2.8}
\]

Its forward gap is \(\Delta_{d-q}-q\), again strictly in \((0,M/2)\).
The same two lemmas rule out a repetition. \(\square\)

Thus the theorem supplies ordinary support incidence, not merely
occurrence multiplicity: every trajectory uses \(M\) distinct targets in
each controlled rank.

## 3. Zero-winding bounded-displacement schedules

The ordinary cyclic packet corresponds to

\[
 \rho_0(c)=c+H.
\tag{3.1}
\]

Let \(\sigma\in S(\mathbb Z_M)\) have unique signed displacements

\[
 \sigma(c)\equiv c+\varepsilon_c\pmod M,
 \qquad |\varepsilon_c|\le D<M/2,
\tag{3.2}
\]

and impose the exact zero-winding condition

\[
 \sum_c\varepsilon_c=0.
\tag{3.3}
\]

Put

\[
 \rho=T_H\circ\sigma,
 \qquad \rho(c)=\sigma(c)+H.
\tag{3.4}
\]

### Corollary 3.1 (banded exact-rainbow rotors)

If

\[
 \boxed{
 H-D>Q,
 \qquad H+D<M/2-Q,}
\tag{3.5}
\]

then (3.4) satisfies Theorem 2.3.  Hence it gives a literal, simultaneous
exact-rainbow radius-\(Q\) trajectory.

Moreover, if \(I_q^\pm(t)\) denotes the corresponding flag of the ordinary
cyclic packet, then

\[
 \boxed{
 d_J(L_q(t),I_q^-(t))\le D,
 \qquad d_J(U_q(t),I_q^+(t))\le D}
\tag{3.6}
\]

uniformly for \(q\le Q\).

#### Proof

The forward gap in (3.4) is

\[
 \Delta_c=H+\varepsilon_c.
\]

Its sum is \(HM\) by (3.3), and (3.5) is exactly (2.3).

A coordinate can differ from the ordinary cyclic owner only at a time cut
between its old arrival phase \(c+H\) and its displaced arrival phase
\(c+H+\varepsilon_c\).  At a fixed time there are at most \(2D\) such
coordinates, so the owner Johnson distance is at most \(D\).  Formulas
(1.13)--(1.14) delete or add the same departure blocks in the perturbed and
unperturbed paths, proving (3.6). \(\square\)

At the calibrated scales, (3.5) permits every

\[
 D<H-Q.
\tag{3.7}
\]

The second inequality is automatic because \(H+D=o(M)\).

### Corollary 3.2 (explicit non-AP switch cubes)

Fix the disjoint adjacent phase pairs

\[
 (0,1),(2,3),\ldots.
\]

Independently fix or transpose every pair.  Each of the resulting

\[
 \boxed{2^{\lfloor M/2\rfloor}}
\tag{3.8}
\]

permutations has \(D=1\) and zero winding, so every one gives a
simultaneous exact-rainbow trajectory for all sufficiently large \(m\).

A nontrivial switch changes two gap lengths from \(H,H\) to
\(H+1,H-1\).  Therefore its coordinate residence/nonresidence multiset is
not that of any cyclic packet; these paths are genuinely non-AP.

More generally, partition a linear set of phases into blocks of length
\(D+1\), permute independently inside every block, and fix the remainder.
This gives at least

\[
 ((D+1)!)^{\lfloor M/(D+1)\rfloor}
 =\exp(\Theta(M\log D))
\tag{3.9}
\]

zero-winding \(D\)-banded trajectories.

Adjacent toggles are literal two-step arrival diamonds.  A toggle changes
one intermediate owner occurrence and, at that same state, one target in
each signed controlled rank; the two paths agree at all other state
positions.  After relabelling the carrier, every oriented Johnson-adjacent
owner exchange occurs in this way.  Thus the owner projection has unit
integral exchanges, with the unavoidable complete vertical flag string as
counterterm.

## 4. Exact symmetric catalogue and all marginal Hall cuts

Let \({\cal P}_D(U)\) contain all schedules from a fixed nonempty admissible
set of gap permutations, all bijective labellings
\(\mathbb Z_M\to U\), and all priority orders of the \(M\) times.  Columns
are kept with their labelled multiplicities.  Let

\[
 R_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{4.1}
\]

Define the nested claimed-phase counts by

\[
 c_0=M,
 \qquad
 c_q=\min\left\{M,\left\lfloor\frac{R_q}{N}\right\rfloor\right\}
 \quad(1\le q\le Q).
\tag{4.2}
\]

At both signed depth-\(q\) rows, claim the first \(c_q\) times in the one
common priority order.  The counts are nonincreasing in \(q\), so the
claims retain one common nested column.

Let \(A=|{\cal P}_D(U)|\), which is independent of \(U\).

### Theorem 4.1 (exact catalogue degrees)

Every carrier tag has degree \(A\).  For a fixed target
\(S\in\binom{[2m]}{m\pm q}\), its global degree is

\[
 \boxed{
 D_q(S)=A\,\frac{c_qN}{R_q}.}
\tag{4.3}
\]

In particular, assigning weight \(1/A\) to every decorated catalogue
column gives a fractional matching which saturates every carrier tag and
has target load

\[
 \boxed{\frac{c_qN}{R_q}\le1.}
\tag{4.4}
\]

At the owner rank this load is

\[
 \frac{MN}{W}=1-o(1).
\tag{4.5}
\]

#### Proof

Coordinate relabelling makes the catalogue invariant under the full
permutation group of \(U\).  Internal rainbowness and priority symmetry
therefore give local target degree

\[
 \frac{Ac_q}{\binom M{m\pm q}}.
\tag{4.6}
\]

A fixed target is contained in
\(\binom{2m-(m\pm q)}{M-(m\pm q)}\) carriers.  The containment identity

\[
 N\binom M{m\pm q}
 =R_q\binom{2m-(m\pm q)}{M-(m\pm q)}
\tag{4.7}
\]

turns (4.6) into (4.3).  Equations (4.4)--(4.5) follow. \(\square\)

### Proposition 4.2 (the scalar leave is \(o(W)\))

The exact fractional scalar leave of the claimed system is

\[
 \boxed{
 W-MN+2\sum_{q=1}^Q(R_q-c_qN)=o(W).}
\tag{4.8}
\]

#### Proof

At a noncapped depth, \(c_q=\lfloor R_q/N\rfloor\), so
\(0\le R_q-c_qN<N\).  Their total contribution is

\[
 O(QN)=O(QW/m)=o(W).
\tag{4.9}
\]

At a capped depth, \(c_q=M\).  Such depths satisfy
\(R_q\ge MN=T\).  The crossing estimate

\[
 W-T=O(WH/m)
\tag{4.10}
\]

and the central-binomial expansion imply that this can occur only for
\(q=O(\sqrt H)\).  Each capped deficit is at most \(W-T\), so their total
is

\[
 O\left(\frac{WH^{3/2}}m\right)=o(W).
\tag{4.11}
\]

The middle deficit is (4.10). \(\square\)

### Theorem 4.3 (every separate-rank Hall inequality)

For every carrier family \({\cal C}\subseteq\binom{[2m]}M\), and every
controlled rank \(r=m\pm q\),

\[
 \boxed{
 |N_r({\cal C})|
 \ge\frac{R_q}{N}|{\cal C}|
 \ge c_q|{\cal C}|.}
\tag{4.12}
\]

At the middle rank, the last term is \(M|{\cal C}|\).

Consequently, for each rank separately, there is an integral assignment of
\(c_q\) distinct rank-\(r\) targets to every carrier, with no target used
twice.

#### Proof

Because all coordinate labellings are allowed, every rank-\(r\) subset of
a carrier occurs as a flag in some catalogue path.  Count containment
edges between \({\cal C}\) and its rank-\(r\) shadow.  Every carrier has
degree \(\binom Mr\), while a target lies in at most
\(\binom{2m-r}{M-r}\) carriers.  Hence

\[
 |N_r({\cal C})|
 \ge
 \frac{\binom Mr}{\binom{2m-r}{M-r}}|{\cal C}|
 =\frac{R_q}{N}|{\cal C}|.
\]

Generalized Hall, after cloning every carrier \(c_q\) times, gives the
assignment. \(\square\)

Theorem 4.3 is deliberately **unbundled**.  The independently assigned
targets at different ranks and carriers need not be the flags of one
common trajectory.  It proves that no individual row, scalar capacity, or
ordinary Hall cut is the remaining obstruction.

## 5. The exact common-trajectory theorem still missing

One decorated trajectory claims

\[
 K_Q=M+2\sum_{q=1}^Qc_q
 = (\sqrt\pi+o(1))m^{3/2}.
\tag{5.1}
\]

The last equality follows from

\[
 \frac{R_q}{N}
 =\frac{\lambda_H}{\lambda_q}
 =(1+o(1))M e^{-q^2/m}
\]

and \(Q/\sqrt m\to\infty\).

### Deterministic banded-rotor assignment theorem (open)

Choose one decorated trajectory from \({\cal P}_D(U)\) for every carrier
\(U\), so that no claimed target is used twice, apart from trajectories on
at most

\[
 \boxed{e=o(W/m^{3/2})}
\tag{5.2}
\]

exceptional carriers.

### Proposition 5.1 (the open theorem implies coefficient one)

If the assignment theorem holds, fill the exceptional carriers
arbitrarily.  Their additional target collision/leave contribution is at
most

\[
 eK_Q=o(W).
\tag{5.3}
\]

The selected nonexceptional paths have disjoint claimed targets.  By
Proposition 4.2 their remaining scalar leave is \(o(W)\).  Hence the
truncated carrier-rotor path theorem holds.  The audited outer reservoir
and tails then give

\[
 \nu(2m)\le W+o(W),
\]

and the standard lift gives the odd case. \(\square\)

On a free group quotient, if \(\Gamma=|G|\), the exact quotient leave
required in (5.2) is

\[
 e=o\left(\frac{W}{\Gamma m^{3/2}}\right).
\tag{5.4}
\]

Theorem 4.1 supplies an exact fractional point, and Theorem 4.3 closes
every separate-rank Hall cut.  Neither statement implies the common-path
integral matching.  Any remaining obstruction is genuinely cross-rank and
chronological.

## 6. Affine rigidity and ambient-atlas obstructions

### Theorem 6.1 (prime affine schedules collapse)

Let \(M=p\) be prime, and suppose

\[
 \rho(c)=ac+b\qquad(c\in\mathbb F_p)
\tag{6.1}
\]

is an affine permutation satisfying the gap hypotheses (1.4) and (2.3).
Then

\[
 \boxed{a=1,qquad b=H,}
\tag{6.2}
\]

so \(\rho(c)=c+H\) is the ordinary cyclic trajectory.

#### Proof

If \(a\ne1\), the differences

\[
 \rho(c)-c=(a-1)c+b
\]

run through every residue, including zero.  This contradicts the strict
positive gap condition.  Thus \(a=1\).  Every forward gap is then the same
integer \(b\in(0,p/2)\), and (1.4) gives \(pb=Hp\), hence \(b=H\).
\(\square\)

Thus direct affine time dynamics supplies no new path even before the
global prime-equivariant factor obstruction is reached.  The switch cubes
of Section 3 are necessarily nonaffine.  They are chosen locally on free
carrier orbits and do not assert a fully invariant exact factor.

### Theorem 6.2 (departure-atlas support obstruction)

Suppose every selected trajectory has a permutation departure order which
is the restriction to its carrier of one of \(K\) ambient cyclic orders.
Assume every owner coordinate has nonresidence at least \(Q+1\), as every
radius-\(Q\) cyclic rotor lift does.

Let \({\cal S}_r^\pm\) be the possible signed rank supports.  Then

\[
 |{\cal S}_m|
 \le K(2m)\binom{2m-Q}{m},
\tag{6.3}
\]

\[
 |{\cal S}_{m-q}^-|
 \le K(2m)\binom{2m-Q}{m-q},
\tag{6.4}
\]

and

\[
 |{\cal S}_{m+q}^+|
 \le K(2m)\binom{2m-(Q-q)}{m+q}.
\tag{6.5}
\]

#### Proof

At state \(t\), the preceding \(Q\) departure coordinates

\[
 u_{t-Q},\ldots,u_{t-1}
\]

are all absent from the owner.  They are consecutive in the restricted
departure order, so the corresponding ambient arc contains a consecutive
\(Q\)-block avoiding the owner.  Every lower flag is a subset of that
owner, proving (6.3)--(6.4).

The upper depth-\(q\) flag restores only the most recent \(q\) departures.
The older \(Q-q\) departures remain absent and consecutive, proving (6.5).
There are \(2m\) possible ambient blocks per order, and a fixed block of
length \(L\) is avoided by \(\binom{2m-L}r\) rank-\(r\) sets. \(\square\)

Uniformly for \(q\le Q=o(m)\),

\[
 \frac{\binom{2m-L}{m\pm q}}{\binom{2m}{m\pm q}}
 \le\exp\bigl(- (\log2-o(1))L\bigr).
\tag{6.6}
\]

Therefore, if \(\log K=o(Q)\), the atlas covers only \(o(1)\) of the
middle row and every lower controlled row.  It also covers only \(o(1)\)
of each upper row \(q\le(1-\varepsilon)Q\), for every fixed
\(\varepsilon>0\).

In particular, choosing affine sorting parameters separately for every
carrier still uses at most

\[
 2m\,\varphi(2m)\le(2m)^2
\tag{6.7}
\]

ambient departure orders.  It fails even if every such departure order is
equipped with all \(2^{\Theta(M)}\) arrival-switch choices from Section 3.
Arrival entropy cannot compensate for a low-complexity departure atlas.

### Corollary 6.2a (internal rainbow plus one path per carrier can fail)

Fix one ambient cyclic order and, on every carrier, take the ordinary
cyclic rotor induced by restricting that order.  This is a deterministic
one-trajectory-per-carrier assignment, and every trajectory is exactly
rainbow at every proper rank.  Nevertheless Theorem 6.2 with \(K=1\)
gives

\[
 \frac{|{\cal S}_m|}{W}
 \le 2m\,2^{-Q}=o(1).
\tag{6.8a}
\]

Thus internal simultaneous rainbowness and literal assignment of one path
to every carrier do not even imply a positive-density middle cover.  The
missing property is cross-carrier dispersion of the departure orders.

### Theorem 6.3 (multirun ambient obstruction)

Let \(\Sigma\) be \(K\) ambient cyclic orders.  Suppose every possible
rank-\(r\) target is a union of at most \(b\) intervals in
\(\sigma|_U\) for some \(\sigma\in\Sigma\).  Put

\[
 d=M-r,
 \qquad s=\left\lceil\frac db\right\rceil.
\tag{6.8}
\]

Then

\[
 \boxed{
 |\operatorname {supp}_r|
 \le K(2m)\binom{2m-s}{r}.}
\tag{6.9}
\]

#### Proof

The complement \(U\setminus S\), of size \(d\), has at most \(b\)
interval components in the restricted order.  One component contains at
least \(s\) carrier coordinates.  Its ambient arc is disjoint from \(S\)
and contains an ambient consecutive \(s\)-block.  Count the avoided block
as in Theorem 6.2. \(\square\)

For \(r=m\pm q\), \(q\le Q=o(H)\), this gives

\[
 \frac{|\operatorname {supp}_r|}{R_q}
 \le K(2m)
 \exp\left[-(\log2-o(1))
 \left\lceil\frac{H-Q}{b}\right\rceil\right].
\tag{6.10}
\]

Hence a polynomial ambient atlas requires

\[
 \boxed{b=\Omega(H/\log m).}
\tag{6.11}
\]

If a target lies within Johnson distance \(D\) of one induced interval,
it has at most \(2D+1\) runs.  Thus bounded-displacement arrival
perturbations with

\[
 D=o(H/\log m)
\tag{6.12}
\]

cannot rescue a polynomial ambient base atlas.  The gap-permutation theorem
does permit \(D\asymp H/\log m\) while remaining exactly rainbow, but
Theorem 6.2 still forces the departure orders themselves to be
carrier-contextual.

## 7. Adversarial audit and exact boundary

The strongest positive statement is Theorems 2.3 and 4.1:

* every catalogue path is literal and exactly rainbow simultaneously at
  all controlled ranks;
* the deterministic catalogue has the exact calibrated fractional loads;
* every separate row admits an integral Hall assignment.

These facts do **not** choose one common trajectory per carrier.  The open
matching in Section 5 is not a consequence of separate Hall, pair balance,
or path abundance.

The strongest negative statement is Theorem 6.2.  It shows that even all
exponentially many arrival permutations over polynomially many affine
departure orders leave \((1-o(1))W\) middle owners uncovered.  Thus
internal rainbowness, one path per carrier, and enormous local switch
entropy can coexist with catastrophic global support.

There is no conflict with the known prime equivariance obstruction:

* Theorem 6.1 says direct affine phase dynamics already collapses to the
  ordinary cyclic path.
* The positive catalogue is top-intrinsic and nonaffine.
* No exact fully invariant factor is claimed; a free group quotient would
  still require the matching leave (5.4) and symmetry-breaking repair on
  the negligible stabilizer sector.

Accordingly, the smallest surviving coefficient-one statement is the
common-path matching (5.2).  All internal chronology, self-collision,
scalar capacity, and separate-rank Hall issues are closed for this
deterministic catalogue.
