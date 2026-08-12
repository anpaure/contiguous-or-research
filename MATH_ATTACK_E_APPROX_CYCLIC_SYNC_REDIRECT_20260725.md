# Approximate cyclic synchronization: exact post-hoc no-go theorems

Date: 2026-07-25  
Line: E — master redirect to the constant-one theorem

## 0. Outcome

This report does **not** prove

\[
\nu(k)\le(1+o(1))W(k),
\]

nor the stronger labelled fixed-window synchronization theorem.

It proves a definitive no-go for the natural **post-hoc row-local cyclic
synchronization mechanism**.  The mechanism starts with an exact wreath
factor, tries to balance its lower flags by row orientations, cyclic phases,
or a sparse collection of replacement rows, and then attempts to absorb the
changes by one connected Gaussian-radius successor rewire in each old row.
All three sources of purported flexibility are quantitatively illusory.

1. A row's rank-`(m-q)` shadow histogram is invariant under every rotation,
   reversal, cyclic phase, and even every bijective reassignment of the same
   row-shadow list among its owners.  This remains true after dropping
   nesting and owner-subset legality.
2. Replacing `R` complete rows changes the mobile balanced-histogram distance
   by at most `nR` at one depth and at most

   \[
   nR\sum_{q\le K}\frac1{c_q}
   \]

   on the fixed window.  Thus `o(B/sqrt(m))` replacement rows have only
   `o(W)` total balancing power.
3. Two oriented wreath packets sharing `m+1` consecutive owners in the same
   successor order are identical.  Consequently every exact-factor rewire
   whose changed successor tails lie in one `O(K)` cyclic arc of each old row
   is the identity when `K=A sqrt(m)`.
4. A separate exact-cover stability proposal also fails sharply: a packet
   multiset with only two middle holes and two duplicates can require
   `Theta(m)` middle-owner reassignments before it becomes an exact factor.
5. Independently selected balanced rank histograms are exponentially far
   from every exact factor across a `Theta(sqrt(m))` subwindow, even when all
   coordinate point margins are within `W^(2/3)` of the exact margins.

The report preserves integrality and literal cyclic rows throughout the
structural no-go theorems.  It does **not** rule out a jointly designed
factor/table pair, ownerwise noncyclic deletion swaps, three-or-more separated
cuts in a row, or a global trade spanning `Omega(m)` row positions.  Those
are precisely the surviving possibilities.

## 1. Fixed-window notation

Put

\[
n=2m+1,
\qquad
\Omega=\binom{[n]}m,
\qquad
W=|\Omega|,
\qquad
B=\frac Wn.
\tag{1.1}
\]

For fixed `A>0`, let

\[
K=\lceil A\sqrt m\rceil,
\qquad
N_q=\binom n{m-q},
\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\tag{1.2}
\]

On this window there is a constant `C_A` such that

\[
1\le c_q\le C_A
\qquad(q\le K),
\tag{1.3}
\]

so, with

\[
S_K=\sum_{q=1}^K\frac1{c_q},
\tag{1.4}
\]

one has

\[
\frac K{C_A}\le S_K\le K,
\qquad
S_K=\Theta_A(\sqrt m).
\tag{1.5}
\]

An oriented wreath row is a cyclic coordinate order

\[
\pi=(\pi_0,\ldots,\pi_{n-1})
\tag{1.6}
\]

modulo rotation.  Its cyclic interval of length `r` beginning at `j` is

\[
I_\pi(j,r)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}.
\tag{1.7}
\]

The row's middle owners are `I_pi(j,m)`, and its canonical depth-`q`
targets are the `n` sets

\[
I_\pi(j,m-q),
\qquad j\in\mathbb Z_n.
\tag{1.8}
\]

Let `F` be an oriented exact factor.  Its depth-`q` histogram is

\[
\mu_q^F(S)
=\#\{X\in\Omega:L_q^F(X)=S\}.
\tag{1.9}
\]

Every balanced depth-`q` histogram has the form

\[
b_{q,H}=c_q\mathbf1+\mathbf1_H,
\qquad
H\subseteq\binom{[n]}{m-q},
\qquad
|H|=\rho_q:=W-c_qN_q.
\tag{1.10}
\]

Define the mobile balanced distance

\[
T_q(F)
=\min_{|H|=\rho_q}
\frac12\|\mu_q^F-b_{q,H}\|_1
\tag{1.11}
\]

and its fixed-window sum

\[
T_A(F)=\sum_{q=1}^K\frac{T_q(F)}{c_q}.
\tag{1.12}
\]

This is the exact minimum histogram transport to a floor/ceiling-balanced
vector.  It is unlabelled; a prescribed owner coupling can cost more.

## 2. Row-shadow histogram rigidity

For one row `pi` and depth `q`, write

\[
\mathcal I_{\pi,q}
=\{I_\pi(j,m-q):j\in\mathbb Z_n\}
\tag{2.1}
\]

as a multiset.  In fact its members are distinct, but the multiset language
makes the invariance immediate.

### Theorem 2.1 (zero balancing power of row-local phases)

At any fixed depth, the row contribution (2.1) is unchanged by any
combination of the following operations, chosen independently in every row:

1. rotate the cyclic representation;
2. reverse the row orientation;
3. apply a constant cyclic phase to the target indices;
4. assign the `n` members of \(\mathcal I_{\pi,q}\) bijectively, in an
   arbitrary order, to the row's `n` labelled owners.

Consequently all global loads `mu_q^F(S)` remain pointwise unchanged.

#### Proof

A rotation or phase replaces `j` by `j+s` in (2.1).  Reversal replaces

\[
I_\pi(j,m-q)
\]

by

\[
I_\pi(-j-(m-q)+1,m-q),
\]

which runs through the same set family as `j` runs through `Z_n`.  An
arbitrary bijective assignment preserves the target multiset by definition.
Summing these invariant row contributions proves pointwise invariance of the
global histogram.  QED.

The theorem is deliberately stronger than a legal nested statement: the
arbitrary bijection in item 4 may violate both owner-subset legality and
cross-depth nesting, yet it still cannot change the histogram.

It does **not** cover a nonbijective owner-dependent phase, a non-dihedral
reordering of the coordinate cycle, or an ownerwise adjacent deletion swap
whose new target is not a member of (2.1).

### Lemma 2.2 (exact coupling lower bound)

Let two labelled owner-state maps at depth `q` have histograms `mu` and
`nu`, and let `e` be their number of mismatched owners.  Then

\[
\boxed{e\ge\frac12\|\mu-\nu\|_1.}
\tag{2.2}
\]

Equality is the minimum over all unconstrained couplings of the two
histograms.

#### Proof

Changing one owner's target removes one unit from one histogram cell and
adds one unit to another, changing the histogram in \(\ell^1\) norm by at most
two.  Hence `||mu-nu||_1<=2e`.

Conversely, the maximum number of equal labels in any coupling is

\[
\sum_S\min\{\mu(S),\nu(S)\}.
\]

Since both histograms have total mass `W`, the uncoupled remainder is

\[
W-\sum_S\min\{\mu(S),\nu(S)\}
=\frac12\|\mu-\nu\|_1.
\]

QED.

For a fixed labelled coupling the inequality can be strict: equal histograms
can still have every owner assigned to a different target.

### Corollary 2.3 (exact obstruction to phase synchronization)

For every balanced nested owner table `P`,

\[
e_q(F,P)\ge T_q(F),
\tag{2.3}
\]

and therefore

\[
\boxed{
\sum_{q=1}^K\frac{e_q(F,P)}{c_q}
\ge T_A(F).}
\tag{2.4}
\]

Any mechanism using only the row-local operations in Theorem 2.1 can attain
`o(W)` weighted error only if the starting exact factor already satisfies

\[
T_A(F)=o(W).
\tag{2.5}
\]

Thus row-local cyclic scheduling supplies literally no new histogram
balancing; it merely relabels an already chosen histogram.

## 3. The sharp row-replacement Lipschitz bound

### Theorem 3.1 (row-sparse changes have bounded transport power)

Let `F'` be obtained from `F` by removing `R` old rows and inserting `R` new
rows.  Then, for every depth `q`,

\[
\boxed{
\|\mu_q^{F'}-\mu_q^F\|_1\le2nR.}
\tag{3.1}
\]

Consequently

\[
\boxed{
|T_q(F')-T_q(F)|\le nR}
\tag{3.2}
\]

and

\[
\boxed{
T_A(F')\ge T_A(F)-nRS_K.}
\tag{3.3}
\]

#### Proof

At depth `q`, one row contributes `n` unit masses.  Removing `R` rows and
inserting `R` rows therefore changes the histogram by \(\ell^1\) norm at most
`2nR`, proving (3.1).

For any nonempty target set \(\mathcal B\) in a normed space, the distance
function \(x\mapsto\operatorname{dist}(x,\mathcal B)\) is one-Lipschitz.
Apply this with the metric \(d(x,y)=\|x-y\|_1/2\) and with
\(\mathcal B\) equal to the balanced
histograms (1.10).  Equations (3.1)-(3.2) follow, and summing (3.2) with
weights `1/c_q` proves (3.3).  QED.

There are two useful quantitative consequences.

1. If `T_q(F)>=epsilon W` at one depth, every exact factor with
   `T_q=o(W)` differs from `F` in at least

   \[
   (\epsilon-o(1))\frac Wn
   =(\epsilon-o(1))B
   \tag{3.4}
   \]

   rows.
2. If `T_A(F)>=epsilon W`, then any family of

   \[
   R=o(B/\sqrt m)
   \tag{3.5}
   \]

   replacement rows changes `T_A` by only `o(W)` and cannot reach the
   labelled fixed-window target.

The count `R` in this theorem is the number of removed old rows; the same
number of new rows is inserted.

## 4. Consecutive-owner rigidity

The preceding theorems concern histograms.  The next obstruction is physical
and uses exact successor cycles.

An oriented row `pi` has middle owners

\[
X_i^\pi=I_\pi(i,m),
\qquad i\in\mathbb Z_n,
\tag{4.1}
\]

and successor `X_i^pi -> X_(i+1)^pi`.

### Lemma 4.1 (a length-`m` successor path determines the row)

If two oriented wreath packets share `m+1` consecutive labelled owners in
the same successor order, then the two oriented packets are identical.

#### Proof

After rotating indices, suppose their common path is

\[
X_0\longrightarrow X_1\longrightarrow\cdots\longrightarrow X_m.
\]

For `0<=i<m`,

\[
X_i\setminus X_{i+1}=\{\pi_i\},
\qquad
X_{i+1}\setminus X_i=\{\pi_{i+m}\}.
\tag{4.2}
\]

The `m` transitions therefore determine

\[
\pi_0,\ldots,\pi_{m-1}
\quad\hbox{and}\quad
\pi_m,\ldots,\pi_{2m-1}.
\]

The last entry `pi_(2m)` is the unique coordinate not yet used.  Thus the
entire oriented cyclic coordinate order is determined.  QED.

The threshold is sharp: `m` consecutive common owners determine all but the
order of the final two coordinates.

Let `F,F'` be oriented exact factors on the same owner universe, with
successor permutations `sigma,tau`.

### Theorem 4.2 (connected Gaussian-radius exact absorbers are trivial)

Assume that, in every old row `C` of `F`, all changed successor tails

\[
\{X\in C:\tau(X)\ne\sigma(X)\}
\tag{4.3}
\]

are contained in one cyclic interval of at most `R` tails.  If

\[
R\le m,
\tag{4.4}
\]

then

\[
\boxed{F'=F}
\tag{4.5}
\]

as oriented factors.

#### Proof

Outside the changed interval, an old row has at least

\[
n-R\ge m+1
\]

consecutive unchanged successor edges.  In particular it has `m`
consecutive unchanged edges, giving `m+1` consecutive old owners which lie
in one new packet in the same order.  Lemma 4.1 forces that new packet to be
the complete old packet, with the same orientation.  Its entire successor
cycle is therefore unchanged.  Apply this to every old row.  QED.

For fixed `A`, every connected absorber with `R=O(K)=O_A(sqrt(m))` satisfies
(4.4) for all sufficiently large `m` and is therefore the identity.

The same conclusion holds for a sequence of such operations if every
intermediate successor system is again an exact oriented factor: every step
is individually trivial.

### Corollary 4.3 (separated cuts are mandatory)

If one old row is genuinely altered, its changed successor tails must meet
every cyclic block of `m` consecutive tails.  In particular it has at least
three changed tails.

#### Proof

If a block of `m` consecutive tails were unchanged, its `m+1` owners would
invoke Lemma 4.1 and force the whole old row to survive.  With at most two
changed tails, the `2m-1` unchanged tails lie in at most two cyclic gaps; one
gap has length at least `m`.  Contradiction.  QED.

The theorem does not exclude three or more widely separated cuts, a trade
spanning `Omega(m)` row positions, or a path through nonexact intermediate
successor systems.

## 5. A sharp failure of packet-multiset owner recourse

A different proposed completion principle starts from a family of literal
wreath rows which almost covers the middle layer, measures only its number
of holes and duplicates, and asserts that a nearby exact factor follows.
At the level of middle-owner row assignments this is false by a factor
`Theta(m)`.

Let \(\mathcal N\) be any family of `B` distinct wreath rows.  Its middle
multiplicity function is

\[
\mu_{\mathcal N}(X)=\#\{C\in\mathcal N:X\in C\}.
\]

Put

\[
D(\mathcal N)
=\frac12\|\mu_{\mathcal N}-\mathbf1_\Omega\|_1.
\tag{5.1}
\]

Because both sides have total mass `W`, \(D(\mathcal N)\) is both the number of
holes and the total duplicate excess.

### Lemma 5.1 (row-granularity lower bound)

Let `H` be an exact factor and put

\[
r=|H\setminus\mathcal N|.
\]

Then at least

\[
\boxed{nr-D(\mathcal N)}
\tag{5.2}

distinct middle sets must acquire a different owning row when \(\mathcal N\)
is replaced by `H`.

#### Proof

The `r` new rows of `H` own `nr` distinct middle sets.  At most
\(D(\mathcal N)\) of these were holes of \(\mathcal N\).  Every remaining set had
an owning row in \(\mathcal N\).  That old owner cannot be a row of
\(H\cap\mathcal N\), because the new `H`-row already owns the same middle set
and distinct rows of an exact factor are owner-disjoint.  Hence its owning
row changes.  QED.

### Proposition 5.2 (two-hole adjacent-swap obstruction)

Take any exact factor `F`, choose one row with cyclic decomposition

\[
C=(u,v,Q,w,P),
\qquad |P|=|Q|=m-1,
\tag{5.3}
\]

and let `C'` swap the adjacent coordinates `u,v`.  Set

\[
\mathcal N=(F\setminus\{C\})\cup\{C'\}.
\tag{5.4}
\]

Then

\[
\mu_{\mathcal N}-\mathbf1_\Omega
=e_{P\cup\{v\}}+e_{Q\cup\{u\}}
-e_{P\cup\{u\}}-e_{Q\cup\{v\}},
\tag{5.5}
\]

so \(D(\mathcal N)=2\).  Nevertheless every exact cleanup `H` forces at least

\[
n-2=2m-1
\tag{5.6}

middle sets to acquire a different owning row.

#### Proof

An adjacent coordinate swap changes exactly two cyclic `m`-intervals.  The
window \(P\cup\{u\}\) becomes \(P\cup\{v\}\), and the window
\(Q\cup\{v\}\) becomes \(Q\cup\{u\}\).  This gives (5.5), two holes, two
duplicates, and exact cancellation of all coordinate point margins.

The family \(\mathcal N\) is not exact, so every exact factor `H` contains at
least one row absent from \(\mathcal N\); hence `r>=1`.  Lemma 5.1 with
`D=2` gives (5.6).  QED.

Thus no universal owner-row recourse theorem of the form

\[
\operatorname{Rec}_{\rm row}\le o(m)D
\tag{5.7}
\]

can hold, even when every hole is Johnson-adjacent to a duplicate and all
point margins cancel.

This does **not** give the same lower bound for the labelled shallow-flag
objective.  Common middle owners of `C,C'` can retain many identical shallow
prefixes.  Proposition 5.2 closes only the coarse owner-row recourse lemma,
not a more delicate flag-local trade theorem.

## 6. Independent quota selection is exponentially nonextendible

The preceding obstructions are deterministic.  There is also a clean
counting no-go for selecting balanced rank histograms independently and only
then seeking an exact factor.

Fix `A>0`.  Choose constants

\[
0<a<b<\min\{A,\sqrt{\log2}\}
\tag{6.1}
\]

and let

\[
J_m=\{q:a\sqrt m\le q\le b\sqrt m\}.
\tag{6.2}
\]

For `q=x sqrt(m)+O(1)`, uniformly on compact `x`-intervals,

\[
\frac W{N_q}=e^{x^2+o(1)}.
\tag{6.3}
\]

Hence, for all large `m`,

\[
c_q=1
\qquad(q\in J_m),
\tag{6.4}
\]

and there is `delta_A>0` such that

\[
\delta_A N_q\le\rho_q=W-N_q\le(1-\delta_A)N_q.
\tag{6.5}
\]

Let \(\mathfrak B_q\) be the set of all balanced histograms at rank `m-q`.
Since `c_q=1`,

\[
|\mathfrak B_q|=\binom{N_q}{\rho_q}
\ge\exp(\gamma_AW)
\tag{6.6}
\]

for a constant `gamma_A>0`.  Because `|J_m|=Theta_A(sqrt(m))`,

\[
\left|\prod_{q\in J_m}\mathfrak B_q\right|
\ge\exp(\gamma'_AW\sqrt m).
\tag{6.7}
\]

### Theorem 6.1 (quota-first entropy no-go)

Choose `b_q` uniformly and independently from \(\mathfrak B_q\) for
`q in J_m`.  For every fixed constant `C>0`,

\[
\Pr\left[
\exists\hbox{ oriented exact factor }F:
\sum_{q\in J_m}
\frac12\|\mu_q^F-b_q\|_1\le CW
\right]
\le\exp(-\Omega_A(W\sqrt m)).
\tag{6.8}
\]

Moreover, with probability tending to one, every chosen quota histogram has
every coordinate point margin within `W^(2/3)` of the exact wreath point
margin.

#### Proof

There are

\[
M=(n-1)!
\]

oriented cyclic rows modulo rotation.  An exact factor is a `B`-set of such
rows, so

\[
\#\{\hbox{oriented exact factors}\}
\le\binom MB.
\tag{6.9}
\]

Stirling's formula gives

\[
\log\binom MB=O(W\log m).
\tag{6.10}
\]

Fix one factor `F`.  For each `q`, select one balanced histogram
`b_q^*` minimizing the half-\(\ell^1\) distance to `mu_q^F`.  If another quota
tuple satisfies the event in (6.8), the triangle inequality gives total
binary Hamming distance at most `4CW` from `(b_q^*)_(q in J_m)`.  The total
number of binary quota coordinates is

\[
D_m=\sum_{q\in J_m}N_q=\Theta_A(W\sqrt m).
\]

Therefore the number of such quota tuples for fixed `F` is at most

\[
\sum_{j\le4CW}\binom{D_m}{j}
\le\exp(O_{A,C}(W\log m)).
\tag{6.11}
\]

Multiplying by (6.9) and dividing by (6.7) proves (6.8), since

\[
W\log m=o(W\sqrt m).
\]

For the point-margin statement, write a random quota as

\[
b_q=\mathbf1+\mathbf1_{H_q},
\qquad |H_q|=\rho_q.
\]

For a coordinate `z`, `deg_(H_q)(z)` is hypergeometric with mean

\[
\frac{(m-q)\rho_q}{n}.
\]

Thus the expected quota point margin is

\[
\binom{n-1}{m-q-1}
+\frac{(m-q)\rho_q}{n}
=\frac{(m-q)W}{n},
\tag{6.12}
\]

the exact point margin of a wreath factor.  A hypergeometric tail bound gives

\[
\Pr\left[
|\deg_{H_q}(z)-\mathbb E\deg_{H_q}(z)|>W^{2/3}
\right]
\le2\exp(-\Omega(W^{1/3})).
\]

A union bound over `n|J_m|` coordinate-depth pairs proves the claim.  QED.

The quota tuples in Theorem 6.1 are not asserted to arise from one nested
owner flow.  The theorem closes only the strategy "choose balanced ranks
independently, then synchronize."  It is not a counterexample to the
existence of a specially correlated balanced nested table.

## 7. Exact scope of the no-go

The proved theorems close the following mechanism.

1. Start from an arbitrary exact factor.
2. Preserve each row's cyclic coordinate order and change only orientations,
   phases, or bijective owner assignments of its existing shadows.
3. If a quota correction remains, replace `o(B/sqrt(m))` complete rows or
   absorb it through one connected successor interval of length `O(K)` in
   each old row.
4. Alternatively, choose rank quotas independently or round a small packet
   discrepancy using only owner-row recourse.

This mechanism cannot create an `o(W)` synchronized pair unless the starting
factor already has `T_A(F)=o(W)`.

The following possibilities remain genuinely open and are not weakened by
the report.

- Choose the exact factor and integral nested balanced table jointly from
  the outset.
- Use ownerwise adjacent deletion swaps whose new targets leave the row's
  canonical shadow family.
- Use support-feasible trades with at least three separated successor cuts
  in an altered row.
- Use a global exchange spanning `Omega(m)` positions or pass through
  nonexact intermediate packet systems.
- Prove a flag-local, rather than row-owner-local, exact-cover stability
  theorem.

In particular, the report does not turn the stronger labelled theorem into
an equivalent formulation of overload MWB.  It proves only that cyclic
phases and Gaussian-radius connected absorbers do not bridge the gap.

## 8. Independent adversarial audit

The two structural main steps were independently rederived.  The following
scope corrections were essential and have been incorporated.

1. Row-shadow invariance requires a bijective reassignment of the same
   `n` shadows.  A nonbijective owner-dependent phase or non-dihedral
   coordinate reorder may change the histogram.
2. Half-\(\ell^1\) distance is the exact minimum over unrestricted couplings,
   not necessarily the mismatch of the fixed labelled coupling.
3. `R` in Theorem 3.1 counts removed old rows, with the same number inserted.
4. Lemma 4.1 is sharp.  Only `m` consecutive common owners leave a two-label
   ambiguity.
5. The connected-absorber theorem is stated with the safe threshold `R<=m`.
   This is more than enough for `R=O_A(sqrt(m))` and avoids an endpoint
   ambiguity between changed owner positions and changed successor tails.
6. The packet-multiset lower bound measures owner-row reassignment, not
   shallow flag mismatch.  The latter may be much smaller.
7. The entropy theorem uses only a subinterval below `sqrt(log 2)`, not the
   entire fixed window for arbitrary `A`.
8. Floor/ceiling balance does not imply exact point regularity.  The random
   quota statement proves only `W^(2/3)` proximity to the exact point
   margins.
9. Independent quota tuples need not be nested.  Hence Theorem 6.1 is a
   mechanism no-go, not an existential obstruction.

The surviving Lane E theorem would have to use genuinely global,
cross-depth, owner-level structure.  None of the post-hoc cyclic operations
ruled out here can produce the required weighted mismatch `o(W)`.
