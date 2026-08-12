# Pascal squares, the structural Catalan bank, and the exact contraction gate

## Status

The same-parity lift has an exact four-sector square ledger.  It explains
simultaneously

* why the `Cat_r` repeated parent upper occurrences are necessary rather
  than defective;
* why a literal square-by-square implementation exposes `Cat_r` interfaces;
* why passive Pascal transport cannot give a contracting defect recurrence;
  and
* exactly which all-cut linkage estimate would give contraction once the
  structural Catalan bank has been built in bulk.

The conclusion is proof-safe and negative/conditional.  The new upper-rich
packets and the Boolean `C14` bank close fractional supply and anonymous
terminal capacity, but they do **not** by themselves bypass the mesoscopic
cover-down.  The missing statement is a named, protected linkage theorem (or
an equivalent bulk Catalan connector theorem).

No finite search or solver is used.

## 1. The four-sector Pascal square

Let the parent ground set be `Omega`, with

\[
 |\Omega|=2r-1,
 \qquad
 W=\binom{2r-1}{r}
   =\binom{2r-1}{r-1}.
\tag{1.1}
\]

Let `x,y` be two new coordinates.  For one directed parent Johnson
transition

\[
 T\longrightarrow T',
 \qquad |T|=|T'|=r,
 \qquad Q=T\cap T',
 \qquad R=T\cup T',
\tag{1.2}
\]

define four child middle owners

\[
 \begin{aligned}
 U&=R,\\
 X&=T\cup\{x\},\\
 A&=Q\cup\{x,y\},\\
 Y&=T'\cup\{y\}.
 \end{aligned}
\tag{1.3}
\]

All four have rank `r+1`, and

\[
                 U-X-A-Y-U
\tag{1.4}
\]

is a Johnson `C4`.  Its four immediate-lower colours are respectively

\[
 T,\quad Q\cup\{x\},\quad Q\cup\{y\},\quad T'.
\tag{1.5}
\]

This is the local square underlying the exact Catalan-leave lift in
`THREAD_K_SEMILENGTH_RAISING_CATALAN_LEAVE_LIFT_AND_ECO_OBSTRUCTION_20260729.md`.

### Theorem 1.1 (exact sector inventory)

For any multiset of parent transitions, let

\[
 (h_{\rm t},e_{\rm t}),\quad
 (h_{\rm h},e_{\rm h}),\quad
 (h_Q,e_Q),\quad
 (h_R,e_R)
\tag{1.6}
\]

be respectively the hole and excess counts of the tail-owner, head-owner,
lower-root, and upper-colour multiplicity vectors.  Apply (1.3) to every
transition occurrence.  Then the child middle-owner inventory has exactly

\[
 h_{\rm child}=h_{\rm t}+h_{\rm h}+h_Q+h_R,
 \qquad
 e_{\rm child}=e_{\rm t}+e_{\rm h}+e_Q+e_R.
\tag{1.7}
\]

In the usual balanced defect model, the tail and head copies have the same
simple owner deficit `x_O`, the root bank has simple deficit `x_Q`, and the
only repeated row is the upper row, with hole/excess pair `(h,e)`.  Then

\[
                    h_{\rm child}=2x_O+x_Q+h,
                    \qquad e_{\rm child}=e.
\tag{1.8}
\]

#### Proof

The four sectors are disjoint according to their intersections with
`{x,y}`.  Their multiplicity vectors are, in order, the parent upper,
tail-owner, lower-root, and head-owner vectors.  Holes and excesses add
across disjoint sectors, proving (1.7).  The specialization (1.8) is
immediate.
\(\square\)

## 2. The Catalan repetition is exactly the child-layer deficit

The parent upper shore has size

\[
 U_+=\binom{2r-1}{r+1}={r-1\over r+1}W,
\tag{2.1}
\]

so

\[
 C_r:=W-U_+={2W\over r+1}=\operatorname {Cat}_r.
\tag{2.2}
\]

The child middle layer splits into the four sectors

\[
 \binom{\Omega}{r+1},\qquad
 \binom{\Omega}{r}\!+x,\qquad
 \binom{\Omega}{r}\!+y,\qquad
 \binom{\Omega}{r-1}\!+x+y,
\tag{2.3}
\]

and therefore

\[
 \binom{2r+1}{r+1}=U_++3W=4W-C_r.
\tag{2.4}
\]

### Theorem 2.1 (Catalan-bank identity)

If the parent owner and lower-root shores are exact and its upper palette is
complete, then its upper excess is exactly `C_r`.  The four-sector square
inventory covers every child owner and has exactly `C_r` excess occurrences.
Consequently every one-copy child selector removes exactly `C_r` `00`-sector
occurrences.

If the parent palette is cap two,

\[
                  \mu_R=1+\mathbf 1_{R\in\mathcal D},
                  \qquad |\mathcal D|=C_r,
\tag{2.5}
\]

then it removes exactly one of the two occurrences of every
`R in \mathcal D`.

#### Proof

There are `W` parent transitions and only `U_+` upper colours.  Completeness
therefore forces excess `W-U_+=C_r`.  Theorem 1.1 gives no child holes and
the same excess.  Equation (2.4) gives the same conclusion by total count.
In the cap-two case each excess unit belongs to a different colour.
\(\square\)

Thus the `C_r` repeated upper occurrences are not a sidecar to be repaired.
They are exactly the structural inventory by which `4W` Pascal-square
occurrences are reduced to the `4W-C_r` child owners.

## 3. Why a local treatment cannot produce `O(1)` task birth

After one occurrence of a duplicated `00` owner is omitted, its local `C4`
is punctured.  The exact semilength-raising construction handles all these
punctures together: the omitted occurrence set is the Catalan leave `J`,
and the cap-two factor reconnects the other three sectors globally.

The following elementary bound records why a bounded collection of local
terminal gadgets cannot replace that global step.

### Proposition 3.1 (square-local Catalan lower bound)

Consider any implementation in which

1. each of the `C_r` omitted `00` occurrences exports one named open square
   interface;
2. an actuator can consume interfaces from at most `s` parent transitions;
   and
3. an interface remains exposed unless some actuator containing its parent
   transition is selected.

Then at least

\[
                         \left\lceil {C_r\over s}\right\rceil
\tag{3.1}
\]

actuators are necessary.

#### Proof

The supports of the chosen actuators must cover all `C_r` named interfaces,
and each support covers at most `s` of them.  \(\square\)

Every fixed Boolean `C6`, `C8`, or `C14` has bounded `s`.  Hence a bounded
number of such gadgets cannot turn the square inventory into a child factor.
The linear-size `C14` reservoir *does* have enough anonymous capacity to use
`Theta(C_r)` gadgets, but assigning the named interfaces to disjoint buffers
is then a mesoscopic linkage problem, not an `O(1)`-task theorem.

Indeed the proved anonymous bank has size at least `W/98`, whereas

\[
                         C_r={2W\over r+1}.
\tag{3.2}
\]

Hence

\[
                         {|\mathcal B_{14}|\over C_r}
                            \ge {r+1\over196}.             \tag{3.3}
\]

For `r>=195`, even a one-buffer-per-leave strategy has ample cardinality.
Its failure, if any, is therefore a named pivot/flag linkage failure, not a
shortage of terminal gadgets.

Proposition 3.1 is deliberately scoped.  It does not rule out one correlated
Catalan-scale connector; indeed the exact degree-two lift is precisely such
a construction.  It rules out only the inference

\[
 \text{bounded local buffer} \Longrightarrow O(1)\text{ task birth}.
\tag{3.4}
\]

## 4. Passive defect transport is expansive

Let the unweighted central defect be

\[
                         \Psi=x_O+x_Q+h.
\tag{4.1}
\]

Theorem 1.1 gives the exact raw child central defect

\[
                         \Psi_{\rm child}^{\rm raw}
                            =2x_O+x_Q+h.
\tag{4.2}
\]

In particular, on the pure owner-defect ray,

\[
                         \Psi_{\rm child}^{\rm raw}=2\Psi.
\tag{4.3}
\]

### Corollary 4.1 (no passive contraction)

No recurrence

\[
                         \Psi_{k+2}\le\theta_k\Psi_k+O(1),
                         \qquad \theta_k<1,
\tag{4.4}
\]

can follow from passive Pascal copying alone.  It requires an active repair
which either absorbs a positive fraction of the child sources or quotients
them into a preconstructed structural object.

The same conclusion holds for any dimension-uniform weighted potential
which assigns comparable positive weight to one owner hole: one owner hole
has two disjoint child copies before repair.

This is the exact source of the coefficient four in the existing guarded
Pascal recurrence: once all lower, upper, residence, topology, and compiler
avatars of one carried task are exposed, one parent task may create up to
four child sources.  A contraction proof must beat that branching factor.

## 5. The sharp all-cut recurrence

The recent packet and `C14` results provide the two endpoint objects:

* upper-rich packets give exact fractional owner/lower/upper supply and a
  large integral packet reservoir;
* Boolean `C14`s give a linear-size resource-disjoint bank of sequential
  terminal buffers.

Let `S_k` be the child source set exposed by a lift and suppose

\[
                         |S_k|\le4\Phi_k+b_0.             \tag{5.1}
\]

Build the **named protected linkage graph** from sources to compatible,
resource-disjoint terminal buffers.  Compatibility must include the lower
flag, upper-provider, residence, topology, and compiler tickets, not just a
common Boolean pivot.

### Theorem 5.1 (all-cut linkage implies contraction)

Suppose there are numbers `epsilon_k` and `gamma` such that for every
`X subseteq S_k`,

\[
                   |N(X)|\ge(1-\epsilon_k)|X|-\gamma.
\tag{5.2}
\]

Suppose also that every linked source-buffer pair is a complete accepting
repair and that the final bounded topology/compiler sidecar contributes at
most `b_1`.  Then

\[
 \boxed{
       \Phi_{k+2}
       \le4\epsilon_k\Phi_k
          +\epsilon_k b_0+\gamma+b_1.}
\tag{5.3}
\]

#### Proof

By the defect form of Hall's theorem, a maximum matching leaves at most

\[
 \max_{X\subseteq S_k}(|X|-|N(X)|)
 \le\epsilon_k|S_k|+\gamma
\tag{5.4}
\]

sources unmatched.  Substitute (5.1) and add the terminal charge `b_1`.
\(\square\)

At triangular depth `d(k)=Theta(sqrt k)`, the natural target

\[
                         \epsilon_k=O(d(k)/k)=O(k^{-1/2})
\tag{5.5}
\]

would give

\[
                         \theta_k=4\epsilon_k=O(k^{-1/2})<1
\tag{5.6}
\]

for all sufficiently large `k`, and hence a bounded regenerative defect on
each parity.

Equation (5.3) is the shortest honest contraction implication now
available.  It isolates exactly what the current supply theorems do not
prove: the all-cut inequality (5.2).

## 6. Why cardinality and codegree do not imply (5.2)

Anonymous `C14` capacity is much larger than `|S_k|`, but prescribed defect
circuits can share one diagonal pivot, so all their direct extensions may
meet one root.  Likewise, the aggregate-linear pull-ring reservoir admits
dense packet clusters for which the defect-to-buffer incidence graph fails
Hall by the factor `h/rho`.

Therefore none of the following implies (5.2):

\[
 \begin{gathered}
 |\mathcal B|\gg|S_k|,\\
 \Delta_2/D=o(1),\\
 \text{linearity and near-regularity},\\
 \text{complete Boolean trade lattice}.
 \end{gathered}
\tag{6.1}
\]

The obstruction is named concentration.  It can be removed only by proving
one of the following genuinely global statements.

1. **Bulk Catalan connector.**  Correlate the occurrence transversal, the
   cap-two factor, all protected flags, and the terminal ports so that the
   entire structural leave is compiled at once and only `O(1)` exceptional
   tasks are exported.
2. **Protected all-cut linkage.**  Prove (5.2) for the mesoscopic source
   family, perhaps after a dense-cluster/ideal decomposition.
3. **Prepared-defect theorem.**  Construct the cover-down so its leave is
   already dispersed across a fixed `C14` bank and avoids the exceptional
   reservoir resources.

These are different formulations of the remaining correlated selector.
The upper-rich packet marginals and the `C14` capacity theorem do not choose
among them.

### Theorem 6.1 (dense-cluster coagulation gives contraction)

There is a weaker alternative to the full all-cut estimate.  Suppose the
child source bank `S_k` satisfies (5.1) and lies outside the exceptional
low-degree set of a packet reservoir.  Assume every source has reservoir
degree at least `delta_k`.

Apply the dense-cluster peeling theorem: write

\[
                         S_k=S_0\mathbin{\dot\cup}
                              C_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_t,
\tag{6.2}
\]

where `S_0` has an injective source-to-packet matching, every `C_i` lies in
one reservoir packet and has size at least `delta_k+1`, and

\[
                         t\le {|S_k|\over\delta_k+1}.
\tag{6.3}
\]

Suppose the matched sources in `S_0` are completely repaired, while every
dense cluster `C_i` can be replaced by at most `a` regenerative output
tasks.  Assume these cluster replacements are jointly compatible, with all
remaining terminal damage bounded by `b_1`.  Then

\[
 \boxed{
 \Phi_{k+2}
 \le {4a\over\delta_k+1}\Phi_k
      +{ab_0\over\delta_k+1}+b_1.}
\tag{6.4}
\]

#### Proof

The dispersed part contributes no output task.  The dense part contributes
at most `at`, and the terminal sidecar contributes at most `b_1`.  Use
(6.3), then (5.1).  \(\square\)

Thus any reservoir with `delta_k -> infinity` yields strict contraction as
soon as a packet-supported dense cluster can be coagulated into a bounded
number of regenerative tasks.  For the linear pull-ring reservoir one may
take `delta_k` of polynomial order (for example `r^(1/4)` in the current
alteration), giving

\[
                         \theta_k=O(r^{-1/4})<1.
\tag{6.5}
\]

This target is weaker than repairing every named source and stronger than
aggregate counting.  It also has a sharp present obstruction to the
naive **one-polarity** pull coalescer: one phase of pull-run toggles changes
a downset in the cyclic interval-containment poset.  The density-`1-o(1)`
cluster consisting of every proper interval except one singleton is not
such a downset.  Hence Theorem 6.1 cannot be invoked for arbitrary peeled
clusters using a one-polarity whole-packet pull.  One must either

* prepare the cover-down so each dense cluster is a union of legal interval
  ideals; or
* prove a signed two-phase pull coalescer whose positive and negative
  Möbius masses fit the core, or a still richer coalescer carrying the
  missing Möbius coefficients and protected upper/compiler tickets.

This is the sharpest currently visible route to a recurrence with
`theta_k<1` which is weaker than the full protected linkage (5.2).

## 7. Conditional reset formulation

There is still a useful `O(1)`-task theorem after the structural bank is
assumed, rather than before it.

### Lemma 7.1 (bounded-task Hall collapse)

Let `S` be a source bank with `|S|<=H`, and let `\mathcal B` be a
resource-disjoint buffer bank.  If every source is compatible with at least
`H` members of `mathcal B`, then the source-buffer graph has a matching
saturating `S`.

#### Proof

For every nonempty `X subseteq S`, choose `s in X`.  Then

\[
                         |N(X)|\ge |N(s)|\ge H\ge|X|.
\tag{7.1}
\]

Hall's theorem applies.  \(\square\)

Thus once genuine task birth is already bounded, no mesoscopic expansion
theorem is needed at the terminal `C14` stage.  It is enough to give every
task a fixed-size complete-ticket list whose size dominates the absolute
task bound.  Anonymous `C14` capacity still does not prove this pointwise
reachability statement, because all direct extensions of one defect may
share a forced pivot.

### Corollary 7.2 (structural-quotient reset)

Assume a bulk Catalan connector which, for every bounded protected input
bank, consumes all `C_r` structural leave interfaces, preserves every
required upper/residence/compiler ticket, and exports at most `b` named
tasks.  Assume the exported terminal circulation links to the `C14` bank.
Then

\[
                         \Phi_{k+2}\le b.                 \tag{7.2}
\]

independently of `r`; equivalently the quotient recurrence has `theta_k=0`.

This would indeed bypass a generic mesoscopic cover-down.  But its premise
is exactly the unproved Catalan-leave chronology/port lemma, now augmented
by the occurrence-level upper and common-cap tickets.  It is not a
consequence of fractional packet balance or terminal buffer capacity.

## 8. Verdict

The same-parity framework can support an `O(1)` theorem only after the
forced Catalan bank is treated as one bulk structural object.  Counting its
`Cat_r` leave positions as independent tasks makes bounded birth impossible,
while passive transport of genuine defects is expansive.

The sharp remaining mathematical target is therefore

\[
 \boxed{
 \text{prove the protected all-cut linkage (5.2), or construct an
 occurrence-addressed bulk Catalan connector.}}
\tag{8.1}
\]

With `epsilon_k=O(k^{-1/2})`, Theorem 5.1 gives the desired strict
contraction.  Without such a theorem, the new packet and `C14` results do
not yet establish `B(k)+O(1)`.
